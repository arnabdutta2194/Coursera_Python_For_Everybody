a=int(input("Enter a name:"))
b=10
c=a+b
print(c)

fruit=input("Enter the name of the fruit:")

length=len(fruit)
index=0

while index<length:
    var=fruit[index]
    print(index,var)
    index=index+1

for i in fruit:
    print(i)

data="From adutta.558.gmail@abc.cd.com Sat Jan 5 09:14:16 2008"

pos1=data.find("@")
print(pos1)
pos2=data.find(" ",pos1)
print(pos2)

data1=data[pos1+1:pos2]
print(data1)