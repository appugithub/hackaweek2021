import sys
n = len(sys.argv)
print("Total arguments passed:", n)
print("\n Sys.argv[1]", sys.argv[1])
# Arguments passed
print("\nName of Python script:", sys.argv[0])
print('test1') 
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
url = sys.argv[1]

import requests, json
from requests_oauthlib import OAuth1

token = "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"
r = requests.patch(url, auth=("appu.rongala@gmail.com", token))
print(r.json())

# url = "https://api.github.com/repos/appugithub/hackaweek2021/pulls/1"
# payload = {
#     "title": "New title"
# }
#
# r = requests.patch(url, auth=("appu.rongala@gmail.com", token), json=payload)
#
# print(r.json())
