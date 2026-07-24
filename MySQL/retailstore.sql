create database if not exists RetailStore;
use RetailStore;

create table Customers(
CustomerID int primary key,
CustomerName varchar(100)
);

create table orders(
OrderID int primary key,
Product varchar(50),
Amount decimal(10,2),
CustomerID int,
foreign key(CustomerID) references Customers (CustomerID)
);

-- Customers Table
insert into Customers(CustomerID,CustomerName)
values
(1,'Rahul Sharma'),
(2,'Anjali Mehta'),
(3,'Amit Verma');

-- Orders Table
insert into Orders Values
(1,'Laptop',50000,2),
(2,'Mouse',500,1),
(3,'Keyboard',700,1);