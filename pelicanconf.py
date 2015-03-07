#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os.path

AUTHOR = u'Wittawat Jitkrittum'
SITENAME = u"WJ's Homepage"
#SITEURL = 'http://wittawat.com'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

GITHUB_URL = 'https://github.com/wittawatj'
TWITTER_URL = 'https://twitter.com/wittawatj'
#GOOGLEPLUS_URL = 'https://plus.google.com/112508555412336958238/'
DISQUS_SITENAME = "wjresearch"

# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/wittawatj'),
          #('google', 'https://plus.google.com/112508555412336958238/'),
          ('github', 'https://github.com/wittawatj'))

DEFAULT_PAGINATION = False
MENUITEMS = [
        ('Work', '/pages/work.html'),
        #('Posts', '/archives.html'), 
        ('Interesting', '/pages/interesting.html')
        ]

#('About', '/pages/about.html')

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# I added
ARTICLE_EXCLUDES = (('pages', 'upload', 'images', 'css', 'js', 'blog', 'projects', 'software'))
#The static paths you want to have accessible on the output path “static”. By default, Pelican will copy the “images” folder to the output folder.
STATIC_PATHS = (['images', 'css', 'upload', 'js', 'pages/', 'pages/images', 'pages/projects', 'blog', 'projects', 'software'])
PDF_GENERATOR = False
#THEME=os.path.expanduser("~/git/pelican-themes/water-iris/")
#THEME = 'theme/water-iris/'
#THEME = 'theme/crowsfoot//'
THEME = 'theme/pelican-bootstrap3'
#THEME = 'theme/built-texts'
PLUGIN_PATH = "plugins"
PLUGINS = ["latex"]
MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra', 'mathjax']
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
#### Dynamic
#DISPLAY_CATEGORIES_ON_MENU = True
#TYPOGRIFY = True

GOOGLE_ANALYTICS = 'UA-9868398-1'
#GOOGLE_ANALYTICS_ID = 'UA-9868398-1'
#GOOGLE_ANALYTICS_SITENAME = 'wittawat.com'


##### For pelican-bootstrap3 theme  ####
#It uses the tag_cloud variable for displaying tags in the sidebar. You can
#control the amount of tags shown with:
TAG_CLOUD_MAX_ITEMS = 20 
DISPLAY_TAGS_INLINE = True
DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
RECENT_POST_COUNT = 5
HIDE_SIDEBAR = False 
#GITHUB_USER = 'wittawatj'
TWITTER_CARDS = True
TWITTER_USERNAME = 'wittawatj'
# This will make my twitter feeds appear on the sidebar
TWITTER_WIDGET_ID = '422661360594329601'
#https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3
SHOW_ARTICLE_CATEGORY = False
CC_LICENSE = "CC-BY"

