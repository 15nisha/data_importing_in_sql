# import pandas as pd
import mysql.connector

# connecting with database
mydb = mysql.connector.connect(host = "localhost", user= "root", password = "", database = "testing")

mycursor = mydb.cursor()

# df = pd.read_csv("Category-Job - Sheet1.csv")


def table1_data_insertion(df):
    """
    It will insert category with unique ID value in table1.
    Input : dataframe (which has category values)
    Output : none
    """
    categ = df['Category']
    n = len(categ)
    for i in range(n):
        sqlform = "Insert into table1(ID ,category) values(%s, %s)"
        val = (i+1,categ[i])
        mycursor.execute(sqlform , val)
        mydb.commit()


def table2_data_insertion(df):
    """
    It will insert job_roles along with Id of category of role.
    Input : Dataframe (which has job_roles and category values)
    output : none
    """
    roles = df['Job Roles']
    categ = df['Category']
    m = len(roles) #len is 29
    ids = []
    for i in range(m):
        k = categ[i]
        query = f"SELECT ID FROM table1 WHERE category = '{k}'"
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        for row in myresult:
            value = row[0]
            ids.append(value)
    for i in range(m):
        job_roles = roles[i].split(',')
        for j in job_roles:
            sqlform = "Insert into table2(Id ,job_roles) values(%s, %s)"
            val = (ids[i] , j)
            mycursor.execute(sqlform , val)
            mydb.commit()


def table3_data_insertion(needed_data):
    """
    It will insert ID,job_roles ,job_description and job_title in table3
    It will derive some information from table1 and table2.
    input : Dataframe (which has description and title) 
    output : none   
    """
    id_and_job_roles = []
    #selecting tuple of (ID,category,job_roles)  by joining table 1 nad table2
    query = "SELECT table1.ID , category , job_roles  FROM testing.table1 JOIN testing.table2  where table1.ID = table2.Id "
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    for row in myresult:
        id_row = row
        id_and_job_roles.append(id_row) 
    # print(len(id_and_job_roles))

    def string_equality(s1,s2):
        """
        find equality of two strings
        input : text
        output :boolean """
        s1 = s1.lower()
        s2 = s2.lower()
        set1 = set(s1.split(' '))
        set2 = set(s2.split(' '))
        return (set1 == set2)
    # storing all tuples in id_and_job_roles list
    table2_len = len(id_and_job_roles)
    for i in range(table2_len):
        k = id_and_job_roles[i]
        ids = k[0]
        categry = k[1]
        role = k[2].strip() 
        search_string = role
        # for each search string we are copmaring with each search query in data if they are equal .
        # If they are equal, we selecting corresponding description and title then storing 
        # in table along with ID, job_roles
        l = len(needed_data)
        for s in range(l):
            x1 = needed_data['jobs/search_query'][s]
            x2 = search_string
            value = string_equality(x1,x2)
            if(value):
                title = needed_data['jobs/title'][s]
                desc = needed_data['jobs/desc'][s]
                sqlform = "Insert into table3(ID,job_roles,description,title) values(%s,%s,%s, %s)"
                val = [ids,role,desc,title]
                mycursor.execute(sqlform , val)
                mydb.commit()






