
"""
SQL(Q-1)- Explain about the DML,DDL,TCL,DQL commands?
Ans:
DML: DML stands for data manupulation language if you want to manupulate your data that time we can use DML commant
DDL: data defination language, if you want to define your data that time we can use DDl command
TCL: Transaction control language will help for transaction purpose
DQL: DATA CONtrol language will well give the revoke and grant privilage

SQL-(Q-2)-Whatis join, explain about the all joins?
Ans:-
join is used for retrive the row data between two or more table.
Left join:  retrieves all rows from the left table and matched rows from the right table.
right join: we will retrieves all rows from the right table and matched rows from the left table.
full join: retrieves all rows when there is a match in one of  the tables,with nulls where there is no match.
cross join: it is a Cartesian product of both tables.
self join: Joins a table with itself.

SQL(Q-3)Difference between Joins vs Subquery?
Ans:
Joins will perform between two or more table but subquery will always perform inside the one query.

SQL(Q-4) Find 3rd Highest Salary Of employee table ?
Ans:-
select max(salary) AS third_highest_salary from employees where
salary < (select max(salary) from employees where
salary < (select max(salary)from employees)

SQL(Q-6)Difference between Rank vs Dense_rank?
Rank always follow sequence and it may be contain gap but in densrank  is should be unique and gap is not allowed between the rang..
"""