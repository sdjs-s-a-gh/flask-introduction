import os.path
import pyodbc
import click
from flask import Flask, g, current_app

# Function to get the database connection
def get_db():
    if 'db' not in g:   # g = current request
        # Constructing the connection string
        file_path = os.path.dirname(os.path.abspath(__file__))
        conn_str = "Driver={Microsoft Access Driver (*.mdb, *.accdb)};" \
                   "Dbq=" + os.path.join(file_path, "testing whether this actually works.accdb") + ";" \
                                                                                                   "Uid=Admin;Pwd=;"

        # Establishing the connection
        g.db = pyodbc.connect(conn_str)

    return g.db


# Function to initialize the database
def init_db():
    db = get_db()
    cursor = db.cursor()

    # Creating user table
    cursor.execute("""CREATE TABLE user (
        id autoincrement PRIMARY KEY,
        username varchar(30) NOT NULL UNIQUE,
        password varchar(147) NOT NULL
    )""")

    # Creating post table
    cursor.execute("""CREATE TABLE post (
        id autoincrement PRIMARY KEY,
        author_id integer NOT NULL,
        created timestamp NOT NULL,
        title varchar(30) NOT NULL,
        body varchar(200) NOT NULL,
        FOREIGN KEY (author_id) REFERENCES user (id)
    )""")

    db.commit()


# Close database connection
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


# Command to initialize the database
@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


# Initialize database command
def init_app(app):
    app.teardown_appcontext(close_db)  # tells Flask to call that function when cleaning up after returning the response.
    app.cli.add_command(init_db_command)  # adds a new command that can be called with the flask command.
