#!/usr/anim/bin/pypix

import cx_Oracle

try:
    conn.close()
except NameError:
    pass

connurl = ""
conn = cx_Oracle.connect(connurl)
cursor = conn.cursor()
cursor.execute('select 2+2 from dual')
r = cursor.fetchone()
print cursor.description
print r
conn.close()
