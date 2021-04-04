# This file is in the public domain.

include build-system/config.mk

# List of all supported languages, add new languages here!
LANGUAGES="en de fr it es ar hi ja ko pt zh_Hant"

# All: build HTML pages in all languages and compile the
# TypeScript logic in web-common.
.PHONY: all
all: locale template
#	($(cp) rendered/static/javascript.html rendered/javascript.html)
	($(cp) rendered/static/robots.txt rendered/robots.txt)
	($(cp) rendered/static/robots.txt rendered/dist/robots.txt)
	(for lang in `echo $(LANGUAGES)` ; do \
		$(cp) rendered/static/robots.txt rendered/$$lang/robots.txt; \
	done)
	($(python) inc/make_sitemap.py -i rendered)
	($(cp) sitemap.xml rendered/sitemap.xml)
	($(cp) sitemap.xml rendered/en/sitemap.xml)
	(for lang in `echo $(LANGUAGES)` ; do \
		$(cp) rendered/sitemap.xml rendered/$$lang ; \
	done)
	($(cp) -R images rendered/static/)
	(for lang in `echo $(LANGUAGES)` ; \
		do $(cp) -R images rendered/$$lang ; \
	done)
	($(cp) -R web-common/* rendered/static/)
	(cd rendered; \
		for lang in `echo $(LANGUAGES)`; do \
			$(cp) $$lang/rss.xml $$lang/news/rss.xml; \
	done)
	(for d in dist ; do \
		$(cp) -R $$d rendered/ ; \
	done)
#	($(cp) -R pdf rendered/static/)
	($(mkdir) -p rendered/.well-known ; $(cp) .well-known/security.txt rendered/.well-known/)

# Extract translateable strings from jinja2 templates.
locale/messages.pot: template/*.j2 common/*.j2 common/*.j2.inc
	$(python) inc/mybabel.py $(pybabel) extract -F locale/babel.map -o locale/messages.pot .

# Update translation (.po) files with new strings.
.PHONY: locale-update
locale-update: locale/messages.pot
	(for lang in `echo $(LANGUAGES)`; do \
		$(msgmerge) -q -U -m --previous locale/$$lang/LC_MESSAGES/messages.po locale/messages.pot ; \
	done)
	if $(grep) -nA1 '#-#-#-#-#' locale/*/LC_MESSAGES/messages.po; then $(echo) -e "\nERROR: Conflicts encountered in PO files.\n"; exit 1; fi

# Compile translation files for use.
.PHONY: locale-compile
locale-compile:
	(for lang in `echo $(LANGUAGES)`; do \
		$(pybabel) -q compile -d locale -l $$lang --use-fuzzy ; \
	done)

# Process everything related to gettext translations.
.PHONY: locale
locale: locale-update locale-compile

# Run the jinja2 templating engine to expand templates to HTML
# incorporating translations.
template: locale-compile
	$(python) ./make_site.py

.PHONY: run
run: all
	$(browser) http://0.0.0.0:8000/rendered/en &
	$(python) -m http.server

.PHONY: install
install: all
	$(mkdir) -p $(prefix)/
	$(cp) -r rendered/* $(prefix)/
	$(cp) -r rendered/.well-known/ $(prefix)/

.PHONY: uninstall
uninstall:
	$(rm) -rf $(prefix)/

.PHONY: clean
clean:
	$(rm) -rf __pycache__ *.pyc  *~ \.*~ \#*\#
	$(rm) -rf rendered/

submodules/update:
	$(git) submodule update --recursive --remote
