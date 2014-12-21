import requests
import os
import json
from django.conf import settings


endpoint = 'https://api.untappd.com/v4'

#credentials = '?client_id=%s&client_secret=%s&compact=true' % (settings.UNTAPPD_CLIENT_ID,
#    settings.UNTAPPD_CLIENT_SECRET)
credentials = '?client_id=%s&client_secret=%s&compact=true' % (os.environ['UNTAPPD_CLIENT_ID'],
    os.environ['UNTAPPD_CLIENT_SECRET'])


def pull_beer():
    path = '%s/beer/info/3558%s' % (endpoint, credentials)

    r = requests.get(path)
    print r.text


def search_beer(name):
	path = '%s/search/beer%s&q=%s&sort=checkin&limit=7' % (endpoint, credentials, name)

	r = requests.get(path)
	raw = json.loads(r.text)

	suggestions = []

	for item in raw['response']['beers']['items']:
		suggestions.append(item['beer']['beer_name'])

	return suggestions



#print search_beer('moinette')
