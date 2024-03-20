import datetime
import tkinter as tk
from tkinter import messagebox
import oracledb

conn = None
row = None
Table_names = []


def run_query(query: str):
    global conn
    res = []
    with conn.cursor() as cur:
        try:
            cur.execute(query)
        except Exception as err:
            message = 'Error while running query: ' + str(err)
            tk.messagebox.showerror(title='Error', message=message)
            return []

        try:
            for x in cur:
                res.append(x)

        finally:

            return res


def connection(name: str, password: str, host: str, port: int, service_name: str) -> list:
    global conn, dsn
    try:
        dsn = oracledb.makedsn(host, port, service_name=service_name)

        conn = oracledb.connect(user=name, password=password, dsn=dsn)

        with conn.cursor() as cursor:
            cursor.execute("SELECT TABLE_NAME FROM USER_TABLES ORDER BY TABLE_NAME")
            table_names = [row[0] for row in cursor]

        print("\nConnection established.\n")
        return table_names

    except Exception as err:
        print("Error while creating the connection: ", str(err))
        return []


def close_connection():
    global conn
    conn.close()
    print("\nConnection closed.")


def convert_to_sql(value):
    if value is None:
        return 'NULL, '

    if type(value) == int or type(value) == float:
        return str(value) + ', '

    if type(value) == datetime.datetime:
        return 'TO_DATE(\'' + str(value.date()) + '\', \'RRRR-MM-DD\'), '

    if type(value) == str:
        if value.__contains__("SELECT"):
            return '(' + value + '), '
        else:
            return '\'' + value + '\', '

    return ', '


def select_from_table(table_name: str) -> list:
    global conn, row
    try:
        row = run_query('SELECT * FROM ' + table_name)
    except oracledb.DatabaseError as err:
        errors = 'WRONG'
        conn.rollback()
        message = 'Error while inserting into table: ' + str(err)
        tk.messagebox.showerror(title='Error', message=message)
        return errors
    return row


def insert_into_table(table_name: str, values: list):
    global conn
    values_String = '('
    for x in values:
        values_String += convert_to_sql(x)

    values_String = values_String[:len(values_String) - 2] + ')'

    try:
        run_query('INSERT INTO ' + table_name + ' VALUES ' + values_String)
    except oracledb.DatabaseError as err:
        errors = 'WRONG'
        conn.rollback()
        message = 'Error while inserting into table: ' + str(err)
        tk.messagebox.showerror(title='Error', message=message)
        return errors


def insert_into_table_clienti(table_name: str, values: list):
    global conn
    values_String = '('
    for x in values:
        values_String += convert_to_sql(x)

    values_String = values_String[:len(values_String) - 2] + ')'

    try:
        with conn.cursor() as cur:
            cur.execute('SAVEPOINT TEMP2')
            cur.execute('INSERT INTO ' + table_name + ' VALUES ' + values_String)
            if len(select_from_table(Table_names[2])) > len(select_from_table(table_name)):
                cur.execute('ROLLBACK TO TEMP')
            elif len(select_from_table(Table_names[2])) < len(select_from_table(table_name)):
                cur.execute('ROLLBACK TO TEMP2')
            else:
                cur.execute('COMMIT')
    except oracledb.DatabaseError as err:
        errors = 'WRONG'
        conn.rollback()
        message = 'Error while inserting into table: ' + str(err)
        tk.messagebox.showerror(title='Error', message=message)
        return errors


def insert_into_table_adrese(table_name: str, values: list):
    global conn
    values_String = '('
    for x in values:
        values_String += convert_to_sql(x)

    values_String = values_String[:len(values_String) - 2] + ')'

    try:
        with conn.cursor() as cur:
            cur.execute('SAVEPOINT TEMP')
            cur.execute('INSERT INTO ' + table_name + ' VALUES ' + values_String)
    except oracledb.DatabaseError as err:
        errors = 'WRONG'
        conn.rollback()
        message = 'Error while inserting into table: ' + str(err)
        tk.messagebox.showerror(title='Error', message=message)
        return errors


def get_Column_names(table_name: str) -> list:
    global conn
    try:
        list = run_query('SELECT COLUMN_NAME FROM USER_TAB_COLUMNS WHERE TABLE_NAME = \'' + table_name + '\'')
    except oracledb.DatabaseError as err:
        message = 'Error while getting column names: ' + str(err)
        tk.messagebox.showerror(title='Error', message=message)

    return list


def update_table(table_name: str, column_name: str, values: str, condition: str):
    try:
        conn.cursor().execute(
            'UPDATE ' + table_name + ' SET ' + column_name + ' = \'' + values + '\' WHERE \'' + condition + '\'')
    except oracledb.DatabaseError as err:
        print('Error while updating table: ', err)
