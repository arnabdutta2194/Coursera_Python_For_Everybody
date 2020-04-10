import urllib.request,urllib.parse,urllib.error
urlhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
print(type(urlhand))
count=dict()
for lines in urlhand:
    line=lines.decode().split()
    for words in line:
        count[words]=count.get(words,0)+1
    
print(count)

