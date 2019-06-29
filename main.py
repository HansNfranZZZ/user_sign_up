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

    username_error = "Username is not valid"
    password_error = ""
    email_error = ""
    retype_error = ""
    
    while True: 
        valid = False 
        if password != verify:
            return str("<span> passwords do not match </span>")
            continue
        elif " " in username or len(username) <= 3 or len(username) >=20:
                    return render_template("front_page.html", username_error = username_error)
                    continue
        elif " " in password or len(password) <= 3 or len(password) >=20:
                    return str("<span> password is not valid </span>")
                    continue
        elif " " in email or len(email) <= 3  or len(email) >=20 or "." not in email or "@" not in email:
                            return str("<span> email is not valid </span>")
                            continue
        else:
            valid = True
            break
    if valid:
        return str("<h1> Welcome, ") + username + str("!</h1>")
    
    @app.route("/welcome")
    def logged_in():
        username = request.args.get("username")
        return render_template("welcome.html",username=username) 
             
     
app.run()