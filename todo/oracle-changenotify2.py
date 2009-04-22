#!/Users/mh/py/bin/python

import cx_Oracle
import time

def callback(message):
    print "Message type:", message.type
    print "Message database name:", message.dbname
    print "Message tables:"
    for table in message.tables:
        print "--> Table Name:", table.name
        print "--> Table Operation:", table.operation
        if table.rows is not None:
            print "--> Table Rows:"
            for row in table.rows:
                print "--> --> Row RowId:", row.rowid
                print "--> --> Row Operation:", row.operation
                print "-" * 60
                if row.operation==2:
                    curs2=connection.cursor()
                    curs2.execute('select * from testexecutemany where rowid=:1',[row.rowid])
                    print 'processing:',curs2.fetchone()
                    curs2.execute('delete from testexecutemany where rowid=:1',[row.rowid])
                    connection.commit()
        print "=" * 60

connection = cx_Oracle.Connection("mh/oracle@templar", events = True)
sub = connection.subscribe(callback = callback, timeout = 1800, rowids = True)
print "Subscription:", sub
print "--> Connection:", sub.connection
print "--> Callback:", sub.callback
print "--> Namespace:", sub.namespace
print "--> Protocol:", sub.protocol
print "--> Timeout:", sub.timeout
print "--> Operations:", sub.operations
print "--> Rowids?:", sub.rowids
print dir(sub)
print dir(sub.operations)


print 'QOS_RELIABLE       =',sub.QOS_RELIABLE
print 'QOS_DEREG_NFY      =',sub.QOS_DEREG_NFY
print 'QOS_ROWIDS         =',sub.QOS_ROWIDS
print 'EVENT_NONE         =',sub.EVENT_NONE
print 'EVENT_STARTUP      =',sub.EVENT_STARTUP
print 'EVENT_SHUTDOWN     =',sub.EVENT_SHUTDOWN
print 'EVENT_SHUTDOWN_ANY =',sub.EVENT_SHUTDOWN_ANY
print 'EVENT_DROP_DB      =',sub.EVENT_DROP_DB
print 'EVENT_DEREG        =',sub.EVENT_DEREG
print 'EVENT_OBJCHANGE    =',sub.EVENT_OBJCHANGE
print 'ALL_OPERATIONS     =',sub.ALL_OPERATIONS
print 'ALL_ROWS           =',sub.ALL_ROWS
print 'INSERTOP           =',sub.INSERTOP
print 'UPDATEOP           =',sub.UPDATEOP
print 'DELETEOP           =',sub.DELETEOP
print 'ALTEROP            =',sub.ALTEROP
print 'DROPOP             =',sub.DROPOP
print 'UNKNOWNOP          =',sub.UNKNOWNOP

sub.registerquery("select * from TestExecuteMany")

while True:
    print "Waiting for notifications...."
    time.sleep(5000)

