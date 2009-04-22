#!/usr/anim/bin/pypix

import cx_Oracle

connstr = ""
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()
curs.execute('select 2+2 "aaa" ,3*3 from dual')

curs.execute("select sysdate from dual")
print curs.fetchone()

curs.execute("ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY MM DD'")
curs.execute("select sysdate from dual")
curs.execute("select to_char(sysdate) from dual")
print curs.fetchone()

curs.execute("ALTER SESSION SET NLS_DATE_FORMAT = 'HH24:MI:SS'")
curs.execute("select sysdate from dual")
curs.execute("select to_char(sysdate) from dual")
print curs.fetchone()

conn.close()
