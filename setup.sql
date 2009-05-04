create table t1(a number, b varchar(20));

create or replace procedure p0
as
begin
    insert into t1(a,b) values(99,'zz');
end;
/
create or replace procedure p2(aa number, bb varchar)
as
begin
    insert into t1(a,b) values(aa,bb);
end;
/
create or replace function f0 return number
as
begin
    return 17;
end;
/
create or replace function f2(x number, y number) return number
as
begin
    return x+y;
end;
/
