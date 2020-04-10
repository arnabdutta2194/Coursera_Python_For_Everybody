#Continue taking input from user untill the user inputs done and find the average of all those inputs

num=0
sum=0
while True:
    sval=input('Enter the Number: ')
    if sval=='Done':
        break
    try:
        fval=float(sval)
    except:
        print("Invalid Input")
        continue
    num=num+1
    sum=sum+fval
print(sum,num,sum/num)
    
