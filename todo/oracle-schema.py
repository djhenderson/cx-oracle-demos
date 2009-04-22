#!/usr/anim/bin/pypix

import cx_Oracle

connurl = "templar/oracle@//templardb01/tmpltest"
conn = cx_Oracle.connect(connurl)
curs = conn.cursor()

def do2(cmd):
    curs.execute(cmd)
    r = curs.fetchall()
    return r

def do_table(table):
    r=do2("select table_name from all_tables where owner='%s'"%(schema))
    for i in r:
        table= i[0]
        do_table(table)

def do_schema(schema):
    r=do2("select table_name from all_tables where owner='%s'"%(schema))
    for i in r:
        table= i[0]
        do_table(table)

do_schema('TEMPLAR')
