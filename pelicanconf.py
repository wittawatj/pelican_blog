#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Wittawat Jitkrittum'
SITENAME = u"WJ's Homepage"
#SITEURL = 'http://wittawat.com'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

GITHUB_URL = 'https://github.com/wittawatj'
TWITTER_URL = 'https://twitter.com/wittawatj'
GOOGLEPLUS_URL = 'https://plus.google.com/112508555412336958238/'
DISQUS_SITENAME = "wjresearch"

# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/wittawatj'),
          ('google', 'https://plus.google.com/112508555412336958238/'),)

DEFAULT_PAGINATION = False
MENUITEMS = [('Projects', '/pages/projects.html'), ('Posts', '/archives.html'), ('Interesting', '/pages/interesting.html')]

#('About', '/pages/about.html')

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# I added
ARTICLE_EXCLUDES = (('pages', 'upload', 'images', 'css', 'js', 'blog', 'projects', 'software'))
#The static paths you want to have accessible on the output path “static”. By default, Pelican will copy the “images” folder to the output folder.
STATIC_PATHS = (['images', 'css', 'upload', 'js', 'pages/files', 'pages/images', 'pages/projects', 'blog', 'projects', 'software'])
PDF_GENERATOR = True
THEME = 'theme/gum'
#THEME = 'theme/built-texts'
PLUGIN_PATH = "plugins"
PLUGINS = ["latex"]
MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra', 'mathjax']
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
#### Dynamic
#DISPLAY_CATEGORIES_ON_MENU = True
#TYPOGRIFY = True

GOOGLE_ANALYTICS_ID = 'UA-9868398-1'
GOOGLE_ANALYTICS_SITENAME = 'wittawat.com'

