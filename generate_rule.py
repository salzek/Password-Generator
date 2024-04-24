import os

def my(m):
    if "?s" in m:
        return m.index("?s")
    else:
        return 1

# charsets="!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

# most common used specialchars from domain users 
# this used to reduce hash cracking time
charsets="\"?!\\\"%'*+,-./>?@_\","

passwords = ""
passwords = open("pass.txt", "r", encoding="utf-8")
rules = []
groups = {}

for password in passwords.readlines():
    rule = ""
    password = password.strip()
    for _chr in password:
        if _chr.islower():
            rule += "?l"
        elif _chr.isupper():
            rule += "?u"
        elif _chr.isdecimal():
            rule += "?d"
        else:
            rule += "?s"
    else:
        rules += [rule]
    
for rule in rules:
    uzunluk = len(rule)
    if str(uzunluk) in groups:
        groups[str(uzunluk)].append(rule)
    else:
        groups[str(uzunluk)] = [rule]

for i in groups:
    eleman = set(groups.get(i))
    eleman = sorted(eleman, key=my)
    
    groups[i] = eleman

item = list(groups.keys())
item.sort()

if os.path.exists("rules.txt"):
    os.remove("rules.txt")
else:
    print("yok")

for i in item:
    #print(i)
    #print("---------------")

    with open("rules.txt", "a", encoding="utf-8") as f:
        for j in groups.get(i):
            #print(j)
            if "?s" in j:
                f.write(charsets+j+'\n')
            else:
                f.write(j+'\n')

