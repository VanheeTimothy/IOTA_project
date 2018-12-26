import urllib2
import json
import iota
command = {
    'command': 'findTransactions',
    'addresses': ['CPEIQD9UTUGPVBYRCUYYFISJARRBWNXBTANAINNYAVHJAOGTQWJGPORHXYXPVCJBH9XSVRCXVQHBFBNWD']
}

stringified = json.dumps(command)

headers = {
    'content-type': 'application/json',
    'X-IOTA-API-Version': '1'
}

request = urllib2.Request(url="https://nodes.thetangle.org:443", data=stringified, headers=headers)
returnData = urllib2.urlopen(request).read()

jsonData = json.loads(returnData)

print type(jsonData)

print(jsonData)
hshs =[]
for tx in jsonData['hashes']:
    hshs.append(tx)
    jsn = json.dump(iota.utils.fromTrytes(tx))
    print jsn


# command = {
#     'command': 'findTransactions',
#     'addresses': hshs
# }
# stringified = json.dumps(command)
# request = urllib2.Request(url="https://nodes.thetangle.org:443", data=stringified, headers=headers)
# returnData = urllib2.urlopen(request).read()
# jsonData = json.loads(returnData)
# print type(jsonData)
# print(jsonData)