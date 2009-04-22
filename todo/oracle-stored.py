#!/usr/anim/bin/pypix

import cx_Oracle

conn = cx_Oracle.connect("")
curs = conn.cursor()
curs.execute('select nextid() from dual')
r = curs.fetchone()
print r
conn.close()

conn = cx_Oracle.connect("")
curs = conn.cursor()
curs.execute('select templar.nextid() from dual')
r = curs.fetchone()
print r
conn.close()
