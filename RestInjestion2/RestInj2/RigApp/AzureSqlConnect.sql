-- exec sp_who
create table test_rig2 (id int, _name varchar(50), _size int)
insert test_rig2
select 1, 'srinivas_koppisetti2', 10
UNION
select 2, 'Neeraja Rao Kuppili2', 11

SHOW TABLES
select * from pysql

SELECT * FROM sys.sysobjects where type='u'



EXEC sp_rename 'RigApp_rig', 'RigApp_rig_old'

EXEC sp_rename 'RigApp_rig_old', 'RigApp_rig'

TRUNCATE TABLE RigApp_rig

DROP TABLE django_admin_log, django_content_type, django_session

DROP TABLE django_migrations

DROP TABLE django_content_type

EXEC sp_fkeys django_content_type
select * from django_migrations