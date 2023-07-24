from sess14B import DBHelper
import datetime
import mysql.connector as db

class Customer:

    def __init__(self):
        self.cid = 0
        self.name = ""
        self.phone = ""
        self.email = ""
        self.age = ""
        self.gender = ""
        self.address = ""
        self.createdon = ""

    def read_customer_data(self):
        self.cid = 0
        self.name = input("Enter your name:- ")
        self.phone = input("Enter your phone:- ")
        self.email = input("Enter your email:- ")
        self.age = int(input("Enter your age:- "))
        self.gender = input("Enter your gender:- ").lower()
        self.address = input("Enter your address:- ")
        self.createdon = str(datetime.datetime.today())
        self.createdon = self.createdon[: self.createdon.rindex(".")]

    def get_insert_sql_query(self):
            sql = "insert into Customer values (null, '{name}', '{phone}', '{email}', {age}, '{gender}', '{address}', '{createdon}');".format_map(vars(self))
            return sql


def main():
    db = DBHelper()
    customer = Customer()
    customer.read_customer_data()
    print(vars(customer))
    sql = customer.get_insert_sql_query()
    db.execute_sql(sql)

if __name__ == "__main__":
    main()


