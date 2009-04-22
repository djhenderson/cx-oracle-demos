#!/usr/anim/bin/pypix

import cx_Oracle

conn = cx_Oracle.connect("mh/oracle@tmpltest")
curs = conn.cursor()

# simple execute
curs.execute('select 2+2 from dual')
print curs.fetchall()

# execute with parameter
curs.execute('select 2*:x from dual',x=3)
print curs.fetchall()

# handling space and apostrophe
curs.execute('select :zzz from dual',zzz="hello world's")
print curs.fetchall()

# execute with into parameter
(a1,a2)=curs.execute('select 2*:x,3*:x into :answer from dual',x=3)
curs.fetchone()
print a1.getvalue()
print a2.getvalue()

# execute with into parameter
(a1,a2)=curs.execute('select 2*:x,3*:x into :answer from dual',x=3)
x=curs.fetchall()
print x

curs.close()
conn.close()
