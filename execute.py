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
There are several ways to call curs.execute().  The simplest way
is to pass a simple sql string.  You can also use "bind variables"
to pass in values.  This is almost always better than catting a
bunch of strings together.

In some cases (for example using table names) you can't pass a
table name in as a bind variable.  In order to avoid SQL injection
attacks there's a demo of how to clean that up.

The "dual" table is a pseudo-table that is used to get computed values.
"""

output="""
4                  (simple)
8                  (positional parameter)
10                 (named parameter)
hello world's      (apostrophe)
(6, 9)             (returning value)
6
9
"""

def demo():
    import sys
    import cx_Oracle
    connstr = sys.argv[1]  # e.g., scott/tiger@orcl
    conn = cx_Oracle.connect(connstr)
    curs = conn.cursor()

    # simple execute
    curs.execute('select 2+2 from dual')
    print curs.fetchone()[0]

    # execute with positional parameter :1=first, :2=second, etc
    curs.execute('select :1 * :2 from dual',[2,4])
    print curs.fetchone()[0]

    # execute with named parameter  :
    curs.execute('select :x * :y from dual',x=2,y=5)
    print curs.fetchone()[0]


    # handling troublesome chars such as space and apostrophe - easy!
    curs.execute('select :x from dual', x="hello world's")
    print curs.fetchone()[0]

    # returning value of select
    (a1,a2)=curs.execute('select 2*:x,3*:x from dual',x=3)
    print curs.fetchone()
    print a1.getvalue()
    print a2.getvalue()

    # select into???

    conn.close()

if __name__ == '__main__':
    demo()
