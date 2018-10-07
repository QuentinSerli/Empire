#!/usr/bin/env python

listeners = [
    "dbx",
    "http_com",
    "http_hop",
    "http_mapi",
    "meterpreter",
    "onedrive",
    "http_foreign",
    "http",
    "redirector",
]

agents = ["powershell","python"]

tests = {
    "agents": [
    ],
    "listener1":[
    ],
    "listener2":[
    ],
    "stager1":[
    ],
    "stager2":[
    ]
}

l1pairs = {}
l2pairs = {}

for l in listeners:
    for l2 in listeners:
        tests["listener1"].append(l)
        tests["listener2"].append(l2)

for i in range(0,len(tests["listener1"])):
    for a in agents:
        if not ("{},{}".format(a,tests["listener1"][i]) in l1pairs and "{},{}".format(a,tests["listener2"][i]) in l2pairs):
            tests["agents"].append(a)
            if "{},{}".format(a,tests["listener1"][i]) not in l1pairs:
                l1pairs["{},{}".format(a,tests["listener1"][i])] = True
            else:
                l2pairs["{},{}".format(a,tests["listener2"][i])] = True
    if len(tests["agents"]) <= i:
        tests["agents"].append("*")

print "listener1,listener2,agent_language"
for l in range(0,len(tests["listener1"])):
    print """{l1},{l2},{a}""".format(l1 = tests["listener1"][l],l2 = tests["listener2"][l], a = tests["agents"][l])
