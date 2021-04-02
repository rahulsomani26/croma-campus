import sqlite3 as s
'''
  Create a table 
  Ask user for his/her ID,name,age 
  Insert that into the table 
  Fetch the user data from the table 
  
'''

con = s.connect('data.db')
cur = con.cursor()
# Ask for user input

# count = 0
# while count < 5:

#     ID = int(input("Enter ID"))
#     name = input("Enter name")
#     age = input("Enter age")
#     cur.execute('insert into USER values(?,?,?)', (ID, name, age))
#     con.commit()
#     count = count+1

result = cur.execute('select name,age from USER')
dataset = result.fetchall()
# print(dataset[0])
for r in dataset:
    print(f' name = {r[0]}')
    print(f' age = {r[1]}')

con.close()
