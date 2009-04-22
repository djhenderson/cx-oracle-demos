#!/usr/anim/bin/pypix
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
    curs.execute('select table_name,tablespace_name from user_tables')
    for row in curs:
        print row

    #-- fetch all rows in one call
    curs.execute('select table_name,tablespace_name from user_tables')
    print curs.fetchall()

    conn.close()

if __name__ == '__main__':
    demo()
