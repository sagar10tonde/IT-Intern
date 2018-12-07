# -*- coding: utf-8 -*-

import psycopg2
import sys
import json

con = None
dict_data = {}
tuple_data = ()
file_name = "pune.json"

def read_json():
    global dict_data
    global tuple_data
    json_file = open(file_name)
    json_str = json_file.read()
    dict_data = json.loads(json_str)
    tuple_data = tuple(dict_data.items())

def db_connect():
    global con
    con = psycopg2.connect("dbname='sagar' user='sagar'")


def create_tables():
    global con
    table_name = file_name.split('.')[0]

    cur = con.cursor()
    cur.execute("CREATE TABLE {}({} {})".format(table_name,tuple_data[0][0], 'VARCHAR(20)'))
    con.commit()

    for data in tuple_data[1:]:
        cur.execute("ALTER TABLE {} ADD {} {}".format(table_name,data[0], 'VARCHAR(20)'))
        con.commit()

def insert_values():
    global con
    table_name = file_name.split('.')[0]
    cur = con.cursor()

    for data in tuple_data:
        cur.execute("INSERT INTO {} ({}) VALUES ({}))".format(table_name,data[0],data[1]))
        con.commit()

    '''
    try:
        #con = psycopg2.connect("dbname='sagar' user='sagar'")

        cur = con.cursor()

        cur.execute("CREATE TABLE aaa(Id INTEGER PRIMARY KEY, Name VARCHAR(20), Price INT)" )
    
        cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
        cur.execute("INSERT INTO Cars VALUES(2,'Mercedes',57127)")
        cur.execute("INSERT INTO Cars VALUES(3,'Skoda',9000)")
        cur.execute("INSERT INTO Cars VALUES(4,'Volvo',29000)")
        cur.execute("INSERT INTO Cars VALUES(5,'Bentley',350000)")
        cur.execute("INSERT INTO Cars VALUES(6,'Citroen',21000)")
        cur.execute("INSERT INTO Cars VALUES(7,'Hummer',41400)")
        cur.execute("INSERT INTO Cars VALUES(8,'Volkswagen',21600)")
        
        con.commit()


    except psycopg2.DatabaseError:
        if con:
            con.rollback()

        print('Error %s')
        sys.exit(1)


    finally:
        if con:
            con.close()
    '''

if __name__ == '__main__':
    read_json()
    db_connect()
    create_tables()
    insert_values()