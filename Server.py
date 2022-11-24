#cd WebServer - jumps forward a directory
#Python3 Server.py
#venv\Scripts\activate   #activates the virtual environment
#flask --app Server.py run <--- run this at home because of secutity risks
#flask --app Server.py --debug run #allows saved changes to occur in realtime

from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route("/") #Loads the page
def home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name) #calls different html files

def writeTXT(data):
    with open("database.txt", mode = "a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email},{subject},{message}")
        
def writeCSV(data):
    with open("database.csv",newline = "", mode="a") as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter = ",", quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route("/submit_form", methods = ["POST","GET"])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            writeCSV(data)
            return redirect("./thankyou.html")
        except:
            return "Did not save to database..."
    else:
        return "Something went wrong, Try again!"
    
    

