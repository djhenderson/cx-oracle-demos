#!/usr/anim/bin/pypix

"""
usage: oracle-table-dump connstr tables...

dumps table data to sql INSERT statements.
"""

import sys
import cx_Oracle

def enquote(data,type):
    """
    convert an oracle datum to its SQL representation.
    """
    if type.find('CHAR')==-1:
        if data is None:
            rv='NULL'
        else:
            rv=str(data)
    else:
        if data is None:
            rv="''"
        else:
            rv="'"+data.replace("'","''")+"'"
    return rv

def dump(conn,tbl):
    """dump one table"""

    tbl=tbl.upper()
    curs=conn.cursor()
    curs.execute(""" 
        SELECT
        column_name,
        data_type
        FROM user_tab_columns
        WHERE table_name=:tbl""",tbl=tbl)
    info=curs.fetchall()

    cols=[]
    type=[]
    for c in info:
        cols.append(c[0])
        type.append(c[1])

    cols=','.join(cols)
    print '--'
    print '--   TABLE:', tbl
    print '-- COLUMNS:', cols
    print '--'

    q='select %s from %s'%(cols,tbl)
    curs.execute(q)
    for r in curs:
        tmpdata=[]
        i=0
        for c in r:
            tmpdata.append(enquote(c,type[i]))
            i=i+1
        data=','.join(tmpdata)
        cmd='insert into %s (%s) values (%s);'%(tbl,cols,data)
        print cmd


connstr = sys.argv[1]
conn = cx_Oracle.connect(connstr)

for table in sys.argv[2:]:
    dump(conn,table)

conn.close()
