#-----------------------------------------------------------------------
# this file is part of the cx-oracle-demo package.
# http://code.google.com/p/cx-oracle-demos
#-----------------------------------------------------------------------

desc="""BLOB, binary large object"""

setup="""
create table blobtest (
  a number,
  b blob
);
"""

cleanup="""
drop table blobtest;
"""

notes="""
To create a blob object, use curs.var(cx_Oracle.BLOB).  To set
data into the blob, use b.setvalue(offset,data).  Use setinputsizes
to tell cx_Oracle the incoming parameter is a blob.

blob operations:  copy(), setvalue(offset, data), getvalue(offset=0)

Note that printing the blob will call its str() function.
"""

output="""
1 <type 'cx_Oracle.LOB'> GIF87a(+binary junk)
2 <type 'cx_Oracle.LOB'> GIF87a(+binary junk)

Look at the table data in sql developer, double click the blobs,
select 'view as image' and you will see a smiley face.
"""

def demo():
    import sys
    import cx_Oracle
    connstr = sys.argv[1]
    conn = cx_Oracle.connect(connstr)
    curs = conn.cursor()

    curs.execute('delete from blobtest')

    # these are the bytes of a 32x32 GIF image
    smiley_gif="\x47\x49\x46\x38\x37\x61\x20\x00\x20\x00\x80\x01\x00"+\
       "\x00\x00\x00\xff\xff\xff\x2c\x00\x00\x00\x00\x20\x00\x20\x00"+\
       "\x00\x02\x38\x8c\x8f\xa9\xcb\xed\x0f\xa3\x9c\xb4\xda\x8b\xb3"+\
       "\xde\xbc\xfb\x07\x84\xc0\x17\x88\x63\x62\x5a\x29\x2a\x92\x2b"+\
       "\x09\xc7\xf2\x4c\xd7\xb6\xf1\x32\xe6\xd9\xec\xe0\xce\x63\xe5"+\
       "\x16\xc0\x62\x51\x62\x4c\x56\x92\xbe\x9b\xf3\xb9\x29\x00\x00\x3b"

    # create the blob and put the data in
    myblob=curs.var(cx_Oracle.BLOB)
    myblob.setvalue(0,smiley_gif)

    # specify the type of vv as a blob, and insert into table
    curs.setinputsizes(vv = cx_Oracle.BLOB)
    curs.execute("insert into blobtest(a,b) values (1,:vv)", vv=myblob)

    # you can also write into a blob in pieces with a LOB locator
    curs.execute("insert into blobtest(a,b) values (2, empty_blob())")
    curs.execute("select b from blobtest where a = 2")
    myblob2, = curs.fetchone()

    # split our smiley image into two chunks
    chunk1=smiley_gif[0:40]
    chunk2=smiley_gif[40:]

    # and write the chuns to the blob
    myblob2.write(chunk1)
    myblob2.write(chunk2,41)

    conn.commit()

    # fetch results.
    curs.execute('select a,b from blobtest')
    for (a,b) in curs:
        print a, type(b), b

    conn.close()

if __name__ == '__main__':
    demo()
