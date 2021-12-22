from flask import Flask, request, render_template, jsonify,url_for,redirect, session, Markup
import os
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
print(os.urandom(24))
idpass={'1032180782@mitwpu.edu.in':'Test@12345'}

app = Flask(__name__)
app.secret_key = os.urandom(24)

s = URLSafeTimedSerializer('Thisisasecret!')

@app.route("/",methods=["POST","GET"])
def login():
    if 'user_id' in session:
        return redirect('/home')
    else:
        if request.method == "POST":
            email_found= request.form.get("email")
            email_found=""
            password= request.form.get("pass")
            if email_found in idpass:
                if password==idpass[email_found]:
                    session['user_id'] = email_found
                    return redirect("/home")
                else:
                    return render_template('login.html',message="wrong password")
            else:
                return render_template('login.html',message="Wrong Email")
        else:
            return render_template('login.html')

@app.route("/home")
def home():
    if 'user_id' in session:
        return render_template('base.html')
    else:
        return redirect('/')

@app.route("/logout")
def logout():
    session.pop('user_id')
    return redirect('/')

if __name__ == "__main__":
    app.run()
