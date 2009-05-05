#-----------------------------------------------------------------------
# this file is part of the cx-oracle-demo package.
# http://code.google.com/p/cx-oracle-demos
#-----------------------------------------------------------------------

desc="""calling a function"""

setup="""
"""

cleanup="""
"""

notes="""
To call a function which is part of a package, or a function which
is part of another schema, use dotted notation like this:
<ul>
<li>package_name.function_name
<li>schema_name.function_name
<li>schema_name.package_name.function_name
</ul>
<p>
Parameters are passed as a list.  callproc() returns a list
of the parameters passed in.  If any parameters are OUT or
IN OUT, the returned list will have the modified values.
<p>
There's nothing special about calling a procedure during a
transaction.  If the procedure modifies a table, you will
need to do a commit.  It's possible that the procedure may
also do a commit (but that is generally a bad practice).
"""

output="""
"""

import sys
import cx_Oracle

def demo(conn,curs):
    x = curs.callfunc('cxdemo.f0', cx_Oracle.NUMBER)
    print x
    x = curs.callfunc('cxdemo.f2', cx_Oracle.NUMBER, [1,2])
    print x

    r = curs.var(cx_Oracle.NUMBER)
    curs.execute('begin :rv := cxdemo.f2(:x,:y); end;', rv=r, x=3, y=4)
    print r

if __name__ == '__main__':
    connstr = sys.argv[1]
    conn = cx_Oracle.connect(connstr)
    curs = conn.cursor()
    demo(conn,curs)
    conn.close()
