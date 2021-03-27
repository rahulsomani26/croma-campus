import sqlite3 
class CreateConnection: 
    
    def __init__(self):   
        con = sqlite3.connect('newuser.db')
       	print(" Database created successfully") 
        self.createTable(con)

    
         
    
    def createTable(self,myconnection):
        self.myconnection = myconnection.cursor()
        self.myconnection.execute(' create table if not exists USER(name TEXT,age INTEGER)')
    
    def insertData(self,username,age):
        self.myconnection.execute(' insert into USER values(?,?)',(username,age))
    
    def readData(self):
        self.res = self.myconnection.execute('select * from USER')
        rec = self.res.fetchall()
        print(rec)
        # for r in self.rec:
        #     print(r)
    

      
   

con = CreateConnection()
 
con.insertData('amit',40)
con.insertData('rahul',23)
con.readData()