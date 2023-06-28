import psycopg2

connection = psycopg2.connect(
    database="store",
    host="127.0.0.1",
    port="5432",
    user="postgres",
    password="12345"
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM orders;")

orders = cursor.fetchall()

for order in orders:
    print(order)

cursor.close()
connection.close()
