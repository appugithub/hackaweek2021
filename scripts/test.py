import sys
n = len(sys.argv)
print("Total arguments passed:", n)
# print("\n Sys.argv[1]", sys.argv[1])
# print("\n Sys.argv[2]", sys.argv[2])
# Arguments passed
# print("\nName of Python script:", sys.argv[0])
# print('test1')
# print("\nArguments passed:", end = " ")
# for i in range(1, n):
#     print(sys.argv[i], end = " ")
url = sys.argv[1]

token = sys.argv[2]

#print(context)
import requests, json
from requests_oauthlib import OAuth1
context = json.loads(sys.argv[3])
repo = context['repository']
pr_number = context['event']['number']
print(repo)
print(pr_number)
commits_url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}/commits"
r = requests.get(commits_url, auth=("appu.rongala@gmail.com", token))
commits = [each for each in r.json()]

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

#response = requests.get(url=test_api_url, auth=pp_token)


global_card_id = None
r = ["Fist commit\n Done1", "Second commit \n Done2"]
for each in r:
   #message = each['commit']['message']
   message = each
   card_id = 15043329
   print(message)
   if len(message.split(':')) > 1:
      card_id = message.split(':')[0].split('-')[1].strip()

   #print(str(card_id))
   if card_id:
      global_card_id = card_id
      message = message.split('-')[1]
      payload = {"attachments": [],
              "encoded_text": message,
              "item_id": card_id,
              "item_name": "card",
              "send_to_external": False,
              "sent_from": "web"}
      card_comment_url = 'https://service.projectplace.com/api/v3/conversations/comment'
      requests.post(url=card_comment_url, auth=pp_token, data=payload)
print(global_card_id)
if global_card_id:
    card_url = f'https://service.projectplace.com/api/v1/cards/{global_card_id}'
    result = requests.get(url=card_url, auth=pp_token)
    r = result.json()
    print(r)
    # print(type(r))
    # print(result)
    print(type(r))
    card_name = r['title']
    card_description = r['description']   
    print('CARD DESCRIPTION')
    print(card_description)

    print('START UPDATE PR')
    url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}"
    payload = {
        "title": card_name,
        "body": card_description
    }

    r = requests.post(url, auth=("appu.rongala@gmail.com", token), json=payload)

    # print(r.json())
    # print('END UPDATE PR')

    # print(response.__dict__)


