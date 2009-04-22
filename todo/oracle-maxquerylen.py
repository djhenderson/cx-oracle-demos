#!/usr/anim/bin/pypix

import cx_Oracle

connstr = ""
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()

s='0'
for i in range(1000000):
    s=s+","+str(i)
    if i%10000==0:
        q= 'select %s from dual'%(s)
        print i,len(q)
        print '--1'
        curs.execute(q)
        print '--2'
        print curs.fetchone()
        print '--3'
