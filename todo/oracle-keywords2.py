#!/usr/anim/bin/pypix

import sys
sys.path.insert(0,'/u0/mh/cx_Oracle/src/cx_Oracle-4.3.2/build/lib.linux-x86_64-2.4')
import cx_Oracle

class Keywords:
    """manage keywords"""
    def __init__(self,curs):
        self.curs=curs

    def add(self,id,kword):
        """add a keyword to an asset"""
        self.curs.callproc('keyword.add',[id,kword])

    def delete(self,id,kword):
        """delete a keyword from an asset"""
        self.curs.callproc('keyword.del',[id,kword])

    def all_words(self):
        """list of all keywords"""
        res=self.curs.callfunc('keyword.all_words',cx_Oracle.CURSOR)
        x=[]
        [x.append(i[0]) for i in res]
        return x

    def get_keywords(self,id):
        """get keywords for an asset"""
        res = self.curs.connection.cursor()
        self.curs.callproc('keyword.get_keywords',[res,id])
        x=[]
        [x.append(i[0]) for i in res]
        return x

    def get_ids(self,kword):
        """get assets that have that keyword"""
        res = self.curs.connection.cursor()
        self.curs.callproc('keyword.get_ids',[res, kword])
        x=[]
        [x.append(i[0]) for i in res]
        return x

    def get_keywords2(self,id):
        """get assets that have that keyword"""
        res=self.curs.callfunc('keyword.get_keywords2',cx_Oracle.CURSOR,[17])
        x=[]
        [x.append(i[0]) for i in res]
        return x

conn = cx_Oracle.connect("mh/oracle@tmpltest")
curs = conn.cursor()

kw=Keywords(curs)
kw.delete(23,'green')
kw.add(23,'green')
kw.add(23,'bright')

print "asset 23:    ",kw.get_keywords(23)
print "asset 17:    ",kw.get_keywords2(17)
print "blue things: ",kw.get_ids('blue')
print "all keywords:",kw.all_words()

conn.commit()
conn.close()
