#!/usr/anim/bin/pypix

import sys
import cx_Oracle

connstr=sys.argv[1]
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()
curs.arraysize=50

curs.execute('select 2+2 "aaa" ,3*3 from dual')
print curs.fetchone()

try:
    #curs.execute('select 1/0 "aaa" ,3*3 from dual')
    curs.execute('select')
except cx_Oracle.Error,e:
    oranum=str(e.message).split(':')[0]
    print 'e=',e
    print 'oranum=',oranum
