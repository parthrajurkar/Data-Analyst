create database if not exists ShopDB;
use ShopDB;

create table Customers(
CustomerID int auto_increment primary key,
Name varchar(100),
Email varchar(100) unicode,
Address varchar(200)
);

insert into Customers(Name,Email,Address)
values
('Parth','parth@gmail.com','Amravati,India'),
('Krishna','krishna@gmail.com','Amravati,India');

select * from Customers;
select name from Customers;
select distinct address from customers;

