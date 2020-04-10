import json

data='''[
    {
        "id" : "001",
        "name" : "Arnab",
        "ph" : "9595"
    },
    {
        "id" : "002",
        "name" : "Ronnie",
        "ph" : "9952125"
    }
]'''

info=json.loads(data)
print(len(info))
print(info)

# print("id:",info[0]["id"])
# print("Phone Number:",info[1]["ph"])

for items in info:
    print("id: ",items["id"])
    print("Name: ",items["name"])
    print("Phone Number: ",items["ph"])


x='''{ "id" : "001",
  "x" : "2",
  "name" : "Chuck"
}'''
d=json.loads(x)
print(d)