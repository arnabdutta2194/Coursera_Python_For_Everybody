import urllib.request,urllib.parse,urllib.error
import ssl
import xml.etree.ElementTree as ET 

url=input("Enter the Url: ")
print("Retrieving ",url)

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

html1=urllib.request.urlopen(url,context='ctx').read()


tree=ET.fromstring(html1)
lst=tree.findall('comments/comment')
arr=list()

for item in lst:
    arr.append(int(item.find('count').text))

print(sum(arr))