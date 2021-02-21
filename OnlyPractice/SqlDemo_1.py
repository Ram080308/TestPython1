
import mysql.connector as connector
import csv

# Connect to database - MySql
myconnection = connector.connect(host = "localhost", user = "root", passwd = "Shonya@0803")
print("Connected Successfully!")

curser = myconnection.cursor()
curser.execute("use nop_admin")
curser.execute("select * from gift_cards")

result = curser.fetchall()

with open("new_file.xlsx" , "w", newline='') as file:
    for row in result:
        csv.writer(file).writerow(row)

curser.close()


