arr=[20,12,33,111,23]
count=0
sum=0
print(arr[0],sum,count)
for i in arr:
    sum=sum+i
    count=count+1
    print(i,sum,count)
avg=sum/count
print(avg)