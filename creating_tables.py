import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user= "root", password = "Nisha@15224", database = "testing")

mycursor = mydb.cursor()



# mycursor.execute("Create table job_category(Id int NOT NULL, Industry varchar(200),PRIMARY KEY (Id))")
# mycursor.execute("Create table job_roles(job_id int NOT NULL  , job_role varchar(),FOREIGN KEY (job_id) REFERENCES job_category(Id))")
# mycursor.execute("Create table job_description(job_role varchar() , job_decs varchar(), job_title varchar(),FOREIGN KEY (job_role) REFERENCES job_roles(job_role)")
# # mycursor.execute("Create table customer ( ID int NOT NULL AUTO_INCREMENT, PRIMARY KEY (ID) )")
# mycursor.execute("show tables")
# mycursor.execute("Create table custom ( ID int NOT NULL ,name varchar(20), PRIMARY KEY (ID) )")
# mycursor.execute("Create table contact ( ID int, customer_Id int,CONSTRAINT fk_customer FOREIGN KEY (Customer_Id) REFERENCES customer(ID) ON DELETE CASCADE  ON UPDATE CASCADE )")
# for tb in mycursor:
# mycursor.execute("Create table cont ( ID int, customer_Id int,CONSTRAINT fk_customs FOREIGN KEY (Customer_Id) REFERENCES custom(ID) ON DELETE CASCADE  ON UPDATE CASCADE )")
#     print(tb)


mycursor.execute("Create table table1( ID int NOT NULL, category varchar(255), PRIMARY KEY (ID))")
mycursor.execute("Create table table2( Id int NOT NULL ,job_roles varchar(255))")
mycursor.execute("Create table table3( ID int NOT NULL ,job_roles LONGTEXT,description LONGTEXT,title LONGTEXT)")