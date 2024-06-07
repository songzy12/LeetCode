/* mysql -u root -p leetcode
 * show databases;
 * show tables;
 * create table Person(PersonId int primary key, FirstName varchar(20), LastName varchar(20));
 * create table Address(AddressId int primary key, PersonId int, City varchar(20), State varchar(20));
 * load data local infile 'Person.txt' into table Person FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n';
 * load data local infile 'Address.txt' into table Address FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n';
 */
 
select FirstName, LastName, City, State from Person p LEFT JOIN Address a on p.PersonId = a.PersonId;

SELECT FirstName, LastName, City, State FROM Person LEFT JOIN Address USING(PersonId);

SELECT FirstName, LastName, City, State FROM Person NATURAL LEFT JOIN Address;

