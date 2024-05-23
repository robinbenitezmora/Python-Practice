# Import psycopg2 module
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
sql='SELECT * FROM people WHERE id_person=%s'

# Request user data
id_person=input('Enter the id of the person you want to see: ')

# Collecting data
data=(id_person,)

# Use Execute method
cursor.execute(sql, data)

# Fetch one record
record=cursor.fetchone()

# Show record
print(record)

# Close cursor and connection
cursor.close()
connection.close()

# End
print('End of the program')

# In this case, the SELECT sentence is used to retrieve a specific record from the table. The user is asked to enter the id of the person to be displayed. The id is passed as a parameter to the execute method. The fetchone method is used to retrieve one record. The record is displayed. Finally, the cursor and connection are closed.
#

