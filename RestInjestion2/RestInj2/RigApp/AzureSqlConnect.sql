-- exec sp_who
create table test_rig2 (id int, _name varchar(50), _size int)
insert test_rig2
select 1, 'srinivas_koppisetti2', 10
UNION
select 2, 'Neeraja Rao Kuppili2', 11

select * from RigApp_rig

SELECT * FROM sys.tables where type='u'
