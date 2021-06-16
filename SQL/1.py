import psycopg2
from psycopg2 import Error
from faker import Faker

fake = Faker()
print(fake.phone_number)
try:
    connection = psycopg2.connect(user="postgres",
                                  password="U9w!rVcc!LTSdAD",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")

    cursor = connection.cursor()

    create_table_query = '''CREATE TABLE Users
              (ID INT PRIMARY KEY     NOT NULL,
               NAME          TEXT     NOT NULL,
               EMAIL         TEXT     NOT NULL,
               PHONE_NUMBER  INT      NOT NULL,
               AGE           INT      NOT NULL); '''

    cursor.execute(create_table_query)
    for i in range(1000):
        insert_query = 'INSERT INTO Users (ID, NAME, EMAIL, PHONE_NUMBER, AGE) VALUES (' + str(i + 1) + ', \'' + \
                       str(fake.name()) + '\', \'' + str(fake.email()) + '\', ' + \
                       str(fake.random_int(100000000, 900000000)) + ', ' + str(fake.random_int(20, 100)) + ')'
        cursor.execute(insert_query)
    cursor.execute("SELECT * from Users")
    print("Result ", cursor.fetchall())
    connection.commit()

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
