#!/bin/sh

for f in $(git ls-files *.j2); do
    for ld in locale/*/; do
	l=$(basename $ld)
	echo "$f: $l"
	python template.py $f $l $(dirname $f)/$(basename $f .html.j2).$l.html
    done
done

for f in $(git ls-files common/*.j2); do
    for ld in locale/*/; do
	l=$(basename $ld)
	echo "$f: $l"
	python template.py $f $l $(dirname $f)/$(basename $f .inc.j2).$l.inc
    done
done
