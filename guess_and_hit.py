# -*- coding: utf-8 -*-
"""Guess and Hit

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HqqzkRSeuwRrtIgt4nd1bDjWoYPTDNQT

##**Guess and Hit**##
"""

def w():
  return print("""
.----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| | _____  _____ | || |  _________   | || |   _____      | || |     ______   | || |     ____     | || | ____    ____ | || |  _________   | |
| ||_   _||_   _|| || | |_   ___  |  | || |  |_   _|     | || |   .' ___  |  | || |   .'    `.   | || ||_   \  /   _|| || | |_   ___  |  | |
| |  | | /\ | |  | || |   | |_  \_|  | || |    | |       | || |  / .'   \_|  | || |  /  .--.  \  | || |  |   \/   |  | || |   | |_  \_|  | |
| |  | |/  \| |  | || |   |  _|  _   | || |    | |   _   | || |  | |         | || |  | |    | |  | || |  | |\  /| |  | || |   |  _|  _   | |
| |  |   /\   |  | || |  _| |___/ |  | || |   _| |__/ |  | || |  \ `.___.'\  | || |  \  `--'  /  | || | _| |_\/_| |_ | || |  _| |___/ |  | |
| |  |__/  \__|  | || | |_________|  | || |  |________|  | || |   `._____.'  | || |   `.____.'   | || ||_____||_____|| || | |_________|  | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
'----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'
""","                                                  ...This is Guessing Game...",sep="\n"*5)

L=[]
def game():
  def ran():
    i=randrange(len(dic))
    j=randrange(len(dic))
    a=dic[i]
    b=dic[j]
    p=True
    while p is True:
      if a != b:
        p = False
      else:
        p = True
    return (a,b)
  a,b=ran()
 # if a

  def choice(a,b):
    c=input(f"""=> Which of the Following has more number of Followers?
                  (i){a}                              (ii){b}
                    [Type(1)]                                    [Type(2)]
                    \n Your Answer :  """)
    if int(c)==1:
      c=a
    elif int(c)==2:
      c=b
    else:
      print("***Invalid input!***")
      print("Please type: (0) or (1)")
      c=None
      exit()
    return c
  c=choice(a,b)
  def result(a,b):
    if d[a] > d[b]:
      r=a
    elif d[b] > d[a]:
      r=b
    return r
  r = result(a,b)
  def judgement(r,c):
    if r==c:
      j="""                                 ***VICTORY! You have won it.***"""
    else:
      j="                               ***Sorry! You lost it.***"
    return j
  j=judgement(r,c)
  print(j)
  if r==c:
    o = True
  else:
    o = False
  return o

from random import randrange
d={"Virat Kohli":263000000,"Priyanka Chopra":89800000,"Shraddha Kapoor":84300000,"Narendra Modi":81000000,"Alia Bhatt":80700000,"Katrina Kaif":77800000,"Akshya Kumar":100000000,"Hrithik Roshan":12500000000,"Sachin Tendulkar":1250000000,"Apple": 15600000,"Google": 22400000,"Microsoft": 14800000,"Amazon": 10200000,"Tesla": 13700000,"Facebook": 21000000,"Samsung": 18300000,"IBM": 9800000,"Intel": 12800000,"Netflix": 16200000,"Twitter": 36000000,"Snapchat": 24000000,"LinkedIn": 33000000,"Oracle": 8300000,"Adobe": 11700000,"Uber": 22000000,"Airbnb": 13000000,"Sony": 17600000,"Cisco": 7800000,"PayPal": 15800000,"Toyota": 7500000,"Volkswagen": 6200000,"General Motors": 5900000,"Ford": 8200000,"Honda": 6900000,"BMW": 6800000,"Mercedes-Benz": 7100000,"Tesla": 13700000,"Nissan": 5800000,"Audi": 6600000,"Hyundai": 5500000}
dic=list(d.keys())
w()
print(5*"\n")
start=input("""To play the game type ('Space') :
For Exit the game type any key :  """)
print(5*"\n")
if start == " ":
  def ran():
    i=randrange(len(dic))
    j=randrange(len(dic))
    a=dic[i]
    b=dic[j]
    p=True
    while p is True:
      if a!=b:
        p = False
      else:
        p = True
    return (a,b)
  a,b=ran()

  def choice(a,b):
    c=input(f"""=> Which of the Following has more number of Followers?
                  (i){a}                              (ii){b}
                    [Type(1)]                                    [Type(2)]
                    \n Your Answer :  """)
    if int(c)==1:
      c=a
    elif int(c)==2:
      c=b
    else:
      print("***Invalid input!***")
      print("Please type: (0) or (1)")
      c=None
      exit()
    return c
  c=choice(a,b)
  def result(a,b):
    if d[a] > d[b]:
      r=a
    elif d[b] > d[a]:
      r=b
    return r
  r = result(a,b)
  def judgement(r,c):
    if r==c:
      j="""                                 ***VICTORY! You have won it.***"""
    elif c==None:
      j=""
    else:
      j="                               ***Sorry! You lost it.***"
    return j
  j=judgement(r,c)
  print(j)
  i=True
  while i is True:
    if r == c:
      i = game()
    else:
      i=False
else:
  print("Thanks! You have exited the game.")
  exit()