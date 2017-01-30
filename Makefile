all: locale template
	cd web-common && tsc

locale/messages.pot: *.j2
	pybabel extract -F locale/babel.map -o locale/messages.pot .

locale-update: locale/messages.pot
	pybabel update -i locale/messages.pot -d locale -l en --previous
	pybabel update -i locale/messages.pot -d locale -l de --previous
	pybabel update -i locale/messages.pot -d locale -l fr --previous
	pybabel update -i locale/messages.pot -d locale -l it --previous
	pybabel update -i locale/messages.pot -d locale -l es --previous

	if grep -nA1 '#-#-#-#-#' locale/*/LC_MESSAGES/messages.po; then echo -e "\nERROR: Conflicts encountered in PO files.\n"; exit 1; fi

locale-compile:
	pybabel compile -d locale -l en --use-fuzzy
	pybabel compile -d locale -l de --use-fuzzy
	pybabel compile -d locale -l fr --use-fuzzy
	pybabel compile -d locale -l it --use-fuzzy
	pybabel compile -d locale -l es --use-fuzzy

locale: locale-update locale-compile

template: locale-compile
	./template.sh
