import psycopg2
from psycopg2 import Error
from faker import Faker

try:
    connection = psycopg2.connect(user="postgres",
                                  password="U9w!rVcc!LTSdAD",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")

    cursor = connection.cursor()

    cursor.execute('SET datestyle = ymd;')

    sort_query = 'SELECT * FROM TASKS ORDER BY DEADLINE ASC'
    cursor.execute(sort_query)

    print("Result ", cursor.fetchall())
    connection.commit()

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
