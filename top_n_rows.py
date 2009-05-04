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

Note that ROWNUM starts at 1 and not 0.
"""

output="""
"""

def demo():
    import sys
    import cx_Oracle
    connstr = sys.argv[1]
    conn = cx_Oracle.connect(connstr)
    curs = conn.cursor()

    # the first 5 rows of the subquery
    curs.execute("""select * from (
                      select a,b from t1 order by a
                    ) where rownum <= 5""")
    for r in curs:
        print r[0]

    conn.close()

if __name__ == '__main__':
    demo()
