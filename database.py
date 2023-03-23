import sqlite3

#conn = sqlite3.connect(':memory:')


#create a database
conn = sqlite3.connect('customer.db')

#create a cursor
c = conn.cursor()

#create a table
#DATATYPES - NULL INTEGER REAL TEXT BLOB
#c.execute("""CREATE TABLE customers (
#    first_name text,
#    last_name text,
#    email text
#    )""")
#-----------------------------------------------------
#insert data manually:
#c.execute("INSERT INTO customers VALUES ('Tim', 'Smith', 'tim@codemy.com')")
#---------------------------------------------------
#insert many into the database
#many_customers = [('Wes', 'Brown', 'wes@brown.com'),
#                   ('Steph', 'Kuewa', 'steph@kuewa.com'),
#                   ('Dan', 'Pas', 'dan@pas.com',)]

#c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)
#---------------------------------------------------

#Query the database
#c.execute("SELECT * FROM customers")
#print(c.fetchone()[0])
#print(c.fetchmany(3))
#print(c.fetchall())

#------------------------------------------------
#print using loop and formating
#print("NAME " + "\t\tEMAIL")
#print("---=--"+"\t\t------")

#for item in items:
#    print(item[0]+ " " + item[1]+ "\t\t" + item[2])
#-------------------------------------------------

#query the database with ID
c.execute("SELECT rowid,* FROM customers")

items = c.fetchall()

for item in items:
    print(item)



#commit our comand
conn.commit()

#close our connection
conn.close()