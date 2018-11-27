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
p = passwords(data)
up = userpasswd(data)
print("total connections = {}".format(total))
print("successful logins = {}".format(success))
print("% success logins = {}".format((success*100)/total))
print("\n")
print("\n")
print("usernames used: {}".format(u))
print("passwords used: {}".format(p))
print("successful user/pass combinations: {}".format(up))
