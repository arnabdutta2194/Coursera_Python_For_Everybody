import re
fopen=open("mbox-short.txt")
arr=list()
for lines in fopen:
    lines=lines.rstrip()
  
    y=re.findall("^X-DSPAM-Confidence: ([0-9.]+)",lines)
    if len(y) != 1:
        continue
    num=float(y[0])
    arr.append(num)

print(max(arr))