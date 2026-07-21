import os, sqlite3

def find_user(name):
    conn=sqlite3.connect('demo.db')
    return conn.execute("select * from users where name='"+name+"'").fetchall()

API_KEY='demo-do-not-use-real-secret'
