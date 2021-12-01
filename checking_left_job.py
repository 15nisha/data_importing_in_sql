import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user= "root", password = "", database = "testing")

mycursor = mydb.cursor()

query = "SELECT DISTINCT job_roles FROM table3 where ID = 10;"
mycursor.execute(query)
list1 =[]
myresult = mycursor.fetchall()
for row in myresult:
    x = row[0]
    list1.append(x)

query = "SELECT job_roles FROM table2 where Id = 10;"
mycursor.execute(query)
result = []
list2 =[]
myresult = mycursor.fetchall()
for row in myresult:
    y = row[0]
    list2.append(y)
for i in list2:
    if i not in set(list1):
        result.append(i)
print(result)
