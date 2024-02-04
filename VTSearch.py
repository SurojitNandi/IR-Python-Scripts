import requests

#Ask for input
IPRep = input( "Enter IP to be reviewed: " )
url = "https://www.virustotal.com/api/v3/ip_addresses/"
url1 = url + str(IPRep)
print(url1)
headers = {
    "accept": "application/json",
    "x-apikey": ""
}

response = requests.get(url1, headers=headers)

print(response.text)