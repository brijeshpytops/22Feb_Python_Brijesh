from . import dbConnection

def cerate_table():
    sql = "create table students(stu_id int primary key auto_increment, fullname varchar(155), age int)"
    dbConnection.cursor.execute(sql)