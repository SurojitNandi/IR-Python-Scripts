#import shodan, json
#import time
#import requests
#import re

#your shodan API key
#SHODAN_API_KEY = 'apikey'
#api = shodan.Shodan(SHODAN_API_KEY)

import shodan
apkey = 'apikey'
api = shodan.Shodan(apkey)
 
# Wrap the request in a try/ except block to catch errors
try:
    results = api.search('apache')
    print('Results found: %s' % results['total'])
    for result in results['matches']:
        print('IP: %s' % result['ip_str'])
        print(result['data'])
        print('')
except shodan.APIError as e:
    print('Error: %s' % e)
