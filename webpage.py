from flask import Flask, render_template, redirect, url_for, request
import pandas as pd
import emailing

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    user_database = pd.read_csv("users.csv", index_col = 0)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        count = user_database['username'].count()
        user_database.loc[count+1] = [username, email, password]
        user_database.to_csv("users.csv", header=True)
        
        emailing.main()
        return "We have sent an email including log files"

    return render_template('signup.html')

@app.route('/signin.html', methods=['GET', 'POST'])
def signin():
    user_database = pd.read_csv("users.csv", index_col = 0)
    error = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            check_index = user_database.loc[user_database['email']==email].index
            check = user_database.iloc[check_index[0]-1]
        except:
            return "Sorry Wrong Credentials"

        if password == check['password']:
            emailing.main()
            return "We have sent an email including log files"
            
        else:
            return "Sorry Wrong Credentials"

    return render_template('signin.html')  

if __name__ == '__main__':
    app.run(host="10.7.6.85", port=5000, debug=True)