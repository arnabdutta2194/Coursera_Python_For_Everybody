import ssl
from bs4 import BeautifulSoup
import urllib.request,urllib.parse,urllib.error

weburl="http://py4e-data.dr-chuck.net/comments_393456.html"

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

html=urllib.request.urlopen(weburl,context=ctx).read()

soup=BeautifulSoup(html,'html.parser')

tags=soup('span')

arr = list()

for tag in tags:
    tag1=int(tag.contents[0])
    print(tag1)
    arr.append(tag1)
 
print(sum(arr))
