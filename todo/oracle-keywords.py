#!/usr/anim/bin/pypix

import sys
sys.path.insert(0,'/u0/mh/cx_Oracle/src/cx_Oracle-4.3.2/build/lib.linux-x86_64-2.4')

import cx_Oracle
conn = cx_Oracle.connect("mh/oracle@tmpltest")
curs = conn.cursor()

curs.callproc('keyword.del',[23,'green'])
curs.callproc('keyword.add',[23,'green'])
curs.callproc('keyword.add',[23,'bright'])

res=conn.cursor()

print 'asset 23 keywords:'
curs.callproc('keyword.get_keywords',[res, 23])
print res.description
for r in res:
    print r

print 'blue things:'
curs.callproc('keyword.get_ids',[res, 'blue'])
print res.description
for r in res:
    print r

### needs cx_Oracle-4.3.2
print 'asset 17 keywords:'
res=curs.callfunc('keyword.get_keywords2',cx_Oracle.CURSOR,[17])
print res.description
for r in res:
    print r

### needs cx_Oracle-4.3.2
print 'all keywords:'
res=curs.callfunc('keyword.all_words',cx_Oracle.CURSOR)
print res.description
for r in res:
    print r

# conn.commit()
conn.close()
