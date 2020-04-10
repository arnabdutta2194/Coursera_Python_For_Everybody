fname=input("Enter the file name: ")
fhand=open(fname)

count=dict()
for line in fhand:
    line.rsplit()
    words=line.split()
    for word in words:
        count[word]=count.get(word,0)+1

print(count)
        
bigword=None
bigcount=None
print(count.items())
for i,j in count.items():
 

    if bigcount is None or j > bigcount:
        bigword=i
        bigcount=j

print(bigword,bigcount)