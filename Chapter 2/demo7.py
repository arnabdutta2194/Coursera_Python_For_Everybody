line=input("Enter A Sentence")
line.rsplit()
arr=line.split()
print(arr)
count=dict()
for words in arr:
    count[words]=count.get(words,0)+1
print(count)