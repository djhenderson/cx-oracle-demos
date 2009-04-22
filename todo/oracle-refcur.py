#!/usr/anim/bin/pypix

import cx_Oracle
conn = cx_Oracle.connect("wikiuser/oracle@templar")
curs = conn.cursor()

res=curs.callfunc('junkpkg.f1',cx_Oracle.CURSOR,['world'])
for r in res:
    print r


funcstr="junkpkg.f1('world')"

res2=conn.cursor()
curs.execute("begin :1 := %s; end;" % (funcstr), [res2])
for r in res2:
    print r

conn.close()
