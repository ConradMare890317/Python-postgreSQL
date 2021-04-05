import sqlite3
from employee import Employee

conn = sqlite3.connect('employee.db')
#conn = sqlite3.connect(':memory:')

c = conn.cursor()

#c.execute("""CREATE TABLE employees (
            #first_name text,
            #last_name text,
            #pay integer
            #)""")

emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)

#print(emp_1.first_name)
#print(emp_1.last_name)
#print(emp_1.pay)

#c.execute("INSERT INTO employees VALUES ('{}', '{}', {})".format(emp_1.first_name, emp_1.last_name, emp_1.pay))
#c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first_name, emp_1.last_name, emp_1.pay))

#conn.commit()

c.execute("INSERT INTO employees VALUES (:first_name, :last_name, :pay)", {'first_name': emp_2.first_name, 'last_name': emp_2.last_name, 'pay': emp_2.pay})

conn.commit()

c.execute("SELECT * FROM employees WHERE last_name = 'Schafer'")

print(c.fetchall())

conn.commit()

conn.close()