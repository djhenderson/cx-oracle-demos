#!/usr/anim/bin/pypix

desc="""calling a stored procedure"""

setup="""

create table mytable (x number, y date);
create or replace procedure myproc_noparm
as
begin
    insert into mytable(x, y) values (99,sysdate);
end;
/
create or replace procedure myproc_1parm(ax number)
as
begin
    insert into mytable(x, y) values (ax,sysdate);
end;
"""

cleanup="""
drop table mytable;
drop procedure myproc_noparm;
drop procedure myproc_1parm;
"""

notes="""
To call a procedure which is part of a package, or a procedure which
is part of another schema, use dotted notation like this:

    package_name.procedure_name
    schema_name.procedure_name
    schema_name.package_name.procedure_name

Parameters are passed as a list.  callproc() returns a list
of the parameters passed in.  If any parameters are OUT or
IN OUT, the returned list will have the modified values.

There's nothing special about calling a procedure during a
transaction.  If the procedure modifies a table, you will
need to do a commit.  It's possible that the procedure may
also do a commit (but that is generally a bad practice).
"""

output="""
(99, datetime.datetime(2009, 5, 1, 22, 24, 55))
(55, datetime.datetime(2009, 5, 1, 22, 24, 55))
"""

def demo():
    import sys
    import cx_Oracle
    connstr = sys.argv[1]
    conn = cx_Oracle.connect(connstr)
    curs = conn.cursor()

    curs.callproc('myproc_noparm')
    curs.callproc('myproc_1parm', [55])
    curs.execute('select * from mytable')
    for r in curs:
        print r

    conn.commit()
    conn.close()

if __name__ == '__main__':
    demo()
