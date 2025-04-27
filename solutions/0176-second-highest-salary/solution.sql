# Write your MySQL query statement below

-- select salary as SecondHighestSalary from (select distinct salary from Employee order by salary desc limit 2)A where salary < (select distinct salary from Employee order by salary desc limit 1); 

SELECT
    (SELECT DISTINCT
            Salary
        FROM
            Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary
;
