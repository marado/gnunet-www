#!/usr/bin/env python3
# This file is in the public domain.
#
# This script runs the jinja2 templating engine on an input template-file
# using the specified locale for gettext translations, and outputs
# the resulting (HTML) ouptut-file.
#
# Note that the gettext files need to be prepared first. This script
# is thus to be invoked via the Makefile.
import os
import os.path
import sys
import re
import gettext
import jinja2
import glob
import codecs
import os
import i18nfix

env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                         extensions=["jinja2.ext.i18n"],
                         lstrip_blocks=True,
                         trim_blocks=True,
                         undefined=jinja2.StrictUndefined,
                         autoescape=False)

langs_full = {"en": "English",
              "fr": "Français",
              "it": "Italiano",
              "es": "Español",
              "de": "Deutsch",
              "ru": "Ру́сский язы́к"}

for in_file in glob.glob("*.j2"):
    name, ext = re.match(r"(.*)\.([^.]+)$", in_file.rstrip(".j2")).groups()
    tmpl = env.get_template(in_file)

    def self_localized(other_locale):
        """
        Return URL for the current page in another locale.
        """
        return "../" + other_locale + "/" + in_file.rstrip(".j2")

    def url_localized(filename):
        return "../" + locale + "/" + filename

    def svg_localized(filename):
        lf = filename + "." + locale + ".svg"
        if "en" == locale or not os.path.isfile (lf):
            return "../" + filename + ".svg"
        else:
            return "../" + lf

    def url(x):
        # TODO: look at the app root environment variable
        # TODO: check if file exists
        return "../" + x

    for l in glob.glob("locale/*/"):
        locale = os.path.basename(l[:-1])

        tr = gettext.translation("messages",
                                 localedir="locale",
                                 languages=[locale])

        tr.gettext = i18nfix.wrap_gettext(tr.gettext)

        env.install_gettext_translations(tr, newstyle=True)


        content = tmpl.render(
                lang=locale,
                lang_full=langs_full[locale],
                url=url,
                self_localized=self_localized,
                url_localized=url_localized,
                svg_localized=svg_localized,
                filename=name + "." + ext)
        out_name = "./" + locale + "/" + in_file.rstrip(".j2")
        os.makedirs("./" + locale, exist_ok=True)
        with codecs.open(out_name, "w", "utf-8") as f:
            f.write(content)
