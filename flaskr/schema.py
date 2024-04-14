import os.path
import pyodbc

file_path = os.path.dirname(os.path.abspath(__file__))

conn_str = "Driver={Microsoft Access Driver (*.mdb, *.accdb)};Dbq=" + file_path + "/testing whether this actually works.accdb;Uid=Admin;Pwd=;"

conn = pyodbc.connect(conn_str)

cursor = conn.cursor()

cursor.execute("""CREATE TABLE user (
    id  autoincrement PRIMARY KEY,
    username varchar(30) NOT NULL, 
    password varchar(30) NOT NULL
)""")

cursor.execute("""CREATE TABLE post (
    id  autoincrement PRIMARY KEY,
    author_id  integer NOT NULL,
    title varchar(30) DEFAULT 'no',
    body varchar(200) NOT NULL,
    FOREIGN KEY (author_id) REFERENCES user (id)
)""")

cursor.commit()
conn.close()
