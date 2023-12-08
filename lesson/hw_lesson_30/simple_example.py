import psycopg2

connection = psycopg2.connect(user="postgres",
                              password="Addidass1988",
                              host="localhost",
                              port="5432",
                              database="postgres")

cursor = connection.cursor()
cursor.execute("SELECT * from userstable;")
connection.commit()
for row in cursor.fetchall():
    print(row)
    print(type(row))
cursor.close()
if connection:
    connection.close()