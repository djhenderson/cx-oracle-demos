#!/usr/anim/bin/pypix

import sys
import cx_Oracle
from pgprint import pgprint
import vlog
from vlog import V,D

connstr='hitech/hitech@templar'
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()
curs.arraysize=50

curs.execute("select login,pic1,pic2 from people where login='mh'")
login,p1,p2=curs.fetchone()
print curs.description
print login
print type(p1),dir(p1)
f=p1.open()
print dir(f)

d=f.read()
print len(d)

conn.close()
