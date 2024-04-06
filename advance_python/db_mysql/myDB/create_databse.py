from . import dbConnection

def create_db():
    database_name = input("eRnter a database name : ")
    sql = f"create database {database_name}"
    dbConnection.cursor.execute(sql)