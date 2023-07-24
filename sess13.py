"""
create table customer (
    cid int primary key auto_increment,
    name text,
    phone number,
    email text
);
"""
import mysql.connector as db

class Customer:

    def __init__(self):
        self.name = input("Enter your name:- ")
        self.phone = input("Enter your phone:- ")
        self.email = input("Enter your email:- ")


class main:
    customer = Customer()
    print (vars(customer))

#Database Connectivity 
    connection = db.connect(user='MCA', 
                            password='BlueSnake', 
                            host='127.0.0.1', 
                            database='test')

    cursor = connection.cursor()

    sql = "insert into customer values (null, '{name}', '{phone}', '{email}');".format_map(vars(customer))
    cursor.execute(sql)
    connection.commit()

    print("Customer Inserted")

if __name__ == "__main__":
    main()