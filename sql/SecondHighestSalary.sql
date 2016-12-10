/* mysql -u root -p leetcode
 */

/* create table Employee (Id int primary key, Salary int);
 * insert into Employee values(1, 100);
 * insert into Employee values(2, 200);
 * insert into Employee values(3, 300);
 */
 
/* LOAD DATA LOCAL INFILE 'SecondHighestSalary.txt' INTO TABLE Employee;
 */

/* delete from Employee where id > 1;
 */
 
select * from Employee;
select Salary as SecondHighestSalary from Employee union select null order by SecondHighestSalary desc limit 1, 1
