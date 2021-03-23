#!/usr/bin/python3
import  requests
import json
import pprint

host_ip = "10.31.70.210"
api_port = "55443"
login = "restapi"
passwd = "j0sg1280-7@"
api_url = 'https://' + host_ip + ':' + api_port
api_token_addr = "/api/v1/auth/token-services"

req = requests.post(api_url+api_token_addr, auth=(login, passwd), verify=False)

token = req.json()["token-id"]

header = {"content-type": "application/json", "X-Auth-Token": token}
ifaces = requests.get(api_url + '/api/v1/interfaces/Loopback3', headers=header, verify=False)


pprint.pprint(ifaces.json())
#print(token)

