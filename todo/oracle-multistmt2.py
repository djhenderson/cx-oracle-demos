#!/usr/anim/bin/pypix

#-----------------------------------------------------------------------
#
# run something like this to generate the keyword class:
#
# /usr/anim/modsquad/cx_autogen.py --conn=mh/oracle@tmpltest -O keyword.py keyword
#
#-----------------------------------------------------------------------

import cx_Oracle

conn = cx_Oracle.connect("apidemo/oracle@templar")
curs=conn.cursor()

def add_V1(parmlist):
    print 'parmlist:',parmlist
    result = curs.executemany("begin KEYWORD.ADD(:1, :2); end;",parmlist)

def add_V2(parmlist):
    result = curs.executemany("begin KEYWORD.ADD(:k, :v); end;",parmlist)

curs.execute("begin KEYWORD.ADD(:1, :2); end;",[11,'aaa'])
curs.executemany("begin KEYWORD.ADD(:1, :2); end;",[[22,'aaa'],[22,'bbb']])

curs.executemany("begin KEYWORD.ADD(:k, :v); end;",
                 [{'k':33,'v':'aaa'},{'k':33,'v':'bbb'}])

add_V1([[44,'aaa'],[44,'bbb']])
add_V2( [{'k':55,'v':'aaa'},{'k':55,'v':'bbb'}])

curs.execute('select * from keywords order by id')
for r in curs: print r
conn.close()
