# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 15:18:50 2019

@author: Jacques-ds
"""

import requests
import json
import base64
import re

# First part - receive a token
url = 'http://InsertYourWeb.com/wp-json/jwt-auth/v1/token'

cred = {"username":"InsertYourUserName","password":"InsertYourPassword"}

r = requests.post(url, json = cred)
a = str(r.content)
x = re.search('token":"([a-zA-Z0-9\\.\\_]+)","user', a)
token = x.group(1)

# Second part - posting
url2 = 'http://InserYourWeb.com/wp-json/wp/v2/posts'

header = {'Authorization': 'Bearer ' + token}

post = {"date": "2019-12-21T10:00:00",
          "title": "First API post",
          "content": "This is your first python wordpress api post!",
          "status": "publish"}

r2 = requests.post(url2, headers = header, json = post)
print(r2)






