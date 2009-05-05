#-----------------------------------------------------------------------
# this file is part of the cx-oracle-demo package.
# http://code.google.com/p/cx-oracle-demos
#-----------------------------------------------------------------------

desc="""several flavors of connect"""

setup="""
"""

cleanup="""
"""

notes="""
Here are several ways to retrieve the data from a query.  For
lots of data, it's best to use the iterator.  For single-row
results, use fetchone().
"""

output="""
"""

import sys
import cx_Oracle

def demo(conn,curs):
    #-- simple one-row fetch: good when you know only one row is returned
    #-- returns None when there is no more data
    curs.execute('select 2+2 from dual')
    print curs.fetchone()

    #-- iterating over a cursor
    #-- best way to loop over a results set
    curs.execute('select a,b from cxdemo_t1')
    for row in curs:
        print row

    #-- fetch all rows in one call
    curs.execute('select a,b from cxdemo_t1')
    print curs.fetchall()

if __name__ == '__main__':
    connstr = sys.argv[1]
    conn = cx_Oracle.connect(connstr)
    curs = conn.cursor()
    demo(conn,curs)
    conn.close()
