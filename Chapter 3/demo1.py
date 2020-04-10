import re

fopen=open("mbox-short.txt",'r')
for lines in fopen:
    lines=lines.rstrip()
    if re.search("^X-DSPAM-P\S+: T.\S+",lines):  ##Extracting lines cotaining thursday
        print(lines)