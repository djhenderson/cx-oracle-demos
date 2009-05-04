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
"""

output="""
"""

def demo():
    import cx_Oracle
    import sys
    connstr = sys.argv[1]
    conn = cx_Oracle.connect(connstr)
    curs = conn.cursor()

    #-- simple one-row fetch: good when you know only one row is returned
    #-- returns None when there is no more data
    curs.execute('select 2+2 from dual')
    print curs.fetchone()

    #-- iterating over a cursor
    #-- best way to loop over a results set
    curs.execute('select a,b from t1')
    for row in curs:
        print row

    #-- fetch all rows in one call
    curs.execute('select a,b from t1')
    print curs.fetchall()

    conn.close()

if __name__ == '__main__':
    demo()
