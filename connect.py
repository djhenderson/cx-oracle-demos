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
connect() returns a connection, cursor() returns a cursor.  These are the
two basic objects you will use.  SYSDBA is needed for system accounts.
"""

output="""
"""

import sys
import cx_Oracle

def demo(conn,curs):
    # normal user connect -- connstr looks like scott/tiger@orcl
    conn = cx_Oracle.connect(connstr)

    # normal user connect, three parms
    conn = cx_Oracle.connect('scott', 'tiger', 'orcl')

    # connect to the database as sysdba
    conn = cx_Oracle.connect('sys/secret@mydb', mode=cx_Oracle.SYSDBA)

if __name__ == '__main__':
    connstr = sys.argv[1]
    conn = cx_Oracle.connect(connstr)
    curs = conn.cursor()
    demo(conn,curs)
    conn.close()
