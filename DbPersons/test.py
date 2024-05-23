# Import psycopg2 module
import psycopg2

# Create database connection
connection=psycopg2.connect(user='postgres',
                            password='peti2020#',
                            host='127.0.0.1',
                            port='5432',
                            database='db_persons'
                            )

# Use cursor
cursor=connection.cursor()

# Create sql sentence
sql='SELECT * FROM people'

# Use Execute method
cursor.execute(sql)

# Fetch all records
records=cursor.fetchall()

# Show records
for record in records:
    print(record)

# Close cursor and connection
cursor.close()
connection.close()

# End
print('End of the program')

# In this case, the SELECT sentence is used to retrieve all records from the table. The fetchall method is used to retrieve all records. The records are displayed using a for loop. Finally, the cursor and connection are closed.
#

