import re
fopen=open("regex_sum_393454.txt")
# inp=file.read()
# inp=inp.rstrip()
# print(type(inp))
# for lines in inp:
#     print(lines)
arr=list()
for line in fopen:
    line=line.rstrip()
    y=re.findall("[0-9]+",line)
    
    if len(y) != 1:
        continue
    print(y[0])

#     num=int(y[0])
#     arr.append(num)

# # print(sum(arr))
# print(sum(arr))
