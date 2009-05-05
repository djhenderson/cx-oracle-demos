create table cxdemo_t1(a number, b varchar(20));

create or replace package cxdemo
as
    procedure p0;
    procedure p2(aa number, bb varchar2);
    function f0 return number;
    function f2(x number, y number) return number;
    function refc return sys_refcursor;
end cxdemo;
/

CREATE OR REPLACE package body cxdemo
as
    procedure p0 is
    begin
        insert into cxdemo_t1(a, b) values (99, 'zz');
    end;

    procedure p2(aa number, bb varchar2) is
    begin
        insert into cxdemo_t1(a, b) values (aa, bb);
    end;

    function f0 return number is
    begin
        return 17;
    end;

    function f2(x number, y number) return number is
    begin
        return x + y;
    end;

    function refc return sys_refcursor is
        rc  sys_refcursor;
    begin
        open rc for
            select a, b
              from cxdemo_t1;
        return rc;
    end;
end cxdemo;
/

