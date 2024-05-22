# Import the psycopg2 module
import psycopg2

connection=psycopg2.connect(user='postgres',
                            password='peti2020#',
                            port='5432',
                            database='db_persons'
                            )

cursor=connection.cursor()

# sql sentence
sql='DELETE FROM persons WHERE id_person=%s'

# Request user data
id_person=input('Enter the id of the person you want to delete: ')

# Execute method
cursor.execute(sql,(id_person,))

# Save changes
connection.commit()

# Close cursor and connection
cursor.close()
connection.close()

# User message
print('Person deleted successfully')

# End of the program
print('End of the program')


