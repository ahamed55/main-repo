import re
import csv
import operator

error={}
user={}

def create_dict():
    with open("syslog.log") as file:
        for i in file:
            error_pattern=re.search(r"ticky: ERROR ([\w ']*) \((.*)\)",i)
            info_pattern=re.search(r"ticky: INFO ([\w ]*) ",i)
            username=re.search(r"ticky: .*\((.*)\)",i)
            if (error_pattern is not None):
                if username[1] not in user:
                    user[username[1]]=dict()
                    user[username[1]]["ERROR"]=1
                    user[username[1]]["INFO"]=0
                else:
                    user[username[1]]["ERROR"]+=1
                if error_pattern[1] not in error:
                    error[error_pattern[1]]=1
                else:
                    error[error_pattern[1]]+=1
            else:
                if username[1] not in user:
                    user[username[1]]=dict()
                    user[username[1]]["INFO"]=1
                    user[username[1]]["ERROR"]=0
                else:
                    user[username[1]]["INFO"]+=1

create_dict()
#print(error)
l=[]
s=[]
for i,j in user.items():
    l.append(i)
    s.append(j)
for i in range(len(l)):
    s[i]["username"]=l[i]
username_list = sorted(s, key=operator.itemgetter('username'))
a=sorted(error.items(), key=operator.itemgetter(1),reverse=True)
with open("error.csv","w") as csvfile:
    writer=csv.writer(csvfile)
    writer.writerows(a)
    keys=["username","INFO","ERROR"]
with open("username.csv","w") as file:
    writer=csv.DictWriter(file,fieldnames=keys)
    writer.writeheader()
    writer.writerows(username_list)