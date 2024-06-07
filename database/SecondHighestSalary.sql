/* mysql -u root -p leetcode
 *
 * create table Employee (Id int primary key, Salary int);
 * insert into Employee values(1, 100);
 * insert into Employee values(2, 200);
 * insert into Employee values(3, 300);
 *
 * LOAD DATA LOCAL INFILE 'Employee.txt' INTO TABLE Employee; 
 * 5	400
 *
 * delete from Employee where id > 1;
 */
 
select * from Employee;

select Salary as SecondHighestSalary 
from Employee 
union 
select null 
order by SecondHighestSalary desc 
limit 1, 1;

select max(Salary) as SecondHighestSalary
from Employee
where Salary < (select max(Salary) from Employee);

select (
  select distinct Salary 
  from Employee 
  order by Salary Desc 
  limit 1 offset 1
)as SecondHighestSalary;

/* [LIMIT {[offset,] row_count | row_count OFFSET offset}]
 */
