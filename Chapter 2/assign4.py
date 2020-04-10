# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. 
# Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

fname=input("Enter the file name: ")
try:
    fhand=open(fname)
except:
    print("Invalid Filename",fname)
    quit()
count=0
val=0
for line in fhand:
    line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    finder=line.find("0")
    value=line[finder:]
    val=val+float(value)
    count=count+1

print("Average spam confidence:", val/count)