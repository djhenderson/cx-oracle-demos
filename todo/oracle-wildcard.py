#!/usr/anim/bin/pypix
import time

def start():
    global time0
    time0 = time.time()

def elapsed():
    global time0
    return time.time() - time0

import cx_Oracle
connurl = ""
conn = cx_Oracle.connect(connurl)
cursor = conn.cursor()
start()
cursor.execute("select count(*) from assetpath where path like '//depot%'")
print elapsed()
conn.close()
