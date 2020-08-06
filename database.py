import sqlite3


CREATE_BEANS_TABLE = "CREATE TABLE IF NOT EXISTS tblRequest (id INTEGER PRIMARY KEY, TimeOfRequest TEXT, PersonDetected TEXT);"
INSERT_BEAN = "INSERT INTO tblRequest (TimeOfRequest, PersonDetected) VALUES (?,?);"
GET_ALL_BEANS = "SELECT * FROM tblRequest;"

def connect():
    return sqlite3.connect("cynapto.db")

def create_tables(connection):
    with connection:
        connection.execute(CREATE_BEANS_TABLE)

def add_bean(connection, TimeOfRequest, PersonDetected):
    with connection:
        connection.execute(INSERT_BEAN, (TimeOfRequest, PersonDetected))

def get_all_beans(connection):
    with connection:
        return connection.execute(GET_ALL_BEANS).fetchall()


def menu(TimeOfRequest, PersonDetected):
    connection = connect()
    create_tables(connection)


    add_bean(connection, TimeOfRequest, PersonDetected)

def display_beans():
	connection = connect()
	beans = get_all_beans(connection)
	for bean in beans:
		print(bean)