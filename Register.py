#register.py
from flask import Flask, request, render_template_string
import os
import csv

app = Flask(__name__)

# Directory and file setup
SAVE_DIR1 = 'Voting'
os.makedirs(SAVE_DIR1, exist_ok=True)
CSV_FILE = os.path.join(SAVE_DIR1, 'VoterList.csv')

# Write header if file doesn't exist
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'UEN'])
txtfile="original.txt"
with open (txtfile,"w") as tf:
    tf.write(" ")
# HTML form as a string
RegisterSite = """
<!DOCTYPE html>
<html>
<head>
    <title>Enrollment Site</title>
</head>
<body>
    <h2>Register Your Name and UNE</h2>
    <h3>Enter Your Name and UEN</h3>
    {% if message %}
        <p style="color:green;">{{ message }}</p>
    {% endif %}
    <form action="/submit" method="post">
        <input type="text" name="name" required placeholder="Name">
        <br><input type="text" name="number" required placeholder="Number">
        <br><button type="submit">Submit</button>
    </form>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(RegisterSite)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    number = request.form.get('number')
    if not name or not number:
        return render_template_string(RegisterSite, message="Both name and number are required!"), 400


    #Append name and number tio txt file
    with open ("original.txt","r+") as of:
        x=of.readlines()
        for i in x:
            if name in i  and number in i:
                return render_template_string(RegisterSite, message=f"Name {name} and Number {number} already saved!")
            
            else:
            # Append name and number to CSV
                with open(CSV_FILE, 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([name, number])
                a=name+"  "+number+"\n"
                of.write(a)
                of.flush()
                return render_template_string(RegisterSite, message=f"Name {name} and Number {number} saved successfully!")

if __name__ == '__main__':
    app.run(debug=True)
