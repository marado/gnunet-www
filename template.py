#!/usr/bin/env python

import os
import sys
import gettext
import jinja2

if len(sys.argv) < 3:
    sys.exit("Usage: " + __file__ + " <template-file> <locale> <output-file>")

in_file = sys.argv[1]
locale = sys.argv[2]
out_file = sys.argv[3]

tr = gettext.translation("messages",
                         localedir="locale",
                         languages=[locale])

env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                         extensions=["jinja2.ext.i18n"],
                         autoescape=False)
env.install_gettext_translations(tr, newstyle=True)

tmpl = env.get_template(in_file)

import codecs
f = codecs.open(out_file, "w", "utf-8")
f.write(tmpl.render())
f.close()
