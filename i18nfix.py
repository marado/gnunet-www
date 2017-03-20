#!/usr/bin/env python3
# This file is in the public domain.

"""
Extract translations from a Jinja2 template, stripping leading newlines.

@author Florian Dold
"""

import jinja2.ext
import re

r = re.compile(r"\n[ \t]+")

def babel_extract(fileobj, keywords, comment_tags, options):
    res = jinja2.ext.babel_extract(fileobj, keywords, comment_tags, options)
    for lineno, funcname, message, comments in res:
        message = message.lstrip()
        message = r.sub("\n", message)
        yield lineno, funcname, message, comments
