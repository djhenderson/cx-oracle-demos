#-----------------------------------------------------------------------
# this file is part of the cx-oracle-demo package.
# http://code.google.com/p/cx-oracle-demos
#-----------------------------------------------------------------------

desc="""calling a stored procedure"""

setup="""
"""

cleanup="""
"""

notes="""
To call a procedure which is part of a package, or a procedure which
is part of another schema, use dotted notation like this:
<ul>
<li>package_name.procedure_name
<li>schema_name.procedure_name
<li>schema_name.package_name.procedure_name
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
    curs.callproc('cxdemo.p0')
    curs.callproc('cxdemo.p2', [55, 66])

if __name__ == '__main__':
    connstr = sys.argv[1]
    conn = cx_Oracle.connect(connstr)
    curs = conn.cursor()
    demo(conn,curs)
    conn.close()
