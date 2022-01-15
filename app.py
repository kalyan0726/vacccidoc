from flask import Flask, render_template, request, url_for, redirect, flash
import database

app = Flask(__name__)
app.config['SECRET_KEY'] = 'F5TH7654KI890PL75RFV12TG78ILF421'


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/register')
def reg():
    return render_template('register.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/que')
def quee():
    return render_template('questionnaire.html')


@app.route('/output')
def out():
    return render_template('output.html')


@app.route('/output1')
def out1():
    return render_template('output1.html')


@app.route('/login_validation', methods=['POST'])
def login_validation():
    email = request.form.get('email')
    password = request.form.get('password')
    flag = database.verify_user(email, password)
    if flag:
        return redirect(url_for("home"))
    else:
        return redirect(url_for("login"))


@app.route('/reg_validation', methods=['POST'])
def reg_validation():
    name = request.form.get('Name')
    email = request.form.get('email')
    password = request.form.get('password')
    re_password = request.form.get('re_password')
    if password == re_password:
        profile = {"user_name": name, "user_email": email, "pw": password}
        database.create_profile_db(profile)
        return redirect(url_for("login"))
    else:
        return redirect(url_for("reg"))


@app.route('/que_validation', methods=['POST'])
def que_validation():
    useroutput1 = request.form.get('browser')
    useroutput2 = request.form.get('browser1')
    useroutput3 = request.form.get('browser2')
    useroutput4 = request.form.get('browser3')
    useroutput5 = request.form.get('browser4')
    useroutput = [useroutput1, useroutput2, useroutput3, useroutput4, useroutput5]
    count1 = useroutput.count('yes')
    count2 = useroutput.count('no')
    if count1 > count2:
        return redirect(url_for("out"))
    else:
        return redirect(url_for("out1"))


if __name__ == "__main__":
    app.run(debug=True)
