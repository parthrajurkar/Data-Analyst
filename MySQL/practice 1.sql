CREATE DATABASE IF NOT EXISTS CollegeDB;
USE CollegeDB;
select database();

create table Students(
StudentID int auto_increment primary key,
Name varchar(100),
Age tinyint,
Email varchar(100),
JoinDate date
);

select * from Students;

insert into Students(Name,Age,Email,JoinDate)
values
("Parth",21,"parth@gmail.com","2026-07-22"),
("Ram",25,"ram@gmail.com","2026-05-01");

alter table Students add column City varchar(50);
alter table Students modify Age smallint;
alter table Students rename column Email to EmailID;

