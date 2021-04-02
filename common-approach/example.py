import sqlite3  # aliasing
con = sqlite3.connect('data.db')
cur = con.cursor()
cur.execute('create table if not exists USER(id int ,name text,age int) ')

# insert  dummy data

ID = 123
name = 'someundra'
age = 40

cur.execute(' insert into USER values(?,?,?) ', (ID, name, age))

# Fetch data
# 1. Fetch all data
# 2. Fetch some data based on a condition
# 3. Fetch specific data

result = cur.execute('select * from USER ')
# print(result)
# # print(result)
# result = result.fetchone()
# print(result)
# print(' ID = {} '.format(result[0]))
# print(' Name = {} '.format(result[1]))
# print(' Age = {} '.format(result[2]))

# Fetch many data
# result = result.fetchall()
# print(result)

result = result.fetchmany()
for row in result:
    print(row)
