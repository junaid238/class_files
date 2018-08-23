table creation
---------------
CREATE TABLE `students` (
 `sno` INT(32) NOT NULL ,
 `rno` INT(32) NOT NULL AUTO_INCREMENT ,
 `name` VARCHAR(64) NOT NULL ,
 `feeStatus` TINYINT(1) NOT NULL 
   );


CREATE TABLE  users (
						id int(11) NOT NULL AUTO_INCREMENT,
							email varchar(45),
							password varchar(45),
								PRIMARY KEY (id)
								
								);


CRUD operations 
Create
Retrive / fetch 
Update 
Delete 

insert query --> columnname , values (data) --> insert data
insert into students(sno , rno , name , feeStatus) values (1 , NULL , "Khan" , 1) ;

select --> fetch data from columns / tables
select columnname from table; single column data 
select columnname1 , columnname2 from table; multiple column data 
select * from table; all columns data 


clauses --> conditions 
where 
as 
and or 











