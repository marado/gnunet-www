# This file is in the public domain.

include build-system/config.mk

# All: build HTML pages in all languages and compile the
.PHONY: all
all:
	./inc/update-messages
	env "BASEURL=$(opt_baseurl)" ./inc/build-site

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
