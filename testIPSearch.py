#import shodan, json
#import time
#import requests
#import re

#your shodan API key
#SHODAN_API_KEY = 'vxgVMr9jL5reGAREMRbkUWH7ErzOYiv9'
#api = shodan.Shodan(SHODAN_API_KEY)

import shodan
apkey = 'vxgVMr9jL5reGAREMRbkUWH7ErzOYiv9'
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
