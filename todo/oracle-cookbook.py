#!/usr/anim/bin/pypix
"""
oracle cookbook.

to prep:

drop table cookbook_a;
create table cookbook_a(x varchar2(10), y number);
"""

import cx_Oracle

#-----------------------------------------------------------------------
# connecting
#-----------------------------------------------------------------------

connstr='scott/tiger@myorcl'
connstr='mh/oracle@tmpltest'
conn = cx_Oracle.connect(connstr)
#conn = cx_Oracle.connect('scott','tiger','myorcl')
#conn = cx_Oracle.connect('sys/topsecret@myorcl',cx_Oracle.SYSDBA)

#-----------------------------------------------------------------------
# getting a cursor.  always set your arraysize for best performance
#-----------------------------------------------------------------------
curs = conn.cursor()
curs.arraysize=50

#-----------------------------------------------------------------------
#
# simplest select
#
# description describes the data being returned
# the first fetchone will return the row.
# the second fetchone will return None, indicating end of data
#
#-----------------------------------------------------------------------

curs.execute('select 2+2 "aaa" ,3*3 from dual')
print curs.description
r=curs.fetchone()
print r
r=curs.fetchone()
print r

#
#-----------------------------------------------------------------------
# inserting data
# there are several ways to pass parameters to your command.
#
#-----------------------------------------------------------------------

myname='charlie'
mynum=3
a=curs.execute('delete from cookbook_a')
a=curs.execute('insert into cookbook_a(x,y) values(:1,:2)',['adam',1])
curs.execute('insert into cookbook_a(x,y) values(:nm,:age)',nm='bob',age=2)
curs.execute('insert into cookbook_a(x,y) values(:x,:y)',x=myname,y=mynum)
conn.commit()

#
#-----------------------------------------------------------------------
# inserting data, DO NOT DO THIS, YOU WILL FAIL ON STRINGS WITH
# EMBEDDED QUOTES.   also see: http://xkcd.com/327/
#-----------------------------------------------------------------------

myname='david'
mynum=4
curs.execute("insert into cookbook_a(x,y) values('%s',%s)"%(myname,mynum))

myname="o'conner"
mynum=4
# syntax error: insert into cookbook_a(x,y) values('o'conner',4)
#curs.execute("insert into cookbook_a(x,y) values('%s',%s)"%(myname,mynum))

conn.commit()


#
#
#-----------------------------------------------------------------------
# execute many
#
#-----------------------------------------------------------------------
#

#-----------------------------------------------------------------------
# calling stored procedures
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
# calling functions
#-----------------------------------------------------------------------



conn.close()
