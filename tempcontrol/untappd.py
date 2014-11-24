import requests
from django.conf import settings
import os


endpoint = 'https://api.untappd.com/v4'

#credentials = '?client_id=%s&client_secret=%s&compact=true' % (settings.UNTAPPD_CLIENT_ID,
#    settings.UNTAPPD_CLIENT_SECRET)
credentials = '?client_id=%s&client_secret=%s&compact=true' % (os.environ['UNTAPPD_CLIENT_ID'],
    os.environ['UNTAPPD_CLIENT_SECRET'])


def pull_beer():
    path = '%s/beer/info/3558%s' % (endpoint, credentials)

    r = requests.get(path)
    print r.text


def beer_search(name):
    path = '%s/search/beer%s&q=%s' % (endpoint, credentials, name)

    r = requests.get(path)
    print r.text


beer_search('moinette')
