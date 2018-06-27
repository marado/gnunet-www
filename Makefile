# This file is in the public domain.

# All: build HTML pages in all languages and compile the
# TypeScript logic in web-common.

PYTHONPATH="$PYTHONPATH:$(pwd)"

all: locale template

# Extract translateable strings from jinga2 templates.
locale/messages.pot: *.j2 common/*.j2.inc
	pybabel extract -F locale/babel.map -o locale/messages.pot .

# Update translation (.po) files with new strings.
locale-update: locale/messages.pot
	msgmerge -U -m --previous locale/en/LC_MESSAGES/messages.po locale/messages.pot 
	msgmerge -U -m --previous locale/de/LC_MESSAGES/messages.po locale/messages.pot
	msgmerge -U -m --previous locale/fr/LC_MESSAGES/messages.po locale/messages.pot
	msgmerge -U -m --previous locale/es/LC_MESSAGES/messages.po locale/messages.pot
	msgmerge -U -m --previous locale/it/LC_MESSAGES/messages.po locale/messages.pot

	if grep -nA1 '#-#-#-#-#' locale/*/LC_MESSAGES/messages.po; then echo -e "\nERROR: Conflicts encountered in PO files.\n"; exit 1; fi

# Compile translation files for use.
locale-compile:
	pybabel compile -d locale -l en --use-fuzzy
	pybabel compile -d locale -l de --use-fuzzy
	pybabel compile -d locale -l fr --use-fuzzy
	pybabel compile -d locale -l it --use-fuzzy
	pybabel compile -d locale -l es --use-fuzzy

# Process everything related to gettext translations.
locale: locale-update locale-compile

# Run the jinga2 templating engine to expand templates to HTML
# incorporating translations.
template: locale-compile
	./template.py

it: template
