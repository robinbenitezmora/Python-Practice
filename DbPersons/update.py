# Import the psycopg2 module

import psycopg2

connection=psycopg2.connect(user='postgres',
                            password='peti2020#',
                            host='127.0.0.1',
                            port='5432',
                            database='db_persons'
                            )

cursor=connection.cursor()

# sql sentence
sql='UPDATE FROM persons WHERE id_person=%s, name=%s, last_name=%s, age=%s WHERE id_person=%s'

# Request user data
id_person=input('Enter the id of the person you want to edit: ')
name=input('Enter your name: ')
last_name=input('Enter your last name: ')
age=input('Enter your age: ')

# Collect data
data(name, last_name, age, id_person)

# Execute method
cursor.execute(sql,(id_person,))

# Save changes
connection.commit()

# Close cursor and connection
cursor.close()
connection.close()

# User message
print('Person record upgraded successfully')

# End of the program
print('End of the program')






