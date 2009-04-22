#!/usr/anim/bin/pypix
import cx_Oracle
import sys
import types

# [('TYPEID', <type 'cx_Oracle.NUMBER'>, 21, 22, 20, 0, 0),
#  ('NAME', <type 'cx_Oracle.STRING'>, 255, 255, 0, 0, 0)]
# [(4, 'folder'), (1, 'pathedasset'), (2, 'menvasset'), (3, 'unitasset')]

def pgprint(desc,rows):

    # set initial max length of each column to be len of the column header
    maxlen=[]
    for i in desc:
        maxlen.append(len(i[0]))
    ncols=len(maxlen)
    print ncols
    print len(desc)

    for r in rows:
        i=0
        while i < ncols:
            tmps=str(r[i])
            tmpl=len(tmps)
            if maxlen[i]<tmpl:
                maxlen[i]=tmpl
            i+=1

    # header
    i=0
    while i < len(desc):
        s=desc[i][0]
        s2=s.center(maxlen[i]).lower()
        if (i>0):
            s2=' | '+s2
        sys.stdout.write(s2)
        i += 1
    sys.stdout.write('\n')

    # underline
    i=0
    while i < len(desc):
        s2='-'*maxlen[i]
        if (i>0):
            s2='-+-'+s2
        sys.stdout.write(s2)
        i += 1
    sys.stdout.write('\n')

    # rows
    for r in rows:
        i=0
        while i < ncols:
            s=str(r[i])
            t=type(r[i])
            if t==types.IntType or t==types.FloatType:
                s2=s.rjust(maxlen[i])
            else:
                s2=s.ljust(maxlen[i])
            if (i>0):
                s2=' | '+s2
            sys.stdout.write(s2)
            i += 1
        sys.stdout.write('\n')

conn = cx_Oracle.connect("templar/oracle@tmpltest")
curs = conn.cursor()

#curs.execute("select sid,username,serial#,audsid,schemaname,to_char(logon_time,'DD-MON-YY HH24:MI:SS'),osuser,process,machine,terminal,program,event,service_name from v$session")

curs.execute('select * from p4_files where rownum<5')
pgprint(curs.description,curs.fetchall())
curs.execute('select * from types')
pgprint(curs.description,curs.fetchall())
