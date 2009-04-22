#!/usr/anim/bin/pypix

import sys
import cx_Oracle
from pgprint import pgprint

connstr='mh/oracle@templar'
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()
curs.arraysize=50

curs.execute('select * from clobtest')
print curs.description
r=curs.fetchone()
print r
print str(r[1])
pgprint(curs.description,curs.fetchall(),False)

conn.close()
