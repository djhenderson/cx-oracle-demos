#!python

desc="""customizing Connection and Cursor classes"""

setup="""
"""

cleanup="""
"""

notes="""
Derive your own Connection class from the cx_Oracle one.
Derive your own Cursor class from the cx_Oracle one.
Augment cx_Oracle.connect() by making it point to your
own Connection class. From now on every code that uses
cx_Oracle in the standard way will print each query
plus arguments.  If you want to switch back, just do
    cx_Oracle.connect = cx_Oracle.Connection
From: Danny Boxhoorn
"""

output="""
execute: ('select 2+2 from dual',)
execute: ('select :1+:2 from dual', [4, 5])
"""

def demo():
    import sys
    import cx_Oracle
    connstr = sys.argv[1]

    class MyConnection(cx_Oracle.Connection):
        def cursor(self):
            return MyCursor(self)

    class MyCursor(cx_Oracle.Cursor):
        def execute(self, *args):
            print 'execute:',args
            return cx_Oracle.Cursor.execute(self, *args)

    cx_Oracle.connect = MyConnection

    conn = cx_Oracle.connect(connstr)
    curs = conn.cursor()

    curs.execute('select 2+2 from dual')
    curs.execute('select :1+:2 from dual', [4,5])

    # how to make it work for this case?
    # curs.execute('select :x+:y from dual', x=2,y=3)

    conn.close()

if __name__ == '__main__':
    demo()


