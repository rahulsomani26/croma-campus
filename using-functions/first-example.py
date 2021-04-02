'''
  create a db connection using functions 

'''

import sqlite3
con = sqlite3.connect('mydata.db')


def create_connection():

    print(' Connection created ')
    create_table()


def create_table():
    # con = sqlite3.connect('mydata.db')
    cur = con.cursor()
    cur.execute(
        'create table if not exists PERSONAL(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,age INTEGER,profession TEXT)')
    print(" Table created ")


# def insert_record():
#     # con = sqlite3.connect('mydata.db')
#     cur = con.cursor()
#     # ID = int(input("Enter ID"))
#     name = input("Enter name")
#     age = int(input("Enter age"))
#     profession = input("Enter profession")
#     cur.execute('insert into PERSONAL values (null,?,?,?)',
#                 (name, age, profession))
#     con.commit()
#     # con.close()


def insert_record_through_arg(name, age, profession):
    cur = con.cursor()
    cur.execute('insert into PERSONAL values (null,?,?,?)',
                (name, age, profession))
    con.commit()
    # con.close()


def fetch_record():
    con = sqlite3.connect('mydata.db')
    cur = con.cursor()
    dataset = cur.execute('select * from PERSONAL where name = (?) ', ('iot',))
    rows = dataset.fetchall()
    for row in rows:
        print(row)
    con.close()


create_connection()
# create_table()
# insert_record_through_arg('iot', 2, 'technology')
# insert_record()
# insert_record()
# insert_record()
fetch_record()
