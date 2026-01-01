#Operation Steps
import time
import tkinter as tk

def opr_pro():
     print(a)

def cust():
    print(b)

def mod():
    print(c)
    
a="""•Run "SQL_Setup.py" for MySQL setup for fisrt time
•Open UEN_Generator.py to generate the UEN for users
•UEN stands for Unique Enrollment Number
•Open "Register.py" & "Authenticator.py"(Directory - Voting) in cmd
•Open Web_Server directory and open "online_portal.html" 
•Then click on User Registration for first time registration or click Login & Cast vote 
•To display results click on voting dirctory click on "Results.py" then the rest happens, finds fraudlant votes, gives rigged voter UEN and Name list, inserts datas into database, then graphical output is generated
•To clear existing datas in SQL run "SQL_Refresh.py"
"""

b="""•To add any new voting category follow these steps:
1.Get into Election.db alter table votes, by adding desired coloumn name with desired datatype
2.Get into Voting\\Templates\\Votesite.html, add <h6> add desired coloumn name and options with radio button
3.Get into Voting\\Authenticator.py, go on to line number 75 you will find 'submit_vote():'.Under it's block add a variable to retive the value from website
4.Get into Voting\\Results.py, go to line number 78 add variable to extract record on coloumn you have added in line 79 add variable in the argument of 'insert()'
5.In same program in line 58 add parameter on 'insert():', in line 61 add coloumn name and %s character and in line 62 add parameter
6.In same program refer line 112 to display the result of the coloumn you have added
7.In same program refer line 137 to create the chart values
8.In same program refer line 146 to display the graphical output of coloumn you added
Happy Coding
"""

c="""•Required Modules:
1.matplotlib
2.mysql.connector.python
3.flask
4.pandas
5.tkinter
"""
    
root=tk.Tk()
root.title("Operating Manual")
tk.Button(root,text="Operating Procedure",command=opr_pro).pack()
tk.Button(root,text="Customize",command=cust).pack()
tk.Button(root,text="Required Modules",command=mod).pack()
tk.Button(root,text="Quit",command=root.quit).pack()
root.mainloop()

