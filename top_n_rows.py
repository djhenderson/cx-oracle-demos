#-----------------------------------------------------------------------
# this file is part of the cx-oracle-demo package.
# http://code.google.com/p/cx-oracle-demos
#-----------------------------------------------------------------------

desc="""top N rows of query"""

setup="""
"""

cleanup="""
"""

notes="""
This select the first N rows of a query.  If you are looking
for the SELECT...LIMIT clause this is it.
<p>
Note that ROWNUM starts at 1 and not 0.
"""

output="""
"""

import sys
import cx_Oracle

def demo(conn,curs):
    # the first 5 rows of the subquery
    curs.execute("""select * from (
                      select a,b from cxdemo_t1 order by a
                    ) where rownum <= 5""")
    for r in curs:
        print r[0]

if __name__ == '__main__':
    connstr = sys.argv[1]
    conn = cx_Oracle.connect(connstr)
    curs = conn.cursor()
    demo(conn,curs)
    conn.close()
