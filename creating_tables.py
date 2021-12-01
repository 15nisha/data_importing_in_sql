import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user= "root", password = "", database = "testing")

mycursor = mydb.cursor()



mycursor.execute("Create table table1( ID int NOT NULL, category varchar(255), PRIMARY KEY (ID))")
mycursor.execute("Create table table2( Id int NOT NULL ,job_roles varchar(255))")
mycursor.execute("Create table table3( ID int NOT NULL ,job_roles LONGTEXT,description LONGTEXT,title LONGTEXT)")
