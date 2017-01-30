#!/bin/sh

for f in $(git ls-files *.j2); do
    for ld in locale/*/; do
	l=$(basename $ld)
	echo "$f: $l"
	python template.py $f $l
    done
done
