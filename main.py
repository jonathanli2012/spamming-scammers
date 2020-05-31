import requests
import os

import string
from user_gen import *

link = 'https://go04forstart.ml/g36g/post.php'

user_len = 200
users = request_users(user_len)


for i in users:
  print(i)
exit()


for i in users:
	data = {'register_email':i.email,'password':i.password}
	r = requests.post(link, allow_redirects=False, data={})
	print(r)
