# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, 
# the program reads through the dictionary using a maximum loop to find the most prolific committer.

fname=input("Enter the file name: ")
try:
    fhand=open(fname)
except:
    print("Invalid Filename")
    quit()

lines2=[]
count=dict()
for lines in fhand:
    lines.rstrip()
    if not lines.startswith("From:"):
        if lines.startswith("From"):
            lines1=lines.split()
            lines2.append(lines1[1])
for words in lines2:
    count[words]=count.get(words,0)+1
        

bigword=None
bigcount=None

for i,j in count.items():
    if bigword is None or bigcount<j:
        bigword=i
        bigcount=j

print(bigword,bigcount)