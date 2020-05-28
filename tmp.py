import requests
import os

link = 'https://go04forstart.ml/g36g/post.php'
names = open("names.txt").readlines()

import random
nums = []
for i in range(0,500):
	n = random.randint(0,10000)
	nums.append(n)

for i in range(0,400):
	password = str(nums[i]*2) + names[i+50][:-1]
	username = names[i][:-1] + str(nums[i])
	print("username: ", username, " password: ", password)
	data = {'register_email':username,'password':password}
	r = requests.post(link, allow_redirects=False, data={})
	print(r)