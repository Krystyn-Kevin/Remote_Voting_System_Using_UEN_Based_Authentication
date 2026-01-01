import mysql.connector as server
import time


        
try:
   km=["This program creates the MySQL database and table so run only once during fresh start of program",
   "You can deploy this program if you have any technical issue with MySQL, but make sure you have deleted the pre-existing database before you deploy this program",
   "Database: Election",
   "Table: Votes"]
   i=0
   while i<len(km):
      print (km[i])
      i+=1

   hst=input("enter hostname: ")
   usr=input("enter username: ")
   pas=input("enter password: ")
   a=server.connect(host=hst,user=usr,password=pas)
   if a.is_connected:
      print("connection established")
   cur=a.cursor()
   qurey="create database if not exists election;"
   cur.execute(qurey)
   qurey="use election;"
   cur.execute(qurey)
   qurey="create table votes(CEO varchar(40),CAR varchar(40),BIKE varchar(40));"
   cur.execute(qurey)
        
except Exception as err:
    print(err)
    print()
        
finally:
    print("SQL Setup Completed")





