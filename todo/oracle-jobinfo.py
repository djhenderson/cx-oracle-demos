#!/usr/anim/bin/pypix
"""
show job info
http://www.oradev.com/dbms_scheduler.jsp
"""

import sys
import optparse
import getpass
import re

import cx_Oracle
import vlog
from vlog import V,D
from pgprint import pgprint

def main():
    """main program"""

    #-------------------------------------------------------------------
    # parse standard options: --conn, --pass, --sys
    #-------------------------------------------------------------------
    p = optparse.OptionParser(usage="usage: %prog options pkg...")
    p.add_option("","--conn",action="store",type="string",dest="conn",
                 help="Database connection string")
    p.add_option("","--pass",action="store",type="string",dest="password",
                 help="Database password")
    p.add_option("","--sys",action="store_true",dest="sys",default=False,
                 help="connect as sysdba")
    p.add_option("","--owner",
                 help="show jobs for this owner")
    (opts,args) = p.parse_args()

    #-------------------------------------------------------------------
    # make sure there is a connection
    #-------------------------------------------------------------------
    if not (opts.conn):
        p.print_help()
        sys.exit(1)

    #-------------------------------------------------------------------
    # process the connection/password as necessary
    # TODO: incorporate os.environ["ORA_USERID"]
    #-------------------------------------------------------------------
    oraconnre = re.compile("^([^/@]*)(/([^@]*))?(@(.*))?$")
    user,password,host=oraconnre.match(opts.conn).groups()[0::2]
    if opts.password:
        password=opts.password
    if not password:
        password=getpass.getpass()
    connstr="%s/%s"%(user,password)
    if host:
        connstr+="@%s" % host

    #-------------------------------------------------------------------
    # handle connection as sysdba
    #-------------------------------------------------------------------
    if opts.sys:
        conn=cx_Oracle.connect(connstr,mode=cx_Oracle.SYSDBA)
    else:
        conn=cx_Oracle.connect(connstr)

    curs = conn.cursor()
    curs.arraysize=50

    dojobs(curs,opts.owner)

def dojobs(curs,owner):

    owner=owner.upper()
    print
    print "jobs for owner: %s"%(owner)
    print
    curs.execute("""select owner,job_name,repeat_interval, enabled,comments
                      from dba_scheduler_jobs
                     where owner=:1""",[owner])
    pgprint(curs.description,curs.fetchall(),False)

    print
    print "failed jobs for owner: %s"%(owner)
    print
    curs.execute("""select job_name, actual_start_date, status,error#
                      from dba_scheduler_job_run_details
                     where status <> 'SUCCEEDED' and
                           job_name in
                            (select job_name
                               from dba_scheduler_jobs
                              where owner=:1)
                    order by job_name,actual_start_date""",[owner])
    pgprint(curs.description,curs.fetchall(),False)

    return

    print
    print "jobs for owner: %s"%(owner)
    print
    curs.execute("""select job_name, actual_start_date, status,error#
                      from dba_scheduler_job_run_details
                     where job_name in
                            (select job_name
                               from dba_scheduler_jobs
                              where owner=:1)
                    order by job_name,actual_start_date""",[owner])
    pgprint(curs.description,curs.fetchall(),False)

    return

    #-------------------------------------------------------------------
    # clean up
    #-------------------------------------------------------------------
    curs.close()
    conn.close()

if __name__=='__main__':
    main()

