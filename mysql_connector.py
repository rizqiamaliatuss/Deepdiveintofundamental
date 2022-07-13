import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="********",
  database=""
)

if mydb.is_connected():
    print('berhasil')