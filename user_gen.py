import random    
import csv

surnames = []
firstnames = []
providers = []
specialchars = ['.','_','-','!']
nouns = []

firstname_file = open("data/firstnames.csv")
firstname_csv = csv.reader(firstname_file)

surname_file = open("data/surnames.csv")
surname_csv = csv.reader(surname_file)

providers_file = open("data/emailproviders.csv")
providers_csv = csv.reader(providers_file)

nouns_file = open("data/nounlist.csv")
nouns_csv = csv.reader(nouns_file)

for i in surname_csv:
  surnames.append(str(i)[2:-2].lower().capitalize())
  
for i in firstname_csv:
  firstnames.append(str(i)[2:-2].lower().capitalize())
  
for i in providers_csv:
  providers.append(str(i)[2:-2].lower().capitalize())
  
for i in nouns_csv:
  nouns.append(str(i)[2:-2])

class user:
  def __init__(self):
    self.birthyear = random.randint(1940,2004)
    self.firstname = random.choice(firstnames)
    self.surname = random.choice(surnames)
    self.username = self.__generate_user()
    self.password = self.__generate_pass()
    self.email = self.__generate_email()
    
  def __str__(self):
    return "----------------\n" +\
      "name: " + self.firstname + " " + self.surname + "\n" +\
      "user pass: " + self.username + " " + self.password +"\n" +\
      "email:" + self.email +\
      "\n----------------"
 
  def __generate_user(self):
    choice = random.randint(0,8)
    if(choice < 2):
      return self.firstname.lower() + self.surname.lower()
    elif(choice < 3):
      return self.firstname.lower() + "." + self.surname.lower()
    elif(choice < 4):
      return self.firstname.lower() + str(self.birthyear)
    elif(choice < 5):
      return self.firstname.lower() + str(self.birthyear*random.randint(0,50))
    elif(choice < 6):
      return self.surname.lower() + self.firstname.lower()
    elif(choice < 8):
      return self.firstname.lower()[0:1] + self.surname.lower()[0:1] + str(self.birthyear*random.randint(0,50))
    else:
      return str(self.birthyear*random.randint(0,50)) + self.firstname.lower()
   
  def __generate_pass(self):
    choice = random.randint(0,6)
    if(choice < 1):
      return random.choice(nouns) + str(self.birthyear*random.randint(0,50)) 
    elif(choice < 2):
      return random.choice(nouns) + random.choice(nouns) 
    elif(choice < 3):
      return random.choice(nouns) + str(self.birthyear) + random.choice(specialchars)
    elif(choice < 4):
      return self.surname.lower() + str(self.birthyear*random.randint(0,50)) + random.choice(specialchars)
    elif(choice < 5):
      return random.choice(nouns).capitalize() + random.choice(specialchars) + str(self.birthyear)
    else:
      return random.choice(nouns).capitalize() + random.choice(nouns)
    
  def __generate_email(self):
    return self.username + random.choice(providers)


def request_users(count):
  users = []

  for i in range(0, count):
    users.append(user())

  return users
  
