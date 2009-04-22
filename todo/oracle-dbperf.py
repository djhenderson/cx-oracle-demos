#!/usr/anim/bin/pypix

import cx_Oracle
import sys

connurl = "mh/oracle@//templardb01/templar"
conn = cx_Oracle.connect(connurl)
cursor = conn.cursor()
cursor.execute('select 2+2 from dual')
r = cursor.fetchone()
print cursor.description
print r

n=2222
for i in range(1,n):
    for sz in range(0,4000,100):
        query="select * from onenumber where x<=%d"%(sz)
        cursor.execute(query)
        rows=cursor.fetchall()
        nrows=len(rows)
        print i,sz,nrows
        sys.stdout.flush()

conn.close()
