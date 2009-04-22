#!/Users/mh/py/bin/python

desc="""client-side change notification"""

setup="""

as sys: grant change notification to public;

create table changeme (
    a varchar2(10),
    b number(3)
);
"""

cleanup="""
drop table changeme;
"""

notes="""
Database Change Notification allows you to register a callback
whenever a specified DML or DDL event takes place, for example
inserting or deleting a row from a table.

<a href=http://download-uk.oracle.com/docs/cd/B19306_01/appdev.102/b14251/adfns_dcn.htm>
http://download-uk.oracle.com/docs/cd/B19306_01/appdev.102/b14251/adfns_dcn.htm</a>

"""

output="""
"""

qos={
    1:'QOS_RELIABLE',
    2:'QOS_DEREG_NFY',
    4:'QOS_ROWIDS',
}

event={
    0:'EVENT_NONE',
    1:'EVENT_STARTUP',
    2:'EVENT_SHUTDOWN',
    3:'EVENT_SHUTDOWN_ANY',
    4:'EVENT_DROP_DB',
    5:'EVENT_DEREG',
    6:'EVENT_OBJCHANGE',
}

ops={
    0:'ALL_OPERATIONS',
    1:'ALL_ROWS',
    2:'INSERTOP',
    4:'UPDATEOP',
    8:'DELETEOP',
    16:'ALTEROP',
    32:'DROPOP',
    64:'UNKNOWNOP',
}

def demo():
    import sys
    import time
    import cx_Oracle
    connstr = sys.argv[1]

    # this function will be called whenever the table CHANGEME is modified
    def callback(message):
        print "Message type:", message.type,event[message.type]
        print "Message database name:", message.dbname
        print "Message tables:"
        for table in message.tables:
            print "--> Table Name:", table.name
            print "--> Table Operation:", table.operation,ops[table.operation]
            if table.rows is not None:
                print "--> Table Rows:"
                for row in table.rows:
                    print "--> --> Row RowId:", row.rowid
                    print "--> --> Row Operation:", row.operation,ops[row.operation]
                    print "-" * 60
            print "=" * 60

    # to enable callbacks: events = True
    conn = cx_Oracle.connect(connstr, events = True)
    sub = conn.subscribe(callback = callback, timeout = 1800, rowids = True)
    print "Subscription:", sub
    print "--> Connection:", sub.connection
    print "--> Callback:", sub.callback
    print "--> Namespace:", sub.namespace
    print "--> Protocol:", sub.protocol
    print "--> Timeout:", sub.timeout
    print "--> Operations:", sub.operations
    print "--> Rowids?:", sub.rowids
    sub.registerquery("select * from changeme")

    while True:
        print "Modify the table CHANGEME to see some callbacks."
        print "Waiting for notifications...."
        time.sleep(5000)

if __name__ == '__main__':
    demo()
