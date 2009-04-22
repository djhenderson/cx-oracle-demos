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
Database Change Notification is a feature that enables client
applications to register queries with the database and receive
notifications in response to DML or DDL changes on the objects
associated with the queries. The notifications are published by the
database when the DML or DDL transaction commits.

During registration, the application specifies a notification handler
and associates a set of interesting queries with the notification
handler. A notification handler is a python function.

<a href=http://download-uk.oracle.com/docs/cd/B19306_01/appdev.102/b14251/adfns_dcn.htm>
http://download-uk.oracle.com/docs/cd/B19306_01/appdev.102/b14251/adfns_dcn.htm</a>

"""

output="""
"""

def demo():
    import sys
    import time
    import cx_Oracle
    connstr = sys.argv[1]

    # this function will be called whenever the table CHANGEME is modified
    def callback(message):
        print " type:", message.type
        print "dbname:", message.dbname
        for table in message.tables:
            print "  table:", table.name
            print "     op:", table.operation
            if table.rows is not None:
                for row in table.rows:
                    print "        rowid:", row.rowid, "op:", row.operation
            print ""

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
