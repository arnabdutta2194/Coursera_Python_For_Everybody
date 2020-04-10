import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignoring SSL Certificates

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

#Reading the URL

urlin="http://py4e-data.dr-chuck.net/known_by_Fikret.html"

#Eshtablising connection and handler and reading the whole webpage as one

# html=urllib.request.urlopen(urlin,context=ctx).read()

# # #Cleaing the data

# soup=BeautifulSoup(html,'html.parser')

# #Retrieving all anchor tags

# tags=soup('a')
# arr=list()
# for tag in tags:
#     tag1=(tag.get("href",None)).strip()
#     arr.append(tag1.split())
# nexturl=arr[2][0]

count=0

while count<3:
    urlin1=urlin
    html1=urllib.request.urlopen(urlin1,context=ctx).read()
    soup1=BeautifulSoup(html1,'html.parser')
    tags1=soup1('a')
    arr1=list()
    for tag1 in tags1:
        tag2=(tag1.get("href",None)).strip()
        arr1.append(tag2.split())
    urlin=arr1[2][0]

    count=count+1
    print(urlin)

