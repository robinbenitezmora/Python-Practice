# Import the psycopg2 module
import psycopg2

# Create connection
connection=psycopg2.connect(user='postgres',
                            password='peti2020#',
                            host='127.0.0.1',
                            port='5432',
                            database='db_persons'
                            )

# Use cursor
cursor=connection.cursor()

# Create sql sentence
sql='UPDATE FROM persons SET name=%s, last_name=%s, age=%s WHERE id_person=%s'

# Request user data
id_person=input('Enter the id of the person you want to edit: ')
name=input('Enter your name: ')
last_name=input('Enter your last name: ')
age=input('Enter your age: ')

# Collecting data
data=(name, last_name, age, id_person)

# Use Execute method
cursor.execute(sql, data)

# Save changes
connection.commit()

# Count the amount of changes
count=cursor.rowcount

# Show user message
print(f'Record updated: {count}')

# Close cursor and connection
cursor.close()
connection.close()

# End
print('End of the program')

# In this case, the UPDATE sentence is used to modify a record in the table. The user is asked to enter the id of the person to be edited, as well as the new data. The data is passed as a parameter to the execute method. The number of records modified is stored in the count variable. Finally, the cursor and connection are closed.
#
