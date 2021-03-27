import sqlite3
# '''
#       Create a database
#       Create a connection to the database you created
#       Create a Table
#       Table must have column name
#       insert values in the table by using sql_query


# ''''

con = sqlite3.connect('user.db')
cur = con.cursor()
cur.execute(' create table if not exists USER(name TEXT,age INTEGER)')
# write some manual values in the table created
name = input("Enter username :  ")
age = int(input("Enter age :   "))
# cur.execute(' insert into USER values("rahul",40)')
cur.execute(' insert into USER values(?,?)',(name,age))
con.commit()

result = cur.execute('select * from USER')
record = result.fetchall()
# print(record)
for row in record:
    print(row)


# cur.close()
# con.close()
