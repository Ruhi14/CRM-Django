# install Mysql in your computer
#pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python


import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost', 
    user = 'root', 
    passwd = 'Ruhi@2003'
)

# prepare a cursor object

cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE Ruhi")

print("all done")