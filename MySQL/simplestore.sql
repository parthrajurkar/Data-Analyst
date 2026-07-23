create database if not exists SimpleStore;
use SimpleStore;

create table Sales(
Product varchar(50),
Category varchar(50),
Amount decimal(10,2),
SaleDate date
);

insert into sales(Product,Category,Amount,SaleDate)
values
('Pen','Stationery',25.00,'2024-03-01'),
('Notebook','Stationery',50.00,'2024-03-01'),
('Mouse','Electronics',500.00,'2024-03-02'),
('Keyboard','Electronics',700.00,'2024-03-02'),
('Charger','Electronics',300.00,'2024-03-03'),
('Bag','Accessories',1000.00,'2024-03-04');

select * from sales;
select count(*) from sales;
select sum(amount) from sales;
select avg(amount) from sales;
select min(amount),max(amount) from sales;

select category,sum(amount)
from sales
group by category

having sum(amount)>1000;
