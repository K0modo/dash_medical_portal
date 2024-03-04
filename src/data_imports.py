####  CSV Files
# \PycharmProjects\Database\sqlite_tables\sqlite_render

# import csv
# import sqlite3
#
# # Connect to database
# connection = sqlite3.connect(',,/db_tynan.db')
#
# # Create cursor object connected to database
# # SQL queries on a database table
# cursor = connection.cursor()

# # Table Definition
# create_table = '''CREATE TABLE v_daily_claims(
#                     charge_trans_date DATE PRIMARY KEY,
#                     period INTEGER,
#                     claims_count INTEGER,
#                     charges_paid FLOAT);
#                     '''

# # Creating a cursor object to execute...create a table
# cursor.execute(create_table)

# Opening csv file
# file = open(r"C:\Users\jchri\PycharmProjects\Database\sqlite_tables\sqlite_render\v_daily_claims.csv")
#
# # Reading the contents of the file
# contents = csv.reader(file)
#
# # SQL query to define what columns will be inserted
# insert_records = "INSERT INTO v_daily_claims (charge_trans_date, period, claims_count, charges_paid) VALUES (?, ?, ?, ?)"
#
# # Importing the data into the table
# cursor.executemany(insert_records, contents)

# SQL query to retrieve data from the table
# select_all = "SELECT * FROM v_daily_claims"
# rows = cursor.execute(select_all).fetchall()
#
# # Output to console
# for r in rows:
#     print(r)
#
# # Committing the changes
# connection.commit()
#
# # Close the database connection
# connection.close()
#
