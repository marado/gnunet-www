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

import jinja2
import os
from inc.site import gen_site
from inc.fileproc import copy_files

env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__),"inc"),
                         extensions=["jinja2.ext.i18n"],
                         lstrip_blocks=True,
                         trim_blocks=True,
                         undefined=jinja2.StrictUndefined,
                         autoescape=False)

def main():
    # rm_rf("rendered")
    x = gen_site()
    conf = x.load_config("www.yml")
    print("generating news abstracts...")
    x.gen_abstract(conf, "newsposts", "abstract", "page", 1000)
    print("generating html from jinja2 templates...")
    x.run("template", conf, env)
    print("generating html from jinja2 news templates...")
    x.run("news", conf, env)
    #for lang in conf["langs_full"]:
    #    copy_files("static", conf, lang, "staticfiles", "rendered")
    # print("generating rss...")
    # x.generate_rss()
    # print("generating sitemap...")
    # x.generate_sitemap()

if __name__ == "__main__":
    main()
