import ssl
from bs4 import BeautifulSoup
import urllib.request,urllib.parse,urllib.error


urlin=input("Enter URL: ")
count=int(input("Enter Count: "))
pos=int(input("Enter Position: "))

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE



    
counter=0

while counter < count:
    urlin1=urlin
    html1=urllib.request.urlopen(urlin1,context=ctx).read()
    soup1=BeautifulSoup(html1,'html.parser')
    tags1=soup1('a')
    arr1=list()
    for tag1 in tags1:
        tag2=(tag1.get("href",None)).strip()
        arr1.append(tag2.split())
    urlin=arr1[pos-1][0]

    counter=counter+1
    print("Retrieving: ",urlin)





