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

def demo():
    import sys
    import cx_Oracle
    connstr = sys.argv[1]
    conn = cx_Oracle.connect(connstr)
    curs = conn.cursor()

    # positional parameters receive a list of lists
    curs.executemany("insert into t1(a,b) values(:1,:2)",
                      [[1,'aa'],[2,'bb']])

    # named parameters received a list of dictionaries
    curs.executemany("insert into t1(a,b) values(:x,:y)",
                      [{'x':3,'y':'cc'},
                       {'x':4,'y':'dd'}])

    # procedures need a begin/end wrapper. semicolon necessary after end
    curs.executemany("begin p2(:1,:2); end;",
                      [[5,'ee'],[6,'ff']])

    # cx_Oracle detects zero parms and doesn't make the call,
    # protecting you from a ORA-24333: zero iteration count
    curs.executemany("insert into t1(a,b) values(:1,:2)", [])

    conn.commit()
    conn.close()

if __name__ == '__main__':
    demo()
