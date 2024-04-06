from . import dbConnection

def show_rows():
    sql = "select * from students order by age DESC"
    dbConnection.cursor.execute(sql)
    mydata = dbConnection.cursor.fetchall()
    for data in mydata:
        print(data)