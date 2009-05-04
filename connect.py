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

def demo():
    import sys
    import cx_Oracle
    connstr = sys.argv[1]  # e.g., scott/tiger@orcl

    # connect to the database and get a cursor
    conn = cx_Oracle.connect(connstr)
    curs = conn.cursor()
    conn.close()

    # connect to the database as sysdba
    conn = cx_Oracle.connect('sys/secret@mydb', mode=cx_Oracle.SYSDBA)
    conn.close()

if __name__ == '__main__':
    demo()
