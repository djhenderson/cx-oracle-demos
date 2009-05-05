#-----------------------------------------------------------------------
# this file is part of the cx-oracle-demo package.
# http://code.google.com/p/cx-oracle-demos
#-----------------------------------------------------------------------

desc="""Connection instance variables"""

setup="""
"""

cleanup="""
"""

notes="""
These are the instance variables associated with a connection.
<p>
R/O
<ul>
<li>dsn		TNS entry of the current connection.
<li>encoding	IANA character set name of the current connection.
<li>maxBytesPerCharacter	maximum number of bytes per character.
<li>nencoding	the IANA character set name of the current connection.
<li>tnsentry	TNS entry of the current connection. ??how does it differ??
<li>username	connection's username
<li>version		version of oracle you are connected to.
</ul>
<p>
R/W
<ul>
<li>current_schema	sets the current schema for the session.
<li>password	password of the current connection
<li>stmtcachesize	size of the statement cache
</ul>
<p>
W/O
<ul>
<li>action		sets [g]v$session.action
<li>clientinfo	sets [g]v$session.client_info
<li>module		sets [g]v$session.module
</ul>
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

import sys
import cx_Oracle

def demo(conn,curs):
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

if __name__ == '__main__':
    connstr = sys.argv[1]
    conn = cx_Oracle.connect(connstr)
    curs = conn.cursor()
    demo(conn,curs)
    conn.close()
