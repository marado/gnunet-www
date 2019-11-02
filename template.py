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
from __future__ import unicode_literals
import os
import os.path
import sys
import re
import gettext
import glob
import codecs
import jinja2
import i18nfix

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

for in_file in glob.glob("template/*.j2"):
    name, ext = re.match(r"(.*)\.([^.]+)$", in_file.rstrip(".j2")).groups()
    tmpl = env.get_template(in_file)

    def self_localized(other_locale):
        """
        Return URL for the current page in another locale.
        """
        return "../" + other_locale + "/" + in_file.replace('template/',
                                                            '').rstrip(".j2")

    def url_localized(filename):
        return "../" + locale + "/" + filename

    def svg_localized(filename):
        lf = filename + "." + locale + ".svg"
        if locale == "en" or not os.path.isfile(lf):
            return "../" + filename + ".svg"
        else:
            return "../" + lf

    def url(x):
        # TODO: look at the app root environment variable
        # TODO: check if file exists
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
                              self_localized=self_localized,
                              url_localized=url_localized,
                              svg_localized=svg_localized,
                              filename=name + "." + ext)
        out_name = "./rendered/" + locale + "/" + in_file.replace(
            'template/', '').rstrip(".j2")
        os.makedirs("./rendered/" + locale, exist_ok=True)
        with codecs.open(out_name, "w", encoding='utf-8') as f:
            f.write(content)


for in_file in glob.glob("news/*.j2"):
    name, ext = re.match(r"(.*)\.([^.]+)$", in_file.rstrip(".j2")).groups()
    tmpl = env.get_template(in_file)

    def self_localized(other_locale):
        """
        Return URL for the current page in another locale.
        """
        return "../" + other_locale + "/" + in_file.replace('news/',
                                                            '').rstrip(".j2")

    def url_localized(filename):
        return "../" + locale + "/" + filename

    def svg_localized(filename):
        lf = filename + "." + locale + ".svg"
        if locale == "en" or not os.path.isfile(lf):
            return "../" + filename + ".svg"
        else:
            return "../" + lf

    def url(x):
        # TODO: look at the app root environment variable
        # TODO: check if file exists
        return "../" + x

    for f in glob.glob("locale/*/"):
        locale = os.path.basename(f[:-1])
        content = tmpl.render(lang=locale,
                              lang_full=langs_full[locale],
                              url=url,
                              self_localized=self_localized,
                              url_localized=url_localized,
                              svg_localized=svg_localized,
                              filename=name + "." + ext)
        out_name = "./rendered/" + locale + "/news/" + in_file.replace('news/', '').rstrip(".j2")
        os.makedirs("./rendered/" + locale + "/news/", exist_ok=True)
        with codecs.open(out_name, "w", encoding='utf-8') as f:
            f.write(content)
