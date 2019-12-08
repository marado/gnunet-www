#
# Copyright (C) 2017, 2018, 2019 GNUnet e.V.
#
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided the copyright
# notice and this notice are preserved.  This file is offered as-is,
# without any warranty.
#
# ----

# All: build HTML pages in all languages and compile the
# TypeScript logic in web-common.

# Hardly anyone seems to read README files anymore, so keep this note here:
# Don't remove the variables for python etc. They exist
# because one system sticks with PEPs, and others opt
# for installing every version side-by-side,
# Same goes for babel.

include config.mk

all: locale template
	($(cp) rendered/static/robots.txt rendered/robots.txt)
	($(cp) rendered/static/stage.robots.txt rendered/stage.robots.txt)
	($(cp) rendered/static/robots.txt rendered/dist/robots.txt)
	(for lang in en de es fr it ; do \
		$(cp) rendered/static/robots.txt rendered/$$lang/robots.txt ; \
	done)
	($(python) inc/make_sitemap.py -i rendered)
	($(cp) sitemap.xml rendered/sitemap.xml)
	($(cp) sitemap.xml rendered/en/sitemap.xml)
	($(cp) static/moved.html rendered/frontpage.html)
	(cd rendered; $(ln) -fs frontpage.html frontpage)
	($(cp) static/moved_gsoc.html rendered/gsoc.html)
	(cd rendered; $(ln) -fs gsoc.html gsoc)
	($(cp) static/moved_gns.html rendered/gns.html)
	(cd rendered; $(ln) -fs gns.html gns)
	($(mkdir) -p rendered/node ; $(cp) static/moved_about.html rendered/node/about.html)
	(cd rendered/node ; $(ln) -fs about.html 397)
	($(cp) static/moved_about.html rendered/about.html)
	(cd rendered ; $(ln) -fs about.html philosophy)
	(cd rendered; \
		for lang in en de es fr it; do \
			$(cp) $$lang/rss.xml $$lang/news/rss.xml; \
		done)

# Extract translateable strings from jinja2 templates.
# Because of the local i18nfix extractor module we need
# to set the pythonpath before invoking pybabel.
locale/messages.pot: common/*.j2.inc template/*.j2
	$(env) PYTHONPATH=. $(pybabel) -q extract -F locale/babel.map -o locale/messages.pot .

# Update translation (.po) files with new strings.
locale-update: locale/messages.pot
	(for lang in en de es fr it; do \
		$(msgmerge) -q -U -m --previous locale/$$lang/LC_MESSAGES/messages.po locale/messages.pot ; \
	done)
	if $(grep) -nA1 '#-#-#-#-#' locale/*/LC_MESSAGES/messages.po; then echo -e "\nERROR: Conflicts encountered in PO files.\n"; exit 1; fi

# Compile translation files for use.
locale-compile:
	(for lang in en de fr it es; do \
		$(pybabel) -q compile -d locale -l $$lang --use-fuzzy ; \
	done)

# Process everything related to gettext translations.
locale: locale-update locale-compile

# Run the jinja2 templating engine to expand templates to HTML
# incorporating translations.
template: locale-compile
	$(python) ./make_site.py

it: template

current_dir = $(shell pwd)

run: all
	$(browser) http://0.0.0.0:8000/rendered/en &
	$(python) -m http.server


# docker-all: Build using a docker image which contains all the needed
# packages.

docker: docker-all

docker-all:
	$(docker) build -t gnunet-www-builder .
	# Importing via the shell like this is hacky,
	# but after trying lots of other ways, this works most reliably...
	$(python) -c 'import i18nfix'
	$(docker) run --rm -v $$(pwd):/tmp/ --user $$(id -u):$$(id -g) gnunet-www-builder

clean:
	$(rm) -rf __pycache__
	$(rm) -rf en/ de/ fr/ it/ es/ ru/
	$(rm) -rf rendered/
	$(rm) -rf *.pyc *~ \.*~ \#*\#
