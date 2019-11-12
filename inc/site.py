import os
import os.path
import sys
import re
import gettext
import glob
import codecs
import jinja2
import hashlib
from pathlib import Path, PurePosixPath
from ruamel.yaml import YAML
import inc.i18nfix
from inc.textproc import cut_news_text
from inc.fileproc import copy_files


class gen_site:
    def load_config(self, name="www.yml"):
        yaml = YAML(typ='safe')
        site_configfile = Path(name)
        return yaml.load(site_configfile)

    def gen_abstract(self, conf, name, member, pages, length):
        for item in conf[name]:
            item[member] = cut_news_text(item[pages], length)

    def run(self, root, conf, env):
        # os.chdir("..")
        print(os.getcwd())
        root = "../" + root
        for in_file in glob.glob(root + "/*.j2"):
            name, ext = re.match(r"(.*)\.([^.]+)$",
                                 in_file.rstrip(".j2")).groups()
            tmpl = env.get_template(in_file)

            def self_localized(other_locale):
                """
                Return URL for the current page in another locale.
                """
                return "../" + other_locale + "/" + in_file.replace(
                    root + '/', '').rstrip(".j2")

            def url_localized(filename):
                if root == "news":
                    return "../../" + locale + "/" + filename
                else:
                    return "../" + locale + "/" + filename

            def url_static(filename):
                if root == "news":
                    return "../../static/" + filename
                else:
                    return "../static/" + filename

            def url_dist(filename):
                if root == "news":
                    return "../../dist/" + filename
                else:
                    return "../dist/" + filename

            def svg_localized(filename):
                lf = filename + "." + locale + ".svg"
                if locale == "en" or not Path(lf).is_file():
                    return "../" + filename + ".svg"
                else:
                    return "../" + lf

            def url(x):
                # TODO: look at the app root environment variable
                # TODO: check if file exists
                #if root == "news":
                #    return "../" + "../" + x
                #else:
                #    return "../" + x
                return "../" + x

            for l in glob.glob("locale/*/"):
                locale = os.path.basename(l[:-1])

                tr = gettext.translation("messages",
                                         localedir="locale",
                                         languages=[locale])

                tr.gettext = i18nfix.wrap_gettext(tr.gettext)

                env.install_gettext_translations(tr, newstyle=True)

                content = tmpl.render(lang=locale,
                                      lang_full=conf["langs_full"][locale],
                                      url=url,
                                      meetingnotesdata=conf["meetingnotes"],
                                      newsdata=conf["newsposts"],
                                      videosdata=conf["videoslist"],
                                      self_localized=self_localized,
                                      url_localized=url_localized,
                                      url_static=url_static,
                                      url_dist=url_dist,
                                      svg_localized=svg_localized,
                                      filename=name + "." + ext)

                if root == "news":
                    out_name = "./rendered/" + locale + "/" + root + "/" + in_file.replace(
                        root + '/', '').rstrip(".j2")
                else:
                    out_name = "./rendered/" + locale + "/" + in_file.replace(
                        root + '/', '').rstrip(".j2")

                outdir = Path("rendered")
                if outdir.exists() is False:
                    sys.exit(1)

                if root == "news":
                    langdir = outdir / locale / root
                else:
                    langdir = outdir / locale

                try:
                    langdir.mkdir(parents=True, exist_ok=True)
                except e as FileNotFoundError:
                    print(e)

                with codecs.open(out_name, "w", encoding='utf-8') as f:
                    try:
                        print(Path.cwd())
                        f.write(content)
                    except e as Error:
                        print(e)
