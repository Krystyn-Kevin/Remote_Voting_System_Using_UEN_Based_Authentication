#results.py
import time
import mysql.connector
import csv
import pandas as pd
import matplotlib.pyplot as plt

print("-----------------------------------------------------------------------")
print("Sql Setup")
hst=input("Hostname: ")
usr=input("Username: ")
pas=input("Password: ")
print("-----------------------------------------------------------------------")
#part1
dup=[]
nondup=[]
rigger=[]
with open ("Votes.csv","r") as vc:
    r=csv.reader(vc)
    for record in r:
        uen=record[0]
        dup.append(uen)
        
for i in dup:
    if dup.count(i)==1:
        nondup.append(i)
    else:
        if i not in rigger:
            rigger.append(i)
        
with open("Votes_No_Duplicate.csv","w",newline="") as vnd:
    w=csv.writer(vnd)
    with open ("Votes.csv","r") as vc:
        r=csv.reader(vc)
        for record in r:
            uen=record[0]
            if uen in nondup:
                w.writerow(record)

with open("rigger.txt","w") as rb:
    for i in rigger:
        rb.write(i)   

print(f"Rigger List {rigger}")
print("-----------------------------------------------------------------------")
print("Establishing connection to server...")
time.sleep(3)


#part2
# appending datas into sql server

def calldb():
    global mydb
    mydb = mysql.connector.connect(
        host=hst,  # Or your MySQL server's IP/hostname
        user=usr,
        password=pas,
        database="election",    
        )
    if mydb.is_connected():
        print("Connection established to server")

def insert(a,b,c):
    
    mycursor =mydb.cursor()
    Query= "insert into "+str(table_name)+"(CEO,CAR,BIKE) values(%s,%s,%s)"
    values=(a,b,c)

    try:    
        mycursor.execute(Query,values)
        mydb.commit()
        print("")
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        mydb.rollback()

def from_csv():
    with open ("Votes_No_Duplicate.csv","r") as vf:
        r=csv.reader(vf)
        for row in r:
            v1,v2,v3=row[1],row[2],row[3]
            insert(v1,v2,v3)
              
#main program for part 2
table_name="votes"
calldb()
from_csv()
print("Datas have been inserted into Database")
print("-----------------------------------------------------------------------")
print("Loading results...")
time.sleep(3)

#part 3
# 1. Connect to MySQL
conn = mysql.connector.connect(
    host=hst,
    user=usr,     
    password=pas, 
    database="election"  
)

# 2. Read SQL table into DataFrame

query = "SELECT * FROM votes;"   
df = pd.read_sql(query, conn)
conn.close()

# 3. Count unique values in each column
counts_col1 = df['CEO'].value_counts()
counts_col2 = df['CAR'].value_counts()
counts_col3 = df['BIKE'].value_counts()

# 4. Plot frequency distributions (side by side)
plt.figure(figsize=(15,5))

plt.subplot(1, 3, 1)
counts_col1.plot(kind='bar', color='skyblue')
plt.title("CEO")
plt.xlabel("Values")
plt.ylabel("Count")

plt.subplot(1, 3, 2)
counts_col2.plot(kind='bar', color='lightgreen')
plt.title("CAR")
plt.xlabel("Values")

plt.subplot(1, 3, 3)
counts_col3.plot(kind='bar', color='salmon')
plt.title("BIKE")
plt.xlabel("Values")

plt.tight_layout()
plt.show()


time.sleep(999)
