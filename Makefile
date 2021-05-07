# This file is in the public domain.

include build-system/config.mk

# List of all supported languages, add new languages here!
LANGUAGES="ar de en es fr hi it ja ko pt zh_Hant"

# All: build HTML pages in all languages and compile the
.PHONY: all
all: locale template
	env BASEURL=$(opt_baseurl) ./inc/make_site.py

# Extract translateable strings from jinja2 templates.
locale/messages.pot: template/*.j2 template/news/*.j2 common/*.j2 common/*.j2.inc
	env PYTHONPATH=$$PWD/inc:$$PYTHONPATH $(pybabel) extract -F locale/babel.map -o locale/messages.pot .

# Update translation (.po) files with new strings.
.PHONY: locale-update
locale-update: locale/messages.pot
	for lang in `echo $(LANGUAGES)`; do \
		$(msgmerge) -q -U -m --previous locale/$$lang/LC_MESSAGES/messages.po locale/messages.pot ; \
	done
	if $(grep) -nA1 '#-#-#-#-#' locale/*/LC_MESSAGES/messages.po; then \
	       	$(echo) -e "\nERROR: Conflicts encountered in PO files.\n"; \
		exit 1; \
	fi

# Compile translation files for use.
.PHONY: locale-compile
locale-compile:
	for lang in `echo $(LANGUAGES)`; do \
		echo compiling $$lang; \
		$(pybabel) -q compile -d locale -l $$lang --use-fuzzy ; \
	done

# Process everything related to gettext translations.
.PHONY: locale
locale: locale-update locale-compile

.PHONY: run
run: all
	$(browser) http://0.0.0.0:8000/rendered/en &
	$(python) -m http.server

variant = $(opt_variant)

ifndef variant
$(error variant is not set)
endif

.PHONY: install
install: all
	$(mkdir) -p $(prefix)/$(variant)
	$(cp) -r rendered/* $(prefix)/$(variant)/
	$(cp) -r rendered/.well-known/ $(prefix)/$(variant)/

.PHONY: clean
clean:
	$(rm) -rf __pycache__ *.pyc  *~ \.*~ \#*\#
	$(rm) -rf rendered/

.PHONY: submodules/update
submodules/update:
	$(git) submodule update --recursive --remote
