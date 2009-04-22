#!/usr/anim/bin/pypix

import os
os.system('hostname |mail -s runfrom mh')

import sys
from vlog import V
import cx_Oracle

connstr = sys.argv[1]
conn = cx_Oracle.connect(connstr)
curs = conn.cursor()
c2 = conn.cursor()
owner=conn.username.upper()
V('owner:',owner)
curs.execute("""
    select table_name
        from all_tables
        where owner=:owner
        order by table_name
""",owner=owner)
for r in curs:
    table=r[0]
    V('processing:',table)
    c2.execute('analyze table "%s" VALIDATE structure'%(table))
    c2.callproc('DBMS_STATS.GATHER_TABLE_STATS',[owner,table])

zz="""
begin
            DBMS_STATS.GATHER_TABLE_STATS (
              ownname => 'TEMPLAR',
          tabname => 'OP_DFTHUMBQ',
          estimate_percent => 100
          );
          end; 
"""
