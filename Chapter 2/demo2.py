data1="Banana is a good fruit"
count=0
# for i in data1:
#     count=count+1
#     print(count,i)
data2=data1[:4:2]
print(data2)

if 'n' in data1:
    print("Found")


print(data1.lower())
print(data1.upper())

b=data1.find('is')
print(b)

data3=data1.replace("is","was")
print(data3)

x = 'From marquard@uct.ac.za'
print(x[8])
print(x[14:17])


data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])