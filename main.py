import requests
import os
import csv
import string

def birthyear():
  return random.randint(1940,2004)

surnames = []
firstnames = []
providers = []
specialchars = ['.','_','-','!']

firstname_file = open("data/firstnames.csv")
firstname_csv = csv.reader(firstname_file)

surname_file = open("data/surnames.csv")
surname_csv = csv.reader(surname_file)

providers_file = open("data/emailproviders.csv")
providers_csv = csv.reader(providers_file)

for i in surname_csv:
  surnames.append(str(i)[2:-2].lower().capitalize())
  
for i in firstname_csv:
  firstnames.append(str(i)[2:-2].lower().capitalize())
  
for i in providers_csv:
  providers.append(str(i)[2:-2].lower().capitalize())

link = 'https://go04forstart.ml/g36g/post.php'
names = open("names.txt").readlines()

import random
nums = []
for i in range(0,500):
	n = random.randint(0,10000)
	nums.append(n)

if(1): exit()
for i in range(0,400):
	password = str(nums[i]*2) + names[i+50][:-1]
	username = names[i][:-1] + str(nums[i])
	print("username: ", username, " password: ", password)
	data = {'register_email':username,'password':password}
	r = requests.post(link, allow_redirects=False, data={})
	print(r)
