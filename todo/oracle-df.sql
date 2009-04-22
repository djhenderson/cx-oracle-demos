create sequence df_thumbq_seq;


create table df_thumbq(
	seqno number(18) primary key,
	unit varchar2(10) not null,
	name varchar2(2048) not null,
	action char(1) not null check (action in ('a','d'))
);

create index idx_df_thumbq_name on df_thumbq(name); 
create index idx_df_thumbq_unit on df_thumbq(unit); 

create or replace trigger df_thumbq_autonumber
before insert on df_thumbq for each row
begin
    if :new.seqno is null then
        select df_thumbq_seq.nextval into :new.seqno from dual;
    end if;
end;
/
