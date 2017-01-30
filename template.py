#!/usr/bin/env python

import os
import sys
import re
import gettext
import jinja2

if len(sys.argv) < 3:
    sys.exit("Usage: " + __file__ + " <template-file> <locale> <output-file>")

in_file = sys.argv[1]
locale = sys.argv[2]

name, ext = re.match(r"(.*)\.([^.]+)$", in_file.rstrip(".j2")).groups()

tr = gettext.translation("messages",
                         localedir="locale",
                         languages=[locale])

env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                         extensions=["jinja2.ext.i18n"],
                         autoescape=False)
env.install_gettext_translations(tr, newstyle=True)

tmpl = env.get_template(in_file)

def self_localized(x):
    return ".".join((name, x, ext))

def url_localized(my_file):
    my_name, my_ext = re.match(r"(.*)\.([^.]+)$", my_file).groups()
    return ".".join((my_name, locale, my_ext))

def url(x):
    # TODO: look at the app root environment variable
    # TODO: check if file exists
    return x

import codecs
f = codecs.open(".".join((name, locale, ext)), "w", "utf-8")
f.write(tmpl.render(lang=locale, url=url, self_localized=self_localized, url_localized=url_localized))
f.close()
