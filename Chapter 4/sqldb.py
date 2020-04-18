import sqlite3
conn = sqlite3.connect("sqldb1.sqlite")
curr=conn.cursor()
curr.execute("DROP TABLE IF EXISTS Counts")
curr.execute("CREATE TABLE Counts (email TEXT,count INTEGER)")
filename=input("Enter File Name that Contains all Email Ids: ")
if len(filename)<1: filename="mbox-short.txt"
fh=open(filename)
for line in fh:
    if not line.startswith("From:"): continue

    pieces=line.split()
    email=pieces[1]
    curr.execute("SELECT count FROM Counts where email=?",(email,))
    row=curr.fetchone()
    if row is None:
        curr.execute("INSERT INTO Counts (email,count) VALUES (?,1)",(email,))
    else:
        curr.execute("UPDATE Counts SET count=count+1 WHERE email=?",(email,))

    conn.commit()

sqlstr="SELECT email,count FROM Counts ORDER BY count DESC"
for row in curr.execute(sqlstr):
    print(str(row[0]),str(row[1]))
curr.close()