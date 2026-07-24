create database if not exists RetailStore;
use RetailStore;

create table Customers(
CustomerID int primary key,
CustomerName varchar(100)
);