#!/usr/anim/bin/pypix

import sys
import cx_Oracle
import time


connstr=sys.argv[1]
owner=sys.argv[2].upper()
table=sys.argv[3].upper()

conn = cx_Oracle.connect(connstr,mode=cx_Oracle.SYSDBA)
curs = conn.cursor()
curs.arraysize=50

epoch=time.time()
def elapsed():
    global epoch
    #return time.ctime()
    return '%6.2f'%(time.time()-epoch)

def do1(curs,cmd):
    print '%s %s'%(elapsed(),cmd)
    try:
        curs.execute(cmd)
    except Exception,e:
        print '    ',str(e).strip()

def doindex(curs,owner,index):
    do1(curs,'alter index %s.%s rebuild'%(owner,index))


def dotable(curs,owner,table):
    do1(curs,'alter table %s.%s enable row movement'%(owner,table))
    do1(curs,'alter table %s.%s shrink space compact'%(owner,table))
    do1(curs,'alter table %s.%s disable row movement'%(owner,table))
    curs.execute("""select index_name from dba_indexes
                    where owner=:1 AND TABLE_NAME=:2""",[owner,table])
    rr=curs.fetchall()
    for r in rr:
        doindex(curs,owner,r[0])

def dotables(curs,owner,table):
    curs.execute("""select table_name from all_tables
                    where owner=:1 and table_name like :2""",[owner,table])
    rr=curs.fetchall()
    for r in rr:
        dotable(curs,owner,r[0])

dotables(curs,owner,table)
print elapsed()

conn.close()
sys.exit(0)
