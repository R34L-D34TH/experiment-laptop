import mysql.connector as db

class DBHelper:

    def __init__(self):
        self.connection = db.connect(user='MCA', 
                            password='123456789', 
                            host='127.0.0.1', 
                            database='gws')
        
        self.cursor = self.connection.cursor()
        print("[DBHelper] Connection created and cursor obtained >>>")
    
    def execute_sql(self, sql):
        print("[DBHelper] Executing Sql: ", sql)
        self.cursor.execute(sql)
        self.connection.commit()
        print("[DBHelper] Sql statement executed")
