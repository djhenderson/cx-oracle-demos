#!/usr/anim/bin/pypix

desc="""Connection instance variables"""

setup="""
"""

cleanup="""
"""

notes="""
These are the instance variables associated with a connection.

R/O
dsn		TNS entry of the current connection.
encoding	IANA character set name of the current connection.
maxBytesPerCharacter	maximum number of bytes per character.
nencoding	the IANA character set name of the current connection.
tnsentry	TNS entry of the current connection. ??how does it differ??
username	connection's username
version		version of oracle you are connected to.

R/W
current_schema	sets the current schema for the session.
password	password of the current connection
stmtcachesize	size of the statement cache

W/O
action		sets [g]v$session.action
clientinfo	sets [g]v$session.client_info
module		sets [g]v$session.module
"""

output="""
Read-Only:
                 dsn = templar
            encoding = US-ASCII
maxBytesPerCharacter = 1
           nencoding = US-ASCII
            tnsentry = templar
            username = mh
             version = 10.2.0.4.0
Read/Write:
current_schema = 
      password = oracle
 stmtcachesize = 50
Write-Only:
"""

def demo():
    import sys
    import cx_Oracle
    connstr = sys.argv[1]
    conn = cx_Oracle.connect(connstr)

    print "Read-Only:"
    print "                 dsn =", conn.dsn
    print "            encoding =", conn.encoding
    print "maxBytesPerCharacter =", conn.maxBytesPerCharacter
    print "           nencoding =", conn.nencoding
    print "            tnsentry =", conn.tnsentry
    print "            username =", conn.username
    print "             version =", conn.version

    print "Read/Write:"
    #conn.current_schema='another_schema'
    conn.stmtcachesize=50
    print "current_schema =", conn.current_schema
    print "      password =", conn.password
    print " stmtcachesize =", conn.stmtcachesize

    print "Write-Only:"
    conn.action = "demoing write/only vars"
    conn.clientinfo = "awesome oracle-demos/conn_vars.py"
    conn.module = "mymodule"
    conn.commit() # to be visible to other processes

    conn.close()


if __name__ == '__main__':
    demo()
