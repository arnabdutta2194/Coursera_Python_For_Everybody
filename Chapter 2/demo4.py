handle=open("mbox.txt",'r')
print(handle)

for line in handle:
    if line.startswith("http"):
        line=line.rstrip()
        print(line)
