import sys
n = len(sys.argv)
print("Total arguments passed:", n)
print("\n Sys.argv[1]", sys.argv[1])
print("\n Sys.argv[2]", sys.argv[2])
# Arguments passed
print("\nName of Python script:", sys.argv[0])
print('test1')
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
url = sys.argv[1]

token = "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"
token = sys.argv[2]
import requests, json
from requests_oauthlib import OAuth1
url = "https://api.github.com/repos/appugithub/hackaweek2021/pulls/2/commits"
r = requests.get(url, auth=("appu.rongala@gmail.com", token))
print(r.json())

print('START UPDATE PR')
url = "https://api.github.com/repos/appugithub/hackaweek2021/pulls/2"
payload = {
    "title": "New title 1"
}

r = requests.post(url, auth=("appu.rongala@gmail.com", token), json=payload)

print(r.json())
print('END UPDATE PR')

CLIENT_KEY = '3e6ea444875da784aadae6abc5124b15'
CLIENT_SECRET = '15d032680057485f96e074978b097179b5155d50'
ACCESS_TOKEN_KEY = '53bf556f2b7eb9523867c8d4d6339b3a'

ACCESS_TOKEN_SECRET = 'b19e74549defb2b0fe2d4f0a397884e1bb7bc165'

auth_code_url = "https://api.projectplace.com/oauth2/authorize"

access_token = "https://api.projectplace.com/oauth2/access_token"


test_api_url = "https://service.projectplace.com/api/v1/cards/14862291"


def get_pp_token_from_yml():
    oauth_pp_token = OAuth1(client_key=CLIENT_KEY, client_secret=CLIENT_SECRET,
                            resource_owner_key=ACCESS_TOKEN_KEY,
                            resource_owner_secret=ACCESS_TOKEN_SECRET)
    return oauth_pp_token

pp_token = get_pp_token_from_yml()

response = requests.get(url=test_api_url, auth=pp_token)
print(response.__dict__)
