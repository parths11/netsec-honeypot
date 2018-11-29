import json
from pprint import pprint
from collections import Counter

def userpasswd(data):
    userpa = []
    for i in data:
        if(i["eventid"]=="cowrie.login.success"):
            userpa.append(i["username"]+"/"+i["password"])
    return userpa

def passwords(data):
    passwd = []
    for i in data:
        if(i["eventid"]=="cowrie.login.success" or i["eventid"]=="cowrie.login.failed"):
            passwd.append(i["password"])
    return passwd

def usernames(data):
    user = []
    for i in data:
        if(i["eventid"]=="cowrie.login.success" or i["eventid"]=="cowrie.login.failed"):
            user.append(i["username"])
    return user

def percent_success_login(data):
    total_conn = 0
    success_login = 0
    for i in data:
        if(i["eventid"]=="cowrie.session.connect"):
            total_conn += 1
        if(i["eventid"]=="cowrie.login.success"):
            success_login +=1
    return total_conn, success_login

def json_readr(file):
    x = []
    for line in open(file, mode="r"):
        x.append(json.loads(line))
    return x

f1 = 'cowrie.json'
f2 = 'cowrie.json.2018-11-08'
f3 = 'cowrie.json.2018-11-07'
f4 = 'cowrie.json.2018-11-06'
data = json_readr(f1) + json_readr(f2) + json_readr(f3) + json_readr(f3)
total, success = percent_success_login(data)
u = usernames(data)
us = set(u)
uc = Counter(u)
for i in uc.most_common():
    print('{}     :{}'.format(i[0], i[1]), file=open("username_freq.txt", "a"))
u10 = uc.most_common(10)
p = passwords(data)
ps = set(p)
for i in ps:
    print(i, file=open("pass_obtained.txt", "a"))
pc = Counter(p)
for i in pc.most_common():
    print('{}     :{}'.format(i[0], i[1]), file=open("password_freq.txt", "a"))
p10 =  pc.most_common(10)
up = userpasswd(data)
ups = set(up)
upc = Counter(up)
for i in upc.most_common():
    print('{}     :{}'.format(i[0], i[1]), file=open("user_pass_freq.txt", "a"))
up10 = upc.most_common(10)
print("total connections = {}".format(total))
print("successful logins = {}".format(success))
print("% success logins = {}".format((success*100)/total))
print("\n")
print("usernames used: {}".format(len(u)))
print("No. of unique username guesses: {}".format(len(us)))
print("Top ten username guesses:")
for i in u10:
    print("{}  :  {}".format(i[0], i[1]))
print("\n")
print("passwords used: {}".format(len(p)))
print("No. of unique password guesses: {}".format(len(ps)))
print("Top ten password guesses:")
for i in p10:
    print("{}  :  {}".format(i[0], i[1]))
print("\n")
print("successful user/pass combinations: {}".format(len(up)))
print("No. of successful unique user/pass combinations: {}".format(len(ups)))
print("Top ten user/pass successes:")
for i in up10:
    print("{}  :  {}".format(i[0], i[1]))
