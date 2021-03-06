#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'seclab'
SITENAME = u'Cyber Security Reading Group @JHU'
SITEURL = 'http://localhost:8000'

PATH = 'content'
THEME = './themes/elegant'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'))

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
STATIC_PATHS = ['files']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
