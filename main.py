
import json
from random import randrange


import requests

from calculateSignature import SignatureManager

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#authentifurl = 'https://test.rodrigue-ws.com/API/AUTHENTICATIONS/current/api'
authentifurl = 'http://172.30.200.151/dev/api_authentication/v1/api'
#authentifurl = 'https://localhost:7201/api'

apiexternesurl = 'https://localhost:7265/api'
#apiexternesurl = 'http://172.30.200.151/dev/api_external/v1/api'
datasurl = 'https://test.rodrigue-ws.com/API/DATAS/current/api'
salt = 'Hw9x]V$33/z,DQ'
partner = "TICKETAC"
bpLogin = "TICKETAC"
bpPassW = "TICKETAC"
structureId = "0588"
request_method = "GET"

TestArray = [] #empty array
class SeatEntity():          # leave this empty
    def __init__(self):   # constructor function using self
        self.SeatID = None  # variable using self.

# Obtenir un token

getTokenUrl = authentifurl + '/' + structureId + '/token/' + partner

print(getTokenUrl)
mySignature = SignatureManager.getSignature(request_method, getTokenUrl, partner, salt)
payload = {}
headers = {
    'Signature': mySignature
}
response = requests.request("GET", getTokenUrl, headers=headers, data=payload, verify=False)
print(response.text);

myToken = response.json()["authenticationToken"]
print("new token", myToken)
#myToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IjEwMTAiLCJyb2xlIjoiVXNlciIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvdXNlcmRhdGEiOlsiNTg4IiwiOTkxIl0sIm5iZiI6MTY4MDI2MDgwOCwiZXhwIjoxNjgwMjYwODM4LCJpYXQiOjE2ODAyNjA4MDgsImlzcyI6InJvZHJpZ3VlIiwiYXVkIjoiVGhlbWlzQVBJIn0.48ROWWXdck4tqVT59UoVaSpfrqoug93aPZDW21pfxM8'
print(myToken)

testToken = authentifurl + '/token/TestAuth'
payload = {}
headers = {
    'Authorization': 'Bearer ' + myToken
}
response = requests.request("GET", testToken, headers=headers, data=payload, verify=False)
print(testToken, response);


#response = requests.request("GET", getBarCode, headers=headers, data=payload, verify=False)


myBarCode = '8054001790 '
myEventId = 315
mySessionId = 3244

getBarCode = apiexternesurl + '/' + structureId + '/barCode/' + myBarCode + '/' + str(myEventId) + '/' + str(mySessionId)
payload = {}
headers = {
    'Authorization': 'Bearer ' + myToken
}
print(getBarCode)

#response = requests.request("GET", getBarCode, headers=headers, data=payload, verify=False)
if response:
    print("ok:", response.text)
else:
    print('ko:', response.status_code)
output = json.loads(response.text)
print(output)
