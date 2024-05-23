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
sql='DELETE FROM persons WHERE id_person=%s'

# Request user data
id_person=input('Enter the id of the person you want to delete: ')

# Execute method
cursor.execute(sql, id_person)

# Save changes
connection.commit()

# Count the amount of changes
remove_records = cursor.rowcount

# If the record was not found
if remove_records == 0:
    print('The record was not found')
else:
    print(f'Records removed: {remove_records}')

# Close cursor and connection
cursor.close()
connection.close()

# End
print('End of the program')
# In this case, the DELETE sentence is used to remove a record from the table. The user is asked to enter the id of the person to be deleted. The id is passed as a parameter to the execute method. The number of records removed is stored in the remove_records variable. If the record was not found, a message is displayed. Finally, the cursor and connection are closed.
#