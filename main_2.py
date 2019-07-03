from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/", methods=['GET'])
def homepage():
    return render_template('front_page.html')


@app.route("/", methods=['POST'])
def sign_up():
    

    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]
    verify = request.form["verify"]

    username_error = ""
    password_error = ""
    email_error = ""
    retype_error = ""
    
    if password != verify:
        retype_error = "The passwords do not match."
    else: 
        retype_error = ""

    if " " in username or len(username) < 3 or len(username) >20:
        username_error = "The username is not valid."
    else: username_error = ""
    
    if " " in password or len(password) < 3 or len(password) >20:
        password_error = "The password is not valid."
    else: username_error = ""
  
    if email != "":
        if " " in email or len(email) < 3  or len(email) >20 or "." not in email or "@" not in email:
            email_error = "The email is not valid."
        else: 
            email_error = ""

    else:
        email_error = ""
        
    if username_error == password_error == email_error == retype_error:
        
        return render_template("welcome.html",username=username)
    else: 
        return render_template("front_page.html",username = username, email = email, username_error=username_error,password_error=password_error, email_error=email_error,retype_error=retype_error)
               
     
app.run()