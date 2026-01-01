#authenticator.py
from flask import Flask, request, render_template, redirect, url_for
import csv
import os

app = Flask(__name__)

CSV_FILE ="VoterList.csv" # Path to your CSV file
voted_file="Voted.txt"
if not os.path.exists(voted_file): # check whether .txt exist 
    with open(voted_file,"a",newline="") as vf:
        x=" "
        vf.write(x)

 
@app.route('/', methods=['GET'])
def index():
    return render_template('VoteLogin.html')

@app.route('/submit', methods=['POST'])
def submit():
    global number
    name = request.form.get('name')
    number = request.form.get('number')
    found = False

    # Check if CSV exists
    if not os.path.exists(CSV_FILE):
        return render_template('VoteLogin.html', error="Data file not found.")

    # Search for matching name and number
    with open(CSV_FILE,newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 2:
                csv_name, csv_number = row[0], row[1]
                if csv_name == name and csv_number == number:
                    found = True
                    break
   
    voted=False
    #check if the user already voted
    if not voted and found == True:
        with open(voted_file,"r") as vf:
            for i in vf:
                if name in i and str(number) in i:
                    voted=True
                else:
                    voted=False
    #writes the user name who didn't voted and loged in now
    with open(voted_file,"a") as vf:
        if not voted and found : 
            x=name+"    "+str(number)+'\n'
            vf.write(x)
            vf.flush
        vf.close
        
    if voted == True and  found == True:   # voted and name found
        return redirect(url_for("ThankYou"))
    if voted == False and found == True:  #not voted but name found
        return redirect(url_for("VoteSite"))
    if not found: #name not found
        return render_template('VoteLogin.html', error="Name and number not found or do not match.")


@app.route('/ThankYou')
def ThankYou():
    return render_template('ThankYou.html')

@app.route('/VoteSite', methods=['GET'])
def VoteSite():
    return render_template("VoteSite.html")

@app.route('/submit_vote', methods=['POST'])
def submit_vote():
    R1= request.form.get('R1')
    R2= request.form.get('R2')
    R3= request.form.get('R3')
    #if more button add that much request needed
    with open("Votes.csv", "a", newline='') as vote_file:
        writer = csv.writer(vote_file)
        writer.writerow([number,R1,R2,R3])#check here for more buttons
    return render_template('TY.html')
   

if __name__ == '__main__':
    app.run(port=8000,debug=True)
