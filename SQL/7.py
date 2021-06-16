import random

import psycopg2
from psycopg2 import Error


try:
    connection = psycopg2.connect(user="postgres",
                                  password="U9w!rVcc!LTSdAD",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")

    cursor = connection.cursor()

    create_table_query = '''CREATE TABLE Relationships
                  (ID  INT PRIMARY KEY    NOT NULL,
                   ID1 INT                NOT NULL,
                   ID2 INT                NOT NULL); '''

    cursor.execute(create_table_query)

    for i in range(1000):
        n = random.randint(1, 1001)
        m = random.randint(1, 1001)
        while n == m:
            m = random.randint(1, 1001)
        insert_query = 'INSERT INTO Relationships (ID, ID1, ID2) VALUES (' + str(i + 1) + ', ' + str(n) + ', ' + str(m)\
                       + ')'
        cursor.execute(insert_query)

    connection.commit()

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
