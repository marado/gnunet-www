# This file is in the public domain.

# All: build HTML pages in all languages and compile the
# TypeScript logic in web-common.
all: locale template
	cd web-common && tsc

# Extract translateable strings from jinga2 templates.
locale/messages.pot: *.j2 common/*.j2 common/*.j2.inc
	env PYTHONPATH="." pybabel extract -F locale/babel.map -o locale/messages.pot .

# Update translation (.po) files with new strings.
locale-update: locale/messages.pot
	pybabel update -i locale/messages.pot -d locale -l en --previous
	pybabel update -i locale/messages.pot -d locale -l de --previous
	pybabel update -i locale/messages.pot -d locale -l fr --previous
	pybabel update -i locale/messages.pot -d locale -l it --previous
	pybabel update -i locale/messages.pot -d locale -l es --previous

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
