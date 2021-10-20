from flask import Flask, redirect, url_for, render_template, request, session, flash
import pandas as pd
import time

app = Flask(__name__)
app.secret_key = 'Ayesha'

@app.route('/')
def start():
    return redirect(url_for('Login'))

@app.route('/Login', methods=['GET', 'POST'])
def Login():
    if 'user' in session:
        return redirect(url_for('Home'))
    else:
        if request.method=='POST':
            Email = request.form['Email']
            pswrd = request.form['Password']
            lg_data = pd.read_csv('loginData.csv')
            try:
                if str(lg_data.iloc[lg_data[lg_data['Email']==Email].index.values[0]]['Password']) == pswrd:
                    session['userEmail'] = Email
                    return redirect(url_for('Home'))
                else:
                    return render_template('Login form.html') 
            except:
                flash("Worng Credenials...", 'error')
                return render_template("Login form.html")
        else:
            return render_template('Login form.html')

@app.route('/Signup', methods=['GET', 'POST'])
def signup():
    if request.method=='POST':
        Name = request.form['Name']
        mail = request.form['Email']
        pswrd = request.form['Password']
        Cpswrd = request.form['CPassword']
        CNICID = request.form['CNIC']
        Phone = request.form['Phone']
        if pswrd == Cpswrd: #len(pswrd)>7 and 
            lg_cre = [[Name, mail, pswrd, CNICID, Phone]]
            lg_data = pd.DataFrame(lg_cre)
            lg_data.to_csv('loginData.csv', mode='a', index=False, header=False)
            if True:
                return redirect(url_for('Login'))
        else:
            return render_template('Signup.html')
    else:
        return render_template('Signup.html')

@app.route('/Home', methods=['GET', 'POST'])
def Home():
    return render_template('Home page.html')

@app.route('/FindJob', methods=['GET', 'POST'])
def FindJob():
    return render_template('Find job.html')

if __name__ == '__main__':
    app.run(debug=True) 
