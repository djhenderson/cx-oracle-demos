#!/usr/anim/bin/pypix

import cx_Oracle

conn = cx_Oracle.connect('mh/oracle@tmpltest2')
conn.commit()
curs = conn.cursor()


curs.execute("alter session set timed_statistics=true")
curs.execute("alter session set max_dump_file_size=unlimited")
curs.execute("alter session set tracefile_identifier='mhtestxyzzy'")
curs.execute("alter session set events '10046 trace name context forever, level 12'")

#cx_Oracle.DatabaseError: ORA-06550: line 1, column 7:
#PLS-00201: identifier 'DBMS_MONITOR' must be declared
#
#curs.callproc('dbms_monitor.session_trace_enable')


curs.execute("delete from x1")

curs.execute("insert into x1(a,b) values (1,'aa')")

s="""begin
insert into x1(a,b) values (2,'bb');
insert into x1(a,b) values (3,'cc');
end;"""
print s
curs.execute(s)

curs.callproc("set_x1", (4, 'dd'))
curs.callproc("set_x1", (5, 'ee'))

s="""begin
set_x1(6,'ff');
set_x1(7,'gg');
end;"""
print s
curs.execute(s)

curs.prepare("call set_x1(:a,:b)")

curs.executemany("call set_x1(:a,:b)",
    [{'a':8,'b':'hh'},
     {'a':9,'b':'ii'}]
)

curs.executemany("call set_x1(:1,:2)", [[10,'jj'],[11,'kk']])

#cx_Oracle.DatabaseError: ORA-24333: zero iteration count
#curs.executemany("call set_x1(:a,:b)",[])

conn.commit()

curs.execute("select * from x1")
for r in curs.fetchall():
    print r

conn.close()
