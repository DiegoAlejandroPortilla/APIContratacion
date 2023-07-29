import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="newpassword",
        database="TennantDB"
    )
    print("Database connected successfully")
except Exception as ex:
    print("Error: ", ex)