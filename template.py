#!/usr/bin/env python3
# coding: utf-8
#
# Copyright (C) 2017, 2018, 2019 GNUnet e.V.
#
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided the copyright
# notice and this notice are preserved.  This file is offered as-is,
# without any warranty.
#
# ----
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
# from __future__ import unicode_literals
import os
import os.path
import sys
import re
import gettext
import glob
import codecs
import jinja2
import i18nfix
from pathlib import Path
import hashlib

# TODO: Turn repetition into a class.

env = jinja2.Environment(loader=jinja2.FileSystemLoader(
    os.path.dirname(__file__)),
                         extensions=["jinja2.ext.i18n"],
                         lstrip_blocks=True,
                         trim_blocks=True,
                         undefined=jinja2.StrictUndefined,
                         autoescape=False)
# DEBUG OUTPUT:
if (os.getenv("DEBUG")):
    print(sys.path)

langs_full = {
    "en": "English",
    "fr": "Français",
    "it": "Italiano",
    "es": "Español",
    "de": "Deutsch"
}

# A construction has:
# symlinks (dict)
# staticfiles (dict)
# robot.txt files (list)
# locales (list)
# shells out to siteindex (todo: python siteindex)
# generation_directories: the one we are building right now
#                         the one we will be replacing
#                         other directories get trashed upon successful build

symlinks = {
    "frontpage.html": "frontpage",
    "gsoc.html": "gsoc",
    "about.html": "philosophy",
    "gns.html": "gns",
    "node/about.html": "397"
}

# Mostly from static/ to rendered/
staticfiles = {
    "favicon.ico": "favicon.ico",
    "moved.html": "frontpage.html",
    "robots.txt": ["static", "dist", list(langs_full)],
    "moved_gsoc.html": "gsoc.html",
    "moved_about.html": "about.html",
    "moved_gns.html": "gns.html"
}


def localized(filename, locale, *args):
    if len(args) == 0:
        return "../" + locale + "/" + filename
    ext = kwargs.get('ext', None)
    if ext is not None:
        lf = filename + "." + locale + "." + ext
        lp = Path(lf)
        if locale == "en" or not lp.is_file():
            return "../" + filename + "." + ext
        else:
            return "../" + lf


def fileop(infile, outfile, action):
    """
    infile: inputfile, Path object
    outfile: outputfile, Path object
    action: action if any, String
    """
    i = Path(infile)
    o = Path(outfile)
    outdir = Path("rendered")
    if i.is_file() is not False:
        if action == "copy":
            # Write content of i to o.
            o.write_text(i.read_text())
        if action == "link":
            o.symlink_to(i)


def write_name(filename, infile, locale, replacer):
    return "./rendered/" + locale + "/" + infile.replace(replacer,
                                                         '').rstrip(".j2")


def sha256sum(_):
    sha256 = hashlib.sha256()
    with io.open(_, mode="rb") as fd:
        content = fd.read()
        sha256.update(content)
    return sha256.hexdigest()


def walksum(_):
    sha256 = hashlib.sha256()
    x = Path(_)
    if not x.exists():
        return -1
    try:
        for root, directories, files in os.walk(_):
            for names in sorted(files):
                filepath = os.path.join(root, names)
                try:
                    fl = open(filepath, 'rb')
                except:
                    fl.close()
                    continue
                while 1:
                    buf = fl.read(4096)
                    if not buf:
                        break
                    sha256.update(hashlib.sha256(buf).hexdigest())
                fl.close()
    except:
        import traceback
        traceback.print_exc()
        return -2
    return sha256.hexdigest()


def rm_rf(directory):
    directory = Path(directory)
    for child in directory.glob('*'):
        if child.is_file():
            child.unlink()
        else:
            rm_rf(child)
    directory.rmdir()


# This generates and switches sites generations, preventing
# in-place modification of the website.
# * save old generation directory name
# * jinja2 creates content in "rendered" (happened before calling this function)
# * calculate sum of "rendered"
# * move "rendered" to out/$sum
# * remove symlink "html_dir"
# * symlink out/$sum to "html_dir"
# * delete old generation directory
def generation_dir(htmldir):
    oldgen = Path(htmldir).resolve()
    # precondition: jinja2 has created the files in "rendered".
    newgen = Path("rendered")
    newgen_sum = walksum(newgen)
    outdir = Path("out")
    outdir.mkdir(parents=True, exist_ok=True)
    newgen_target = Path("out") / newgen_sum
    newgen.rename(newgen_target)
    html = Path(htmldir)
    html.unlink()
    fileop(newgen, html, "link")
    rm_rf(oldgen)


def copy_static(locale, indict):
    for key, value in indict.items():
        print(locale + "/" + key + " ...to... " + locale + "/" + value)


# TODO: Move the lists elsewhere?

meetingnotes = [
    { "year": "2013", "date": "2013-12-27" },
    { "year": "2014", "date": "2014-12-28" },
    { "year": "2015", "date": "2015-12-29" },
    { "year": "2016", "date": "2016-12-28" },
    { "year": "2017", "date": "2017-12-27" },
    { "year": "2018", "date": "2018-12-27" },
]

# At this moment in time, constructing this list dynamically would be
# too much pointless code.
newsposts = [
    {
        "page": "2019-0.11.8.html",
        "date": "2019-10-30",
        "title": "GNUnet 0.11.8"
    },
    {
        "page": "2019-0.11.7.html",
        "date": "2019-10-27",
        "title": "GNUnet 0.11.7"
    },
    {
        "page": "2019-10-ICANNPanel.html",
        "date": "2019-10-20",
        "title": "ICANN Panel"
    },
    {
        "page": "2019-10-GNSSpec1.html",
        "date": "2019-10-04",
        "title": "GNS Spec 1"
    },
    {
        "page": "2019-0.11.6.html",
        "date": "2019-07-24",
        "title": "GNUnet 0.11.6"
    },
    {
        "page": "2019-07-GHM_Aug_2019.html",
        "date": "2019-07-17",
        "title": "GNUnet Hacker Meeting 2019"
    },
    {
        "page": "2019-06-DSTJ.html",
        "date": "2019-06-28",
        "title": "Peer DSTJ is dead, long live peer Y924"
    },
    {
        "page": "2019-0.11.5.html",
        "date": "2019-06-05",
        "title": "GNUnet 0.11.5"
    },
    {
        "page": "2019-06.html",
        "date": "2019-06-01",
        "title": "2019-06"
    },
    {
        "page": "2019-0.11.4.html",
        "date": "2019-05-12",
        "title": "GNUnet 0.11.4"
    },
    {
        "page": "2019-0.11.3.html",
        "date": "2019-04-07",
        "title": "GNUnet 0.11.3"
    },
    {
        "page": "2019-0.11.2.html",
        "date": "2019-04-04",
        "title": "GNUnet 0.11.2"
    },
    {
        "page": "2019-0.11.1.html",
        "date": "2019-04-03",
        "title": "GNUnet 0.11.1"
    },
    {
        "page": "2019-0.11.0.html",
        "date": "2019-02-28",
        "title": "GNUnet 0.11.0"
    },
    {
        "page": "2019-02.html",
        "date": "2019-02-01",
        "title": "Google Summer of Code 2019"
    },
    {
        "page": "2018-08.html",
        "date": "2018-08-14",
        "title": "GSoC 2018 - GNUnet Web-based User Interface"
    },
    {
        "page": "2018-07.html",
        "date": "2018-07-01",
        "title": "Second GNUnet Hacker Meeting 2018"
    },
    {
        "page": "2018-06.html",
        "date": "2018-06-06",
        "title": "GNUnet 0.11.0pre66"
    },
    {
        "page": "2017-10.html",
        "date": "2017-10-01",
        "title": "Launching the new gnunet.org"
    },
]

# <!-- FIXME 2015: source only available on yt. <li>Ludovic Courtès, <a href="">Reproducible Software Deployment with GNU Guix</a>, Inria</li> -->
# <!-- FIXME 2014: no source link on web. <li>Julian Kirsch, <a href="">"Knocking down the HACIENDA"</a>, GNU Hacker Meeting 2014</li> -->
# <!-- FIXME 2014: no source link on web. <li>Peter Schaar, <a href="">"Technik, Recht und Überwachung"</a>, Technische Universität München</li> -->
# <!-- FIXME 2014: no source link on web. <li>Christian Grothoff, <a href="">"A Public Key Infrastructure for Social Movements in the Age of Universal Surveillance"</a>, University of Oxford</li> -->
# <!-- FIXME 2013: no source link on web. <li>Bart Polot, <a href="">"GNUnet CADET and GNUnet Conversation" at YBTI/30c3</a>, 30C3</li> -->
# <!-- FIXME 2013: no media link. <li>Roger Dingledine and Jacob Appelbaum, "Q &amp; A", Technische Universität München (<a href="https://archive.org/details/RogerDingledineAndJacobAppelbaumQAMarathon" download>download</a>)</li> -->
# <!-- FIXME 2013: no source link on web. <li>Maximilian Szengel, <a href="">"Decentralized Evaluation of Regular Expressions for Capability Discovery in Peer-to-Peer Networks"</a>, Technische Universität München</li> -->

videoslist = [
    {
        "year": "2019",
        "author": "Christian Grothoff",
        "location": "IETF",
        "description": "",
        "name": "GNU Name System",
        "source": "https://git.gnunet.org/gnunet-videos-2019.git/plain/IETF104/GNU_Name_System_-_2019_Edition_IETF104__Christian_Grothoff.webm",
        "mirror_source": "",
        "slides": "",
        "comment": ""
    },
    {
        "year": "2018",
        "author": "t3sserakt",
        "location": "Datenspuren 2018",
        "description": "",
        "name": "State of the GNUnet",
        "source": "https://git.gnunet.org/gnunet-videos-2018.git/plain/Datenspuren2018/DS2018-9337-deu-State_of_the_GNUnet_webm-hd.webm",
        "mirror_source": "",
        "slides": "",
        "comment": ""
    },
    {
        "year": "2018",
        "author": "sva",
        "location": "hack.lu",
        "description": "",
        "name": "You Broke The Internet - Let's Make a GNU One",
        "source": "https://git.gnunet.org/gnunet-videos-2018.git/plain/hack.lu/Hack.lu_2018_LT_-_GNUnet_-_You_Broke_The_Internet_Lets_Make_A_GNU_One__sva.webm",
        "mirror_source": "",
        "slides": "",
        "comment": ""
    },
    {
        "year": "2018",
        "author": "Christian Grothoff",
        "location": "",
        "description": "",
        "name": "GNS - The GNU Name System - Overview",
        "source": "https://git.gnunet.org/gnunet-videos-2018.git/plain/GNS_-_The_GNU_Name_System_-_Overview.webm",
        "mirror_source": "",
        "slides": "",
        "comment": ""
    },
    {
        "year": "2017",
        "author": "Christian Grothoff",
        "location": "Technische Universitaet Muenchen",
        "description": "",
        "name": "Big Data, Little Data, No Data",
        "source": "https://git.gnunet.org/gnunet-videos-2017.git/plain/Big_Data-Little_Data-No_Data.mp4",
        "mirror_source": "",
        "slides": "",
        "comment": ""
    },
    {
        "year": "2017",
        "author": "lynX",
        "location": "34C3",
        "description": "",
        "name": "Three Ways to Enhance Metadata Protection Beyond Tor",
        "source": "https://git.gnunet.org/gnunet-videos-2017.git/plain/34c3/34c3-chaoswest-1-eng-Three_Ways_to_Enhance_Metadata_Protection_Beyond_Tor_-_secushareorg_webm-hd.webm",
        "mirror_source": "",
        "slides": "",
        "comment": ""
    },
    {
        "year": "2017",
        "author": "t3sserakt",
        "location": "34C3",
        "description": "",
        "name": "Modeling Trust in a Distributed Private Social Network",
        "source": "https://git.gnunet.org/gnunet-videos-2017.git/plain/34c3/34c3-chaoswest-2-eng-Modeling_Trust_in_a_Distributed_Private_Social_Network_-_secushareorg_webm-hd.webm",
        "mirror_source": "",
        "slides": "",
        "comment": ""
    },
    {
        "year": "2017",
        "author": "lynX",
        "location": "34C3",
        "description": "",
        "name": "Scalable and privacy-respectful distributed systems - Our chance to avoid cloud computing",
        "source": "https://git.gnunet.org/gnunet-videos-2017.git/plain/34c3/34c3-chaoswest-7-eng-Scalable_and_privacy-respectful_distributed_systems_-_Our_chance_to_avoid_cloud_computing_webm-hd.webm",
        "mirror_source": "",
        "slides": "",
        "comment": ""
    },
    {
        "year": "2017",
        "author": "lynX, Christian Grothoff",
        "location": "34C3",
        "description": "",
        "name": "Privacy-Oriented Distributed Networking for an Ethical Internet",
        "source": "https://git.gnunet.org/gnunet-videos-2017.git/plain/34c3/34c3-chaoswest-6-eng-Privacy-Oriented_Distributed_Networking_for_an_Ethical_Internet_-_including_50_subsystems_of_GNUnet_webm-hd.webm",
        "mirror_source": "",
        "slides": "",
        "comment": ""
    },
    {
        "year": "2016",
        "author": "Daniel Golle",
        "location": "Battlemesh v9 (Porto, Portugal)",
        "description": "",
        "name": "GNUnet For Mesh Communities",
        "source": "https://git.gnunet.org/gnunet-videos-2016.git/plain/Battlemeshv9/Gnunet%20For%20Mesh%20Communities%20-%20Battlemesh%20v9%20(Porto,%20Portugal).mp4",
        "mirror_source": "",
        "slides": "",
        "comment": ""
    },
    {
        "year": "2016",
        "author": "Jeff Burdges",
        "location": "GNU Hacker Meeting 2016",
        "description": "",
        "name": "Xolotl - A compact mixnet format with stronger forwared secrecy and hybrid anonymity",
        "source": "https://git.gnunet.org/gnunet-videos-2015.git/plain/GHM%202015/expose-GNUJeffBurdges19aout2016.mp4",
        "mirror_source": "",
        "slides": "",
        "comment": ""
    },
    {
        "year": "2016",
        "author": "t3sserakt, xrs",
        "location": "Datenspuren 2016",
        "description": "",
        "name": "secushare",
        "source": "https://git.gnunet.org/gnunet-videos-2016.git/plain/Datenspuren2016/DS2016-7775-deu-Secushare_webm-hd.webm",
        "mirror_source": "",
        "slides": "",
        "comment": ""
    },
    {
        "year": "2015",
        "author": "Christian Grothoff",
        "location": "PSC 2015",
        "description": "",
        "name": "The Architecture of the GNUnet: 45 Subsystems in 45 Minutes",
        "source": "https://git.gnunet.org/gnunet-videos-2015.git/plain/psc2015/grothoff.webm",
        "mirror_source": "",
        "slides": "",
        "comment": ""
    },
    {
        "year": "2015",
        "author": "t3sserakt, demos",
        "location": "Datenspuren 2015",
        "description": "",
        "name": "Echt Dezentrales Netzwerk",
        "source": "https://git.gnunet.org/gnunet-videos-2015.git/plain/Datenspuren2015/datenspuren15-7069-de-EDN_-_Echt_Dezentrales_Netzwerk_webm.webm",
        "mirror_source": "",
        "slides": "",
        "comment": ""
    },
    {
        "year": "2015",
        "author": "Florian Dold",
        "location": "32C3",
        "description": "",
        "name": "Byzantine Fault Tolerance Set Consensus with Efficient Set Reconciliation",
        "source": "https://git.gnunet.org/gnunet-videos-2015.git/plain/32c3/byzantine-fault-tolerant-set-consensus-with-efficient-set-reconciliation.mp4",
        "mirror_source": "",
        "slides": "",
        "comment": ""
    },
    {
        "year": "2015",
        "author": "Daniel Golle",
        "location": "BattleMesh 2015",
        "description": "",
        "name": "GNUnet in Community Networks",
        "source": "https://git.gnunet.org/gnunet-videos-2015.git/plain/BattleMeshV8/GNUnet%20in%20Community%20Mesh%20Networks%20+%20Slides%20-%20BattleMeshV8.webm",
        "mirror_source": "",
        "slides": "",
        "comment": ""
    },
    {
        "year": "2014",
        "author": "Florian Dold",
        "location": "31C3",
        "description": "",
        "name": "Electronic Voting and Key Generation in Distributed Systems",
        "source": "https://git.gnunet.org/gnunet-videos-2014.git/plain/31c3/voting-voting.webm",
        "mirror_source": "",
        "slides": "",
        "comment": ""
    },
    {
        "year": "2014",
        "author": "Markus Sabadello, Suhin Mohan Adapa",
        "location": "31C3",
        "description": "",
        "name": "FreedomBox Status Update",
        "source": "https://git.gnunet.org/gnunet-videos-2014.git/plain/31c3/freedombox-freedombox.webm",
        "mirror_source": "",
        "slides": "",
        "comment": ""
    },
    {
        "year": "2014",
        "author": "Lucas Fulchir",
        "location": "31C3",
        "description": "",
        "name": "why TLS sucks and what I am doing about it",
        "source": "https://git.gnunet.org/gnunet-videos-2014.git/plain/31c3/fenrir-fenrir.webm",
        "mirror_source": "",
        "slides": "",
        "comment": ""
    },
    {
        "year": "2014",
        "author": "Nicolas Benes",
        "location": "31C3",
        "description": "",
        "name": "Panic! An approach for home routers to securely erase sensitive data",
        "source": "https://git.gnunet.org/gnunet-videos-2014.git/plain/31c3/do-panic-do-panic.webm",
        "mirror_source": "",
        "slides": "",
        "comment": ""
    },
    {
        "year": "2014",
        "author": "Christian Grothoff, Douwe Korff, Jacob Appelbaum",
        "location": "Council of Europe",
        "description": "",
        "name": "After Snowden: using law and technology to counter snooping",
        "source": "https://git.gnunet.org/gnunet-videos-2014.git/plain/2014-coe.webm",
        "mirror_source": "",
        "slides": "",
        "comment": ""
    },
    {
        "year": "2014",
        "author": "Christian Grothoff, Florian Dold",
        "location": "31C3",
        "description": "",
        "name": "Taler",
        "source": "https://git.gnunet.org/gnunet-videos-2014.git/plain/31c3/taler-taler.webm",
        "mirror_source": "",
        "slides": "",
        "comment": ""
    },
    {
        "year": "2014",
        "author": "Markus Benter",
        "location": "31C3",
        "description": "",
        "name": "Complex Queries in P2P networks",
        "source": "https://git.gnunet.org/gnunet-videos-2014.git/plain/31c3/queries-queries.webm",
        "mirror_source": "",
        "slides": "",
        "comment": ""
    },
    {
        "year": "2014",
        "author": "Bernd Paysan",
        "location": "31C3",
        "description": "",
        "name": "net2o - Reinventing the Internet",
        "source": "https://git.gnunet.org/gnunet-videos-2014.git/plain/31c3/net2o-net2o.webm",
        "mirror_source": "",
        "slides": "",
        "comment": ""
    },
    {
        "year": "2013",
        "author": "Christian Grothoff, Carlo von Lynx, jacob Appelbaum, Richard Stallman",
        "location": "Berlin",
        "description": "",
        "name": "You broke the Internet. We're making ourselves a GNU one.",
        "source": "https://git.gnunet.org/gnunet-videos-2013.git/plain/you%20broke%20the%20internet/internetistschuld.webm",
        "mirror_source": "",
        "slides": "",
        "comment": ""
    },
    {
        "year": "2013",
        "author": "Christian Grothoff",
        "location": "GNU Hacker Meeting 2013",
        "description": "",
        "name": "The GNU Name System and the Future of Social Networking with GNUnet",
        "source": "",
        "mirror_source": "https://audio-video.gnu.org/video/ghm2013/Christian_Grothoff-The_GNU_Name_System_and_the_Future_of_Social_Networking_with_GNUnet_.webm",
        "slides": "",
        "comment": ""
    },
    {
        "year": "2013",
        "author": "Christian Grothoff",
        "location": "30C3",
        "description": "",
        "name": "The GNU Name System",
        "source": "",
        "mirror_source": "https://cdn.media.ccc.de/congress/2013/mp4-lq/30c3-5212-en-The_GNU_Name_System_h264-iprod.mp4",
        "slides": "",
        "comment": ""
    },
    {
        "year": "2013",
        "author": "Markus Teich",
        "location": "Technische Universitaet Muenchen",
        "description": "",
        "name": "Monkey - generating Useful Bug Reports Automatically",
        "source": "",
        "mirror_source": "https://media.net.in.tum.de/videos/standalonevideo/video/491",
        "slides": "",
        "comment": "TUM internal access"
    },
    {
        "year": "2012",
        "author": "Martin Schanzenbach",
        "location": "Technische Universitaet Muenchen",
        "description": "",
        "name": "A Censorship-Resistant and Fully Decentralized Naming System",
        "source": "",
        "mirror_source": "https://media.net.in.tum.de/videoarchive/SS12/Oberseminar/2012+09+19_1600+Design+and+Implementation+of+a+Censorship+Resist/priv/camera.mp4",
        "slides": "",
        "comment": ""
    },
    {
        "year": "2010",
        "author": "Matthias Wachs",
        "location": "GNU Hacker Meeting 2010",
        "description": "",
        "name": "GNUnet - Transport and Transport Selection",
        "source": "https://git.gnunet.org/gnunet-videos-2010.git/plain/GHM_Hague/GNUnet_-_Transports_and_Transport_Selection.ogv",
        "mirror_source": "",
        "slides": "",
        "comment": ""
    },
    {
        "year": "2010",
        "author": "Nathan S. Evan",
        "location": "GNU Hacker Meeting 2010",
        "description": "",
        "name": "GNUnet Distributed Data Storage - DHT and Distance Vector Transport",
        "source": "https://git.gnunet.org/gnunet-videos-2010.git/plain/GHM_Hague/GNUnet_Distributed_Data_Storage_-_DHT_and_Distance_Vector_Transport.ogv",
        "mirror_source": "",
        "slides": "",
        "comment": ""
    },
    {
        "year": "2010",
        "author": "Christian Grothoff",
        "location": "GNU Hacker Meeting 2010",
        "description": "",
        "name": "Introduction to the GNUnet Peer-to-Peer Framework",
        "source": "https://git.gnunet.org/gnunet-videos-2010.git/plain/GHM_Hague/Introduction_to_The_GNUnet_Peer-to-Peer_Framework.ogv",
        "mirror_source": "",
        "slides": "",
        "comment": ""
    },
]

def generate_site(root):
    for in_file in glob.glob(root + "/*.j2"):
        name, ext = re.match(r"(.*)\.([^.]+)$", in_file.rstrip(".j2")).groups()
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
            if locale == "en" or not os.path.isfile(lf):
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
                                  lang_full=langs_full[locale],
                                  url=url,
                                  meetingnotesdata=meetingnotes,
                                  newsdata=newsposts,
                                  videosdata=videoslist,
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

            if root == "news":
                langdir = outdir / locale / root
            else:
                langdir = outdir / locale

            langdir.mkdir(parents=True, exist_ok=True)
            # os.makedirs("./rendered/" + locale, exist_ok=True)
            with codecs.open(out_name, "w", encoding='utf-8') as f:
                f.write(content)


def main():
    # rm_rf("rendered")
    print("generating template")
    generate_site("template")
    print("generating news")
    generate_site("news")


#    for l in glob.glob("locale/*/"):
#        locale = os.path.basename(l[:-1])
#        copy_static (locale, staticfiles)
# generate_rss
#print("running generation")
#generation_dir

if __name__ == "__main__":
    main()
