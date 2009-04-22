#!/usr/anim/bin/pypix

import cx_Oracle

connstr = "templar/oracle@tmpltest"
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()


if 0:
    curs.execute('select * from op_thumb_queue')
    n=0
    for r in curs.fetchall():
        n+=1
        x=r
    print n

if 1:
    n=0
    curs.execute('select * from op_thumb_queue')
    for r in curs:
        print r
        n+=1
        x=r
    print n
