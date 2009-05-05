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
<p>
In some cases (for example using table names) you can't pass a
table name in as a bind variable.  In order to avoid SQL injection
attacks there's a demo of how to clean that up.
<p>
curs.description describes the data being returned.
<p>
The "dual" table is a pseudo-table that is used to get computed values.
"""

output="""
[('2+2', <type 'cx_Oracle.NUMBER'>, 127, 2, 0, 0, 1)]
4                  (simple)
8                  (positional parameter)
10                 (named parameter)
hello world's      (apostrophe)
(6, 9)             (returning value)
6
9
"""

import sys
import cx_Oracle

def demo(conn,curs):
    # simple execute
    curs.execute('select 2+2 from dual')
    print curs.description
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

    # select into???

if __name__ == '__main__':
    connstr = sys.argv[1]
    conn = cx_Oracle.connect(connstr)
    curs = conn.cursor()
    demo(conn,curs)
    conn.close()
