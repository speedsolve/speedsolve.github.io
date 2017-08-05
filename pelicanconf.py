#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Sinpei Araki'
SITENAME = 'Sinpei Araki''s Blog'
SITEURL = 'http://localhost:8000'
SITELOGO = 'https://scontent-nrt1-1.xx.fbcdn.net/v/t1.0-9/18403698_1714019478615303_5287730190355027188_n.jpg?oh=95c98b8619be4997e9e4e3bc1e270f1e&oe=59F5A3CC'
SITETITLE = AUTHOR
SITESUBTITLE = 'Speedcuber'

PATH = 'content'
THEME = './themes/Flex'
TIMEZONE = 'Asia/Tokyo'

COPYRIGHT_NAME = 'Sinpei Araki'
COPYRIGHT_YEAR = '2017'

DEFAULT_LANG = 'ja'
LOCALE='ja_JP'
DATE_FORMATS = {
    'ja': '%B %d, %Y',
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/speedsolve'),
	  ('facebook', 'https://www.facebook.com/speedsolve'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

