#!/usr/anim/bin/pypix

import cx_Oracle

#-----------------------------------------------------------------------
# Derive your own Connection class from the cx_Oracle one.
# Derive your own Cursor class from the cx_Oracle one.
# Augment cx_Oracle.connect() by making it point to your
# own Connection class. From now on every code that uses
# cx_Oracle in the standard way will print each query
# plus arguments.  If you want to switch back, just do
#     cx_Oracle.connect = cx_Oracle.Connection
# From: Danny Boxhoorn, danny@astro.rug.nl
#-----------------------------------------------------------------------

class MyConnection(cx_Oracle.Connection):
    def cursor(self):
        return MyCursor(self)

class MyCursor(cx_Oracle.Cursor):
    def execute(self, *args):
        print 'execute:',args
        return cx_Oracle.Cursor.execute(self, *args)

cx_Oracle.connect = MyConnection

conn = cx_Oracle.connect(foo)
cursor = conn.cursor()
cursor.execute('select 2+2 from '
               ' dual')
print 'result=',cursor.fetchone()
cursor.execute('select zzsysdate from '
               ' dual where 5<>:something', {'something': 5})
print 'result=',cursor.fetchone()
cursor.close()
conn.close()
