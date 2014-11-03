import requests
from django.conf import settings


endpoint = 'https://api.untappd.com/v4'

credentials = '?client_id=%s&client_secret=%s&compact=true' % (settings.UNTAPPD_CLIENT_ID,
    settings.UNTAPPD_CLIENT_SECRET)


def pull_beer():
    path = '%s/beer/info/3558%s' % (endpoint, credentials)

    r = requests.get(path)
    print r.text


def beer_search():
    path = '%s/search/beer%s&q=moinette' % (endpoint, credentials)

    r = requests.get(path)
    print r.text


beer_search()
