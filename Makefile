# Makefile for NetBSD make (portable version: "bmake"),
# GNU make will find 'GNUmakefile' first and use that file instead.
# This file is in the public domain.
#
# I keep and maintain this file for personal use, it is faster than
# the gmake approach.

.include "config.mk"

DESTDIR=$(prefix)

_LOCALELIST= en de fr it es
_DIRLIST= dist static

.PHONY:	all run locale-compile locale install clean css

.OBJDIR=rendered

# Work this into an mk file

# All: build HTML pages in all languages and compile the
# TypeScript logic in web-common.
all: css locale template
.for _dir in ${_DIRLIST}
	$(cp) -R ${_dir} rendered/
.endfor
.for _lang in ${_LOCALELIST}
	($(cp) rendered/static/robots.txt rendered/${_lang})
	($(cp) rendered/static/stage.robots.txt rendered/${_lang})
	($(cp) rss.xml rendered/${_lang})
.endfor
.for _lang in ${_LOCALELIST}
	(cd rendered/${_lang}; $(ln) -fs ../dist dist)
	(cd rendered/${_lang}; $(ln) -fs ../dist/css css)
	(cd rendered/${_lang}; $(ln) -fs ../static static)
.endfor
	($(cp) rendered/static/robots.txt rendered/dist/robots.txt)
	($(cp) favicon.ico rendered/)
	$(sh) make_sitemap.sh
.for _lang in ${_LOCALELIST}
	($(cp) rendered/sitemap.xml rendered/${_lang})
.endfor
	($(cp) static/moved.html rendered/frontpage.html)
	(cd rendered; $(ln) -fs frontpage.html frontpage)
	($(cp) static/moved_gsoc.html rendered/gsoc.html)
	(cd rendered; $(ln) -fs gsoc.html gsoc)
	($(cp) static/moved_gns.html rendered/gns.html)
	(cd rendered; $(ln) -fs gns.html gns)
	($(mkdir) -p rendered/node; $(cp) static/moved_about.html rendered/node/about.html)
	(cd rendered/node ; $(ln) -fs about.html 397)
	($(cp) static/moved_about.html rendered/about.html)
	(cd rendered ; $(ln) -fs about.html philosophy)
#.for _lang in ${_LOCALELIST}
#	$(sh) rssg rendered/${_lang}/news/index.html 'title' > rendered/${_lang}/rss.xml
#.endfor

# Extract translateable strings from jinja2 templates.
locale/messages.pot: template/*.j2 common/*.j2 common/*.j2.inc
	$(env) PYTHONPATH="." $(pybabel) -q extract -F locale/babel.map -o locale/messages.pot .

# Update translation (.po) files with new strings.
locale-update: locale/messages.pot
.for _lang in ${_LOCALELIST}
	$(msgmerge) -q -U -m --previous locale/${_lang}/LC_MESSAGES/messages.po locale/messages.pot
.endfor
	if $(grep) -nA1 '#-#-#-#-#' locale/*/LC_MESSAGES/messages.po; then \
		$(echo) -e "\nERROR: Conflicts encountered in PO files.\n"; \
		exit 1; \
	fi

# Compile translation files for use.
locale-compile:
.for _lang in ${_LOCALELIST}
	$(pybabel) -q compile -d locale -l ${_lang} --use-fuzzy
.endfor

# Process everything related to gettext translations.
locale: locale-update locale-compile

# Run the jinja2 templating engine to expand templates to HTML
# incorporating translations.
template: locale-compile
	$(python) ./template.py

css:
	$(sassc) static/styles.sass static/styles.css

run:
.if defined(browser) && !empty(DESTDIR) && !empty(python)
	$(browser) http://0.0.0.0:8000/rendered/en/ &
	$(python) -m http.server
.endif

install:
	$(mkdir) -p $(prefix)/share/gnunet-www
	$(cp) -R rendered/* $(prefix)/share/gnunet-www

uninstall:
	$(rm) -rf $(prefix)/share/gnunet-www

submodules/init:
	$(git) submodule update --init --recursive

submodules/update:
	$(git) submodule update --recursive --remote

docker: docker-all

docker-all:
.if defined(docker)
	$(docker) build -t gnunet-www-builder .
	# Importing via the shell like this is hacky,
	# but after trying lots of other ways, this works most reliably...
	$(python) -c 'import i18nfix'
	$(docker) run --rm -v $$(pwd):/tmp/ --user $$(id -u):$$(id -g) gnunet-www-builder
.endif

CLEANFILES+=    *.pyc *~ \.*~ *.core

.include <bsd.prog.mk>
