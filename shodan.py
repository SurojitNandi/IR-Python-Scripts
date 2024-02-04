import shodan
import requests

SHODAN_API_KEY = "{Insert Shodan API Key}"
api = shodan.Shodan(SHODAN_API_KEY)

target = 'www.packetpub.com'

dnsResolve = 'https://api.shodan.io/dns/resolve?hostnames=' + target + '&key=' + shodan_api_key

