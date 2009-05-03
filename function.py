#!/usr/anim/bin/pypix

desc="""calling a function"""

setup="""
create or replace function current_time return date
as
begin
    declare
        x date;
    begin
        select sysdate into x from dual;
        return x;
    end;
end;

create or replace function add_three(x number, y number, z number))
as
begin
    return x + y + z;
end;
"""

cleanup="""
drop function current_time;
drop function add_three;
"""

notes="""
To call a function which is part of a package, or a function which
is part of another schema, use dotted notation like this:

    package_name.function_name
    schema_name.function_name
    schema_name.package_name.function_name

Parameters are passed as a list.  callproc() returns a list
of the parameters passed in.  If any parameters are OUT or
IN OUT, the returned list will have the modified values.

There's nothing special about calling a procedure during a
transaction.  If the procedure modifies a table, you will
need to do a commit.  It's possible that the procedure may
also do a commit (but that is generally a bad practice).
"""

output="""
2009-05-01 22:30:33
6.0
"""

def demo():
    import sys
    import cx_Oracle
    connstr = sys.argv[1]
    conn = cx_Oracle.connect(connstr)
    curs = conn.cursor()

    now = curs.callfunc('current_time', cx_Oracle.DATETIME)
    print now
    sum = curs.callfunc('add_three', cx_Oracle.NUMBER, [1,2,3])
    print sum

    conn.commit()
    conn.close()

if __name__ == '__main__':
    demo()
