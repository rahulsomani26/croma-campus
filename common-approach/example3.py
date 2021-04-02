import sqlite3 as s

'''
    select data based on id 

'''

con = s.connect('data.db')
cur = con.cursor()

result = cur.execute('select name,age from USER where id=3')
dataset = result.fetchall()
for r in dataset:
    print(f' name = {r[0]}')
    print(f' age = {r[1]}')

con.close()
