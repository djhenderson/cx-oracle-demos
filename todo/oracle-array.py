#!/usr/anim/bin/pypix

import sys
import cx_Oracle

connstr='mh/oracle@templar'
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()

a=curs.arrayvar(cx_Oracle.STRING, ['a','b','c'])
anum=curs.arrayvar(cx_Oracle.NUMBER, [1,2,3,4,5])
curs.execute('begin ptst.p(:pa); end;', pa=a)
curs.callproc('ptst.p', [a])

rv = curs.var(cx_Oracle.NUMBER)
curs.execute('begin :rv := ptst.f(:a); end;', rv=rv, a=a)
print rv

rv = curs.callfunc('ptst.f',cx_Oracle.NUMBER,[a])
print rv
rv = curs.callfunc('ptst.fnum',cx_Oracle.NUMBER,[anum])
print rv

conn.close()
