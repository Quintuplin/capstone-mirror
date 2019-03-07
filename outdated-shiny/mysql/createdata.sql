# Create the sample database
create database testdb;

# Create a table in the database
create table testdb.testtab (id smallint unsigned not null auto_increment,
                             name varchar(100) not null,
                             constraint pk_example primary key(id));

# Load some data into the database
insert into testdb.testtab (name) values ('Mary');
insert into testdb.testtab (name) values ('Joe');
