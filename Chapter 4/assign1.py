import sqlite3
import re
conn = sqlite3.connect("orgcount.sqlite")
curr=conn.cursor()
curr.execute("DROP TABLE IF EXISTS Counts")
curr.execute("CREATE TABLE Counts (org TEXT,count INTEGER)")
filename=input("Enter File Name that Contains all org: ")
if len(filename)<1: filename="mbox.txt"
fh=open(filename)
for line in fh:
    if not line.startswith("From:"): continue
    pieces=line.split()
    orgn=re.findall('@(\S+)',pieces[1])
    org=orgn[0]
    
    curr.execute("SELECT count FROM Counts where org=?",(org,))
    row=curr.fetchone()
    if row is None:
        curr.execute("INSERT INTO Counts (org,count) VALUES (?,1)",(org,))
    else:
        curr.execute("UPDATE Counts SET count=count+1 WHERE org=?",(org,))

   
conn.commit()
sqlstr="SELECT org,count FROM Counts ORDER BY count DESC"
for row in curr.execute(sqlstr):
    print(str(row[0]),str(row[1]))
curr.close()