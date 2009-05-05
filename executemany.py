#-----------------------------------------------------------------------
# this file is part of the cx-oracle-demo package.
# http://code.google.com/p/cx-oracle-demos
#-----------------------------------------------------------------------

desc="""several flavors of execute"""

setup="""
"""

cleanup="""
"""

notes="""
This allows many operations to be executed without an
an equal number of client/server round trips.
"""

output="""
"""

import sys
import cx_Oracle

def demo(conn,curs):
    # positional parameters receive a list of lists
    curs.executemany("insert into cxdemo_t1(a,b) values(:1,:2)",
                      [[1,'aa'],[2,'bb']])

    # named parameters received a list of dictionaries
    curs.executemany("insert into cxdemo_t1(a,b) values(:x,:y)",
                      [{'x':3,'y':'cc'},
                       {'x':4,'y':'dd'}])

    # procedures need a begin/end wrapper. semicolon necessary after end
    curs.executemany("begin cxdemo.p2(:1,:2); end;",
                      [[5,'ee'],[6,'ff']])

    # cx_Oracle detects zero parms and doesn't make the call,
    # protecting you from a ORA-24333: zero iteration count
    curs.executemany("insert into cxdemo_t1(a,b) values(:1,:2)", [])

if __name__ == '__main__':
    connstr = sys.argv[1]
    conn = cx_Oracle.connect(connstr)
    curs = conn.cursor()
    demo(conn,curs)
    conn.close()
