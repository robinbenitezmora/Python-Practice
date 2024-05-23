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
sql='INSERT INTO persons(name, last_name, age) VALUES(%s, %s, %s)'

# Request user data
name=input('Enter your name: ')
last_name=input('Enter your last name: ')
age=input('Enter your age: ')

# Collecting data
data=(name, last_name, age)

# Use Execute method
cursor.execute(sql, data)

# Save changes
connection.commit()

# Count inserted records
inserted_records=cursor.rowcount

# Show user message
print(f'Records inserted: {inserted_records}')

# Close cursor and connection
cursor.close()
connection.close()

# End
print('End of the program')

# In this case, the INSERT sentence is used to add a record to the table. The user is asked to enter the data of the new person. The data is passed as a parameter to the execute method. The number of records inserted is stored in the inserted_records variable. Finally, the cursor and connection are closed.
#
