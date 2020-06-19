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
# the resulting (HTML) output-file.
#
# Note that the gettext files need to be prepared first. This script
# is thus to be invoked via the Makefile.

import jinja2
import sys
from pathlib import Path, PurePath
from inc.site import gen_site
from inc.fileproc import copy_files

env = jinja2.Environment(loader=jinja2.FileSystemLoader(str(PurePath(__file__).parent)),
                         extensions=["jinja2.ext.i18n"],
                         lstrip_blocks=True,
                         trim_blocks=True,
                         undefined=jinja2.StrictUndefined,
                         autoescape=False)

if len(sys.argv) >= 2 and sys.argv[1] == "-vv":
    DEBUG=1
elif len(sys.argv) >= 2 and sys.argv[1] == "-vvv":
    DEBUG=2
elif len(sys.argv) >= 2 and sys.argv[1] == "-vvvv":
    DEBUG=3
else:
    DEBUG=0

def main():
    # rm_rf("rendered")
    x = gen_site(DEBUG)
    conf = x.load_config("www.yml")
    x.gen_abstract(conf, "newsposts", "abstract", "page", 500)
    #    for lang in conf["langs_full"]:
    #        x.gen_newspost_content(conf, "newsposts", "content", "page", lang)
    x.gen_newspost_content(conf, "newsposts", "content", "page", "en")
    x.gen_rss("inc", conf, env)
    if DEBUG:
        print("generating html from jinja2 templates...")
    x.run("template", conf, env)
    if DEBUG >= 2:
        print(Path.cwd())
        _ = Path("rendered")
        for child in _.iterdir():
            print(child)
    if DEBUG >= 2:
        print(Path.cwd())
    if DEBUG:
        print("generating html from jinja2 news templates...")
    x.run("news", conf, env)
    #for lang in conf["langs_full"]:
    #    copy_files("static", conf, lang, "staticfiles", "rendered")
    if DEBUG:
        print("copying directories...")
    x.copy_trees("static")
    x.copy_trees("dist")
    # print("generating rss...")
    # x.generate_rss()
    # print("generating sitemap...")
    # x.generate_sitemap()

if __name__ == "__main__":
    main()
