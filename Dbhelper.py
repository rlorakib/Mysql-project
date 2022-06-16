import mysql.connector as connector

class dbhelper:
    def __init__(self):
        self.conn = connector.connect(host='localhost',
                                      port = 3306, 
                                      user='root',
                                      password = 'bukacuda2121',
                                      database='pythonest')
        query = 'create table if not exists user(userId int primary key,userName varchar(200), phone varchar(12))'                               
        cur = self.conn.cursor()
        cur.execute(query)
        print('Created')



    def insert_user(self,userid,username,phone):
        query = "insert into user(userId,userName,phone) Values({},'{}','{}')".format(userid,username,phone)
        print(query)
        curr = self.conn.cursor()
        curr.execute(query)
        self.conn.commit()
        print('user saved to db')
    

  
  
    def fetch_all(self):
        query = 'select * from user'
        cur =self.conn.cursor()
        cur.execute(query)
        for row in cur:
            print('User Id :',row[0])
            print('User Name :',row[1])
            print('User phone :',row[2])
            print()
            print()

    def delete_user(self,userid):
        query = "Delete from user where userid ={}".format(userid)
        print(query)
        c = self.conn.cursor()
        c.execute(query)
        self.conn.commit()
        print('deleted')

    
    def update_user(self, userid, newName, newPhone):
        query = "Update user set userName ='{}', phone='{}' where userId={}".format(newName, newPhone, userid)
        print(query)
        cu = self.conn.cursor()
        cu.execute(query)
        self.conn.commit()
        print('Updated')

