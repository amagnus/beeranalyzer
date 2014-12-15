from django.db import models


class BeerStyles:

    styles_list = { '4-7': ('hefeweizen', 'kolsch', 'pilsner', 'golden',
                            'berliner weisse', 'lager', 'white', 'lambic'),
                    '8-12': ('pale ale', 'common', 'stout', 'porter', 'gueuze',
                             'belgian ale', 'altbier', 'tripel', 'french',
                             'dunkel', 'smoked', 'altbier'),
                    '12-14': ('bitter', 'brown', 'india pale ale', 'ipa',
                              'saison', 'de garde', 'strong ale', 'bock'),
                    '14-16': ('barley wine', 'quadrupel', 'quad', 'imperial')
                  }


    def compute_style(self, style_name):
        for key, value in self.styles_list.iteritems():
            for x in value:
                if (style_name.lower() in x) or (x in style_name.lower()):
                    return key
                    #print x


match_style = BeerStyles()
print match_style.compute_style('biere de garde')
