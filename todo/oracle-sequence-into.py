#!/usr/anim/bin/pypix

import sys
import cx_Oracle

connstr='mh/oracle@templar1'
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()

myseq=curs.var(cx_Oracle.NUMBER)
curs.prepare("insert into seqtest2(x) values('bbb') returning seq into :x")
print curs.bindnames()
curs.execute(None, x=myseq)
print int(myseq.getvalue())

myseq=curs.var(cx_Oracle.NUMBER)
curs.execute("insert into seqtest2(x) values('bbb') returning seq into :x", x=myseq)
print int(myseq.getvalue())

conn.close()
