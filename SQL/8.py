import psycopg2
from psycopg2 import Error


try:
    connection = psycopg2.connect(user="postgres",
                                  password="U9w!rVcc!LTSdAD",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")

    cursor = connection.cursor()

    cursor.execute('''SELECT Users.NAME
                   FROM Users
                   INNER JOIN Relationships
                   ON Users.ID=Relationships.ID2
                   WHERE Relationships.ID1 > 18''')
    print(cursor.fetchall())

    connection.commit()

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
