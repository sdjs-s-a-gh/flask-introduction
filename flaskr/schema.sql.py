import os.path

import pyodbc
file_path = os.path.dirname(os.path.abspath(__file__))
db_name = "testing whether this actually works"


connection = os.path.join(file_path, db_name)

conn_str = "Driver={Microsoft Access Driver (*.mdb, *.accdb)};Dbq=" + file_path + "/testing whether this actually works.accdb;Uid=Admin;Pwd=;"

print(conn_str)
conn = pyodbc.connect(conn_str)

print(conn_str)

