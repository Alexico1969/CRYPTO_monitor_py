import sqlite3, os
from flask import g

DATABASE = 'crypto.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def get_amounts_owned():
    cur = get_db().cursor()
    result = cur.execute('''
       select name, owned from cryptos;
    ''')
    data = result.fetchall()
    output = {}
    for key, value in data:
        output[key] = value
    
    return output

def create_first_data():
    conn = get_db()
    cur = conn.cursor()
    cur.execute('''
       insert into cryptos (name, owned) values ("bitcoin","0.02225897");
    ''')
    cur.execute('''
       insert into cryptos (name, owned) values ("ethereum","0.1160818");
    ''')
    cur.execute('''
       insert into cryptos (name, owned) values ("dogecoin","233.5857");
    ''')
    conn.commit()
    return

def create_tables():
    # Creates all the tables
    connection = get_db()
    sql = connection.cursor()
    sql.execute('''
        CREATE TABLE if not exists cryptos (
	    crypto_id INTEGER PRIMARY KEY AUTOINCREMENT,
   	    name text NOT NULL,
	    owned text NOT NULL
        )
    ''')

def clear_table():
    connection = get_db()
    sql = connection.cursor()
    sql.execute('''
            delete from cryptos;
                ''')
    return


def update_owned_amounts(b_owned, e_owned, d_owned):
    connection = get_db()
    sql = connection.cursor()
    sql.execute('''UPDATE cryptos set owned=? where name=?''', (b_owned, "bitcoin"))
    connection.commit()
    sql.execute('''UPDATE cryptos set owned=? where name=?''', (e_owned, "ethereum"))
    connection.commit()
    sql.execute('''UPDATE cryptos set owned=? where name=?''', (d_owned, "dogecoin"))
    connection.commit()