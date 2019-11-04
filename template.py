#!/usr/bin/env python3
# coding: utf-8
#
# Copyright (C) 2017, 2018, 2019 GNUnet e.V.
#
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided the copyright
# notice and this notice are preserved.  This file is offered as-is,
# without any warranty.
#
# ----
#
# This script runs the jinja2 templating engine on an input template-file
# using the specified locale for gettext translations, and outputs
# the resulting (HTML) ouptut-file.
#
# Note that the gettext files need to be prepared first. This script
# is thus to be invoked via the Makefile.
#
# We import unicode_literals until people have understood how unicode
# with bytes and strings changed in python2->python3.
# from __future__ import unicode_literals
import os
import os.path
import sys
import re
import gettext
import glob
import codecs
import jinja2
import i18nfix
from pathlib import Path
import hashlib

# TODO: Turn repetition into a class.

env = jinja2.Environment(loader=jinja2.FileSystemLoader(
    os.path.dirname(__file__)),
                         extensions=["jinja2.ext.i18n"],
                         lstrip_blocks=True,
                         trim_blocks=True,
                         undefined=jinja2.StrictUndefined,
                         autoescape=False)
# DEBUG OUTPUT:
if (os.getenv("DEBUG")):
    print(sys.path)

langs_full = {
    "en": "English",
    "fr": "Français",
    "it": "Italiano",
    "es": "Español",
    "de": "Deutsch"
}

# A construction has:
# symlinks (dict)
# staticfiles (dict)
# robot.txt files (list)
# locales (list)
# shells out to siteindex (todo: python siteindex)
# generation_directories: the one we are building right now
#                         the one we will be replacing
#                         other directories get trashed upon successful build

symlinks = {
    "frontpage.html": "frontpage",
    "gsoc.html": "gsoc",
    "about.html": "philosophy",
    "gns.html": "gns",
    "node/about.html": "397"
}

# Mostly from static/ to rendered/
staticfiles = {
    "favicon.ico": "favicon.ico",
    "moved.html": "frontpage.html",
    "robots.txt": ["static", "dist", list(langs_full)],
    "moved_gsoc.html": "gsoc.html",
    "moved_about.html": "about.html",
    "moved_gns.html": "gns.html"
}


def localized(filename, locale, *args):
    if len(args) == 0:
        return "../" + locale + "/" + filename
    ext = kwargs.get('ext', None)
    if ext is not None:
        lf = filename + "." + locale + "." + ext
        lp = Path(lf)
        if locale == "en" or not lp.is_file():
            return "../" + filename + "." + ext
        else:
            return "../" + lf


def fileop(infile, outfile, action):
    """
    infile: inputfile, Path object
    outfile: outputfile, Path object
    action: action if any, String
    """
    i = Path(infile)
    o = Path(outfile)
    outdir = Path("rendered")
    if i.is_file() is not False:
        if action == "copy":
            # Write content of i to o.
            o.write_text(i.read_text())
        if action == "link":
            o.symlink_to(i)


def write_name(filename, infile, locale, replacer):
    return "./rendered/" + locale + "/" + infile.replace(replacer,
                                                         '').rstrip(".j2")


def sha256sum(_):
    sha256 = hashlib.sha256()
    with io.open(_, mode="rb") as fd:
        content = fd.read()
        sha256.update(content)
    return sha256.hexdigest()


def walksum(_):
    sha256 = hashlib.sha256()
    x = Path(_)
    if not x.exists():
        return -1
    try:
        for root, directories, files in os.walk(_):
            for names in sorted(files):
                filepath = os.path.join(root, names)
                try:
                    fl = open(filepath, 'rb')
                except:
                    fl.close()
                    continue
                while 1:
                    buf = fl.read(4096)
                    if not buf:
                        break
                    sha256.update(hashlib.sha256(buf).hexdigest())
                fl.close()
    except:
        import traceback
        traceback.print_exc()
        return -2
    return sha256.hexdigest()


def rm_rf(directory):
    directory = Path(directory)
    for child in directory.glob('*'):
        if child.is_file():
            child.unlink()
        else:
            rm_rf(child)
    directory.rmdir()


# This generates and switches sites generations, preventing
# in-place modification of the website.
# * save old generation directory name
# * jinja2 creates content in "rendered" (happened before calling this function)
# * calculate sum of "rendered"
# * move "rendered" to out/$sum
# * remove symlink "html_dir"
# * symlink out/$sum to "html_dir"
# * delete old generation directory
def generation_dir(htmldir):
    oldgen = Path(htmldir).resolve()
    # precondition: jinja2 has created the files in "rendered".
    newgen = Path("rendered")
    newgen_sum = walksum(newgen)
    outdir = Path("out")
    outdir.mkdir(parents=True, exist_ok=True)
    newgen_target = Path("out") / newgen_sum
    newgen.rename(newgen_target)
    html = Path(htmldir)
    html.unlink()
    fileop(newgen, html, "link")
    rm_rf(oldgen)


def copy_static (locale, indict):
    for key, value in indict.items():
        print(locale + "/" + key + " ...to... " + locale + "/" + value)
#    fileop(in, out, "copy")

# At this moment in time, constructing this list dynamically would be
# too much pointless code. In fact all of what we use in jinja is
# no real use of jinja yet and furthermore we would be better off
# just using static html + css + some awk and other base tools.
newsposts = [
    {'page': '2019-0.11.8.html', 'date': '2019-10-30', 'title': 'GNUnet 0.11.8'},
    {'page': '2019-0.11.7.html', 'date': '2019-10-27', 'title': 'GNUnet 0.11.7'},
    {'page': '2019-10-ICANNPanel.html', 'date': '2019-10-20', 'title': 'ICANN Panel'},
    {'page': '2019-10-GNSSpec1.html', 'date': '2019-10-04', 'title': 'GNS Spec 1'},
    {'page': '2019-0.11.6.html', 'date': '2019-07-24', 'title': 'GNUnet 0.11.6'},
    {'page': '2019-07-GHM_Aug_2019.html', 'date': '2019-07-17', 'title': 'GNUnet Hacker Meeting 2019'},
    {'page': '2019-06-DSTJ.html', 'date': '2019-06-28', 'title': 'DSTJ'},
    {'page': '2019-0.11.5.html', 'date': '2019-06-05', 'title': 'GNUnet 0.11.5'},
    {'page': '2019-06.html', 'date': '2019-06-01', 'title': '2019-06'},
    {'page': '2019-0.11.4.html', 'date': '2019-05-12', 'title': 'GNUnet 0.11.4'},
    {'page': '2019-0.11.3.html', 'date': '2019-04-07', 'title': 'GNUnet 0.11.3'},
    {'page': '2019-0.11.2.html', 'date': '2019-04-04', 'title': 'GNUnet 0.11.2'},
    {'page': '2019-0.11.1.html', 'date': '2019-04-03', 'title': 'GNUnet 0.11.1'},
    {'page': '2019-0.11.0.html', 'date': '2019-02-28', 'title': 'GNUnet 0.11.0'},
    {'page': '2019-02.html', 'date': '2019-02-01', 'title': 'Google Summer of Code 2019'},
    {'page': '2017-10.html', 'date': '2017-10-01', 'title': 'Launching the new gnunet.org'},
]


def generate_site(root):
    for in_file in glob.glob(root + "/*.j2"):
        name, ext = re.match(r"(.*)\.([^.]+)$", in_file.rstrip(".j2")).groups()
        tmpl = env.get_template(in_file)

        def self_localized(other_locale):
            """
            Return URL for the current page in another locale.
            """
            return "../" + other_locale + "/" + in_file.replace(
                root + '/', '').rstrip(".j2")

        def url_localized(filename):
            if root == "news":
                return "../../" + locale + "/" + filename
            else:
                return "../" + locale + "/" + filename

        def url_static (filename):
            if root == "news":
                return "../../static/" + filename
            else:
                return "../static/" + filename

        def url_dist (filename):
            if root == "news":
                return "../../dist/" + filename
            else:
                return "../dist/" + filename

        def svg_localized(filename):
            lf = filename + "." + locale + ".svg"
            if locale == "en" or not os.path.isfile(lf):
                return "../" + filename + ".svg"
            else:
                return "../" + lf

        def url(x):
            # TODO: look at the app root environment variable
            # TODO: check if file exists
            #if root == "news":
            #    return "../" + "../" + x
            #else:
            #    return "../" + x
            return "../" + x


        for l in glob.glob("locale/*/"):
            locale = os.path.basename(l[:-1])

            tr = gettext.translation("messages",
                                     localedir="locale",
                                     languages=[locale])

            tr.gettext = i18nfix.wrap_gettext(tr.gettext)

            env.install_gettext_translations(tr, newstyle=True)

            content = tmpl.render(lang=locale,
                                  lang_full=langs_full[locale],
                                  url=url,
                                  newsdata=newsposts,
                                  self_localized=self_localized,
                                  url_localized=url_localized,
                                  url_static=url_static,
                                  url_dist=url_dist,
                                  svg_localized=svg_localized,
                                  filename=name + "." + ext)

            if root == "news":
                out_name = "./rendered/" + locale + "/" + root + "/" + in_file.replace(
                    root + '/', '').rstrip(".j2")
            else:
                out_name = "./rendered/" + locale + "/" + in_file.replace(
                    root + '/', '').rstrip(".j2")

            outdir = Path("rendered")

            if root == "news":
                langdir = outdir / locale / root
            else:
                langdir = outdir / locale

            langdir.mkdir(parents=True, exist_ok=True)
            # os.makedirs("./rendered/" + locale, exist_ok=True)
            with codecs.open(out_name, "w", encoding='utf-8') as f:
                f.write(content)


def main():
    # rm_rf("rendered")
    print("generating template")
    generate_site("template")
    print("generating news")
    generate_site("news")
#    for l in glob.glob("locale/*/"):
#        locale = os.path.basename(l[:-1])
#        copy_static (locale, staticfiles)
    # generate_rss
    #print("running generation")
    #generation_dir


if __name__ == "__main__":
    main()

# for in_file in glob.glob("news/*.j2"):
#     name, ext = re.match(r"(.*)\.([^.]+)$", in_file.rstrip(".j2")).groups()
#     tmpl = env.get_template(in_file)

#     def self_localized(other_locale):
#         """
#         Return URL for the current page in another locale.
#         """
#         return "../" + other_locale + "/" + in_file.replace('news/',
#                                                             '').rstrip(".j2")

#     def url_localized(filename):
#         return "../" + locale + "/" + filename

#     def svg_localized(filename):
#         lf = filename + "." + locale + ".svg"
#         if locale == "en" or not os.path.isfile(lf):
#             return "../" + filename + ".svg"
#         else:
#             return "../" + lf

#     def url(x):
#         # TODO: look at the app root environment variable
#         # TODO: check if file exists
#         return "../" + x

#     for f in glob.glob("locale/*/"):
#         locale = os.path.basename(f[:-1])
#         content = tmpl.render(lang=locale,
#                               lang_full=langs_full[locale],
#                               url=url,
#                               self_localized=self_localized,
#                               url_localized=url_localized,
#                               svg_localized=svg_localized,
#                               filename=name + "." + ext)
#         out_name = "./rendered/" + locale + "/news/" + in_file.replace('news/', '').rstrip(".j2")
#         outdir = Path("rendered")
#         langdir = outdir / locale / "news"
#         langdir.mkdir(parents=True, exist_ok=True)
#         # os.makedirs("./rendered/" + locale + "/news/", exist_ok=True)
#         with codecs.open(out_name, "w", encoding='utf-8') as f:
#             f.write(content)
