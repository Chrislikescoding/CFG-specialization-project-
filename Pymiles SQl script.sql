CREATE DATABASE Person;
use Person;
SELECT p.person_name,c.claimed_this_month from Persons as p inner join Personclaims as c on p.email_address = c.email_address
where p.email_address= 'CBelle.Sharp@gmail.com';

CREATE TABLE Persons(
email_address VARCHAR(60) NOT NULL,
department VARCHAR(50),
person_name VARCHAR(50),
surname VARCHAR(50),
address VARCHAR(200),
postcode VARCHAR(20),
PRIMARY KEY (email_address)
);

INSERT INTO
Persons 
(email_address,department, person_name, surname, address, postcode)
VALUES
("cbelle.sharp@gmail.com","Python department","Christabelle", "Sharp","Top Farm, Meg Fen,Lincoln", "LN4 3AW");

SELECT * from Persons;

#("mj@outlook.com","accounts","Mary", "Jones","12 Station road,Bognor", "GU12 1AA"),
#//("js@gmail.com","IT","Julie", "Smith", "10 St John’s Close, Ryhall,Stamford", "PE9 4HS"),
#("HW@yahoo.com","T","Harold", "Wilson", "10 downing Street,London","W1");

CREATE TABLE Personclaims
(email_address VARCHAR(60) NOT NULL,
claimed_last_month DECIMAL(8,2),
claimed_this_month DECIMAL(8,2),
total_claimed DECIMAL(8,2),
total_miles DECIMAL(6,0),

PRIMARY KEY (email_address(60))
);

	INSERT INTO
	Personclaims 
	(email_address, claimed_last_month , claimed_this_month, total_claimed,total_miles)
	VALUES
	("js@gmail@gmail.com",100.00,100.00,10100.00,9000),
    ("mj@outlook.com",210.00,300.00,20500.00,6000),
    ("HW@yahoo.com",1000.00,1000.00,10100.00,11000);
    
#//("js@gmail.com","IT","Julie", "Smith", "10 St John’s Close, Ryhall,Stamford", "PE9 4HS"),
#("HW@yahoo.com","T","Harold", "Wilson", "10 downing Street,London","W1");
    
    SET SQL_SAFE_UPDATES = 0;
	
    UPDATE
	Personclaims 
	SET claimed_last_month=100,claimed_this_month = 100,  total_claimed = 200,total_miles=400
    WHERE email_address='cbelle.sharp@gmail.com';
	
SELECT * from Personclaims;
SELECT email_address,claimed_this_month from PersonClaims;

#("js@gmail.com",150.00,200.00,1000.00),

CREATE TABLE Mileage
(email_address VARCHAR(60) NOT NULL,
postcode_from VARCHAR(200),
place_from VARCHAR(200),
place_to VARCHAR(200),
miles VARCHAR(10)
);
DELETE from Mileage where miles=24565; 
SELECT sum(miles) from Mileage;
SELECT * from Mileage;
DELETE FROM MILEAGE;

INSERT INTO Mileage VALUES('cbelle.sharp@gmail.com',"LN4", "LN4 ", "",24565);




