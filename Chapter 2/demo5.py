 arr=[1,109,23]
# # print(arr[2])
# # arr[1]=19
# # print(arr)
# # arr1=arr.sort()
# # print(arr1)

# # for i in range(0,10,2):
# #     print(i)

# # a=[10,23,1]
# # b=[11,10,23]
# # c=a+b
# # print(c)

# # d=c[:3]
# # print(d)
# # z=type(d)
# # print(z)
# # print(dir(z))

# # d.append(10)
# # print(d)

# # arr=[]
# # while True:
# #     inp=input("Enter your number: ")
# #     if inp=="done":
# #         break
# #     value=float(inp)
# #     arr.append(value)
# # print(arr)


# sent="Hi My Name is Arnab"
# sentarr=sent.split()
# print(sentarr)

# sent1="Hi;My;Name;is;Arnab"
# sentarr1=sent1.split(";")
# print(sentarr1)

fhand=open("mbox.txt","r")
for line in fhand:
    line.rstrip()
    if not line.startswith("From"):
        continue
    line1=line.split()
    if len(line1)>3:
        print(line1[2])