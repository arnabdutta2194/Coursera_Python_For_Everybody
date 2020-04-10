# Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method.
# The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes,
# sort and print the resulting words in alphabetical order.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt

fname=input("Enter the filename: ")
try:
    fhand=open(fname)
except:
    print("Invalid file name",fname)
    quit()
arr=[]

for lines in fhand:
    line1=lines.rstrip().split()
    for i in range(len(line1)):
        if line1[i] not in arr:
            arr.append(line1[i])
    
arr.sort()
print(arr)