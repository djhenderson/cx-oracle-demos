#-----------------------------------------------------------------------
# this file is part of the cx-oracle-demo package.
# http://code.google.com/p/cx-oracle-demos
#-----------------------------------------------------------------------

desc="""Handling an oracle exception"""

setup="""
"""

cleanup="""
"""

notes="""
cx_Oracle will throw cx_Oracle.DatabaseError exceptions.  Here's how
to extract the oracle error code and error message.
"""

output="""
   Exception: ORA-01476: divisor is equal to zero

   ErrorCode: 1476
ErrorMessage: ORA-01476: divisor is equal to zero
"""

import sys
import cx_Oracle

def demo(conn,curs):
    try:
        curs.execute('select 1/0 from dual')
    except cx_Oracle.DatabaseError, e:
        print "Exception:", e
        errorObj, = e.args
        print "   ErrorCode:", errorObj.code
        print "ErrorMessage:", errorObj.message

if __name__ == '__main__':
    connstr = sys.argv[1]
    conn = cx_Oracle.connect(connstr)
    curs = conn.cursor()
    demo(conn,curs)
    conn.close()
