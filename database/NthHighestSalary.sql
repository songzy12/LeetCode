DROP FUNCTION IF EXISTS getNthHighestSalary;
delimiter $$
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
SET M=N-1;
  RETURN (
     # Write your MySQL query statement below.
     SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT M, 1
     # SELECT IFNULL((SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT M ,1), NULL)
  );
END$$
delimiter ;

/* SELECT e1.Salary
   FROM (SELECT DISTINCT Salary FROM Employee) e1
   WHERE (SELECT COUNT(*) FROM (SELECT DISTINCT Salary FROM Employee) e2 WHERE e2.Salary > e1.Salary) = N - 1  
 */
