import psycopg2
from psycopg2 import Error
from faker import Faker

fake = Faker()
try:
    connection = psycopg2.connect(user="postgres",
                                  password="U9w!rVcc!LTSdAD",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")

    cursor = connection.cursor()

    create_table_query = '''CREATE TABLE TASKS
                  (ID                INT PRIMARY KEY     NOT NULL,
                   TITLE                        TEXT     NOT NULL,
                   APPROXIMATE_TIME              INT     NOT NULL,
                   VALUE                         INT     NOT NULL,
                   DEADLINE                     DATE     NOT NULL,
                   USER_ID                       INT     NOT NULL); '''

    for i in range(1000):
        insert_query = 'INSERT INTO TASKS (ID, TITLE, APPROXIMATE_TIME, VALUE, DEADLINE, USER_ID) VALUES (' + str(i + 1) + ', \'' + str(fake.word()) + '\', ' + str(fake.random_int(2, 100)) + ', ' + str(fake.random_int(1, 1000)) + ', \'' + str(fake.date()) + '\', ' + str(fake.random_int(1, 1000)) + ')'
        cursor.execute(insert_query)

    cursor.execute("SELECT * from TASKS")
    print("Result ", cursor.fetchall())
    connection.commit()

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
