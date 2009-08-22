#-----------------------------------------------------------------------
# this file is part of the cx-oracle-demo package.
# http://code.google.com/p/cx-oracle-demos
#-----------------------------------------------------------------------

desc="""Transaction Level Read Consistency"""

setup="""
create table isolation_demo(x number);
"""

cleanup="""
drop table isolation_demo;
"""

notes="""
This shows how to set the isolation level to lock your transaction
to a single point in time, isolating you from other people's updates.<p>

When running this demo, add one extra parameter "reader" or "writer".<p>
Run this demo in several windows.  In the first, run as "writer".  Then
in several other windows, run as "reader".<p>

"Oracle also offers the option of enforcing transaction-level read
consistency. When a transaction runs in serializable mode, all data
accesses reflect the state of the database as of the time the transaction
began. This means that the data seen by all queries within the same
transaction is consistent with respect to a single point in time, except
that queries made by a serializable transaction do see changes made
by the transaction itself. Transaction-level read consistency produces
repeatable reads and does not expose a query to phantoms."<p>

<a href=http://download.oracle.com/docs/cd/B19306_01/server.102/b14220/consist.htm>
http://download.oracle.com/docs/cd/B19306_01/server.102/b14220/consist.htm
</a>
"""

output="""
The writer window will count from 1,2,3....

Each reader window will show the value consistent from the beginning
of the transaction.
"""

import sys
import cx_Oracle

def demo(conn,curs):
    import time

    if role == 'writer':
        # this code loops and sets the value to 1,2,3,...

        curs.execute("delete from isolation_demo");
        curs.execute("insert into isolation_demo(x) values(0)");
        while True:
            curs.execute('select x from isolation_demo')
            print time.asctime(),curs.fetchall()
            curs.execute('update isolation_demo set x=x+1')
            conn.commit()
            time.sleep(1)
    else:
        # this code loops and prints the current value in the table.
        # because it has set the isolation level, all queries are
        # "locked" in time and will not be affected by other processes
        # modifying the database.

        # read only mode is similar to serializable mode, but all
        # data modifications are disallowed and will throw errors.
        curs.execute('set transaction read only')
        #curs.execute('set transaction isolation level serializable')

        while True:
            curs.execute('select x from isolation_demo')
            print time.asctime(),curs.fetchall()
            time.sleep(1)

if __name__ == '__main__':
    connstr = sys.argv[1]
    role = sys.argv[2]
    conn = cx_Oracle.connect(connstr)
    curs = conn.cursor()
    demo(conn,curs)
    conn.close()
