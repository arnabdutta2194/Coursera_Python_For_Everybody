# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname=input("Enter the file name: ")
try:
    fhand=open(fname)
except:
    print("Invalid Filename")
    quit()

arr=list()

for line in fhand:
    line.rstrip()
    if not line.startswith("From:"):
        if line.startswith("From"):
            line1=line.split()
            arr.append(line1[5])

arr1=list()
for time in arr:
    time1=time.split(":")
    arr1.append(time1[0])

counts=dict()
for hours in arr1:
    counts[hours]=counts.get(hours,0)+1
tup=tuple()
lst=list()
for k,v in counts.items():
    tup=(k,v)
    lst.append(tup)

lst=sorted(lst)

for k,v in lst:
    print(k,v)
