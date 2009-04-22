#!/usr/anim/bin/pypix

import sys
import time
import cx_Oracle

def killstring(curs):
    """return a string that will kill this db connection"""
    curs.execute("""SELECT dbms_debug_jdwp.current_session_id,
                           dbms_debug_jdwp.current_session_serial,
                           sys_context('USERENV', 'INSTANCE_NAME')
                    FROM dual""")
    (sid,serial,instance)=curs.fetchone()
    s="echo \"alter system kill session '%s,%s';\"|sqlplus -SL sys/foo@%s"%\
            (sid,serial,instance)
    s="oracle-killsession %s %s %s"%(sid,serial,instance)
    return s

connstr=sys.argv[1]
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()
curs.arraysize=50

while True:
    s=killstring(curs)
    print s
    time.sleep(1)

conn.close()
