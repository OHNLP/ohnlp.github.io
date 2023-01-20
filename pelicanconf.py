"""Pelican Configuration

For a simple conference 
"""
from datetime import datetime

AUTHOR = 'Huan He'
SITENAME = 'OHNLP'

# just set this to relative path due to deployment issue
SITEURL = './'

# where to store the markdown contents and other materials
PATH = 'content'

# I'm here
TIMEZONE = 'America/Chicago'

# by default
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# customized plugins
PLUGINS = [
    'myplugins'
]

# Social widget if needed.
SOCIAL = (('https://twitter.com/', '#'),
          ('https://facebook.com/', '#'),)

# we don't need pagination as there is no blog
DEFAULT_PAGINATION = False

# put all contents under year folder
ARTICLE_URL = "{category}/{slug}.html"
ARTICLE_SAVE_AS = "{category}/{slug}.html"

# for page
PAGE_URL = "page/{slug}.html"
PAGE_SAVE_AS = "page/{slug}.html"

# for conference site author category is not needed
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""

# no need for tags page
TAGS_SAVE_AS = ""

# no need for archive page
ARCHIVES_SAVE_AS = ""

# no need for categorys page
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""

# current year of this site
CURRENT_YEAR = datetime.today().strftime('%Y')

# specify the customized theme
THEME = "./themes/ohnlp-theme"

# for tools
OHNLP_TOOLS = [
{
    "name": "Backbone",
    "link": "https://github.com/OHNLP/Backbone",
    "desc": "Backbone aims to simplify scalable ETL (Extract-Transform-Load) processes by transforming such operations into a sequence of simple user-accessible JSON configurations, with a particular focus on Healthcare NLP-related tasks.",
},
{
    "name": "MedTagger",
    "link": "https://github.com/OHNLP/MedTagger",
    "desc": "MedTagger is a light weight clinical NLP system built upon Apache UIMA.",
},
{
    "name": "MedTime",
    "link": "https://github.com/OHNLP/MedTime",
    "desc": "MedTime is an Apache UIMA based temporal information extraction system developed by the Mayo Clinic NLP program.",
},
{
    "name": "MedTator",
    "link": "https://github.com/OHNLP/MedTator",
    "desc": "MedTator is a serverless text annotation tool for corpus development. It is built on HTML5 techniques and many open-source packages, and was designed to be easy-to-use for your annotation task."
},
{
    "name": "MedXN",
    "link": "https://github.com/OHNLP/MedXN",
    "desc": "MedXN is a medication normalization system built upon Apache UIMA framework."
}
]

