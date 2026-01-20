import mysql.connector as con


connection = con.connect(
    host="localhost",
    user = "root",
    password = "Anant@1234",
    database = "pythondb"
)
print("Connection is done")

cursor = connection.cursor()

# driver ko bola - code ko sql ke pass lejao -> execute -> code apka run hojaega -> DB
cursor.execute("select * from pythondb")

print("Database is created")