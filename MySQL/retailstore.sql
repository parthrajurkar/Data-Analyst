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
foreign key(CustomerID) references Customer (CustomerID)
);