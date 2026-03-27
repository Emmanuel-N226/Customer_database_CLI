import sqlite3


#connect to sqlite3
conn = sqlite3.connect('customer.db')

#create a cursor to edit database
c = conn.cursor()

#function for creating a Table
def create_table():
    #every function should have the connection and cursor
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS customers(
            firstname TEXT,
            lastname TEXT,
            email TEXT
            )""")
    print(">> code ran successfully")
    conn.commit()
    conn.close()

#run table on import
create_table()

#Adding all the data
def add_items():
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()

    customer_data = [('Liam', 'Johnson', 'liam@gamil.com'),
                     ('Amanda', 'Berry', 'berry.com'),
                     ('Noah', 'Smith','noah.smith@outlook.com'),
                     ('Emma','Brown','emma.brown@gmail.com'),
                     ('James','Taylor','james.taylor@yahoo.com'),
                     ('Sophia', 'Anderson', 'sophia.anderson@outlook.com')]
    c.executemany("INSERT INTO customers VALUES(?,?,?)", customer_data)
    print(">> code ran succcessfully..")
    conn.commit()
    conn.close()

    #viewng all the data with ROWID
def viewall_customer_data():
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM customers")

    items = c.fetchall()

    for item in items:
      print(item)
    
    conn.close()   


#update a first_name column
def update_first_name(row_id, new_first_name): 
       conn = sqlite3.connect("customer.db")
       c = conn.cursor()
       #Sql update first_name
       c.execute("UPDATE customers SET firstname = ? WHERE rowid = ? ",(new_first_name, row_id))
       print(">> first name has been updated...")
       conn.commit()
       conn.close()

#update a last_name column
def update_last_name(row_id, new_last_name): 
       conn = sqlite3.connect("customer.db")
       c = conn.cursor()
       #Sql update first_name
       c.execute("UPDATE customers SET lastname = ? WHERE rowid = ? ",(new_last_name, row_id))
       print(">> last name has been updated...")
       conn.commit()
       conn.close()
       
#update the email column
def update_email(row_id, new_email): 
       conn = sqlite3.connect("customer.db")
       c = conn.cursor()
       #Sql update first_name
       c.execute("UPDATE customers SET email = ? WHERE rowid = ? ",(new_email, row_id))
       print(">> email has been updated...")
       conn.commit()
       conn.close()

#delete a row usid its row_id
def delete_row(row_id): 
    conn = sqlite3.connect("customer.db")
    c = conn.cursor()
    #Sql update first_name
    c.execute("DELETE from customers WHERE rowid = ? ",(row_id,))
    print(">> Row succesfully deleted...")
    conn.commit()
    conn.close()