import requests,mmh3,base64
inp = input("Enter Favicon URL: ")
response = requests.get(inp)
favicon = base64.encodebytes(response.content)
hash = mmh3.hash(favicon)
print(hash)
print ("Use this:" + str(hash))
