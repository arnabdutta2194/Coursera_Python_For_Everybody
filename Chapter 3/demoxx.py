import re
fopen=open("regex_sum_393454.txt")
inp=fopen.read()

y=re.findall("[0-9]+",inp)
print(y)
count=0
arr=list()
for i in range(len(y)):
    int1=int(y[count])
    arr.append(int1)
    count=count+1

print(sum(arr))


