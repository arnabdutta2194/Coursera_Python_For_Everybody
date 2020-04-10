arr=[23,101,22,11,129,2,333,1,21]
largest=0
for i in arr:
    if largest < i:
        print(i,largest)
        largest=i
print(largest)
smallest=arr[0]
for j in arr:
    if j < smallest:
        print(j,smallest)
        smallest=j
print(smallest)
    
        