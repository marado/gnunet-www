#!/usr/bin/env python3
# coding: utf-8
# This file is in the public domain.
#
# This script runs the jinja2 templating engine on an input template-file
# using the specified locale for gettext translations, and outputs
# the resulting (HTML) ouptut-file.
#
# Note that the gettext files need to be prepared first. This script
# is thus to be invoked via the Makefile.
#
# We import unicode_literals until people have understood how unicode
# with bytes and strings changed in python2->python3.
#
# Includes work derived from Jeff Knupp's "blug", which is licensed
# MIT license, (C) 2013 Jeff Knupp
#
from __future__ import unicode_literals
import os
import os.path
import sys
import re
import gettext
import glob
import codecs
import jinja2
import i18nfix
import collections
import datetime
import shutil
from ruamel import yaml

env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                         extensions=["jinja2.ext.i18n"],
                         lstrip_blocks=True,
                         trim_blocks=True,
                         undefined=jinja2.StrictUndefined,
                         autoescape=False)
# DEBUG OUTPUT:
if (os.getenv("DEBUG")):
    print(sys.path)

langs_full = {"en": "English", "fr": "Français", "it": "Italiano", "es": "Español", "de": "Deutsch"}

# Caveat: might include error in transcription, needs to be checked on
# full unicode system.
umlaute_dict = {
        'ä': 'ae',
        'ö': 'oe',
        'Ä': 'Ae',
        'Ö': 'Oe',
        'Ü': 'Ue',
        'ß': 'ss',
        }


config = yaml.safe_load(open('config.yaml'))

def replace_german_umlaute(string_in):
    utf8_string = string_in.encode('utf-8')
    for k in umlaute_dict.keys():
        utf8_string = utf8_string.replace(k, umlaute_dict[k])
    return utf8_string.decode()

# if we use relative URLs, we will never need this. This is a
# more generalized variant of svg_localized() which we inherited
# from taler.net
def imagefile_localized(filename, locale, extension):
    lf = filename + "." + locale + "." + extension
    if locale == "en" or not os.path.isfile(lf):
        return "../" + filename + "." + extension
    else:
        return "../" + lf

def generate_post_file_name(title):
    """Return the filename a post should use based on its title and date"""
    return ''.join(char for char in title.lower() if (
        char.isalnum() or char == ' ')
        ).replace(' ', '-')


def generate_post_file_path(title, date):
    """Return the relative path to a post based on its title and date"""
    return os.path.join(
        datetime.datetime.strftime(date, '%Y/%m/%d/'),
        generate_post_file_name(title))


def extract_metadata(input_file, pattern):
    """
    Don't try this at home warning:
    We have decided to attach metadata to quasi-html files via
    html-comments. We extract PATTERN from INPUT_FILE as a means
    to grab for example a title + date + author
    and use this to produce a list of posts later on.
    Brachialsimplistic: using html for what it wasn't designed to
    do simply because the alternatives suck even more for now.
    """
    file = codecs.open(input_file, "rb")
    input = file.read()
    find = re.search('<!--(.' + pattern + '.*?)-->', input.decode('utf-8'))
    intermediate = find.group(1).strip()
    int_list = intermediate.split(':', 1)
    result = int_list[1].strip()
    result_split = int_list[1].strip().split()
    if pattern == 'categories':
        return result_split
    else:
        return result


def get_all_posts(content_dir, blog_prefix, canonical_url, blog_root=None):
    """Return a list of dictionaries representing converted posts"""
    input_files = os.listdir(content_dir)
    all_posts = list()

    for post_file_name in input_files:
        if os.path.splitext(post_file_name)[1] != ".inc":
            continue

        post = dict()
        post_output_path = os.path.join(content_dir, post_file_name)
        with open(post_output_path, encoding='ascii') as post_file:
            post_file_buffer = post_file.read()

        # parse the html file for metadata
        post['title'] = extract_metadata(post_file_name, 'title')
        post['author'] = extract_metadata(post_file_name, 'author')
        post['date'] = extract_metadata(post_file_name, 'date')

        read_in_file = codecs.open(post_file_name, 'rb')
        read_in_input = read_in_file.read().decode('utf-8')
        post['body'] = read_in_input
        post['categories'] = extract_metadata(post_file_name, 'categories')

        # Construct datetime from the provided one
        post['date'] = datetime.datetime.strptime((post['date']), '%Y-%m-%d %H:%M')

        # In general we know the layout on disk must match the generated urls
        # This doesn't hold in the case that there is an appendix to the
        # domain that the site resides on. For example, if my WidgetFactory
        # marketing department blog lived at
        # www.widgetfactory.com/marketing/blog/, we would generate the
        # files in the /blog sub-directory but the links would need to
        # include /marketing/blog
        post['relative_path'] = generate_post_file_path(post['title'],
                                                        post['date'])

        if blog_prefix:
            post['relative_path'] = os.path.join(
                blog_prefix, post['relative_path'])

        if blog_root:
            post['relative_url'] = os.path.join('/', blog_root,
                                                post['relative_path'])
        else:
            post['relative_url'] = os.path.join('/', post['relative_path'])

        post['canonical_url'] = canonical_url + post['relative_url']

        all_posts.append(post)
    return all_posts


def create_path_to_file(path):
    """Given a path, make sure all intermediate directories exist;
    create them if they don't"""
    if not os.path.splitext(path)[1]:
        path += '/'
    else:
        path = os.path.dirname(path)
    if not os.path.exists(path):
        os.makedirs(path)


def generate_post(post, template_variables, template_environment):
    """Generate a single post's HTML file"""
    output_path = os.path.join(template_variables['output_dir'],
                               post['relative_path'], 'index.html')

    if not post['body']:
        raise EnvironmentError('No content for post [{post}] found.'.format(
            post=post['relative_path']))

    # Need to keep 'post' and 'site' variables separate
    post_vars = {'post': post}

    template_variables.update(post_vars)
    template = template_environment.get_template('post_index.html')
    create_path_to_file(output_path)
    with open(output_path, 'w') as output:
        output.write(template.render(template_variables))


def generate_static_page(template_variables, output_dir, template,
                         filename='index.html'):
    """Generate a static page"""
    create_path_to_file(output_dir)
    with open(
        os.path.join(
            output_dir, filename), 'w', encoding='ascii') as output_file:
        output_file.write(template.render(template_variables))

def generate_static_files(site_config, posts, categories, template_environment):
    """Generate all 'static' files, files not based on markdown conversion"""
    # Generate an index.html at both the root level and 
    # the 'blog' level, so both www.foo.com and
    # www.foo.com/blog can serve the blog
    list_template = template_environment.get_template('list.html.j2')
    archives_template = template_environment.get_template('archives.html')
    atom_template = template_environment.get_template('atom.xml')
    about_template = template_environment.get_template('about.html.j2')

    canonical_url_base = site_config['url']
    canonical_blog_base = '{url}/{blog_prefix}/'.format(
            url=canonical_url_base,
            blog_prefix=site_config['blog_prefix'])

    # Generate main 'index.html' and '/blog/index.html' pages,
    # showing the five most recent posts
    template_variables = copy(site_config)
    template_variables['next_page'] = 1
    template_variables['canonical_url'] = template_variables['url']
    template_variables['current_posts'] = posts[:5]
    generate_static_page(template_variables,
                         site_config['output_dir'], list_template)

    template_variables['canonical_url'] = canonical_blog_base
    generate_static_page(template_variables,
                         site_config['blog_dir'], list_template)

    # TODO: simplify. for-loop?
    # Generate about page
    template_variables['canonical_url'] = canonical_url_base + '/about/'
    generate_static_page(template_variables,
                         os.path.join(site_config['output_dir'], 'about'),
                         about_template)
    # Generate architecture page
    template_variables['canonical_url'] = canonical_url_base + '/architecture/'
    generate_static_page(template_variables,
                         os.path.join(site_config['output_dir'], 'architecture'),
                         architecture_template)
    # Generate contact page
    template_variables['canonical_url'] = canonical_url_base + '/contact/'
    generate_static_page(template_variables,
                         os.path.join(site_config['output_dir'], 'contact'),
                         contact_template)
    # Generate copyright page
    template_variables['canonical_url'] = canonical_url_base + '/copyright/'
    generate_static_page(template_variables,
                         os.path.join(site_config['output_dir'], 'copyright'),
                         copyright_template)
    # Generate developers page
    template_variables['canonical_url'] = canonical_url_base + '/developers/'
    generate_static_page(template_variables,
                         os.path.join(site_config['output_dir'], 'developers'),
                         developers_template)
    # Generate download page
    template_variables['canonical_url'] = canonical_url_base + '/download/'
    generate_static_page(template_variables,
                         os.path.join(site_config['output_dir'], 'download'),
                         download_template)
    # Generate engage page
    template_variables['canonical_url'] = canonical_url_base + '/engage/'
    generate_static_page(template_variables,
                         os.path.join(site_config['output_dir'], 'engage'),
                         engage_template)
    # Generate ev page
    template_variables['canonical_url'] = canonical_url_base + '/ev/'
    generate_static_page(template_variables,
                         os.path.join(site_config['output_dir'], 'ev'),
                         ev_template)
    # Generate faq page
    template_variables['canonical_url'] = canonical_url_base + '/faq/'
    generate_static_page(template_variables,
                         os.path.join(site_config['output_dir'], 'faq'),
                         faq_template)
    # Generate glossary page
    template_variables['canonical_url'] = canonical_url_base + '/glossary/'
    generate_static_page(template_variables,
                         os.path.join(site_config['output_dir'], 'glossary'),
                         glossary_template)
    # Generate gnurl page
    template_variables['canonical_url'] = canonical_url_base + '/gnurl/'
    generate_static_page(template_variables,
                         os.path.join(site_config['output_dir'], 'gnurl'),
                         gnurl_template)
    # Generate gsoc-2018-gnunet-webui page
    template_variables['canonical_url'] = canonical_url_base + '/gsoc-2018-gnunet-webui/'
    generate_static_page(template_variables,
                         os.path.join(site_config['output_dir'], 'gsoc-2018-gnunet-webui'),
                         gsoc-2018-gnunet-webui_template)
    # Generate gsoc page
    template_variables['canonical_url'] = canonical_url_base + '/gsoc/'
    generate_static_page(template_variables,
                         os.path.join(site_config['output_dir'], 'gsoc'),
                         gsoc_template)
    # Generate index page
    template_variables['canonical_url'] = canonical_url_base + '/index/'
    generate_static_page(template_variables,
                         os.path.join(site_config['output_dir'], 'index'),
                         index_template)
    # Generate install page
    template_variables['canonical_url'] = canonical_url_base + '/install/'
    generate_static_page(template_variables,
                         os.path.join(site_config['output_dir'], 'install'),
                         install_template)
    # Generate install-on-archpi page
    template_variables['canonical_url'] = canonical_url_base + '/install-on-archpi/'
    generate_static_page(template_variables,
                         os.path.join(site_config['output_dir'], 'install-on-archpi'),
                         install-on-archpi_template)
    # Generate install-on-debian9 page
    template_variables['canonical_url'] = canonical_url_base + '/install-on-debian9/'
    generate_static_page(template_variables,
                         os.path.join(site_config['output_dir'], 'install-on-debian9'),
                         install-on-debian9_template)
    # Generate install-on-macos page
    template_variables['canonical_url'] = canonical_url_base + '/install-on-macos/'
    generate_static_page(template_variables,
                         os.path.join(site_config['output_dir'], 'install-on-macos'),
                         install-on-macos_template)
    # Generate install-on-netbsd page
    template_variables['canonical_url'] = canonical_url_base + '/install-on-netbsd/'
    generate_static_page(template_variables,
                         os.path.join(site_config['output_dir'], 'install-on-netbsd'),
                         install-on-netbsd_template)
    # Generate install-on-ubuntu1804 page
    template_variables['canonical_url'] = canonical_url_base + '/install-on-ubuntu1804/'
    generate_static_page(template_variables,
                         os.path.join(site_config['output_dir'], 'install-on-ubuntu1804'),
                         install-on-ubuntu1804_template)
    # Generate team page
    template_variables['canonical_url'] = canonical_url_base + '/team/'
    generate_static_page(template_variables,
                         os.path.join(site_config['output_dir'], 'team'),
                         team_template)
    # Generate use page
    template_variables['canonical_url'] = canonical_url_base + '/use/'
    generate_static_page(template_variables,
                         os.path.join(site_config['output_dir'], 'use'),
                         use_template)
    # Generate video page    
    template_variables['canonical_url'] = canonical_url_base + '/video/'
    generate_static_page(template_variables,
                         os.path.join(site_config['output_dir'], 'video'),
                         video_template)

    # Generate blog archives page
    template_variables['all_posts'] = posts
    template_variables['canonical_url'] = canonical_blog_base + 'archives/'
    generate_static_page(template_variables,
                         os.path.join(site_config['blog_dir'],
                         'archives'), archives_template)

    # Generate atom.xml feed
    template_variables['now'] = datetime.datetime.now().isoformat()
    generate_static_page(template_variables, site_config['output_dir'],
                         atom_template, 'atom.xml')

    # Generate a category "archive" page listing the posts in each category
    for category, posts in categories.items():
        template_variables['all_posts'] = posts
        generate_static_page(template_variables, os.path.join(
            site_config['blog_dir'],
           'categories', category), archives_template)
        generate_static_page(template_variables, os.path.join(
            site_config['blog_dir'],
            'categories', category), atom_template, 'atom.xml')

def generate_pagination_pages(site_config, all_posts, template):
    """Generate the additional index.html files required for pagination"""
    template_variables = copy(site_config)
    num_posts = len(all_posts)
    for index, page in enumerate(
            [all_posts[index:index + 5] for index in range(5, num_posts, 5)]):
        # Overcome the fact that enumerate is 0-indexed
        current_page = index + 1
        # Since we're reusing the index.html template, make it think
        # these posts are the only ones
        template_variables['current_posts'] = page
        template_variables['next_page'] = current_page + 1

        # if we've reached the "last" page, don't present a link to older
        # content
        if (current_page * 5) >= num_posts - 5:
            template_variables['next_page'] = None

        output_dir = os.path.join(site_config['blog_dir'],
                                  'page', str(current_page))
        generate_static_page(template_variables, output_dir, template)


def generate_all_files(site_config):
    """Generate all HTML files from the content directory using the site-wide
    configuration"""
    all_posts = get_all_posts(site_config['content_dir'],
                              site_config['blog_prefix'],
                              site_config['url'],
                              site_config['blog_root'])
    all_posts.sort(key=lambda i: i['date'], reverse=True)
    categories = collections.defaultdict(list)
    for post in all_posts:
        for category in post['categories']:
            categories[category].append(post)

    config['now'] = datetime.datetime.now().isoformat()

    template_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(
                                              site_config['template_dir']))

    generate_static_files(site_config, all_posts,
                          categories, template_environment)

    generate_pagination_pages(site_config, all_posts,
                              template_environment.get_template('list.html.j2'))

    for index, post in enumerate(all_posts):
        try:
            post['post_previous'] = all_posts[index + 1]
        except IndexError:
            post['post_previous'] = all_posts[0]
        generate_post(post, site_config, template_environment)

def copy_static_content(output_dir, root_dir):
    """Copy (if necessary) the static content to the appropriate directory"""
    if os.path.exists(output_dir):
        print ('Removing old content...')
        shutil.rmtree(output_dir)
        shutil.copytree(os.path.join(root_dir, 'static'), output_dir)

def generate_site():
    """Generate the static HTML pages based on the configuration 
    file and content directory"""
    site_config = config

    site_config['blog_dir'] = os.path.join(
        site_config['output_dir'], 
        site_config['blog_prefix'])
    print ('Generating...')

    copy_static_content(site_config['output_dir'], os.getcwd())
    generate_all_files(site_config)

    return True

def main():
    generate_site()

if __name__ == '__main__':
    sys.exit(main())


'''
for in_file in glob.glob("template/*.j2"):
    name, ext = re.match(r"(.*)\.([^.]+)$", in_file.rstrip(".j2")).groups()
    tmpl = env.get_template(in_file)

    def self_localized(other_locale):
        """
        Return URL for the current page in another locale.
        """
        return "../" + other_locale + "/" + in_file.replace('template/', '').rstrip(".j2")

    def url_localized(filename):
        return "../" + locale + "/" + filename

    def svg_localized(filename):
        lf = filename + "." + locale + ".svg"
        if locale == "en" or not os.path.isfile(lf):
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

        content = tmpl.render(lang=locale,
                              lang_full=langs_full[locale],
                              url=url,
                              self_localized=self_localized,
                              url_localized=url_localized,
                              svg_localized=svg_localized,
                              filename=name + "." + ext)
        out_name = "./rendered/" + locale + "/" + in_file.replace('template/', '').rstrip(".j2")
        os.makedirs("./rendered/" + locale, exist_ok=True)
        with codecs.open(out_name, "w", encoding='utf-8') as f:
            f.write(content)
'''
