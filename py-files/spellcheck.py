import http.client, urllib.parse, json

text = 'Hollo, wrld!'

data = {'text': text}

# NOTE: Replace this example key with a valid subscription key.
key = 'ENTER KEY HERE'

host = 'api.cognitive.microsoft.com'
path = '/bing/v7.0/spellcheck?'
params = 'mkt=en-us&mode=proof'

headers = {'Ocp-Apim-Subscription-Key': key,
'Content-Type': 'application/x-www-form-urlencoded'}

# The headers in the following example 
# are optional but should be considered as required:
#
# X-MSEdge-ClientIP: 999.999.999.999  
# X-Search-Location: lat: +90.0000000000000;long: 00.0000000000000;re:100.000000000000
# X-MSEdge-ClientID: <Client ID from Previous Response Goes Here>

conn = http.client.HTTPSConnection(host)
body = urllib.parse.urlencode (data)
conn.request ("POST", path + params, body, headers)
response = conn.getresponse ()
output = json.dumps(json.loads(response.read()), indent=4)
print (output)