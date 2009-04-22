#!/usr/anim/bin/pypix

import cx_Oracle

# basic oracle:
# - find your connect string
# - connect to the database
# - get a cursor
# - execute a statement in the cursor
# - fetch data from cursor
# - close cursor, connection

connstr = "mh/oracle@tmpltest"
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()
curs.execute('select 2+2 "aaa" ,3*3 from dual')
r = curs.fetchone()
print curs.description
print r
conn.close()

# don't use these, these are special case constructs
#connstr = ""
#connstr = ""
#connstr = ""
#connstr = ""
