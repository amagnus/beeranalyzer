import requests
from django.conf import settings


endpoint = 'https://api.untappd.com/v4'

def pull_beer():
    path = '%s/beer/info/3558?client_id=%s&client_secret=%s&compact=true' % (endpoint, settings.UNTAPPD_CLIENT_ID, settings.UNTAPPD_CLIENT_SECRET)

    r = requests.get(path)
    print r.text



pull_beer()
