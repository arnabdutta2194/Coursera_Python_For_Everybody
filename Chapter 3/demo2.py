import re
str1="I have 10 rupees and you have 20 rupees"
y=re.findall("[0-9]+",str1)
print(y)

str2="From: today I am going to: Study"
z=re.findall("F.+?:",str2)
print(z)

str3="From: abc.ua.xd@hd.com.bc Sat Jan 5 09:14:16"
q=re.findall("\S+@\S+",str3)
m=re.findall("@[^ ]+",str3)

a=re.findall("^F.+ (\S+@\S+)",str3)
print(q)
print(m)
print(a)

str4="I have $10 rupees and you have $20 rupees"
s=re.findall("\$[0-9]+",str4)

print(s)

