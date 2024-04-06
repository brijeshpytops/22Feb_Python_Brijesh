from . import dbConnection

def add_data():
    sql = """INSERT INTO students (fullname, age) VALUES
    ('John Doe', 20),
    ('Jane Smith', 22),
    ('Michael Johnson', 21),
    ('Emily Brown', 19),
    ('David Wilson', 23),
    ('Sarah Martinez', 20),
    ('James Taylor', 22),
    ('Emma Anderson', 21),
    ('Daniel Clark', 19),
    ('Olivia White', 20);
    """
    dbConnection.cursor.execute(sql)
    dbConnection.db.commit()