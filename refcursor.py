#-----------------------------------------------------------------------
# this file is part of the cx-oracle-demo package.
# http://code.google.com/p/cx-oracle-demos
#-----------------------------------------------------------------------

desc="""processing a reference cursor"""

setup="""
"""

cleanup="""
"""

notes="""
A reference cursor is Oracle's iterator.  In this example, the
stored procedure refc returns a reference cursor and the python
code iterates over the rows pointed to by the reference cursor.
<pre>
    -- pl/sql function that returns a ref cursor
    function refc return sys_refcursor is
        rc  sys_refcursor;
    begin
        open rc for select a, b from cxdemo_t1;
        return rc;
    end;
</pre>
"""

output="""
"""

import sys
import cx_Oracle

def demo(conn,curs):
    res=curs.callfunc('cxdemo.refc',cx_Oracle.CURSOR)
    for r in res:
        print r

    res2=conn.cursor()
    curs.execute("begin :1 := cxdemo.refc; end;",[res2])
    for r in res2:
        print r

if __name__ == '__main__':
    connstr = sys.argv[1]
    conn = cx_Oracle.connect(connstr)
    curs = conn.cursor()
    demo(conn,curs)
    conn.close()
