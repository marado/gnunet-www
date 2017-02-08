#!/bin/sh
# This file is in the public domain.
#
# Wrapper around 'template.py', running it on all
# of our jinja2 input files for all languages for which
# we have translations.
#
# Note that the gettext files need to be prepared first. This script
# is thus to be invoked via the Makefile.
for f in $(git ls-files *.j2); do
    for ld in locale/*/; do
	l=$(basename $ld)
        mkdir -p $(basename $l)
	echo "$f: $l"
	python template.py $f $l
    done
done
