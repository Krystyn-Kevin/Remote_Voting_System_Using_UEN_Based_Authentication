#sql_log_clearance
import mysql.connector as sqcon
import time

try:
    def proceed():
        cur.execute("Delete from votes")
        server.commit()
        print("SQL pre-existing records cleared")
        
    hst=input("Hostname: ")
    usr=input("Username: ")
    pas=input("Password: ")

    server=sqcon.connect(
        host=hst,
        user=usr,
        password=pas,
        database="Election")
    cur=server.cursor()

    x=input("Press Y/y to proceed SQL Data Clearance")
    if x.lower()=="y":
        proceed()

except Exception as err:
    print(err)

finally:
    time.sleep(999)
    

