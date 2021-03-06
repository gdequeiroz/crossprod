#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://nacnudus.github.io/crossprod'
RELATIVE_URLS = False

FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/category.%s.atom.xml'
CATEGORY_FEED_RSS = 'feeds/category.%s.rss.xml'
TAG_FEED_ATOM = 'feeds/tag.%s.atom.xml'
TAG_FEED_RSS = 'feeds/tag.%s.rss.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = 'crossprod'
GOOGLE_ANALYTICS = "UA-45097885-3"
FEATURED_IMAGE = SITEURL + '/theme/images/apple-touch-icon-152x152.png'
