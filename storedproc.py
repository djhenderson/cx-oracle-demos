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
"""

def demo():
    import sys
    import cx_Oracle
    connstr = sys.argv[1]
    conn = cx_Oracle.connect(connstr)
    curs = conn.cursor()

    curs.callproc('p0')
    curs.callproc('p2', [55, 66])

    conn.commit()
    conn.close()

if __name__ == '__main__':
    demo()
