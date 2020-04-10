## Py code to find top 10 words in a File

fname=input("Enter the file name: ")
try:
    fhand=open(fname)
except:
    print("Invalid Filename")
    quit()

count=dict()


for line in fhand:
    # line.rstrip()
    words=line.split()
    for word in words:
        count[word]=count.get(word,0)+1
lst=list()  
for k,v in count.items():
    tup=(v,k)
    lst.append(tup)
lst=sorted(lst,reverse=True)
for v,k in lst[:10]:
    print(k,v)