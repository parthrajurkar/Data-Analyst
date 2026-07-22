create database if not exists ShopDB;
use ShopDB;

create table Customers(
CustomerID int auto_increment primary key,
Name varchar(100),
Email varchar(100) unicode,
Address varchar(100)
);

insert into Customers(Name,Email,Address)
values
('Parth','parth@gmail.com','Amravati,India'),
('Krishna','krishna@gmail.com','Amravati,India'),
('Ram','ram@gmail.com','Mumbai,India');

select * from customers;
update customers
set address='Pune'
where Name='Parth';