#!/usr/anim/bin/pypix

import cx_Oracle
connstr='mh/oracle@templar'
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()
curs.arraysize=50

curs.execute('select * from faketbl')
print curs.description
for r in curs:
    print r
    print r[1]
    print str(r[1])
    print dir(r[1])

conn.close()
