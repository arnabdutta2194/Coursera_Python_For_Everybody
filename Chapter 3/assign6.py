import json
import urllib.request,urllib.parse,urllib.error


serviceurl=input("Enter location: ")
uh=urllib.request.urlopen(serviceurl)
print("Retrieving ",serviceurl)

data=uh.read().decode()
print("Retrieved",len(data),"characters")

try:
    info=json.loads(data)
except:
    info=None

arr=list()


for item in info["comments"]:
    arr.append((item["count"]))

print(sum(arr))

