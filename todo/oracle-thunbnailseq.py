#!/usr/anim/bin/pypix

import cx_Oracle

connstr = ""
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()
#curs.execute("select get_thumbnail_seq(5,'queued') from dual")
curs.execute("select * from array(get_thumbnail_seq(5,'queued'))")
r = curs.fetchall()
print curs.description
print r
conn.close()
