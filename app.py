from bitcoin import json
from os import getenv, environ
from flask import Flask, render_template, session, request, redirect, url_for,g
from db import get_db, get_amounts_owned, create_tables, create_first_data, clear_table, update_owned_amounts, update_notes, get_notes
from helper import strip, break_down

app = Flask(__name__)

app.secret_key = 'Bruce Wayne is Batman'

DATABASE = 'crypto.db'



@app.route('/', methods=['GET', 'POST'])
def home_page():
    #clear_table()
    #create_tables()
    #create_first_data()
    print( 40 * "-")
    print()
    amounts_owned = get_amounts_owned()
    b_owned = amounts_owned['bitcoin']
    e_owned = amounts_owned['ethereum']
    d_owned = amounts_owned['dogecoin']

    notes = get_notes()
    data = json['data']
    
    for item in data:
        name = item['name']
        if name == "Bitcoin":
            temp = item['quote']['EUR']['price']
            bitcoin = int(temp)
        elif name == "Ethereum":
            temp = item['quote']['EUR']['price']
            ethereum = int(temp)
        elif name == "Dogecoin":
            temp = item['quote']['EUR']['price']
            dogecoin = int(temp*1000)/1000
    print()
    print( 40 * "-")

    if request.method == "POST":
        action = request.form.get("submit")
        if action == "save":
            notes = request.form.get("message")
            update_notes(notes)
            session['notes'] = notes

    return render_template('home.html', 
            json=json, 
            page_title="Home", 
            bitcoin=bitcoin, 
            ethereum=ethereum, 
            dogecoin=dogecoin,
            b_owned=b_owned,
            e_owned=e_owned,
            d_owned=d_owned,
            notes=notes
            )


@app.route('/update', methods=['GET', 'POST'])
def update_page():
    amounts_owned = get_amounts_owned()
    b_owned = amounts_owned['bitcoin']
    e_owned = amounts_owned['ethereum']
    d_owned = amounts_owned['dogecoin']

    data = json['data']
    for item in data:
        name = item['name']
        if name == "Bitcoin":
            temp = item['quote']['EUR']['price']
            bitcoin = int(temp)
        elif name == "Ethereum":
            temp = item['quote']['EUR']['price']
            ethereum = int(temp)
        elif name == "Dogecoin":
            temp = item['quote']['EUR']['price']
            dogecoin = int(temp*1000)/1000

    if request.method == "POST":
        b_owned = request.form.get("b_update")
        e_owned = request.form.get("e_update")
        d_owned = request.form.get("d_update")

        update_owned_amounts(b_owned, e_owned, d_owned)

    return render_template("update.html", 
            json=json, 
            page_title="Update", 
            bitcoin=bitcoin, 
            ethereum=ethereum, 
            dogecoin=dogecoin, 
            b_owned=b_owned,
            e_owned=e_owned,
            d_owned=d_owned
            )



@app.route("/chart")
def chart():
    notes = session.get('notes')
    data = strip(notes)
    chart_string = break_down(data)
    #print(f"*{data}*")
    return render_template("chart.html", chart=chart_string)


'''

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = verify_user(password=password, email=email)
        if user:
            session['userid'] = user[0]
            return render_template('home.html', user=user);
        else:
            msg = 'Invalid email or password'
            return render_template('login.html', msg=msg);

        return
    elif request.method == 'GET':
        return render_template('login.html');

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm = request.form['confirm-password']
        msg = None
        if password != confirm:
            msg = 'Passwords Do Not Match'
        elif not email:
            msg = 'Must have an email'
        elif not name:
            msg = 'Must have a name'
        else:
            user = add_user(name=name, password=password, email=email)
            if not user:
                msg = 'Unable To Add User'
            return redirect(url_for('login'))
        return render_template('signup.html', msg=msg);
    elif request.method == 'GET':
        return render_template('signup.html');

@app.route('/logout')
def logout():
    session.pop('userid', None)
    return redirect(url_for('home_page'))


'''

# Do not alter this if statement below
# This should stay towards the bottom of this file
if __name__ == "__main__":
    flask_env = getenv('FLASK_ENV')
    if flask_env != 'production':
        environ['FLASK_ENV'] = 'development'
        app.debug = True
        app.asset_debug = True
        server = Server(app.wsgi_app)
        server.serve()
    app.run()

    #https://api.nasa.gov/planetary/apod?api_key=VM2f40EQQ0tk58nvmPhpVa6gthc5ma6Chgll56N7