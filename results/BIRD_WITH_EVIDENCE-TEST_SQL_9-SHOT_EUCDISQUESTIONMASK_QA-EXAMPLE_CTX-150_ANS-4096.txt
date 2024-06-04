SELECT MAX(`Free Meal Count (K-12)` / `Enrollment (K-12)`) AS Highest_Eligible_Free_Rate FROM frpm INNER JOIN schools ON frpm.CDSCode = schools.CDSCode WHERE schools.County = 'Alameda'
SELECT `School Name`, `Free Meal Count (Ages 5-17)` / `Enrollment (Ages 5-17)` AS FreeRate FROM frpm WHERE `School Type` = 'Continuation' ORDER BY FreeRate ASC LIMIT 3 
SELECT DISTINCT T2.Zip FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.CDSCode = T2.CDSCode WHERE T1.`Charter School (Y/N)` = 1 AND T2.District = 'Fresno County Office of Education'
SELECT MailStreet, MailCity, MailState, MailZip FROM schools WHERE CDSCode = ( SELECT CDSCode FROM frpm ORDER BY `FRPM Count (K-12)` DESC LIMIT 1 )
SELECT T2.Phone FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.CDSCode = T2.CDSCode WHERE T1.`Charter School (Y/N)` = 1 AND T2.OpenDate > '2000-01-01' AND T2.FundingType = 'Directly funded'
SELECT COUNT(DISTINCT T1.CDSCode) FROM schools AS T1 INNER JOIN satscores AS T2 ON T1.CDSCode = T2.cds WHERE T2.AvgScrMath < 400 AND T1.Virtual = 'F'
SELECT sname FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.cds = T2.CDSCode WHERE T1.NumTstTakr > 500 AND T2.Magnet = 1
SELECT T1.Phone FROM schools AS T1 INNER JOIN satscores AS T2 ON T1.CDSCode = T2.cds ORDER BY T2.NumGE1500 DESC LIMIT 1;
SELECT T2.NumTstTakr FROM frpm AS T1 INNER JOIN satscores AS T2 ON T1.CDSCode = T2.cds WHERE T1.`FRPM Count (K-12)` = ( SELECT MAX(`FRPM Count (K-12)`) FROM frpm )
SELECT COUNT(schools.CDSCode) FROM schools INNER JOIN satscores ON schools.CDSCode = satscores.cds WHERE satscores.AvgScrMath > 560 AND schools.FundingType = 'Directly funded'
SELECT T1.`FRPM Count (Ages 5-17)` FROM frpm AS T1 INNER JOIN satscores AS T2 ON T1.CDSCode = T2.cds ORDER BY T2.AvgScrRead DESC LIMIT 1;
SELECT CDSCode FROM frpm WHERE (`Enrollment (K-12)` + `Enrollment (Ages 5-17)`) > 500
SELECT MAX(T1.`Percent (%) Eligible Free (Ages 5-17)`) FROM frpm AS T1 INNER JOIN satscores AS T2 ON T1.CDSCode = T2.cds WHERE T2.NumGE1500 / T2.NumTstTakr > 0.3
SELECT T2.Phone FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.cds = T2.CDSCode ORDER BY (T1.NumGE1500 / T1.NumTstTakr) DESC LIMIT 3
SELECT NCESSchool FROM frpm ORDER BY `Enrollment (Ages 5-17)` DESC LIMIT 5
SELECT dname FROM satscores WHERE cds IN (SELECT CDSCode FROM schools WHERE StatusType = 'Active') ORDER BY AvgScrRead DESC LIMIT 1
SELECT COUNT(schools.CDSCode) FROM schools INNER JOIN satscores ON schools.CDSCode = satscores.cds WHERE schools.County = 'Alameda' AND satscores.NumTstTakr < 100
SELECT T2.CharterNum FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.cds = T2.CDSCode WHERE T1.AvgScrWrite = 499 
SELECT COUNT(schools.CDSCode) FROM schools INNER JOIN satscores ON schools.CDSCode = satscores.cds WHERE schools.County = 'Contra Costa' AND schools.FundingType = 'Directly funded' AND satscores.NumTstTakr <= 250
SELECT T2.Phone FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.cds = T2.CDSCode ORDER BY T1.AvgScrMath DESC LIMIT 1
SELECT COUNT(*) FROM frpm WHERE `County Name` = 'Amador' AND `Low Grade` = '9' AND `High Grade` = '12'
SELECT COUNT(schools.CDSCode) FROM schools INNER JOIN frpm ON schools.CDSCode = frpm.CDSCode WHERE schools.County = 'Los Angeles' AND frpm.`Free Meal Count (K-12)` > 500 AND frpm.`FRPM Count (K-12)` < 700
SELECT T1.`School Name` FROM frpm AS T1 INNER JOIN satscores AS T2 ON T1.CDSCode = T2.cds WHERE T1.`County Name` = 'Contra Costa' ORDER BY T2.NumTstTakr DESC LIMIT 1
SELECT T1.`School Name`, T2.Street FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.CDSCode = T2.CDSCode WHERE ABS(T1.`Enrollment (K-12)` - T1.`Enrollment (Ages 5-17)`) > 30
SELECT T1.`School Name` FROM frpm AS T1 INNER JOIN satscores AS T2 ON T1.CDSCode = T2.cds WHERE T1.`Percent (%) Eligible Free (K-12)` > 0.1 AND T2.NumGE1500 >= 1500
SELECT s.School, s.FundingType FROM satscores AS sat INNER JOIN schools AS s ON sat.cds = s.CDSCode WHERE s.County = 'Riverside' AND sat.AvgScrMath > 400 GROUP BY s.School HAVING AVG(sat.AvgScrMath) > 400
SELECT T1.`School Name`, T1.Street, T1.City, T1.Zip, T1.State FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.CDSCode = T2.CDSCode WHERE T1.`FRPM Count (Ages 5-17)` > 800 AND T1.`County Name` = 'Monterey' AND T1.`School Type` = 'High School'
SELECT s.School, AVG(sat.AvgScrWrite), s.Phone FROM satscores AS sat INNER JOIN schools AS s ON sat.cds = s.CDSCode WHERE s.OpenDate > '1991-12-31' OR (s.ClosedDate IS NOT NULL AND s.ClosedDate < '2000-01-01') GROUP BY s.School, s.Phone
SELECT T2.School, T2.DOCTYPE FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.CDSCode = T2.CDSCode WHERE T1.`Enrollment (K-12)` - T1.`Enrollment (Ages 5-17)` > (SELECT AVG(T3.`Enrollment (K-12)` - T3.`Enrollment (Ages 5-17)`) FROM frpm AS T3 INNER JOIN schools AS T4 ON T3.CDSCode = T4.CDSCode WHERE T4.FundingType = 'Local') AND T2.FundingType = 'Local'
SELECT OpenDate FROM schools WHERE CDSCode = ( SELECT CDSCode FROM frpm WHERE `Enrollment (K-12)` = ( SELECT MAX(`Enrollment (K-12)`) FROM frpm ) )
SELECT City, SUM(`Enrollment (K-12)`) as Total_Enrollment FROM frpm INNER JOIN schools ON frpm.CDSCode = schools.CDSCode GROUP BY City ORDER BY Total_Enrollment ASC LIMIT 5
SELECT `School Name`, `Free Meal Count (K-12)` / `Enrollment (K-12)` AS `Eligible Free Rate` FROM frpm ORDER BY `Enrollment (K-12)` DESC LIMIT 9, 2 
SELECT T1.`School Name`, (T1.`FRPM Count (K-12)` / T1.`Enrollment (K-12)`) AS 'Eligible FRPM Rate' FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.CDSCode = T2.CDSCode WHERE T2.DOC = '66' ORDER BY T1.`FRPM Count (K-12)` DESC LIMIT 5
SELECT T2.`School`, T2.`Website` FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.CDSCode = T2.CDSCode WHERE T1.`Free Meal Count (Ages 5-17)` BETWEEN 1900 AND 2000
SELECT (`Free Meal Count (Ages 5-17)` / `Enrollment (Ages 5-17)`) AS FreeRate FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.CDSCode = T2.CDSCode WHERE T2.AdmFName1 = 'Kacey' AND T2.AdmLName1 = 'Gibson'
SELECT s.AdmEmail1 FROM schools AS s INNER JOIN frpm AS f ON s.CDSCode = f.CDSCode WHERE f.`Charter School (Y/N)` = 1 ORDER BY f.`Enrollment (K-12)` ASC LIMIT 1 
SELECT T3.AdmFName1, T3.AdmLName1, T3.AdmFName2, T3.AdmLName2, T3.AdmFName3, T3.AdmLName3 FROM satscores AS T1 INNER JOIN schools AS T3 ON T1.cds = T3.CDSCode ORDER BY T1.NumGE1500 DESC LIMIT 1
SELECT T2.Street, T2.City, T2.Zip, T2.State FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.cds = T2.CDSCode ORDER BY T1.NumGE1500 / T1.NumTstTakr ASC LIMIT 1
SELECT T3.Website FROM satscores AS T1 INNER JOIN frpm AS T2 ON T1.cds = T2.CDSCode INNER JOIN schools AS T3 ON T1.cds = T3.CDSCode WHERE T2.`County Name` = 'Los Angeles' AND T1.NumTstTakr BETWEEN 2000 AND 3000
SELECT AVG(T2.NumTstTakr) FROM schools AS T1 INNER JOIN satscores AS T2 ON T1.CDSCode = T2.cds WHERE T1.County = 'Fresno' AND STRFTIME('%Y', T1.OpenDate) = '1980'
SELECT T3.Phone FROM satscores AS T1 INNER JOIN schools AS T3 ON T1.cds = T3.CDSCode WHERE T3.District = 'Fresno Unified' ORDER BY T1.AvgScrRead ASC LIMIT 1
SELECT sname FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.cds = T2.CDSCode WHERE T2.Virtual = 'F' ORDER BY T1.AvgScrRead DESC LIMIT 5; 
SELECT EILName FROM schools WHERE CDSCode = (SELECT cds FROM satscores ORDER BY AvgScrMath DESC LIMIT 1);
SELECT satscores.AvgScrMath, schools.County FROM satscores INNER JOIN schools ON satscores.cds = schools.CDSCode ORDER BY (satscores.AvgScrMath + satscores.AvgScrRead + satscores.AvgScrWrite) / 3 LIMIT 1
SELECT satscores.AvgScrWrite, schools.City FROM satscores INNER JOIN schools ON satscores.cds = schools.CDSCode WHERE satscores.NumGE1500 = ( SELECT MAX(NumGE1500) FROM satscores )
SELECT T1.School, AVG(T2.AvgScrWrite) AS Average_Writing_Score FROM schools AS T1 INNER JOIN satscores AS T2 ON T1.CDSCode = T2.cds WHERE T1.AdmFName1 = 'Ricci' AND T1.AdmLName1 = 'Ulrich' GROUP BY T1.School
SELECT School, `Enrollment (K-12)` FROM frpm INNER JOIN schools ON frpm.CDSCode = schools.CDSCode WHERE DOC = 31 ORDER BY `Enrollment (K-12)` DESC LIMIT 1 
SELECT COUNT(*)/12 AS 'Monthly Average' FROM schools WHERE County = 'Alameda' AND DOC = '52' AND STRFTIME('%Y', OpenDate) = '1980'
SELECT (SELECT COUNT(*) FROM schools WHERE DOC = 54 AND County = 'Orange') / (SELECT COUNT(*) FROM schools WHERE DOC = 52 AND County = 'Orange') AS Ratio
SELECT County, School, ClosedDate FROM schools WHERE StatusType = 'Closed' GROUP BY County ORDER BY COUNT(School) DESC 
SELECT s.School, s.Street FROM schools AS s INNER JOIN satscores AS ss ON s.CDSCode = ss.cds ORDER BY ss.AvgScrMath DESC LIMIT 5, 1
SELECT T1.MailStreet, T1.School FROM schools AS T1 INNER JOIN satscores AS T2 ON T1.CDSCode = T2.cds ORDER BY T2.AvgScrRead LIMIT 1
SELECT COUNT(*) FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.cds = T2.CDSCode WHERE T1.AvgScrRead + T1.AvgScrMath + T1.AvgScrWrite >= 1500 AND T2.MailCity = 'Lakeport'
SELECT SUM(NumTstTakr) FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.cds = T2.CDSCode WHERE T2.MailCity = 'Fresno'
SELECT School, MailZip FROM schools WHERE AdmFName1 = 'Avetik' AND AdmLName1 = 'Atoian'
SELECT CAST(COUNT(CASE WHEN County = 'Colusa' THEN 1 ELSE NULL END) AS REAL) / COUNT(CASE WHEN County = 'Humboldt' THEN 1 ELSE NULL END) FROM schools WHERE MailState = 'CA'
SELECT COUNT(*) FROM schools WHERE MailState = 'CA' AND StatusType = 'Active' AND County = 'San Joaquin'
SELECT T1.Phone, T1.Ext FROM schools AS T1 INNER JOIN satscores AS T2 ON T1.CDSCode = T2.cds ORDER BY T2.AvgScrWrite DESC LIMIT 1 OFFSET 332;
SELECT T1.School, T1.Phone, T1.Ext FROM schools AS T1 WHERE T1.Zip = '95203-3704'
SELECT T1.Website FROM schools AS T1 WHERE (T1.AdmFName1 = 'Mike' AND T1.AdmLName1 = 'Larson') OR (T1.AdmFName2 = 'Dante' AND T1.AdmLName2 = 'Alvarez') OR (T1.AdmFName3 = 'Mike' AND T1.AdmLName3 = 'Larson') OR (T1.AdmFName3 = 'Dante' AND T1.AdmLName3 = 'Alvarez')
SELECT Website FROM schools WHERE Virtual = 'P' AND Charter = 1 AND County = 'San Joaquin'
SELECT COUNT(*) FROM schools WHERE City = 'Hickman' AND DOC = 52 AND Charter = 1
SELECT COUNT(*) FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.CDSCode = T2.CDSCode WHERE T2.County = 'Los Angeles' AND T2.Charter = 0 AND (T1.`Free Meal Count (K-12)` * 100 / T1.`Enrollment (K-12)`) < 0.18 
SELECT T1.School, T1.City, T1.AdmFName1, T1.AdmLName1, T1.AdmFName2, T1.AdmLName2, T1.AdmFName3, T1.AdmLName3 FROM schools AS T1 WHERE T1.Charter = 1 AND T1.CharterNum = '00D2'
SELECT COUNT(*) FROM schools WHERE MailCity = 'Hickman' AND CharterNum = '00D4'
SELECT CAST(SUM(CASE WHEN FundingType = 'Locally Funded' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(*) FROM schools WHERE County = 'Santa Clara'
SELECT COUNT(*) FROM schools WHERE County = 'Stanislaus' AND FundingType = 'Directly Funded' AND OpenDate BETWEEN '2000-01-01' AND '2005-12-31'
SELECT COUNT(*) FROM schools WHERE DOCType = 'Community College District' AND ClosedDate LIKE '1989%' AND City = 'San Francisco'
SELECT County FROM schools WHERE SOC = '11' AND STRFTIME('%Y', ClosedDate) BETWEEN '1980' AND '1989' GROUP BY County ORDER BY COUNT(*) DESC LIMIT 1
SELECT NCESSchool FROM schools WHERE SOC = 31
SELECT COUNT(DISTINCT District) FROM schools WHERE County = 'Alpine' AND DOCType = 'District Community Day School' AND (StatusType = 'Active' OR StatusType = 'Closed')
SELECT `District Code` FROM frpm WHERE `School Name` IN (SELECT School FROM schools WHERE City = 'Fresno' AND Magnet = 0)
SELECT `Enrollment (Ages 5-17)` FROM frpm INNER JOIN schools ON frpm.CDSCode = schools.CDSCode WHERE `Academic Year` = '2014-2015' AND City = 'Fremont' AND EdOpsCode = 'SSS'
SELECT `FRPM Count (Ages 5-17)` FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.CDSCode = T2.CDSCode WHERE T2.School = 'Youth Authority School' AND T2.MailStreet = 'PO Box 1040'
SELECT `Low Grade` FROM frpm WHERE `District Type` = 'SPECON' AND `District Code` = 613360 ORDER BY `Low Grade` ASC LIMIT 1
SELECT T1.`School Name`, T1.`Educational Option Type` FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.CDSCode = T2.CDSCode WHERE T1.`NSLP Provision Status` = 'Breakfast Provision 2' AND T1.`County Code` = '37'
SELECT City FROM schools WHERE CDSCode IN ( SELECT CDSCode FROM frpm WHERE `Low Grade` = '9' AND `High Grade` = '12' AND `NSLP Provision Status` = '2' AND `County Name` = 'Merced' ) AND EILCode = 'HS'
SELECT T1.`School`, T1.`GSserved`, T2.`Percent (%) Eligible FRPM (Ages 5-17)` FROM schools AS T1 INNER JOIN frpm AS T2 ON T1.CDSCode = T2.CDSCode WHERE T1.County = 'Los Angeles' AND T1.GSserved = 'K-9'
SELECT GSserved FROM schools WHERE City = 'Adelanto' GROUP BY GSserved ORDER BY COUNT(GSserved) DESC LIMIT 1
SELECT County, COUNT(*) as NumberOfSchools FROM schools WHERE Virtual = 'F' AND County IN ('San Diego', 'Santa Barbara') GROUP BY County ORDER BY NumberOfSchools DESC LIMIT 1
SELECT T1.`School Type`, T1.`School Name`, T2.Latitude FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.CDSCode = T2.CDSCode ORDER BY T2.Latitude DESC LIMIT 1
SELECT `City`, `School`, `Low Grade` FROM schools WHERE `State` = 'CA' ORDER BY `Latitude` ASC LIMIT 1
SELECT GSoffered FROM schools ORDER BY Longitude DESC LIMIT 1 
SELECT City, COUNT(School) AS NumberOfSchools FROM schools WHERE Magnet = 1 AND GSoffered = 'K-8' AND EdOpsName = 'Multiple Provision Types' GROUP BY City
SELECT AdmFName1, District, COUNT(*) AS Count FROM schools GROUP BY AdmFName1, District ORDER BY Count DESC LIMIT 2 
SELECT T1.`District Code`, (T1.`Free Meal Count (K-12)` / T1.`Enrollment (K-12)`) * 100 AS `Percent (%) Eligible Free (K-12)` FROM frpm AS T1 INNER JOIN schools AS T2 ON T1.CDSCode = T2.CDSCode WHERE T2.AdmFName1 = 'Alusine'
SELECT AdmLName1, District, County, School FROM schools WHERE CharterNum = '40'
SELECT AdmEmail1 FROM schools WHERE County = 'San Bernardino' AND District = 'San Bernardino City Unified' AND OpenDate BETWEEN '2009-01-01' AND '2010-12-31' AND (SOC = '62' OR DOC = '54')
SELECT T1.sname, T1.AdmEmail1 FROM satscores AS T1 INNER JOIN schools AS T2 ON T1.cds = T2.CDSCode ORDER BY T1.NumGE1500 DESC LIMIT 1
SELECT COUNT(T1.account_id) FROM account AS T1 INNER JOIN district AS T2 ON T1.district_id = T2.district_id WHERE T1.frequency = 'POPLATEK PO OBRATU' AND T2.A3 = 'east Bohemia'
SELECT COUNT(DISTINCT T1.account_id) FROM account AS T1 INNER JOIN district AS T2 ON T1.district_id = T2.district_id INNER JOIN loan AS T3 ON T1.account_id = T3.account_id WHERE T2.A3 = 'Prague'
SELECT IIF(AVG(A12) > AVG(A13), '1995', '1996') FROM district 
SELECT COUNT(DISTINCT T1.district_id) FROM client AS T1 INNER JOIN district AS T2 ON T1.district_id = T2.district_id WHERE T1.gender = 'F' AND T2.A11 > 6000 AND T2.A11 < 10000
SELECT COUNT(client.client_id) FROM client INNER JOIN district ON client.district_id = district.district_id WHERE client.gender = 'M' AND district.A3 = 'North Bohemia' AND district.A11 > 8000
SELECT T1.account_id, MIN(T3.A11) - MAX(T3.A11) FROM disp AS T1 INNER JOIN client AS T2 ON T1.client_id = T2.client_id INNER JOIN district AS T3 ON T2.district_id = T3.district_id WHERE T2.gender = 'F' GROUP BY T1.account_id ORDER BY T2.birth_date DESC LIMIT 1 
SELECT T1.account_id FROM account AS T1 INNER JOIN disp AS T2 ON T1.account_id = T2.account_id INNER JOIN client AS T3 ON T2.client_id = T3.client_id INNER JOIN district AS T4 ON T3.district_id = T4.district_id WHERE T3.birth_date = ( SELECT MAX(birth_date) FROM client ) AND T4.A11 = ( SELECT MAX(A11) FROM district )
SELECT COUNT(T1.client_id) FROM client AS T1 INNER JOIN disp AS T2 ON T1.client_id = T2.client_id INNER JOIN account AS T3 ON T2.account_id = T3.account_id WHERE T3.frequency = 'POPLATEK TYDNE' AND T2.type = 'OWNER'
SELECT T2.client_id, T2.gender, T2.birth_date FROM disp AS T1 INNER JOIN client AS T2 ON T1.client_id = T2.client_id WHERE T1.type = 'Disponent' AND T1.account_id IN (SELECT account_id FROM account WHERE frequency = 'POPLATEK PO OBRATU')
SELECT T1.account_id, T1.amount FROM loan AS T1 INNER JOIN account AS T2 ON T1.account_id = T2.account_id WHERE T1.status = 'A' AND STRFTIME('%Y', T1.date) = '1997' AND T2.frequency = 'POPLATEK TYDNE' ORDER BY T1.amount ASC LIMIT 1
SELECT T1.account_id, T1.amount FROM loan AS T1 INNER JOIN account AS T2 ON T1.account_id = T2.account_id WHERE T1.duration > 12 AND strftime('%Y', T2.date) = '1993' ORDER BY T1.amount DESC LIMIT 1
SELECT COUNT(DISTINCT T1.account_id) FROM account AS T1 INNER JOIN disp AS T2 ON T1.account_id = T2.account_id INNER JOIN client AS T3 ON T2.client_id = T3.client_id INNER JOIN district AS T4 ON T3.district_id = T4.district_id WHERE T3.gender = 'F' AND T3.birth_date < '1950-01-01' AND T4.A2 = 'Sokolov'
SELECT account_id FROM account WHERE date = (SELECT MIN(date) FROM account WHERE STRFTIME('%Y', date) = '1995')
SELECT T1.account_id FROM account AS T1 INNER JOIN trans AS T2 ON T1.account_id = T2.account_id WHERE T1.date < '1997-01-01' AND T2.amount > 3000
SELECT T1.client_id FROM client AS T1 INNER JOIN disp AS T2 ON T1.client_id = T2.client_id INNER JOIN card AS T3 ON T2.disp_id = T3.disp_id WHERE T3.issued = '1994-03-03'
SELECT T1.date FROM account AS T1 INNER JOIN trans AS T2 ON T1.account_id = T2.account_id WHERE T2.amount = 840 AND T2.date = '1998-10-14'
SELECT T1.district_id FROM account AS T1 INNER JOIN loan AS T2 ON T1.account_id = T2.account_id WHERE T2.date = '1994-08-25'
SELECT MAX(T1.amount) FROM trans AS T1 INNER JOIN disp AS T2 ON T1.account_id = T2.account_id INNER JOIN card AS T3 ON T2.disp_id = T3.disp_id WHERE T3.issued = '1996-10-21'
SELECT T1.gender FROM client AS T1 INNER JOIN disp AS T2 ON T1.client_id = T2.client_id INNER JOIN account AS T3 ON T2.account_id = T3.account_id INNER JOIN district AS T4 ON T1.district_id = T4.district_id WHERE T4.A11 = (SELECT MAX(A11) FROM district) ORDER BY T1.birth_date ASC LIMIT 1
SELECT T4.amount FROM loan AS T1 INNER JOIN disp AS T2 ON T1.account_id = T2.account_id INNER JOIN client AS T3 ON T2.client_id = T3.client_id INNER JOIN trans AS T4 ON T1.account_id = T4.account_id WHERE T1.amount = ( SELECT MAX(amount) FROM loan ) ORDER BY T4.date ASC LIMIT 1
SELECT COUNT(T1.client_id) FROM client AS T1 INNER JOIN disp AS T2 ON T1.client_id = T2.client_id INNER JOIN account AS T3 ON T2.account_id = T3.account_id INNER JOIN district AS T4 ON T3.district_id = T4.district_id WHERE T1.gender = 'F' AND T4.A2 = 'Jesenik'
SELECT T2.disp_id FROM trans AS T1 INNER JOIN disp AS T2 ON T1.account_id = T2.account_id WHERE T1.amount = 5100 AND STRFTIME('%Y-%m-%d', T1.date) = '1998-09-02'
SELECT COUNT(account_id) FROM account INNER JOIN district ON account.district_id = district.district_id WHERE district.A2 = 'Litomerice' AND YEAR(account.date) = 1996
SELECT DISTINCT T4.A2 FROM client AS T1 INNER JOIN disp AS T2 ON T1.client_id = T2.client_id INNER JOIN account AS T3 ON T2.account_id = T3.account_id INNER JOIN district AS T4 ON T3.district_id = T4.district_id WHERE T1.gender = 'F' AND T1.birth_date = '1976-01-29'
SELECT T1.birth_date FROM client AS T1 INNER JOIN disp AS T2 ON T1.client_id = T2.client_id INNER JOIN loan AS T3 ON T2.account_id = T3.account_id WHERE T3.amount = 98832 AND T3.date = '1996-01-03'
SELECT T1.account_id FROM account AS T1 INNER JOIN district AS T2 ON T1.district_id = T2.district_id WHERE T2.A3 = 'Prague' ORDER BY T1.date LIMIT 1
SELECT CAST(COUNT(CASE WHEN T2.gender = 'M' THEN 1 ELSE NULL END) AS REAL) * 100 / COUNT(T2.client_id) FROM district AS T1 INNER JOIN client AS T2 ON T1.district_id = T2.district_id WHERE T1.A3 = 'south Bohemia' AND T1.A4 = (SELECT MAX(A4) FROM district WHERE A3 = 'south Bohemia')
SELECT (CAST((SELECT balance FROM trans WHERE account_id = (SELECT account_id FROM loan WHERE date = '1993-07-05' ORDER BY date LIMIT 1) AND date = '1998-12-27') AS REAL) - (SELECT balance FROM trans WHERE account_id = (SELECT account_id FROM loan WHERE date = '1993-07-05' ORDER BY date LIMIT 1) AND date = '1993-03-22')) / (SELECT balance FROM trans WHERE account_id = (SELECT account_id FROM loan WHERE date = '1993-07-05' ORDER BY date LIMIT 1) AND date = '1993-03-22') * 100 AS increase_rate FROM trans WHERE account_id = (SELECT account_id FROM loan WHERE date = '1993-07-05' ORDER BY date LIMIT 1)
SELECT CAST(SUM(CASE WHEN status = 'A' THEN amount ELSE 0 END) AS REAL) * 100 / SUM(amount) FROM loan 
SELECT CAST(SUM(CASE WHEN T2.status = 'C' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.account_id) FROM account AS T1 INNER JOIN loan AS T2 ON T1.account_id = T2.account_id WHERE T2.amount < 100000 
SELECT T1.account_id, T3.A2 AS district_name, T3.A3 AS district_region FROM account AS T1 INNER JOIN trans AS T2 ON T1.account_id = T2.account_id INNER JOIN district AS T3 ON T1.district_id = T3.district_id WHERE T1.frequency = 'POPLATEK PO OBRATU' AND STRFTIME('%Y', T2.date) = '1993'
SELECT T1.account_id, T1.frequency, T3.gender FROM account AS T1 INNER JOIN district AS T2 ON T1.district_id = T2.district_id INNER JOIN client AS T3 ON T2.district_id = T3.district_id INNER JOIN disp AS T4 ON T3.client_id = T4.client_id WHERE T2.A3 = 'east Bohemia' AND T1.date BETWEEN '1995-01-01' AND '2000-12-31' AND T4.type = 'OWNER'
SELECT T1.account_id, T1.date FROM account AS T1 INNER JOIN district AS T2 ON T1.district_id = T2.district_id WHERE T2.A2 = 'Prachatice'
SELECT T1.A2 AS district, T1.A3 AS region FROM district AS T1 INNER JOIN account AS T2 ON T1.district_id = T2.district_id INNER JOIN loan AS T3 ON T2.account_id = T3.account_id WHERE T3.loan_id = 4990
SELECT T1.account_id, T2.A2 AS district, T2.A3 AS region FROM loan AS T1 INNER JOIN district AS T2 ON T1.account_id = T2.district_id WHERE T1.amount > 300000
SELECT T1.loan_id, T2.A3 AS district, T2.A11 AS average_salary FROM loan AS T1 INNER JOIN district AS T2 ON T1.account_id = T2.district_id WHERE T1.duration = 60
SELECT T3.A3 AS district, T3.A2 AS state, ((T3.A13 - T3.A12) / T3.A12) * 100 AS unemployment_rate_increment FROM loan AS T1 INNER JOIN account AS T2 ON T1.account_id = T2.account_id INNER JOIN district AS T3 ON T2.district_id = T3.district_id WHERE T1.status = 'D'
SELECT CAST(SUM(CASE WHEN T2.A2 = 'Decin' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(*) FROM account AS T1 INNER JOIN district AS T2 ON T1.district_id = T2.district_id WHERE STRFTIME('%Y', T1.date) = '1993'
SELECT account_id FROM account WHERE frequency = 'POPLATEK MESICNE'
SELECT T1.A2, COUNT(T2.client_id) AS num FROM district AS T1 INNER JOIN client AS T2 ON T1.district_id = T2.district_id WHERE T2.gender = 'F' GROUP BY T1.A2 ORDER BY num DESC LIMIT 10
SELECT T2.A2, T1.amount FROM trans AS T1 INNER JOIN district AS T2 ON T1.account_id = T2.district_id WHERE T1.type = 'VYDAJ' AND STRFTIME('%Y-%m', T1.date) = '1996-01' ORDER BY T1.amount DESC LIMIT 10
SELECT COUNT(DISTINCT T1.account_id) FROM account AS T1 INNER JOIN district AS T2 ON T1.district_id = T2.district_id LEFT JOIN disp AS T3 ON T1.account_id = T3.account_id LEFT JOIN card AS T4 ON T3.disp_id = T4.disp_id WHERE T2.A3 = 'South Bohemia' AND T4.card_id IS NULL
SELECT A3 FROM district WHERE district_id = ( SELECT district_id FROM account WHERE account_id = ( SELECT account_id FROM loan WHERE status IN ('C', 'D') GROUP BY account_id ORDER BY COUNT(loan_id) DESC LIMIT 1 ) )
SELECT AVG(T2.amount) FROM client AS T1 INNER JOIN loan AS T2 ON T1.client_id = T2.account_id WHERE T1.gender = 'M'
SELECT A2, A3 FROM district ORDER BY A13 DESC LIMIT 1 
SELECT COUNT(account_id) FROM account WHERE district_id = (SELECT district_id FROM district ORDER BY A16 DESC LIMIT 1)
SELECT COUNT(DISTINCT T1.account_id) FROM trans AS T1 INNER JOIN account AS T2 ON T1.account_id = T2.account_id WHERE T1.operation = 'VYBER KARTOU' AND T2.frequency = 'POPLATEK MESICNE' AND T1.balance < 0
SELECT COUNT(DISTINCT loan.loan_id) FROM loan INNER JOIN account ON loan.account_id = account.account_id WHERE loan.amount >= 250000 AND account.frequency = 'POPLATEK MESICNE' AND loan.date BETWEEN '1995-01-01' AND '1997-12-31' AND loan.status = 'A'
SELECT COUNT(account_id) FROM account WHERE account_id IN (SELECT account_id FROM loan WHERE status IN ('C', 'D')) AND district_id = 1
SELECT COUNT(T1.gender) FROM client AS T1 INNER JOIN district AS T2 ON T1.district_id = T2.district_id WHERE T2.A15 = (SELECT MAX(A15) FROM district WHERE A15 < (SELECT MAX(A15) FROM district)) AND T1.gender = 'M'
SELECT COUNT(T1.card_id) FROM card AS T1 INNER JOIN disp AS T2 ON T1.disp_id = T2.disp_id WHERE T1.type = 'gold' AND T2.type = 'disponent'
SELECT COUNT(account_id) FROM account WHERE district_id IN (SELECT district_id FROM district WHERE A2 = 'Pisek')
SELECT DISTINCT T3.A2 FROM trans AS T1 INNER JOIN account AS T2 ON T1.account_id = T2.account_id INNER JOIN district AS T3 ON T2.district_id = T3.district_id WHERE T1.amount > 10000 AND STRFTIME('%Y', T1.date) = '1997'
SELECT T1.account_id FROM `order` AS T1 INNER JOIN account AS T2 ON T1.account_id = T2.account_id INNER JOIN district AS T3 ON T2.district_id = T3.district_id WHERE T1.k_symbol = 'SIPO' AND T3.A3 = 'Pisek'
SELECT T1.account_id FROM disp AS T1 INNER JOIN card AS T2 ON T1.disp_id = T2.disp_id WHERE T2.type IN ('gold', 'junior') GROUP BY T1.account_id HAVING COUNT(DISTINCT T2.type) = 2
SELECT AVG(T1.amount) FROM trans AS T1 INNER JOIN card AS T2 ON T1.account_id = T2.disp_id WHERE T1.operation = 'VYBER KARTOU' AND STRFTIME('%Y', T1.date) = '2021' AND STRFTIME('%m', T1.date) = '01'
SELECT T1.disp_id FROM disp AS T1 INNER JOIN trans AS T2 ON T1.account_id = T2.account_id WHERE T2.operation = 'VYBER KARTOU' AND STRFTIME('%Y', T2.date) = '1998' GROUP BY T1.disp_id HAVING AVG(T2.amount) < (SELECT AVG(amount) FROM trans WHERE operation = 'VYBER KARTOU' AND STRFTIME('%Y', date) = '1998')
SELECT T1.client_id, T1.gender FROM client AS T1 INNER JOIN disp AS T2 ON T1.client_id = T2.client_id INNER JOIN card AS T3 ON T2.disp_id = T3.disp_id INNER JOIN loan AS T4 ON T2.account_id = T4.account_id WHERE T1.gender = 'F' AND T3.type = 'credit'
SELECT COUNT(DISTINCT T1.account_id) FROM account AS T1 INNER JOIN disp AS T2 ON T1.account_id = T2.account_id INNER JOIN client AS T3 ON T2.client_id = T3.client_id INNER JOIN district AS T4 ON T1.district_id = T4.district_id WHERE T3.gender = 'F' AND T4.A3 = 'south Bohemia'
SELECT T1.account_id FROM account AS T1 INNER JOIN district AS T2 ON T1.district_id = T2.district_id INNER JOIN disp AS T3 ON T1.account_id = T3.account_id WHERE T2.A2 = 'Tabor' AND T3.type = 'OWNER'
SELECT DISTINCT T1.type FROM account AS T1 INNER JOIN district AS T2 ON T1.district_id = T2.district_id LEFT JOIN loan AS T3 ON T1.account_id = T3.account_id WHERE T3.account_id IS NULL AND T2.A11 > 8000 AND T2.A11 <= 9000
SELECT COUNT(DISTINCT T1.account_id) FROM account AS T1 INNER JOIN district AS T2 ON T1.district_id = T2.district_id INNER JOIN trans AS T3 ON T1.account_id = T3.account_id WHERE T2.A3 = 'North Bohemia' AND T3.bank = 'AB'
SELECT DISTINCT T2.A2 FROM trans AS T1 INNER JOIN district AS T2 ON T1.account_id = T2.district_id WHERE T1.type = 'VYDAJ'
SELECT T1.A3, AVG(T1.A15) FROM district AS T1 INNER JOIN account AS T2 ON T1.district_id = T2.district_id WHERE T1.A15 > 4000 AND YEAR(T2.date) >= 1997 GROUP BY T1.A3 
SELECT COUNT(T1.card_id) FROM card AS T1 INNER JOIN disp AS T2 ON T1.disp_id = T2.disp_id INNER JOIN loan AS T3 ON T2.account_id = T3.account_id WHERE T1.type = 'classic' AND T2.type = 'OWNER'
SELECT COUNT(T1.client_id) FROM client AS T1 INNER JOIN district AS T2 ON T1.district_id = T2.district_id WHERE T2.A2 = 'Hl.m. Praha' AND T1.gender = 'M'
SELECT CAST(SUM(CASE WHEN type = 'Gold' AND STRFTIME('%Y', issued) < '1998' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(*) FROM card
SELECT T3.gender, T3.birth_date FROM loan AS T1 INNER JOIN disp AS T2 ON T1.account_id = T2.account_id INNER JOIN client AS T3 ON T2.client_id = T3.client_id WHERE T2.type = 'OWNER' ORDER BY T1.amount DESC LIMIT 1 
SELECT A15 FROM district WHERE district_id = (SELECT district_id FROM account WHERE account_id = 532)
SELECT T1.district_id FROM account AS T1 INNER JOIN `order` AS T2 ON T1.account_id = T2.account_id WHERE T2.order_id = 33333
SELECT T2.trans_id, T2.date, T2.amount FROM disp AS T1 INNER JOIN trans AS T2 ON T1.account_id = T2.account_id WHERE T1.client_id = 3356 AND T2.operation = 'VYBER'
SELECT COUNT(*) FROM account AS T1 INNER JOIN loan AS T2 ON T1.account_id = T2.account_id WHERE T1.frequency = 'POPLATEK TYDNE' AND T2.amount < 200000
SELECT T2.type FROM disp AS T1 INNER JOIN card AS T2 ON T1.disp_id = T2.disp_id WHERE T1.client_id = 13539
SELECT A3 FROM client AS T1 INNER JOIN district AS T2 ON T1.district_id = T2.district_id WHERE T1.client_id = 3541
SELECT T.district_id FROM ( SELECT T1.district_id, COUNT(DISTINCT T2.account_id) FROM account AS T1 INNER JOIN loan AS T2 ON T1.account_id = T2.account_id WHERE T2.status = 'A' GROUP BY T1.district_id ORDER BY COUNT(DISTINCT T2.account_id) DESC LIMIT 1 ) t
SELECT T1.client_id FROM client AS T1 INNER JOIN disp AS T2 ON T1.client_id = T2.client_id INNER JOIN `order` AS T3 ON T2.account_id = T3.account_id WHERE T3.order_id = 32423
SELECT T1.trans_id, T1.account_id, T1.date, T1.type, T1.operation, T1.amount, T1.balance, T1.k_symbol, T1.bank, T1.account FROM trans AS T1 INNER JOIN account AS T2 ON T1.account_id = T2.account_id WHERE T2.district_id = 5
SELECT COUNT(account_id) FROM account INNER JOIN district ON account.district_id = district.district_id WHERE district.A3 = 'Jesenik'
SELECT T1.client_id FROM disp AS T1 INNER JOIN card AS T2 ON T1.disp_id = T2.disp_id WHERE T2.type = 'junior' AND T2.issued >= '1997-01-01'
SELECT CAST(SUM(IIF(C.gender = 'F', 1, 0)) AS REAL) * 100 / COUNT(*) FROM client AS C INNER JOIN disp AS D ON C.client_id = D.client_id INNER JOIN account AS A ON D.account_id = A.account_id INNER JOIN district AS DI ON A.district_id = DI.district_id WHERE DI.A11 > 10000
SELECT ((SELECT SUM(T2.amount) FROM client AS T1 INNER JOIN loan AS T2 ON T1.client_id = T2.account_id WHERE T1.gender = 'M' AND strftime('%Y', T2.date) = '1997') - (SELECT SUM(T2.amount) FROM client AS T1 INNER JOIN loan AS T2 ON T1.client_id = T2.account_id WHERE T1.gender = 'M' AND strftime('%Y', T2.date) = '1996')) * 100.0 / (SELECT SUM(T2.amount) FROM client AS T1 INNER JOIN loan AS T2 ON T1.client_id = T2.account_id WHERE T1.gender = 'M' AND strftime('%Y', T2.date) = '1996') AS 'Growth Rate'
SELECT COUNT(trans_id) FROM trans WHERE operation = 'VYBER KARTOU' AND STRFTIME('%Y', date) > '1995'
SELECT (SELECT A16 FROM district WHERE A3 = 'North Bohemia' AND A2 = '1996') - (SELECT A16 FROM district WHERE A3 = 'East Bohemia' AND A2 = '1996') AS difference_in_crimes 
SELECT type, COUNT(*) FROM disp WHERE account_id BETWEEN 1 AND 10 GROUP BY type
SELECT T1.frequency, T2.k_symbol FROM account AS T1 INNER JOIN trans AS T2 ON T1.account_id = T2.account_id WHERE T1.account_id = 3 AND T2.amount = 3539
SELECT birth_date FROM client AS T1 INNER JOIN disp AS T2 ON T1.client_id = T2.client_id WHERE T2.account_id = 130
SELECT COUNT(*) FROM account AS T1 INNER JOIN disp AS T2 ON T1.account_id = T2.account_id WHERE T2.type = 'OWNER' AND T1.frequency = 'POPLATEK PO OBRATU'
SELECT T1.amount AS 'Debt Amount', T2.status AS 'Payment Status' FROM loan AS T1 INNER JOIN disp AS T2 ON T1.account_id = T2.account_id INNER JOIN client AS T3 ON T2.client_id = T3.client_id WHERE T3.client_id = 992 
SELECT T1.balance, T3.gender FROM trans AS T1 INNER JOIN disp AS T2 ON T1.account_id = T2.account_id INNER JOIN client AS T3 ON T2.client_id = T3.client_id WHERE T1.trans_id = 851 AND T3.client_id = 4 
SELECT T2.type FROM client AS T1 INNER JOIN disp AS T2 ON T1.client_id = T2.client_id INNER JOIN card AS T3 ON T2.disp_id = T3.disp_id WHERE T1.client_id = 9
SELECT SUM(t.amount) FROM trans t INNER JOIN disp d ON t.account_id = d.account_id WHERE d.client_id = '617' AND YEAR(t.date) = 1998
SELECT T1.client_id, T1.birth_date, T2.A3 FROM client AS T1 INNER JOIN district AS T2 ON T1.district_id = T2.district_id WHERE T1.birth_date BETWEEN '1983-01-01' AND '1987-12-31' AND T2.A3 = 'East Bohemia'
SELECT T1.client_id FROM client AS T1 INNER JOIN disp AS T2 ON T1.client_id = T2.client_id INNER JOIN loan AS T3 ON T2.account_id = T3.account_id WHERE T1.gender = 'F' ORDER BY T3.amount DESC LIMIT 3 
SELECT COUNT(T1.client_id) FROM client AS T1 INNER JOIN disp AS T2 ON T1.client_id = T2.client_id INNER JOIN trans AS T3 ON T2.account_id = T3.account_id WHERE T1.gender = 'M' AND T1.birth_date BETWEEN '1974-01-01' AND '1976-12-31' AND T3.k_symbol = 'SIPO' AND T3.amount > 4000
SELECT COUNT(T1.account_id) FROM account AS T1 INNER JOIN district AS T2 ON T1.district_id = T2.district_id WHERE T2.A3 = 'Beroun' AND STRFTIME('%Y', T1.date) > '1996'
SELECT COUNT(*) FROM client AS T1 INNER JOIN disp AS T2 ON T1.client_id = T2.client_id INNER JOIN card AS T3 ON T2.disp_id = T3.disp_id WHERE T1.gender = 'F' AND T3.type = 'junior'
SELECT CAST(SUM(CASE WHEN T1.gender = 'F' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.client_id) FROM client AS T1 INNER JOIN disp AS T2 ON T1.client_id = T2.client_id INNER JOIN account AS T3 ON T2.account_id = T3.account_id INNER JOIN district AS T4 ON T3.district_id = T4.district_id WHERE T4.A3 = 'Prague'
SELECT CAST(SUM(CASE WHEN T1.gender = 'M' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.client_id) FROM client AS T1 INNER JOIN account AS T2 ON T1.client_id = T2.account_id WHERE T2.frequency = 'POPLATEK TYDNE'
SELECT COUNT(T2.client_id) FROM account AS T1 INNER JOIN disp AS T2 ON T1.account_id = T2.account_id WHERE T1.frequency = 'POPLATEK TYDNE' AND T2.type = 'USER'
SELECT T1.account_id FROM loan AS T1 INNER JOIN account AS T2 ON T1.account_id = T2.account_id WHERE T1.duration > 24 AND T2.date < '1997-01-01' ORDER BY T1.amount ASC LIMIT 1
SELECT T1.account_id FROM account AS T1 INNER JOIN disp AS T2 ON T1.account_id = T2.account_id INNER JOIN client AS T3 ON T2.client_id = T3.client_id INNER JOIN district AS T4 ON T3.district_id = T4.district_id WHERE T3.gender = 'F' GROUP BY T1.account_id, T3.birth_date, T4.A11 HAVING T3.birth_date = MAX(T3.birth_date) AND T4.A11 = MIN(T4.A11)
SELECT COUNT(DISTINCT T1.client_id) FROM client AS T1 INNER JOIN district AS T2 ON T1.district_id = T2.district_id WHERE T2.A3 = 'east Bohemia' AND strftime('%Y', T1.birth_date) = '1920'
SELECT COUNT(account_id) FROM loan INNER JOIN account ON loan.account_id = account.account_id WHERE loan.duration = 24 AND account.frequency = 'POPLATEK TYDNE'
SELECT AVG(T1.amount) FROM loan AS T1 INNER JOIN account AS T2 ON T1.account_id = T2.account_id INNER JOIN trans AS T3 ON T2.account_id = T3.account_id WHERE T1.status IN ('C', 'D') AND T3.k_symbol = 'POPLATEK PO OBRATU'
SELECT T1.client_id, T1.district_id FROM client AS T1 INNER JOIN disp AS T2 ON T1.client_id = T2.client_id WHERE T2.type = 'OWNER'
SELECT T1.client_id, DATE_PART('year', AGE(T1.birth_date)) AS age FROM client AS T1 INNER JOIN disp AS T2 ON T1.client_id = T2.client_id INNER JOIN card AS T3 ON T2.disp_id = T3.disp_id INNER JOIN loan AS T4 ON T2.account_id = T4.account_id WHERE T3.type = 'gold'
SELECT bond_type FROM bond GROUP BY bond_type ORDER BY COUNT(bond_type) DESC LIMIT 1
SELECT COUNT(DISTINCT T1.molecule_id) FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.molecule_id = T2.molecule_id WHERE T2.label = '-' AND T1.element = 'cl'
SELECT AVG(CASE WHEN T1.element = 'o' THEN 1 ELSE 0 END) FROM atom AS T1 INNER JOIN connected AS T2 ON T1.atom_id = T2.atom_id INNER JOIN bond AS T3 ON T2.bond_id = T3.bond_id WHERE T3.bond_type = '-'
SELECT CAST(COUNT(CASE WHEN T3.bond_type = '-' THEN T1.atom_id ELSE NULL END) AS REAL) / COUNT(T1.atom_id) FROM atom AS T1 INNER JOIN connected AS T2 ON T1.atom_id = T2.atom_id INNER JOIN bond AS T3 ON T2.bond_id = T3.bond_id INNER JOIN molecule AS T4 ON T1.molecule_id = T4.molecule_id WHERE T4.label = '+'
SELECT COUNT(DISTINCT T1.atom_id) FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.molecule_id = T2.molecule_id WHERE T1.element = 'na' AND T2.label = '-'
SELECT molecule_id FROM molecule WHERE label = '+' AND molecule_id IN (SELECT molecule_id FROM bond WHERE bond_type = '#')
SELECT CAST(SUM(CASE WHEN T1.element = 'c' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.atom_id) FROM atom AS T1 INNER JOIN connected AS T2 ON T1.atom_id = T2.atom_id INNER JOIN bond AS T3 ON T2.bond_id = T3.bond_id WHERE T3.bond_type = '='
SELECT COUNT(bond_id) FROM bond WHERE bond_type = '#'
SELECT COUNT(atom_id) FROM atom WHERE element != 'br'
SELECT COUNT(*) FROM molecule WHERE molecule_id BETWEEN 'TR000' AND 'TR099' AND label = '+'
SELECT DISTINCT T2.molecule_id FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.molecule_id = T2.molecule_id WHERE T1.element = 'si'
SELECT T1.element FROM atom AS T1 INNER JOIN connected AS T2 ON T1.atom_id = T2.atom_id WHERE T2.bond_id = 'TR004_8_9'
SELECT DISTINCT atom.element FROM atom INNER JOIN connected ON atom.atom_id = connected.atom_id INNER JOIN bond ON connected.bond_id = bond.bond_id WHERE bond.bond_type = 'double'
SELECT T2.label FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.molecule_id = T2.molecule_id WHERE T1.element = 'h' GROUP BY T2.label ORDER BY COUNT(T2.label) DESC LIMIT 1
SELECT T2.bond_type FROM atom AS T1 INNER JOIN connected AS T3 ON T1.atom_id = T3.atom_id INNER JOIN bond AS T2 ON T3.bond_id = T2.bond_id WHERE T1.element = 'te'
SELECT T1.atom_id, T1.atom_id2 FROM connected AS T1 INNER JOIN bond AS T2 ON T1.bond_id = T2.bond_id WHERE T2.bond_type = '-'
SELECT T1.atom_id, T1.atom_id2 FROM connected AS T1 INNER JOIN atom AS T2 ON T1.atom_id = T2.atom_id INNER JOIN molecule AS T3 ON T2.molecule_id = T3.molecule_id WHERE T3.label = '-'
SELECT T2.element FROM molecule AS T1 INNER JOIN atom AS T2 ON T1.molecule_id = T2.molecule_id WHERE T1.label = '-' GROUP BY T2.element ORDER BY COUNT(T2.element) ASC LIMIT 1
SELECT T2.bond_type FROM connected AS T1 INNER JOIN bond AS T2 ON T1.bond_id = T2.bond_id WHERE (T1.atom_id = 'TR004_8' AND T1.atom_id2 = 'TR004_20') OR (T1.atom_id = 'TR004_20' AND T1.atom_id2 = 'TR004_8')
SELECT label FROM molecule WHERE molecule_id NOT IN (SELECT molecule_id FROM atom WHERE element = 'sn')
SELECT COUNT(DISTINCT a.atom_id) FROM atom a JOIN connected c ON a.atom_id = c.atom_id OR a.atom_id = c.atom_id2 JOIN bond b ON c.bond_id = b.bond_id WHERE a.element IN ('i', 's') AND b.bond_type = '-'
SELECT T1.atom_id, T1.atom_id2 FROM connected AS T1 INNER JOIN bond AS T2 ON T1.bond_id = T2.bond_id WHERE T2.bond_type = '#'
SELECT T3.atom_id2 FROM atom AS T1 INNER JOIN connected AS T2 ON T1.atom_id = T2.atom_id INNER JOIN atom AS T3 ON T2.atom_id2 = T3.atom_id WHERE T1.molecule_id = 'TR181'
SELECT CAST(SUM(CASE WHEN T2.element != 'F' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.molecule_id) FROM molecule AS T1 INNER JOIN atom AS T2 ON T1.molecule_id = T2.molecule_id WHERE T1.label = '+'
SELECT CAST(SUM(CASE WHEN T2.bond_type = '#' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T2.bond_id) FROM molecule AS T1 INNER JOIN bond AS T2 ON T1.molecule_id = T2.molecule_id WHERE T1.label = '+'
SELECT CASE WHEN element = 'cl' THEN 'Chlorine' WHEN element = 'c' THEN 'Carbon' WHEN element = 'h' THEN 'Hydrogen' WHEN element = 'o' THEN 'Oxygen' WHEN element = 's' THEN 'Sulfur' WHEN element = 'n' THEN 'Nitrogen' WHEN element = 'p' THEN 'Phosphorus' WHEN element = 'na' THEN 'Sodium' WHEN element = 'br' THEN 'Bromine' WHEN element = 'f' THEN 'Fluorine' WHEN element = 'i' THEN 'Iodine' WHEN element = 'sn' THEN 'Tin' WHEN element = 'pb' THEN 'Lead' WHEN element = 'te' THEN 'Tellurium' WHEN element = 'ca' THEN 'Calcium' END AS 'Element' FROM atom WHERE molecule_id
SELECT T1.atom_id, T1.atom_id2 FROM connected AS T1 INNER JOIN atom AS T2 ON T1.atom_id = T2.atom_id INNER JOIN bond AS T3 ON T1.bond_id = T3.bond_id INNER JOIN molecule AS T4 ON T2.molecule_id = T4.molecule_id WHERE T4.molecule_id = 'TR001' AND T3.bond_id = 'TR001_2_6'
SELECT SUM(CASE WHEN label = '+' THEN 1 ELSE 0 END) - SUM(CASE WHEN label = '-' THEN 1 ELSE 0 END) AS DIFFERENCE FROM molecule
SELECT atom_id, atom_id2 FROM connected WHERE bond_id = 'TR_000_2_5'
SELECT bond_id FROM connected WHERE atom_id2 = 'TR000_2'
SELECT T1.label FROM molecule AS T1 INNER JOIN bond AS T2 ON T1.molecule_id = T2.molecule_id WHERE T2.bond_type = ' = ' GROUP BY T1.label ORDER BY T1.label ASC LIMIT 5
SELECT CAST(SUM(CASE WHEN T2.bond_type = ' = ' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T2.bond_id) FROM molecule AS T1 INNER JOIN bond AS T2 ON T1.molecule_id = T2.molecule_id WHERE T1.molecule_id = 'TR008'
SELECT CAST(SUM(CASE WHEN label = '+' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(molecule_id) FROM molecule
SELECT CAST(SUM(CASE WHEN element = 'h' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(atom_id) AS percentage FROM atom WHERE molecule_id = 'TR206'
SELECT T2.bond_type FROM molecule AS T1 INNER JOIN bond AS T2 ON T1.molecule_id = T2.molecule_id WHERE T1.molecule_id = 'TR000'
SELECT T1.element, T2.label FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.molecule_id = T2.molecule_id WHERE T2.molecule_id = 'TR060'
SELECT T1.bond_type, T3.label FROM bond AS T1 INNER JOIN connected AS T2 ON T1.bond_id = T2.bond_id INNER JOIN molecule AS T3 ON T1.molecule_id = T3.molecule_id WHERE T3.molecule_id = 'TR018' GROUP BY T1.bond_type ORDER BY COUNT(T1.bond_type) DESC LIMIT 1
SELECT T1.label FROM molecule AS T1 INNER JOIN bond AS T2 ON T1.molecule_id = T2.molecule_id INNER JOIN connected AS T3 ON T2.bond_id = T3.bond_id WHERE T2.bond_type = 'single' AND T1.label != 'carcinogenic' GROUP BY T1.label ORDER BY T1.label ASC LIMIT 3
SELECT T1.bond_type FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.molecule_id = T2.molecule_id WHERE T2.molecule_id = 'TR006' ORDER BY T1.bond_type ASC LIMIT 2
SELECT COUNT(bond_id) FROM connected WHERE (atom_id = 'TR009_12' OR atom_id2 = 'TR009_12') AND bond_id LIKE 'TR009_%'
SELECT COUNT(DISTINCT T1.molecule_id) FROM molecule AS T1 INNER JOIN atom AS T2 ON T1.molecule_id = T2.molecule_id WHERE T1.label = '+' AND T2.element = 'br'
SELECT T1.bond_type, T2.atom_id, T2.atom_id2 FROM bond AS T1 INNER JOIN connected AS T2 ON T1.bond_id = T2.bond_id WHERE T1.bond_id = 'TR001_6_9'
SELECT T2.label, CASE WHEN T2.label = '+' THEN 'Carcinogenic' ELSE 'Not Carcinogenic' END AS Carcinogenic FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.molecule_id = T2.molecule_id WHERE T1.atom_id = 'TR001_10'
SELECT COUNT(DISTINCT T1.molecule_id) FROM bond AS T1 WHERE T1.bond_type = '#'
SELECT COUNT(bond_id) FROM connected WHERE atom_id LIKE 'TR%_19' OR atom_id2 LIKE 'TR%_19'
SELECT element FROM atom WHERE molecule_id = 'TR004'
SELECT COUNT(molecule_id) FROM molecule WHERE label = '-'
SELECT DISTINCT T2.molecule_id, T2.label FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.molecule_id = T2.molecule_id WHERE SUBSTRING(T1.atom_id, 7, 2) BETWEEN 21 AND 25 AND T2.label = '+'
SELECT T3.bond_id FROM connected AS T3 INNER JOIN atom AS T1 ON T1.atom_id = T3.atom_id INNER JOIN atom AS T2 ON T2.atom_id = T3.atom_id2 WHERE (T1.element = 'P' AND T2.element = 'N') OR (T1.element = 'N' AND T2.element = 'P')
SELECT CASE WHEN T1.label = '+' THEN 'Yes' ELSE 'No' END AS Is_Carcinogenic FROM molecule AS T1 INNER JOIN ( SELECT molecule_id, COUNT(bond_id) AS double_bonds FROM bond WHERE bond_type = '=' GROUP BY molecule_id ORDER BY double_bonds DESC LIMIT 1 ) AS T2 ON T1.molecule_id = T2.molecule_id
SELECT CAST(COUNT(T2.bond_id) AS REAL) / COUNT(T1.atom_id) FROM atom AS T1 INNER JOIN connected AS T2 ON T1.atom_id = T2.atom_id WHERE T1.element = 'I'
SELECT T2.bond_type, T2.bond_id FROM connected AS T1 INNER JOIN bond AS T2 ON T1.bond_id = T2.bond_id WHERE SUBSTR(T1.atom_id, 7, 2) + 0 = 45
SELECT element FROM atom WHERE atom_id NOT IN (SELECT atom_id FROM connected)
SELECT T1.atom_id FROM atom AS T1 INNER JOIN connected AS T2 ON T1.atom_id = T2.atom_id INNER JOIN bond AS T3 ON T2.bond_id = T3.bond_id WHERE T3.bond_type = '#' AND T1.molecule_id = 'TR447'
SELECT T1.element FROM atom AS T1 INNER JOIN connected AS T2 ON T1.atom_id = T2.atom_id WHERE T2.bond_id = 'TR144_8_19'
SELECT T1.label FROM molecule AS T1 INNER JOIN bond AS T2 ON T1.molecule_id = T2.molecule_id WHERE T1.label = '+' AND T2.bond_type = '=' GROUP BY T1.label ORDER BY COUNT(T2.bond_type) DESC LIMIT 1
SELECT element FROM atom WHERE molecule_id IN (SELECT molecule_id FROM molecule WHERE label = '+') GROUP BY element ORDER BY COUNT(*) ASC LIMIT 1
SELECT T2.atom_id FROM connected AS T1 INNER JOIN atom AS T2 ON T1.atom_id2 = T2.atom_id WHERE T1.atom_id IN (SELECT atom_id FROM atom WHERE element = 'pb')
SELECT T1.element FROM atom AS T1 INNER JOIN connected AS T2 ON T1.atom_id = T2.atom_id INNER JOIN bond AS T3 ON T2.bond_id = T3.bond_id WHERE T3.bond_type = '#'
SELECT CAST(COUNT(T1.bond_id) AS REAL) * 100 / (SELECT COUNT(T2.atom_id) FROM (SELECT atom_id, COUNT(atom_id) AS atom_count FROM connected GROUP BY atom_id ORDER BY atom_count DESC LIMIT 1) AS T2) FROM bond AS T1 INNER JOIN connected AS T2 ON T1.bond_id = T2.bond_id
SELECT CAST(SUM(CASE WHEN T1.label = '+' THEN 1 ELSE 0 END) AS REAL) / COUNT(T2.bond_id) FROM molecule AS T1 INNER JOIN bond AS T2 ON T1.molecule_id = T2.molecule_id WHERE T2.bond_type = '-'
SELECT COUNT(atom_id) FROM atom WHERE element IN ('c', 'h')
SELECT T2.atom_id2 FROM atom AS T1 INNER JOIN connected AS T2 ON T1.atom_id = T2.atom_id WHERE T1.element = 's'
SELECT DISTINCT T3.bond_type FROM atom AS T1 INNER JOIN connected AS T2 ON T1.atom_id = T2.atom_id INNER JOIN bond AS T3 ON T2.bond_id = T3.bond_id WHERE T1.element = 'sn'
SELECT COUNT(DISTINCT T1.element) FROM atom AS T1 INNER JOIN connected AS T2 ON T1.atom_id = T2.atom_id INNER JOIN bond AS T3 ON T2.bond_id = T3.bond_id WHERE T3.bond_type = '-'
SELECT COUNT(DISTINCT T1.atom_id) FROM atom AS T1 INNER JOIN connected AS T2 ON T1.atom_id = T2.atom_id INNER JOIN bond AS T3 ON T2.bond_id = T3.bond_id WHERE T3.bond_type = '#' AND T1.element IN ('p', 'br')
SELECT bond_id FROM bond WHERE molecule_id IN (SELECT molecule_id FROM molecule WHERE label = '+')
SELECT DISTINCT T1.molecule_id FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.molecule_id = T2.molecule_id WHERE T1.bond_type = '-' AND T2.label = '-'
SELECT CAST(SUM(CASE WHEN T1.element = 'cl' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.atom_id) FROM atom AS T1 INNER JOIN connected AS T2 ON T1.atom_id = T2.atom_id INNER JOIN bond AS T3 ON T2.bond_id = T3.bond_id WHERE T3.bond_type = '-'
SELECT label FROM molecule WHERE molecule_id IN ('TR000', 'TR001', 'TR002')
SELECT molecule_id FROM molecule WHERE label = '-'
SELECT COUNT(T1.molecule_id) FROM molecule AS T1 WHERE T1.label = '+' AND T1.molecule_id BETWEEN 'TR000' AND 'TR030'
SELECT T2.bond_type FROM molecule AS T1 INNER JOIN bond AS T2 ON T1.molecule_id = T2.molecule_id WHERE T1.molecule_id BETWEEN 'TR000' AND 'TR050'
SELECT T1.element FROM atom AS T1 INNER JOIN connected AS T2 ON T1.atom_id = T2.atom_id WHERE T2.bond_id = 'TR001_10_11'
SELECT COUNT(DISTINCT bond_id) FROM connected WHERE atom_id IN (SELECT atom_id FROM atom WHERE element = 'I')
SELECT CASE WHEN SUM(CASE WHEN T2.label = '+' THEN 1 ELSE 0 END) > SUM(CASE WHEN T2.label = '-' THEN 1 ELSE 0 END) THEN 'Carcinogenic' ELSE 'Non-Carcinogenic' END AS Result FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.molecule_id = T2.molecule_id WHERE T1.element = 'Ca'
SELECT CASE WHEN COUNT(DISTINCT T1.element) = 2 THEN 'yes' ELSE 'no' END AS yn FROM atom AS T1 INNER JOIN connected AS T2 ON T1.atom_id = T2.atom_id WHERE T2.bond_id = 'TR001_1_8' AND T1.element IN ('cl', 'c')
SELECT molecule_id FROM molecule AS m INNER JOIN atom AS a ON m.molecule_id = a.molecule_id INNER JOIN connected AS c ON a.atom_id = c.atom_id INNER JOIN bond AS b ON c.bond_id = b.bond_id WHERE a.element = 'c' AND b.bond_type = '#' AND m.label = '-' LIMIT 2
SELECT CAST(SUM(CASE WHEN T1.element = 'cl' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T2.molecule_id) FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.molecule_id = T2.molecule_id WHERE T2.label = '+'
SELECT T1.element FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.molecule_id = T2.molecule_id WHERE T2.molecule_id = 'TR001'
SELECT molecule_id FROM bond WHERE bond_type = ' = '
SELECT T1.atom_id, T2.atom_id2 FROM connected AS T1 INNER JOIN bond AS T2 ON T1.bond_id = T2.bond_id WHERE T2.bond_type = '#'
SELECT T1.element FROM atom AS T1 INNER JOIN connected AS T2 ON T1.atom_id = T2.atom_id WHERE T2.bond_id = 'TR005_16_26' AND T1.element IN ('cl', 'c', 'h', 'o', 's', 'n', 'p', 'na', 'br', 'f', 'i', 'sn', 'pb', 'te', 'ca')
SELECT COUNT(DISTINCT T2.molecule_id) FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.molecule_id = T2.molecule_id WHERE T1.bond_type = '-' AND T2.label = '-'
SELECT T1.label FROM molecule AS T1 INNER JOIN bond AS T2 ON T1.molecule_id = T2.molecule_id WHERE T2.bond_id = 'TR001_10_11'
SELECT T1.bond_id, T2.label AS 'Carcinogenic' FROM bond AS T1 INNER JOIN molecule AS T2 ON T1.molecule_id = T2.molecule_id WHERE T1.bond_type = '#'
SELECT element, COUNT(*) AS count FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.molecule_id = T2.molecule_id WHERE T2.label = '+' AND substr(T1.atom_id, 7, 1) = '4' GROUP BY T1.element
SELECT CAST(SUM(CASE WHEN element = 'H' THEN 1 ELSE 0 END) AS REAL) / COUNT(*), label FROM atom INNER JOIN molecule ON atom.molecule_id = molecule.molecule_id WHERE atom.molecule_id = 'TR006'
SELECT CASE WHEN T4.label = '+' THEN 'Yes' ELSE 'No' END AS Is_Carcinogenic FROM atom AS T1 INNER JOIN connected AS T2 ON T1.atom_id = T2.atom_id INNER JOIN bond AS T3 ON T2.bond_id = T3.bond_id INNER JOIN molecule AS T4 ON T1.molecule_id = T4.molecule_id WHERE T1.element = 'ca'
SELECT DISTINCT T3.bond_type FROM atom AS T1 INNER JOIN connected AS T2 ON T1.atom_id = T2.atom_id INNER JOIN bond AS T3 ON T2.bond_id = T3.bond_id WHERE T1.element = 'te'
SELECT T1.element FROM atom AS T1 INNER JOIN connected AS T2 ON T1.atom_id = T2.atom_id WHERE T2.bond_id = 'TR001_10_11'
SELECT CAST(SUM(CASE WHEN T2.bond_type = '#' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(*) FROM molecule AS T1 INNER JOIN bond AS T2 ON T1.molecule_id = T2.molecule_id
SELECT CAST(SUM(CASE WHEN T2.bond_type = ' = ' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T2.bond_id) FROM molecule AS T1 INNER JOIN bond AS T2 ON T1.molecule_id = T2.molecule_id WHERE T1.molecule_id = 'TR047'
SELECT CASE WHEN T1.label = '+' THEN 'Yes' ELSE 'No' END AS Is_Carcinogenic FROM molecule AS T1 INNER JOIN atom AS T2 ON T1.molecule_id = T2.molecule_id WHERE T2.atom_id = 'TR001_1'
SELECT CASE WHEN label = '+' THEN 'Yes' ELSE 'No' END AS Is_Carcinogenic FROM molecule WHERE molecule_id = 'TR151'
SELECT T1.element FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.molecule_id = T2.molecule_id WHERE T2.label = 'TR151' AND T1.element IN ('cl', 'br', 'f', 'i', 'sn', 'pb', 'te')
SELECT COUNT(molecule_id) FROM molecule WHERE label = '+'
SELECT atom_id FROM atom WHERE element = 'c' AND substr(molecule_id, 3, 3) BETWEEN 10 AND 50
SELECT COUNT(atom_id) FROM atom WHERE molecule_id IN (SELECT molecule_id FROM molecule WHERE label = '+')
SELECT bond_id FROM bond AS b INNER JOIN molecule AS m ON b.molecule_id = m.molecule_id WHERE m.label = '+' AND b.bond_type = '='
SELECT COUNT(atom_id) FROM atom WHERE molecule_id IN (SELECT molecule_id FROM molecule WHERE label = '+') AND element = 'H'
SELECT T1.molecule_id FROM bond AS T1 INNER JOIN connected AS T2 ON T1.bond_id = T2.bond_id INNER JOIN atom AS T3 ON T2.atom_id = T3.atom_id WHERE T1.bond_id = 'TR00_1_2' AND T3.atom_id = 'TR00_1'
SELECT T1.atom_id FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.molecule_id = T2.molecule_id WHERE T1.element = 'C' AND T2.label = '-'
SELECT CAST(SUM(CASE WHEN T1.label = '+' AND T2.element = 'h' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.molecule_id) FROM molecule AS T1 INNER JOIN atom AS T2 ON T1.molecule_id = T2.molecule_id
SELECT CASE WHEN label = '+' THEN 'Yes' ELSE 'No' END AS Is_Carcinogenic FROM molecule WHERE molecule_id = 'TR124'
SELECT T1.atom_id, T1.element FROM atom AS T1 WHERE T1.molecule_id = 'TR186'
SELECT T2.bond_type FROM connected AS T1 INNER JOIN bond AS T2 ON T1.bond_id = T2.bond_id WHERE T1.atom_id = 'TR007_4_19' OR T1.atom_id2 = 'TR007_4_19'
SELECT T1.element FROM atom AS T1 INNER JOIN connected AS T2 ON T1.atom_id = T2.atom_id WHERE T2.bond_id = 'TR001_2_4'
SELECT COUNT(bond_id) AS DoubleBonds, CASE WHEN label = '+' THEN 'Yes' ELSE 'No' END AS IsCarcinogenic FROM molecule LEFT JOIN bond ON molecule.molecule_id = bond.molecule_id WHERE molecule.molecule_id = 'TR006' AND bond.bond_type = ' = '
SELECT T1.label, T2.element FROM molecule AS T1 INNER JOIN atom AS T2 ON T1.molecule_id = T2.molecule_id WHERE T1.label = '+'
SELECT T1.bond_id, T2.atom_id, T3.atom_id2 FROM bond AS T1 INNER JOIN connected AS T2 ON T1.bond_id = T2.bond_id INNER JOIN connected AS T3 ON T1.bond_id = T3.bond_id WHERE T1.bond_type = '-'
SELECT T3.label, T1.element FROM atom AS T1 INNER JOIN connected AS T2 ON T1.atom_id = T2.atom_id INNER JOIN molecule AS T3 ON T1.molecule_id = T3.molecule_id INNER JOIN bond AS T4 ON T2.bond_id = T4.bond_id WHERE T4.bond_type = '#' GROUP BY T3.label, T1.element
SELECT T1.element FROM atom AS T1 INNER JOIN connected AS T2 ON T1.atom_id = T2.atom_id WHERE T2.bond_id = 'TR000_2_3'
SELECT COUNT(bond_id) FROM bond WHERE molecule_id IN (SELECT molecule_id FROM atom WHERE element = 'cl')
SELECT T1.atom_id, COUNT(T3.bond_type) FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.molecule_id = T2.molecule_id INNER JOIN bond AS T3 ON T2.molecule_id = T3.molecule_id WHERE T2.label = 'TR346' GROUP BY T1.atom_id
SELECT COUNT(DISTINCT T1.molecule_id) AS TotalMolecules, COUNT(DISTINCT T2.molecule_id) AS CarcinogenicMolecules FROM bond AS T1 LEFT JOIN molecule AS T2 ON T1.molecule_id = T2.molecule_id AND T2.label = '+' WHERE T1.bond_type = '='
SELECT COUNT(DISTINCT m.molecule_id) FROM molecule m LEFT JOIN atom a ON m.molecule_id = a.molecule_id LEFT JOIN connected c ON a.atom_id = c.atom_id LEFT JOIN bond b ON c.bond_id = b.bond_id WHERE a.element != 's' AND b.bond_type != ' = '
SELECT T3.label FROM bond AS T1 INNER JOIN connected AS T2 ON T1.bond_id = T2.bond_id INNER JOIN molecule AS T3 ON T1.molecule_id = T3.molecule_id WHERE T1.bond_id = 'TR001_2_4' AND T3.label = '+'
SELECT COUNT(atom_id) FROM atom WHERE molecule_id = 'TR005'
SELECT COUNT(bond_id) FROM bond WHERE bond_type = '-'
SELECT T2.label FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.molecule_id = T2.molecule_id WHERE T1.element = 'cl' AND T2.label = '+'
SELECT T2.label FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.molecule_id = T2.molecule_id WHERE T1.element = 'C' AND T2.label = '-'
SELECT CAST(SUM(CASE WHEN T1.label = '+' AND T2.element = 'Cl' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.molecule_id) FROM molecule AS T1 INNER JOIN atom AS T2 ON T1.molecule_id = T2.molecule_id
SELECT molecule_id FROM bond WHERE bond_id = 'TR001_1_7'
SELECT COUNT(DISTINCT T1.element) FROM atom AS T1 INNER JOIN connected AS T2 ON T1.atom_id = T2.atom_id WHERE T2.bond_id = 'TR001_3_4'
SELECT T2.bond_type FROM connected AS T1 INNER JOIN bond AS T2 ON T1.bond_id = T2.bond_id WHERE T1.atom_id = 'TR000_1' AND T1.atom_id2 = 'TR000_2'
SELECT T3.label FROM atom AS T1 INNER JOIN connected AS T2 ON T1.atom_id = T2.atom_id INNER JOIN molecule AS T3 ON T1.molecule_id = T3.molecule_id WHERE T1.atom_id = 'TR000_2' AND T2.atom_id2 = 'TR000_4'
SELECT element FROM atom WHERE atom_id = 'TR000_1'
SELECT CASE WHEN label = '+' THEN 'Yes' WHEN label = '-' THEN 'No' ELSE 'Unknown' END AS Is_Carcinogenic FROM molecule WHERE molecule_id = 'TR000'
SELECT CAST(SUM(CASE WHEN T2.bond_type = '-' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.atom_id) FROM atom AS T1 INNER JOIN connected AS T2 ON T1.atom_id = T2.atom_id INNER JOIN bond AS T3 ON T2.bond_id = T3.bond_id
SELECT COUNT(DISTINCT T1.molecule_id) FROM molecule AS T1 INNER JOIN atom AS T2 ON T1.molecule_id = T2.molecule_id WHERE T1.label = '+' AND T2.element = 'n'
SELECT T3.label FROM molecule AS T3 INNER JOIN atom AS T1 ON T3.molecule_id = T1.molecule_id INNER JOIN connected AS T2 ON T1.atom_id = T2.atom_id INNER JOIN bond AS T4 ON T2.bond_id = T4.bond_id WHERE T1.element = 'S' AND T4.bond_type = '='
SELECT T1.molecule_id, T1.label FROM molecule AS T1 INNER JOIN atom AS T2 ON T1.molecule_id = T2.molecule_id GROUP BY T1.molecule_id, T1.label HAVING COUNT(T2.atom_id) > 5 AND T1.label = '-'
SELECT T1.element FROM atom AS T1 INNER JOIN connected AS T2 ON T1.atom_id = T2.atom_id INNER JOIN bond AS T3 ON T2.bond_id = T3.bond_id WHERE T3.bond_type = '=' AND T1.molecule_id = 'TR024'
SELECT molecule.label FROM molecule INNER JOIN atom ON molecule.molecule_id = atom.molecule_id WHERE molecule.label = '+' GROUP BY molecule.molecule_id ORDER BY COUNT(atom.atom_id) DESC LIMIT 1
SELECT CAST(SUM(CASE WHEN T1.label = '+' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.molecule_id) FROM molecule AS T1 INNER JOIN atom AS T2 ON T1.molecule_id = T2.molecule_id INNER JOIN connected AS T3 ON T2.atom_id = T3.atom_id INNER JOIN bond AS T4 ON T3.bond_id = T4.bond_id WHERE T2.element = 'h' AND T4.bond_type = '#'
SELECT COUNT(molecule_id) FROM molecule WHERE label = '+'
SELECT COUNT(DISTINCT T1.molecule_id) FROM molecule AS T1 INNER JOIN bond AS T2 ON T1.molecule_id = T2.molecule_id WHERE T2.bond_type = '-' AND T1.molecule_id BETWEEN 'TR004' AND 'TR010'
SELECT COUNT(atom_id) FROM atom WHERE molecule_id = 'TR008' AND element = 'c'
SELECT T1.element FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.molecule_id = T2.molecule_id WHERE T1.atom_id = 'TR004_7' AND T2.label = '-'
SELECT COUNT(DISTINCT molecule_id) FROM atom JOIN connected ON atom.atom_id = connected.atom_id JOIN bond ON connected.bond_id = bond.bond_id WHERE element = 'O' AND bond_type = '='
SELECT COUNT(DISTINCT T1.molecule_id) FROM molecule AS T1 INNER JOIN bond AS T2 ON T1.molecule_id = T2.molecule_id WHERE T2.bond_type = '#' AND T1.label = '-'
SELECT T1.element, T3.bond_type FROM atom AS T1 INNER JOIN connected AS T2 ON T1.atom_id = T2.atom_id INNER JOIN bond AS T3 ON T2.bond_id = T3.bond_id WHERE T1.molecule_id = 'TR016'
SELECT T1.atom_id FROM atom AS T1 INNER JOIN connected AS T2 ON T1.atom_id = T2.atom_id INNER JOIN bond AS T3 ON T2.bond_id = T3.bond_id WHERE T1.element = 'C' AND T3.bond_type = '=' AND T1.molecule_id = 'TR012'
SELECT T1.atom_id FROM atom AS T1 INNER JOIN molecule AS T2 ON T1.molecule_id = T2.molecule_id WHERE T2.label = '+' AND T1.element = 'O'
SELECT * FROM cards WHERE cardKingdomFoilId = cardKingdomId AND cardKingdomId IS NOT NULL
SELECT name FROM cards WHERE borderColor = 'borderless' AND (cardKingdomFoilId IS NULL OR cardKingdomId IS NULL) 
SELECT name FROM cards WHERE faceConvertedManaCost = ( SELECT MAX(faceConvertedManaCost) FROM cards )
SELECT name FROM cards WHERE frameVersion = '2015' AND edhrecRank < 100
SELECT T1.name FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.uuid = T2.uuid WHERE T1.rarity = 'mythic' AND T2.status = 'Banned' AND T2.format = 'gladiator'
SELECT T1.name, T3.status FROM cards AS T1 INNER JOIN legalities AS T3 ON T1.uuid = T3.uuid WHERE T1.types LIKE '%Artifact%' AND T1.side IS NULL AND T3.format = 'vintage'
SELECT T1.id, T1.artist FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.uuid = T2.uuid WHERE (T1.power = '*' OR T1.power IS NULL) AND T2.format = 'commander' AND T2.status = 'Legal'
SELECT T1.name, T2.text, T1.hasContentWarning FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.uuid = T2.uuid WHERE T1.artist = 'Stephen Daniele'
SELECT T2.text FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.uuid = T2.uuid WHERE T1.name = 'Sublime Epiphany' AND T1.number = '74s'
SELECT T1.name, T1.artist, T1.isPromo FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.uuid = T2.uuid GROUP BY T1.name, T1.artist, T1.isPromo ORDER BY COUNT(T2.uuid) DESC LIMIT 1 
SELECT T2.language FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.uuid = T2.uuid WHERE T1.name = 'Annul' AND T1.number = '29'
SELECT T1.name FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.uuid = T2.uuid WHERE T2.language = 'Japanese'
SELECT CAST(SUM(CASE WHEN T1.language = 'Chinese Simplified' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(*) FROM foreign_data AS T1 INNER JOIN cards AS T2 ON T1.uuid = T2.uuid
SELECT T1.name, T1.totalSetSize FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.code = T2.setCode WHERE T2.language = 'Italian'
SELECT COUNT(DISTINCT T1.type) FROM cards AS T1 WHERE T1.artist = 'Aaron Boyd'
SELECT keywords FROM cards WHERE name = 'Angel of Mercy'
SELECT COUNT(id) FROM cards WHERE power = '*'
SELECT promoTypes FROM cards WHERE name = 'Duress'
SELECT borderColor FROM cards WHERE name = 'Ancestor's Chosen' 
SELECT originalType FROM cards WHERE name = 'Ancestor's Chosen'
SELECT T2.language FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.code = T2.setCode WHERE T1.code = (SELECT setCode FROM cards WHERE name = 'Angel of Mercy') GROUP BY T2.language
SELECT COUNT(T1.id) FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.uuid = T2.uuid WHERE T2.status = 'restricted' AND T1.isTextless = 0
SELECT T2.text FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.uuid = T2.uuid WHERE T1.name = 'Condemn'
SELECT COUNT(*) FROM cards INNER JOIN legalities ON cards.uuid = legalities.uuid WHERE legalities.status = 'restricted' AND cards.isStarter = 1
SELECT T2.status FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.uuid = T2.uuid WHERE T1.name = 'Cloudchaser Eagle'
SELECT type FROM cards WHERE name = 'Benalish Knight' 
SELECT T2.format FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.uuid = T2.uuid WHERE T1.name = 'Benalish Knight'
SELECT DISTINCT T1.artist FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.uuid = T2.uuid WHERE T2.language = 'Phyrexian'
SELECT CAST(SUM(CASE WHEN borderColor = 'borderless' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(id) FROM cards
SELECT COUNT(T1.id) FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.uuid = T2.uuid WHERE T2.language = 'German' AND T1.isReprint = 1 
SELECT COUNT(DISTINCT T1.id) FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.uuid = T2.uuid WHERE T1.borderColor = 'borderless' AND T2.language = 'Russian'
SELECT CAST(SUM(CASE WHEN T2.language = 'French' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.id) FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.uuid = T2.uuid WHERE T1.isStorySpotlight = 1
SELECT COUNT(id) FROM cards WHERE toughness = '99'
SELECT name FROM cards WHERE artist = 'Aaron Boyd'
SELECT COUNT(id) FROM cards WHERE borderColor = 'black' AND availability = 'mtgo'
SELECT id FROM cards WHERE convertedManaCost = 0
SELECT DISTINCT cards.layout FROM cards WHERE cards.keywords LIKE '%flying%'
SELECT COUNT(*) FROM cards WHERE originalType = 'Summon - Angel' AND subtypes != 'Angel'
SELECT id FROM cards WHERE cardKingdomFoilId IS NOT NULL AND cardKingdomId IS NOT NULL
SELECT id FROM cards WHERE duelDeck = 'a'
SELECT edhrecRank FROM cards WHERE frameVersion = '2015'
SELECT DISTINCT T1.artist FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.uuid = T2.uuid WHERE T2.language = 'Chinese Simplified'
SELECT T1.name FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.uuid = T2.uuid WHERE T1.availability = 'paper' AND T2.language = 'Japanese'
SELECT COUNT(*) FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.uuid = T2.uuid WHERE T2.status = 'Banned' AND T1.borderColor = 'white'
SELECT T1.uuid, T2.language FROM legalities AS T1 INNER JOIN foreign_data AS T2 ON T1.uuid = T2.uuid WHERE T1.format = 'legacy'
SELECT T2.text FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.uuid = T2.uuid WHERE T1.name = 'Beacon of Immortality'
SELECT COUNT(T1.id), T2.status FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.uuid = T2.uuid WHERE T1.frameVersion = 'future' AND T2.status = 'legal'
SELECT T1.name, T1.colors FROM cards AS T1 INNER JOIN sets AS T2 ON T1.setCode = T2.code WHERE T2.code = 'OGW'
SELECT T1.name, T3.language FROM cards AS T1 INNER JOIN sets AS T2 ON T1.setCode = T2.code INNER JOIN set_translations AS T3 ON T2.code = T3.setCode WHERE T1.convertedManaCost = 5 AND T2.code = '10E'
SELECT T1.name, T2.date FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.uuid = T2.uuid WHERE T1.originalType = 'Creature - Elf'
SELECT T1.colors, T2.format FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.uuid = T2.uuid WHERE T1.id BETWEEN 1 AND 20
SELECT cards.name, foreign_data.language FROM cards INNER JOIN foreign_data ON cards.uuid = foreign_data.uuid WHERE cards.originalType = 'Artifact' AND cards.colors LIKE '%B%'
SELECT T1.name FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.uuid = T2.uuid WHERE T1.rarity = 'uncommon' ORDER BY T2.date ASC LIMIT 3
SELECT COUNT(*) FROM cards WHERE artist = 'John Avon' AND cardKingdomId IS NOT NULL AND cardKingdomFoilId IS NULL 
SELECT COUNT(id) FROM cards WHERE borderColor = 'white' AND cardKingdomFoilId = cardKingdomId AND cardKingdomId IS NOT NULL
SELECT COUNT(*) FROM cards WHERE artist = 'UDON' AND availability LIKE '%mtgo%' AND hand = '-1'
SELECT COUNT(id) FROM cards WHERE frameVersion = '1993' AND availability = 'paper' AND hasContentWarning = 1
SELECT manaCost FROM cards WHERE layout = 'normal' AND frameVersion = '2003' AND borderColor = 'black' AND (availability = 'paper' OR availability = 'mtgo')
SELECT SUM(convertedManaCost) FROM cards WHERE artist = 'Rob Alexander'
SELECT DISTINCT subtypes, supertypes FROM cards WHERE availability = 'arena'
SELECT DISTINCT T1.setCode FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.uuid = T2.uuid WHERE T2.language = 'Spanish'
SELECT CAST(COUNT(CASE WHEN hand = '+3' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(id) FROM cards WHERE frameEffects = 'legendary'
SELECT CAST(SUM(CASE WHEN isStorySpotlight = 1 AND isTextless = 0 THEN 1 ELSE 0 END) AS REAL) * 100 / SUM(CASE WHEN isStorySpotlight = 1 THEN 1 ELSE 0 END) AS percentage, id FROM cards GROUP BY id
SELECT CAST(SUM(CASE WHEN T2.language = 'Spanish' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.id), T2.name FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.uuid = T2.uuid
SELECT T2.language FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.code = T2.setCode WHERE T1.baseSetSize = 309
SELECT COUNT(DISTINCT setCode) FROM set_translations AS T1 INNER JOIN sets AS T2 ON T1.setCode = T2.code WHERE T2.block = 'Commander' AND T1.language = 'Portuguese (Brasil)'
SELECT cards.id FROM cards INNER JOIN legalities ON cards.uuid = legalities.uuid WHERE legalities.status = 'legal' AND cards.types LIKE '%Creature%'
SELECT DISTINCT T1.subtypes, T1.supertypes FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.uuid = T2.uuid WHERE T2.language = 'German' AND T1.subtypes IS NOT NULL AND T1.supertypes IS NOT NULL
SELECT COUNT(*) FROM cards WHERE (power IS NULL OR power = '*') AND text LIKE '%triggered ability%'
SELECT COUNT(*) FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.uuid = T2.uuid INNER JOIN rulings AS T3 ON T1.uuid = T3.uuid WHERE T2.format = 'premodern' AND T3.text = 'This is a triggered mana ability' AND T1.side IS NULL
SELECT id FROM cards WHERE artist = 'Erica Yang' AND availability = 'paper' AND uuid IN (SELECT uuid FROM legalities WHERE format = 'pauper')
SELECT artist FROM cards WHERE text = 'Das perfekte Gegenmittel zu einer dichten Formation'
SELECT T2.name FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.uuid = T2.uuid WHERE T1.artist = 'Matthew D. Wilson' AND T1.borderColor = 'black' AND T1.layout = 'normal' AND T1.type LIKE '%Creature%' AND T2.language = 'French'
SELECT COUNT(T1.id) FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.uuid = T2.uuid WHERE T1.rarity = 'rare' AND T2.date = '2009-01-10'
SELECT T2.language FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.code = T2.setCode WHERE T1.baseSetSize = 180 AND T1.block = 'Ravnica'
SELECT CAST(SUM(CASE WHEN T1.hasContentWarning = 0 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.id) FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.uuid = T2.uuid WHERE T2.format = 'commander' AND T2.status = 'legal'
SELECT CAST(SUM(CASE WHEN T2.language = 'French' AND (T1.power IS NULL OR T1.power = '*') THEN 1 ELSE 0 END) AS REAL) * 100 / SUM(CASE WHEN T1.power IS NULL OR T1.power = '*' THEN 1 ELSE 0 END) FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.uuid = T2.uuid
SELECT CAST(SUM(CASE WHEN T1.language = 'Japanese' AND T2.type = 'expansion' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.language) FROM set_translations AS T1 INNER JOIN sets AS T2 ON T1.setCode = T2.code
SELECT availability FROM cards WHERE artist = 'Daren Bader'
SELECT COUNT(id) FROM cards WHERE borderColor = 'borderless' AND edhrecRank > 12000 
SELECT COUNT(id) FROM cards WHERE isOversized = 1 AND isReprint = 1 AND isPromo = 1
SELECT name FROM cards WHERE (power IS NULL OR power = '*') AND promoTypes = 'arenaleague' ORDER BY name ASC LIMIT 3
SELECT language FROM foreign_data WHERE multiverseid = 149934 
SELECT cardKingdomFoilId, cardKingdomId FROM cards WHERE cardKingdomFoilId IS NOT NULL AND cardKingdomId IS NOT NULL ORDER BY cardKingdomFoilId ASC LIMIT 3 
SELECT CAST(SUM(CASE WHEN isTextless = 1 AND layout = 'normal' THEN 1 ELSE 0 END) AS REAL) / COUNT(isTextless) * 100 FROM cards
SELECT number FROM cards WHERE otherFaceIds IS NULL AND subtypes LIKE '%Angel%' AND subtypes LIKE '%Wizard%'
SELECT name FROM sets WHERE mtgoCode IS NULL OR mtgoCode = '' ORDER BY name ASC LIMIT 3
SELECT T2.language FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.code = T2.setCode WHERE T1.mcmName = 'Archenemy' AND T1.code = 'ARC'
SELECT T1.name, T2.translation FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.code = T2.setCode WHERE T1.id = 5
SELECT T1.language, T2.type FROM set_translations AS T1 INNER JOIN sets AS T2 ON T1.setCode = T2.code WHERE T2.id = 206
SELECT T1.id, T1.code FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.code = T2.setCode INNER JOIN cards AS T3 ON T1.code = T3.setCode WHERE T2.language = 'Italian' AND T1.block = 'Shadowmoor' ORDER BY T1.code ASC LIMIT 2
SELECT T1.id FROM sets AS T1 INNER JOIN cards AS T2 ON T1.code = T2.setCode INNER JOIN foreign_data AS T3 ON T2.uuid = T3.uuid WHERE T1.isForeignOnly = 1 AND T1.isFoilOnly = 1 AND T3.language = 'Japanese'
SELECT T1.code FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.code = T2.setCode WHERE T2.language = 'Russian' ORDER BY T1.baseSetSize DESC LIMIT 1
SELECT CAST(SUM(CASE WHEN T1.isOnlineOnly = 1 AND T2.language = 'Chinese Simplified' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.isOnlineOnly) FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.uuid = T2.uuid
SELECT COUNT(*) FROM sets AS T1 LEFT JOIN set_translations AS T2 ON T1.code = T2.setCode WHERE T2.language = 'Japanese' AND (T1.mtgoCode IS NULL OR T1.mtgoCode = '')
SELECT id FROM cards WHERE borderColor = 'Black'
SELECT id FROM cards WHERE frameEffects = 'extendedart'
SELECT name FROM cards WHERE borderColor = 'Black' AND isFullArt = 1
SELECT T1.language FROM set_translations AS T1 WHERE T1.setCode = '174'
SELECT name FROM sets WHERE code = 'ALL'
SELECT language FROM foreign_data WHERE name = 'A Pedra Fellwar' 
SELECT setCode FROM sets WHERE releaseDate = '2007-07-13'
SELECT baseSetSize, code FROM sets WHERE block IN ('Masques', 'Mirage')
SELECT setCode FROM sets WHERE type = 'expansion'
SELECT T2.name, T2.type FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.uuid = T2.uuid WHERE T1.watermark = 'boros'
SELECT T2.language, T2.flavorText, T1.type FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.uuid = T2.uuid WHERE T1.watermark = 'colorpie'
SELECT CAST(SUM(CASE WHEN T1.convertedManaCost = 10 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.convertedManaCost) FROM cards AS T1 INNER JOIN sets AS T2 ON T1.setCode = T2.code WHERE T2.name = 'Abyssal Horror'
SELECT setCode FROM sets WHERE type = 'expansion' AND name LIKE '%Commander%'
SELECT T2.name, T2.type FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.uuid = T2.uuid WHERE T1.watermark = 'abzan'
SELECT T2.language, T1.type FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.uuid = T2.uuid WHERE T1.watermark = 'azorius'
SELECT COUNT(*) FROM cards WHERE artist = 'Aaron Miller' AND cardKingdomFoilId = cardKingdomId AND cardKingdomId IS NOT NULL
SELECT COUNT(*) FROM cards WHERE availability LIKE '%paper%' AND hand LIKE '+%'
SELECT name FROM cards WHERE isTextless = 0
SELECT convertedManaCost FROM cards WHERE name = 'Ancestor`s Chosen'
SELECT COUNT(id) FROM cards WHERE borderColor = 'white' AND (power = '*' OR power IS NULL)
SELECT name FROM cards WHERE isPromo = 1 AND side IS NOT NULL
SELECT subtypes, supertypes FROM cards WHERE name = 'Molimo, Maro-Sorcerer'
SELECT purchaseUrls FROM cards WHERE promoTypes = 'bundle'
SELECT COUNT(DISTINCT artist) FROM cards WHERE borderColor = 'black' AND availability LIKE '%arena,mtgo%'
SELECT name FROM cards WHERE name IN ('Serra Angel', 'Shrine Keeper') ORDER BY convertedManaCost DESC LIMIT 1 
SELECT T1.artist FROM cards AS T1 WHERE T1.flavorName = 'Battra, Dark Destroyer'
SELECT name FROM cards WHERE frameVersion = '2003' ORDER BY convertedManaCost DESC LIMIT 3
SELECT T3.translation FROM cards AS T1 INNER JOIN sets AS T2 ON T1.setCode = T2.code INNER JOIN set_translations AS T3 ON T2.code = T3.setCode WHERE T1.name = 'Ancestor's Chosen' AND T3.language = 'Italian'
SELECT COUNT(T2.translation) FROM cards AS T1 INNER JOIN set_translations AS T2 ON T1.setCode = T2.setCode WHERE T1.name = 'Angel of Mercy'
SELECT T1.name FROM cards AS T1 INNER JOIN set_translations AS T2 ON T1.setCode = T2.setCode WHERE T2.translation = 'Hauptset Zehnte Edition'
SELECT CASE WHEN EXISTS (SELECT 1 FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.uuid = T2.uuid WHERE T1.name = 'Ancestor''s Chosen' AND T2.language = 'Korean') THEN 'Yes' ELSE 'No' END AS 'Exists'
SELECT COUNT(T1.id) FROM cards AS T1 INNER JOIN sets AS T2 ON T1.setCode = T2.code INNER JOIN set_translations AS T3 ON T2.code = T3.setCode WHERE T1.artist = 'Adam Rex' AND T3.translation = 'Hauptset Zehnte Edition'
SELECT baseSetSize FROM sets WHERE code = ( SELECT setCode FROM set_translations WHERE translation = 'Hauptset Zehnte Edition' )
SELECT translation FROM set_translations WHERE setCode = (SELECT code FROM sets WHERE name = 'Eighth Edition') AND language = 'Simplified Chinese'
SELECT T1.mtgoCode FROM cards AS T1 WHERE T1.name = 'Angel of Mercy' AND T1.mtgoCode IS NOT NULL 
SELECT T2.releaseDate FROM cards AS T1 INNER JOIN sets AS T2 ON T1.setCode = T2.code WHERE T1.name = 'Ancestor''s Chosen'
SELECT T1.type FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.code = T2.setCode WHERE T2.translation = 'Hauptset Zehnte Edition'
SELECT COUNT(DISTINCT T1.id) FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.code = T2.setCode WHERE T1.block = 'Ice Age' AND T2.language = 'Italian'
SELECT T2.isForeignOnly FROM cards AS T1 INNER JOIN sets AS T2 ON T1.setCode = T2.code WHERE T1.name = 'Adarkar Valkyrie'
SELECT COUNT(DISTINCT T2.setCode) FROM set_translations AS T1 INNER JOIN sets AS T2 ON T1.setCode = T2.code WHERE T1.language = 'Italian' AND T2.baseSetSize < 10
SELECT COUNT(id) FROM cards WHERE setCode = (SELECT code FROM sets WHERE name = 'Coldsnap') AND borderColor = 'black'
SELECT name FROM cards WHERE setCode = (SELECT code FROM sets WHERE name = 'Coldsnap') ORDER BY convertedManaCost DESC LIMIT 1
SELECT T1.artist FROM cards AS T1 INNER JOIN sets AS T2 ON T1.setCode = T2.code WHERE T2.name = 'Coldsnap' AND T1.artist IN ('Jeremy Jarvis', 'Aaron Miller','Chippy')
SELECT T1.name FROM cards AS T1 INNER JOIN sets AS T2 ON T1.setCode = T2.code WHERE T2.name = 'Coldsnap' AND T1.number = '4'
SELECT COUNT(T1.id) FROM cards AS T1 INNER JOIN sets AS T2 ON T1.setCode = T2.code WHERE T2.name = 'Coldsnap' AND T1.convertedManaCost > 5 AND (T1.power = '*' OR T1.power IS NULL)
SELECT T2.flavorText FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.uuid = T2.uuid WHERE T1.name = 'Ancestor''s Chosen' AND T2.language = 'Italian'
SELECT language FROM foreign_data WHERE uuid IN (SELECT uuid FROM cards WHERE name = 'Ancestor''s Chosen') AND flavorText IS NOT NULL
SELECT T2.type FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.uuid = T2.uuid WHERE T2.language = 'German' AND T1.name = 'Ancestor''s Chosen'
SELECT T1.text FROM rulings AS T1 INNER JOIN cards AS T2 ON T1.uuid = T2.uuid INNER JOIN sets AS T3 ON T2.setCode = T3.code INNER JOIN set_translations AS T4 ON T3.code = T4.setCode WHERE T3.name = 'Coldsnap' AND T4.language = 'Italian'
SELECT T3.name FROM cards AS T1 INNER JOIN sets AS T2 ON T1.setCode = T2.code INNER JOIN foreign_data AS T3 ON T1.uuid = T3.uuid WHERE T2.name = 'Coldsnap' AND T3.language = 'Italian' ORDER BY T1.convertedManaCost DESC
SELECT rulings.date FROM rulings INNER JOIN cards ON rulings.uuid = cards.uuid WHERE cards.name = 'Reminisce'
SELECT CAST(SUM(CASE WHEN T1.convertedManaCost = 7 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.id) FROM cards AS T1 INNER JOIN sets AS T2 ON T1.setCode = T2.code WHERE T2.name = 'Coldsnap'
SELECT CAST(SUM(CASE WHEN T1.cardKingdomFoilId = T1.cardKingdomId AND T1.cardKingdomId IS NOT NULL THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.name) FROM cards AS T1 INNER JOIN sets AS T2 ON T1.setCode = T2.code WHERE T2.name = 'Coldsnap'
SELECT code FROM sets WHERE releaseDate = '2017-07-14'
SELECT keyruneCode FROM sets WHERE code = 'PKHC'
SELECT mcmId FROM sets WHERE code = 'SS2'
SELECT mcmName FROM sets WHERE releaseDate = '2017-06-09'
SELECT type FROM sets WHERE name LIKE '%From the Vault: Lore%'
SELECT parentCode FROM sets WHERE name = 'Commander 2014 Oversized'
SELECT T1.name, T3.text, CASE WHEN T1.hasContentWarning = 1 THEN 'Yes' ELSE 'No' END AS 'Missing or Degraded Properties and Values' FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.uuid = T2.uuid INNER JOIN rulings AS T3 ON T2.id = T3.id WHERE T1.artist = 'Jim Pavelec'
SELECT T2.releaseDate FROM cards AS T1 INNER JOIN sets AS T2 ON T1.setCode = T2.code WHERE T1.name = 'Evacuation'
SELECT T1.baseSetSize FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.code = T2.setCode WHERE T2.translation = 'Rinascita di Alara'
SELECT T1.type FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.code = T2.setCode WHERE T2.translation = 'Huitième édition'
SELECT T2.translation FROM cards AS T1 INNER JOIN set_translations AS T2 ON T1.setCode = T2.setCode WHERE T1.name = 'Tendo Ice Bridge' AND T2.language = 'French'
SELECT COUNT(T1.translation) FROM set_translations AS T1 INNER JOIN sets AS T2 ON T1.setCode = T2.code WHERE T2.name = 'Salvat 2011' AND T1.translation IS NOT NULL
SELECT T4.translation FROM cards AS T1 INNER JOIN sets AS T2 ON T1.setCode = T2.code INNER JOIN set_translations AS T4 ON T2.code = T4.setCode WHERE T1.name = 'Fellwar Stone' AND T4.language = 'Japanese'
SELECT T1.name FROM cards AS T1 INNER JOIN sets AS T2 ON T1.setCode = T2.code WHERE T2.name = 'Journey into Nyx Hero''s Path' ORDER BY T1.convertedManaCost DESC LIMIT 1
SELECT T1.releaseDate FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.code = T2.setCode WHERE T2.translation = 'Ola de frío'
SELECT T1.type FROM sets AS T1 INNER JOIN cards AS T2 ON T1.code = T2.setCode WHERE T2.name = 'Samite Pilgrim'
SELECT COUNT(*) FROM cards AS T1 INNER JOIN sets AS T2 ON T1.setCode = T2.code WHERE T2.name = 'World Championship Decks 2004' AND T1.convertedManaCost = 3
SELECT T2.translation FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.code = T2.setCode WHERE T1.name = 'Mirrodin' AND T2.language = 'Chinese Simplified'
SELECT CAST(SUM(CASE WHEN T1.isNonFoilOnly = 1 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(*) FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.code = T2.setCode WHERE T2.language = 'Japanese'
SELECT CAST(SUM(CASE WHEN T1.isOnlineOnly = 1 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(*) FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.code = T2.setCode WHERE T2.language = 'Portuguese (Brazil)'
SELECT availability FROM cards WHERE artist = 'Aleksi Briclot' AND isTextless = 1
SELECT id FROM sets ORDER BY baseSetSize DESC LIMIT 1
SELECT artist FROM cards WHERE side IS NULL ORDER BY convertedManaCost DESC LIMIT 1
SELECT frameEffects FROM cards WHERE cardKingdomFoilId IS NOT NULL AND cardKingdomId IS NOT NULL GROUP BY frameEffects ORDER BY COUNT(*) DESC LIMIT 1 
SELECT COUNT(id) FROM cards WHERE power IS NULL OR power = '*' AND hasFoil = 0 AND duelDeck = 'a'
SELECT id FROM sets WHERE type = 'commander' ORDER BY totalSetSize DESC LIMIT 1
SELECT cards.name, cards.convertedManaCost FROM cards INNER JOIN legalities ON cards.uuid = legalities.uuid WHERE legalities.format = 'duel' ORDER BY cards.convertedManaCost DESC LIMIT 10
SELECT T1.originalReleaseDate, T3.format FROM cards AS T1 INNER JOIN legalities AS T3 ON T1.uuid = T3.uuid WHERE T1.rarity = 'mythic' AND T3.status = 'legal' ORDER BY T1.originalReleaseDate ASC LIMIT 1
SELECT COUNT(T1.id) FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.uuid = T2.uuid WHERE T1.artist = 'Volkan Baga' AND T2.language = 'French'
SELECT COUNT(*) FROM cards AS c INNER JOIN legalities AS l ON c.uuid = l.uuid WHERE c.rarity = 'rare' AND c.types = 'Enchantment' AND c.name = 'Abundance' AND l.status = 'Legal'
SELECT T1.format, T2.name FROM legalities AS T1 INNER JOIN cards AS T2 ON T1.uuid = T2.uuid WHERE T1.status = 'banned' GROUP BY T1.format ORDER BY COUNT(*) DESC LIMIT 1 
SELECT T1.language FROM set_translations AS T1 INNER JOIN sets AS T2 ON T1.setCode = T2.code WHERE T2.name = 'Battlebond'
SELECT T1.artist, T3.format FROM cards AS T1 LEFT JOIN foreign_data AS T2 ON T1.uuid = T2.uuid LEFT JOIN legalities AS T3 ON T1.uuid = T3.uuid GROUP BY T1.artist HAVING COUNT(T1.artist) = (SELECT COUNT(artist) FROM cards GROUP BY artist ORDER BY COUNT(artist) ASC LIMIT 1)
SELECT T4.status FROM cards AS T1 INNER JOIN foreign_data AS T2 ON T1.uuid = T2.uuid INNER JOIN legalities AS T3 ON T1.uuid = T3.uuid INNER JOIN rulings AS T4 ON T1.uuid = T4.uuid WHERE T1.frameVersion = '1997' AND T1.artist = 'D. Alexander Gregory' AND T1.hasContentWarning = 1 AND T3.format = 'legacy'
SELECT T1.name, T2.format FROM cards AS T1 INNER JOIN legalities AS T2 ON T1.uuid = T2.uuid WHERE T1.edhrecRank = 1 AND T2.status = 'banned'
SELECT CAST(COUNT(T1.id) AS REAL) / 4 AS 'Average Annual Sets', T2.language AS 'Common Language' FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.code = T2.setCode WHERE T1.releaseDate BETWEEN '2012-01-01' AND '2015-12-31' GROUP BY T2.language ORDER BY COUNT(T2.language) DESC LIMIT 1
SELECT DISTINCT artist FROM cards WHERE borderColor = 'black' AND availability = 'arena'
SELECT uuid FROM legalities WHERE format = 'oldschool' AND (status = 'banned' OR status = 'restricted')
SELECT COUNT(*) FROM cards WHERE artist = 'Matthew D. Wilson' AND availability = 'paper'
SELECT T2.text FROM cards AS T1 INNER JOIN rulings AS T2 ON T1.uuid = T2.uuid WHERE T1.artist = 'Kev Walker' ORDER BY T2.date DESC
SELECT T1.name, T3.format FROM cards AS T1 INNER JOIN sets AS T2 ON T1.setCode = T2.code INNER JOIN legalities AS T3 ON T1.uuid = T3.uuid WHERE T2.name = 'Hour of Devastation' AND T3.status = 'legal'
SELECT T1.name FROM sets AS T1 INNER JOIN set_translations AS T2 ON T1.code = T2.setCode WHERE T2.language = 'Korean' AND T1.code NOT IN (SELECT setCode FROM set_translations WHERE language = 'Japanese')
SELECT T1.frameVersion, T1.name, T2.status FROM cards AS T1 LEFT JOIN legalities AS T2 ON T1.uuid = T2.uuid WHERE T1.artist = 'Allen Williams' AND T2.status = 'banned'
SELECT DisplayName, Reputation FROM users WHERE DisplayName IN ('Harlan', 'Jarrod Dixon') ORDER BY Reputation DESC LIMIT 1
SELECT DisplayName FROM users WHERE STRFTIME('%Y', CreationDate) = '2014'
SELECT COUNT(*) FROM users WHERE LastAccessDate > '2014-09-01 00:00:00'
SELECT DisplayName FROM users ORDER BY Views DESC LIMIT 1
SELECT COUNT(Id) FROM users WHERE UpVotes > 100 AND DownVotes > 1
SELECT COUNT(*) FROM users WHERE Views > 10 AND strftime('%Y', CreationDate) > '2013'
SELECT COUNT(Id) FROM posts WHERE OwnerUserId = (SELECT Id FROM users WHERE DisplayName = 'csgillespie')
SELECT T1.Title FROM posts AS T1 INNER JOIN users AS T2 ON T1.OwnerUserId = T2.Id WHERE T2.DisplayName = 'csgillespie'
SELECT T2.DisplayName FROM posts AS T1 INNER JOIN users AS T2 ON T1.OwnerUserId = T2.Id WHERE T1.Title = 'Eliciting priors from experts'
SELECT T2.Title FROM users AS T1 INNER JOIN posts AS T2 ON T1.Id = T2.OwnerUserId WHERE T1.DisplayName = 'csgillespie' ORDER BY T2.ViewCount DESC LIMIT 1
SELECT T2.DisplayName FROM posts AS T1 INNER JOIN users AS T2 ON T1.OwnerUserId = T2.Id ORDER BY T1.FavoriteCount DESC LIMIT 1
SELECT SUM(T1.CommentCount) FROM posts AS T1 INNER JOIN users AS T2 ON T1.OwnerUserId = T2.Id WHERE T2.DisplayName = 'csgillespie'
SELECT T1.AnswerCount FROM posts AS T1 INNER JOIN users AS T2 ON T1.OwnerUserId = T2.Id WHERE T2.DisplayName = 'csgillespie' ORDER BY T1.AnswerCount DESC LIMIT 1 
SELECT T2.DisplayName FROM posts AS T1 INNER JOIN users AS T2 ON T1.LastEditorUserId = T2.Id WHERE T1.Title = 'Examples for teaching: Correlation does not mean causation'
SELECT COUNT(*) FROM posts WHERE OwnerUserId = (SELECT Id FROM users WHERE DisplayName = 'csgillespie') AND ParentId IS NULL
SELECT T2.DisplayName FROM posts AS T1 INNER JOIN users AS T2 ON T1.OwnerUserId = T2.Id WHERE T1.ClosedDate IS NOT NULL
SELECT COUNT(T1.Id) FROM posts AS T1 INNER JOIN users AS T2 ON T1.OwnerUserId = T2.Id WHERE T2.Age > 65 AND T1.Score >= 20
SELECT T2.Location FROM posts AS T1 INNER JOIN users AS T2 ON T1.OwnerUserId = T2.Id WHERE T1.Title = 'Eliciting priors from experts'
SELECT T2.Body FROM tags AS T1 INNER JOIN posts AS T2 ON T1.ExcerptPostId = T2.Id WHERE T1.TagName = 'bayesian'
SELECT T2.Body FROM tags AS T1 INNER JOIN posts AS T2 ON T1.ExcerptPostId = T2.Id ORDER BY T1.Count DESC LIMIT 1 
SELECT COUNT(Id) FROM badges WHERE UserId = (SELECT Id FROM users WHERE DisplayName = 'csgillespie')
SELECT T1.Name FROM badges AS T1 INNER JOIN users AS T2 ON T1.UserId = T2.Id WHERE T2.DisplayName = 'csgillespie'
SELECT COUNT(*) FROM badges WHERE UserId = (SELECT Id FROM users WHERE DisplayName = 'csgillespie') AND strftime('%Y', Date) = '2011'
SELECT T1.DisplayName FROM users AS T1 INNER JOIN badges AS T2 ON T1.Id = T2.UserId GROUP BY T1.Id, T1.DisplayName ORDER BY COUNT(T2.Id) DESC LIMIT 1
SELECT AVG(T1.Score) FROM posts AS T1 INNER JOIN users AS T2 ON T1.OwnerUserId = T2.Id WHERE T2.DisplayName = 'csgillespie'
SELECT CAST(COUNT(T1.Id) AS REAL) / COUNT(DISTINCT T1.UserId) FROM badges AS T1 INNER JOIN users AS T2 ON T1.UserId = T2.Id WHERE T2.Views > 200
SELECT CAST(SUM(CASE WHEN T1.Age > 65 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T2.Id) FROM users AS T1 INNER JOIN posts AS T2 ON T1.Id = T2.OwnerUserId WHERE T2.Score > 20 
SELECT COUNT(*) FROM votes WHERE UserId = 58 AND DATE(CreationDate) = '2010-07-19'
SELECT CreationDate FROM votes GROUP BY CreationDate ORDER BY COUNT(Id) DESC LIMIT 1 
SELECT COUNT(Id) FROM badges WHERE Name = 'Revival'
SELECT T2.Title FROM comments AS T1 INNER JOIN posts AS T2 ON T1.PostId = T2.Id ORDER BY T1.Score DESC LIMIT 1;
SELECT COUNT(T2.Id) FROM posts AS T1 INNER JOIN comments AS T2 ON T1.Id = T2.PostId WHERE T1.ViewCount = 1910 
SELECT T2.FavoriteCount FROM comments AS T1 INNER JOIN posts AS T2 ON T1.PostId = T2.Id WHERE T1.UserId = 3025 AND T1.CreationDate = '2014-04-23 20:29:39.0'
SELECT T1.Text FROM comments AS T1 INNER JOIN posts AS T2 ON T1.PostId = T2.Id WHERE T2.ParentId = 107829 AND T2.CommentCount = 1
SELECT CASE WHEN T2.ClosedDate IS NULL THEN 'No' ELSE 'Yes' END AS 'Well-Finished' FROM comments AS T1 INNER JOIN posts AS T2 ON T1.PostId = T2.Id WHERE T1.UserId = 23853 AND T1.CreationDate = '2013-07-12 09:08:18.0'
SELECT T2.Reputation FROM posts AS T1 INNER JOIN users AS T2 ON T1.OwnerUserId = T2.Id WHERE T1.Id = 65041 
SELECT COUNT(T1.Id) FROM posts AS T1 INNER JOIN users AS T2 ON T1.OwnerUserId = T2.Id WHERE T2.DisplayName = 'Tiago Pasqualini'
SELECT T2.DisplayName FROM votes AS T1 INNER JOIN users AS T2 ON T1.UserId = T2.Id WHERE T1.Id = 6347 
SELECT COUNT(T1.Id) FROM votes AS T1 INNER JOIN posts AS T2 ON T1.PostId = T2.Id WHERE T2.Title LIKE '%data visualization%'
SELECT T1.Name FROM badges AS T1 INNER JOIN users AS T2 ON T1.UserId = T2.Id WHERE T2.DisplayName = 'DatEpicCoderGuyWhoPrograms'
SELECT CAST(COUNT(T1.Id) AS REAL) / COUNT(T2.Id) FROM posts AS T1 INNER JOIN votes AS T2 ON T1.OwnerUserId = T2.UserId WHERE T1.OwnerUserId = 24 
SELECT ViewCount FROM posts WHERE Title = 'Integration of Weka and/or RapidMiner into Informatica PowerCenter/Developer'
SELECT Text FROM comments WHERE Score = 17
SELECT DisplayName FROM users WHERE WebsiteUrl = 'http://stackoverflow.com'
SELECT T1.Name FROM badges AS T1 INNER JOIN users AS T2 ON T1.UserId = T2.Id WHERE T2.DisplayName = 'SilentGhost'
SELECT T2.DisplayName FROM comments AS T1 INNER JOIN users AS T2 ON T1.UserId = T2.Id WHERE T1.Text = 'thank you user93!'
SELECT T2.Text FROM users AS T1 INNER JOIN comments AS T2 ON T1.Id = T2.UserId WHERE T1.DisplayName = 'A Lion'
SELECT T2.DisplayName, T2.Reputation FROM posts AS T1 INNER JOIN users AS T2 ON T1.OwnerUserId = T2.Id WHERE T1.Title = 'Understanding what Dassault iSight is doing?'
SELECT T2.Text FROM posts AS T1 INNER JOIN comments AS T2 ON T1.Id = T2.PostId WHERE T1.Title = 'How does gentle boosting differ from AdaBoost?'
SELECT T2.DisplayName FROM badges AS T1 INNER JOIN users AS T2 ON T1.UserId = T2.Id WHERE T1.Name = 'Necromancer' LIMIT 10
SELECT T2.DisplayName FROM posts AS T1 INNER JOIN users AS T2 ON T1.LastEditorUserId = T2.Id WHERE T1.Title = 'Open source tools for visualizing multi-dimensional data'
SELECT T1.Title FROM posts AS T1 INNER JOIN users AS T2 ON T1.LastEditorUserId = T2.Id WHERE T2.DisplayName = 'Vebjorn Ljosa'
SELECT SUM(T1.Score), T2.WebsiteUrl FROM posts AS T1 INNER JOIN users AS T2 ON T1.LastEditorUserId = T2.Id WHERE T2.DisplayName = 'Yevgeny'
SELECT T2.Text FROM posts AS T1 INNER JOIN comments AS T2 ON T1.Id = T2.PostId INNER JOIN postHistory AS T3 ON T1.Id = T3.PostId WHERE T1.Title = 'Why square the difference instead of taking the absolute value in standard deviation?' AND T3.UserId = T2.UserId 
SELECT SUM(T2.BountyAmount) FROM posts AS T1 INNER JOIN votes AS T2 ON T1.Id = T2.PostId WHERE T1.Title LIKE '%data%'
SELECT T3.DisplayName FROM votes AS T1 INNER JOIN posts AS T2 ON T1.PostId = T2.Id INNER JOIN users AS T3 ON T1.UserId = T3.Id WHERE T1.BountyAmount = 50 AND T2.Title LIKE '%variance%'
SELECT AVG(T1.ViewCount), T1.Title, T2.Text, T1.Score FROM posts AS T1 INNER JOIN comments AS T2 ON T1.Id = T2.PostId INNER JOIN tags AS T3 ON T1.Id = T3.ExcerptPostId WHERE T3.TagName = 'humor'
SELECT COUNT(Id) FROM comments WHERE UserId = 13 
SELECT UserId FROM users ORDER BY Reputation DESC LIMIT 1
SELECT UserId FROM users ORDER BY Views ASC LIMIT 1
SELECT COUNT(UserId) FROM badges WHERE Name = 'Supporter' AND strftime('%Y', Date) = '2011'
SELECT UserId, COUNT(Name) AS BadgeCount FROM badges GROUP BY UserId HAVING COUNT(Name) > 5
SELECT COUNT(DISTINCT T1.UserId) FROM badges AS T1 INNER JOIN users AS T2 ON T1.UserId = T2.Id WHERE T1.Name IN ('Supporter', 'Teacher') AND T2.Location = 'New York'
SELECT T1.DisplayName, T1.Reputation FROM users AS T1 INNER JOIN posts AS T2 ON T1.Id = T2.OwnerUserId WHERE T2.Id = 1 
SELECT UserId FROM postHistory GROUP BY UserId, PostId HAVING COUNT(Id) = 1 INTERSECT SELECT UserId FROM users WHERE Views >= 1000
SELECT T1.UserId, T2.Name FROM comments AS T1 INNER JOIN badges AS T2 ON T1.UserId = T2.UserId GROUP BY T1.UserId ORDER BY COUNT(T1.Id) DESC LIMIT 1
SELECT COUNT(DISTINCT T1.UserId) FROM badges AS T1 INNER JOIN users AS T2 ON T1.UserId = T2.Id WHERE T2.Location LIKE '%India%' AND T1.Name = 'Teacher'
SELECT 100.0 * (SUM(CASE WHEN strftime('%Y', Date) = '2010' AND Name = 'Student' THEN 1 ELSE 0 END) / COUNT(Name) - SUM(CASE WHEN strftime('%Y', Date) = '2011' AND Name = 'Student' THEN 1 ELSE 0 END) / COUNT(Name)) AS percentage_difference FROM badges
SELECT T1.PostHistoryTypeId, COUNT(DISTINCT T2.UserId) FROM postHistory AS T1 LEFT JOIN comments AS T2 ON T1.PostId = T2.PostId WHERE T1.PostId = 3720 
SELECT T1.*, T2.ViewCount AS Popularity FROM postLinks AS T1 INNER JOIN posts AS T2 ON T1.PostId = T2.Id WHERE T1.RelatedPostId = 61217
SELECT T1.Score, T2.LinkTypeId FROM posts AS T1 INNER JOIN postLinks AS T2 ON T1.Id = T2.PostId WHERE T1.Id = 395
SELECT Id, OwnerUserId FROM posts WHERE Score > 60
SELECT SUM(FavoriteCount) FROM posts WHERE OwnerUserId = 686 AND YEAR(CreaionDate) = 2011
SELECT AVG(T1.UpVotes), AVG(T1.Age) FROM users AS T1 INNER JOIN posts AS T2 ON T1.Id = T2.OwnerUserId GROUP BY T1.Id HAVING COUNT(T2.Id) > 10 
SELECT COUNT(UserId) FROM badges WHERE Name = 'Announcer'
SELECT Name FROM badges WHERE Date = '2010-07-19 19:39:08'
SELECT COUNT(Id) FROM comments WHERE Score > 60;
SELECT Text FROM comments WHERE CreationDate = '2010-07-19 19:25:47.0'
SELECT COUNT(Id) FROM posts WHERE Score = 10
SELECT Name FROM badges WHERE UserId IN ( SELECT Id FROM users WHERE Reputation = ( SELECT MAX(Reputation) FROM users ) )
SELECT T2.Reputation FROM badges AS T1 INNER JOIN users AS T2 ON T1.UserId = T2.Id WHERE T1.Date = '2010-07-19 19:39:08.0'
SELECT T1.Name FROM badges AS T1 INNER JOIN users AS T2 ON T1.UserId = T2.Id WHERE T2.DisplayName = 'Pierre'
SELECT T1.Date FROM badges AS T1 INNER JOIN users AS T2 ON T1.UserId = T2.Id WHERE T2.Location = 'Rochester, NY'
SELECT CAST(COUNT(DISTINCT CASE WHEN Name = 'Teacher' THEN UserId ELSE NULL END) AS REAL) * 100 / COUNT(DISTINCT UserId) AS percentage FROM badges
SELECT CAST(SUM(CASE WHEN T2.Age BETWEEN 13 AND 18 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.UserId) AS percentage FROM badges AS T1 INNER JOIN users AS T2 ON T1.UserId = T2.Id WHERE T1.Name = 'Organizer'
SELECT T2.Score FROM posts AS T1 INNER JOIN comments AS T2 ON T1.Id = T2.PostId WHERE T1.CreationDate = '2010-07-19 19:19:56.0'
SELECT T2.Text FROM posts AS T1 INNER JOIN comments AS T2 ON T1.Id = T2.PostId WHERE T1.CreaionDate = '2010-07-19 19:37:33.0'
SELECT T2.Age FROM badges AS T1 INNER JOIN users AS T2 ON T1.UserId = T2.Id WHERE T2.Location = 'Vienna, Austria'
SELECT COUNT(DISTINCT T1.UserId) FROM badges AS T1 INNER JOIN users AS T2 ON T1.UserId = T2.Id WHERE T1.Name = 'Supporter' AND T2.Age BETWEEN 19 AND 65
SELECT SUM(T1.Views) FROM users AS T1 INNER JOIN badges AS T2 ON T1.Id = T2.UserId WHERE T2.Date = '2010-07-19 19:39:08.0'
SELECT T2.Name FROM users AS T1 INNER JOIN badges AS T2 ON T1.Id = T2.UserId WHERE T1.Reputation = ( SELECT MIN(Reputation) FROM users )
SELECT T1.Name FROM badges AS T1 INNER JOIN users AS T2 ON T1.UserId = T2.Id WHERE T2.DisplayName = 'Sharpie'
SELECT COUNT(T1.UserId) FROM badges AS T1 INNER JOIN users AS T2 ON T1.UserId = T2.Id WHERE T1.Name = 'Supporter' AND T2.Age > 65
SELECT DisplayName FROM users WHERE Id = 30 
SELECT COUNT(*) FROM users WHERE Location LIKE '%New York%'
SELECT COUNT(Id) FROM votes WHERE STRFTIME('%Y', CreationDate) = '2010'
SELECT COUNT(Id) FROM users WHERE Age BETWEEN 19 AND 65
SELECT DisplayName FROM users ORDER BY Views DESC LIMIT 1
SELECT CAST(SUM(CASE WHEN STRFTIME('%Y', CreationDate) = '2010' THEN 1 ELSE 0 END) AS REAL) / SUM(CASE WHEN STRFTIME('%Y', CreationDate) = '2011' THEN 1 ELSE 0 END) FROM votes
SELECT T2.TagName FROM posts AS T1 INNER JOIN tags AS T2 ON T1.Id = T2.ExcerptPostId INNER JOIN users AS T3 ON T1.OwnerUserId = T3.Id WHERE T3.DisplayName = 'John Stauffer'
SELECT COUNT(*) FROM posts WHERE OwnerUserId = (SELECT Id FROM users WHERE DisplayName = 'Daniel Vassallo')
SELECT COUNT(T2.Id) FROM users AS T1 INNER JOIN votes AS T2 ON T1.Id = T2.UserId WHERE T1.DisplayName = 'Harlan'
SELECT T1.Id FROM posts AS T1 INNER JOIN users AS T2 ON T1.OwnerUserId = T2.Id WHERE T2.DisplayName = 'slashnick' ORDER BY T1.AnswerCount DESC LIMIT 1 
SELECT DisplayName, MAX(ViewCount) AS Popularity FROM posts AS p INNER JOIN users AS u ON p.OwnerUserId = u.Id WHERE DisplayName IN ('Harvey Motulsky', 'Noah Snyder') GROUP BY DisplayName ORDER BY Popularity DESC LIMIT 1
SELECT COUNT(DISTINCT T1.Id) FROM posts AS T1 INNER JOIN users AS T2 ON T1.OwnerUserId = T2.Id INNER JOIN votes AS T3 ON T1.Id = T3.PostId WHERE T2.DisplayName = 'Matt Parker' GROUP BY T1.Id HAVING COUNT(T3.Id) > 4
SELECT COUNT(T2.Score) FROM users AS T1 INNER JOIN comments AS T2 ON T1.Id = T2.UserId INNER JOIN posts AS T3 ON T2.PostId = T3.Id WHERE T1.DisplayName = 'Neil McGuigan' AND T2.Score < 60
SELECT T2.TagName FROM posts AS T1 INNER JOIN tags AS T2 ON T1.Id = T2.ExcerptPostId INNER JOIN users AS T3 ON T1.OwnerUserId = T3.Id WHERE T3.DisplayName = 'Mark Meckes' AND T1.CommentCount = 0
SELECT T2.DisplayName FROM badges AS T1 INNER JOIN users AS T2 ON T1.UserId = T2.Id WHERE T1.Name = 'Organizer' 
SELECT CAST(SUM(CASE WHEN T2.TagName = 'r' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.Id) FROM posts AS T1 INNER JOIN tags AS T2 ON T1.Id = T2.ExcerptPostId INNER JOIN users AS T3 ON T1.OwnerUserId = T3.Id WHERE T3.DisplayName = 'Community'
SELECT (SUM(CASE WHEN T2.DisplayName = 'Mornington' THEN T1.ViewCount ELSE 0 END) - SUM(CASE WHEN T2.DisplayName = 'Amos' THEN T1.ViewCount ELSE 0 END)) AS ViewCountDifference FROM posts AS T1 INNER JOIN users AS T2 ON T1.OwnerUserId = T2.Id
SELECT COUNT(DISTINCT UserId) FROM badges WHERE Name = 'Commentator' AND YEAR(Date) = 2014; 
SELECT COUNT(Id) FROM posts WHERE CreationDate BETWEEN '2010-07-21 00:00:00' AND '2010-07-21 23:59:59'
SELECT DisplayName, Age FROM users WHERE Views = ( SELECT MAX(Views) FROM users )
SELECT LastEditDate, LastEditorUserId FROM posts WHERE Title = 'Detecting a given face in a database of facial images' 
SELECT COUNT(Id) FROM comments WHERE Score < 60 AND UserId = 13
SELECT T1.Title, T2.UserDisplayName FROM posts AS T1 INNER JOIN comments AS T2 ON T1.Id = T2.PostId WHERE T2.Score > 60 
SELECT T1.Name FROM badges AS T1 INNER JOIN users AS T2 ON T1.UserId = T2.Id WHERE STRFTIME('%Y', T1.Date) = '2011' AND T2.Location = 'North Pole'
SELECT T1.DisplayName, T1.WebsiteUrl FROM users AS T1 INNER JOIN posts AS T2 ON T1.Id = T2.OwnerUserId WHERE T2.FavoriteCount > 150 
SELECT COUNT(T1.Id) AS PostHistoryCount, MAX(T1.CreationDate) AS LastEditDate FROM postHistory AS T1 INNER JOIN posts AS T2 ON T1.PostId = T2.Id WHERE T2.Title = 'What is the best introductory Bayesian statistics textbook?'
SELECT T1.LastAccessDate, T1.Location FROM users AS T1 INNER JOIN badges AS T2 ON T1.Id = T2.UserId WHERE T2.Name = 'Outliers'
SELECT T2.Title FROM postLinks AS T1 INNER JOIN posts AS T2 ON T1.RelatedPostId = T2.Id WHERE T1.PostId = (SELECT Id FROM posts WHERE Title = 'How to tell if something happened in a data set which monitors a value over time')
SELECT T1.PostId, T2.Name FROM posts AS T1 INNER JOIN badges AS T2 ON T1.OwnerUserId = T2.UserId WHERE T1.OwnerDisplayName = 'Samuel' AND YEAR(T1.CreationDate) = 2013 AND YEAR(T2.Date) = 2013
SELECT T2.DisplayName FROM posts AS T1 INNER JOIN users AS T2 ON T1.OwnerUserId = T2.Id ORDER BY T1.ViewCount DESC LIMIT 1 
SELECT T2.DisplayName, T2.Location FROM tags AS T1 INNER JOIN users AS T2 ON T1.ExcerptPostId = T2.Id WHERE T1.TagName = 'hypothesis-testing'
SELECT T2.Title, T1.LinkTypeId FROM postLinks AS T1 INNER JOIN posts AS T2 ON T1.RelatedPostId = T2.Id WHERE T1.PostId = (SELECT Id FROM posts WHERE Title = 'What are principal component scores?')
SELECT T1.DisplayName FROM users AS T1 INNER JOIN posts AS T2 ON T1.Id = T2.OwnerUserId WHERE T2.Id = ( SELECT ParentId FROM posts WHERE Score = ( SELECT MAX(Score) FROM posts WHERE ParentId IS NOT NULL ) )
SELECT T2.DisplayName, T2.WebsiteUrl FROM votes AS T1 INNER JOIN users AS T2 ON T1.UserId = T2.Id WHERE T1.VoteTypeId = 8 ORDER BY T1.BountyAmount DESC LIMIT 1 
SELECT Title FROM posts ORDER BY ViewCount DESC LIMIT 5; 
SELECT COUNT(*) FROM tags WHERE Count BETWEEN 5000 AND 7000;
SELECT OwnerUserId FROM posts ORDER BY FavoriteCount DESC LIMIT 1 
SELECT Age FROM users WHERE Reputation = ( SELECT MAX(Reputation) FROM users )
SELECT COUNT(*) FROM posts AS T1 INNER JOIN votes AS T2 ON T1.Id = T2.PostId WHERE YEAR(T1.CreaionDate) = 2011 AND T2.BountyAmount = 50
SELECT Id FROM users ORDER BY Age ASC LIMIT 1
SELECT T1.Score FROM posts AS T1 INNER JOIN tags AS T2 ON T1.Id = T2.ExcerptPostId ORDER BY T2.Count DESC LIMIT 1 
SELECT CAST(COUNT(T1.Id) AS REAL) / 12 FROM postLinks AS T1 INNER JOIN posts AS T2 ON T1.PostId = T2.Id WHERE STRFTIME('%Y', T1.CreationDate) = '2010' AND T2.AnswerCount <= 2 
SELECT T1.PostId FROM votes AS T1 INNER JOIN posts AS T2 ON T1.PostId = T2.Id WHERE T1.UserId = 1465 ORDER BY T2.FavoriteCount DESC LIMIT 1
SELECT T2.Title FROM postLinks AS T1 INNER JOIN posts AS T2 ON T1.PostId = T2.Id ORDER BY T1.CreationDate ASC LIMIT 1 
SELECT T2.DisplayName FROM badges AS T1 INNER JOIN users AS T2 ON T1.UserId = T2.Id GROUP BY T1.UserId ORDER BY COUNT(T1.Name) DESC LIMIT 1 
SELECT MIN(CreationDate) FROM votes WHERE UserId = (SELECT Id FROM users WHERE DisplayName = 'chl')
SELECT MIN(posts.CreaionDate) FROM users INNER JOIN posts ON users.Id = posts.OwnerUserId ORDER BY users.Age DESC LIMIT 1
SELECT T2.DisplayName FROM badges AS T1 INNER JOIN users AS T2 ON T1.UserId = T2.Id WHERE T1.Name = 'Autobiographer' ORDER BY T1.Date ASC LIMIT 1 
SELECT COUNT(DISTINCT T1.Id) FROM users AS T1 INNER JOIN posts AS T2 ON T1.Id = T2.OwnerUserId WHERE T1.Location LIKE '%United Kingdom%' AND T2.FavoriteCount >= 4
SELECT AVG(T1.PostId) FROM votes AS T1 INNER JOIN users AS T2 ON T1.UserId = T2.Id WHERE T2.Age = (SELECT MAX(Age) FROM users) 
SELECT DisplayName FROM users ORDER BY Reputation DESC LIMIT 1
SELECT COUNT(Id) FROM users WHERE Reputation > 2000 AND Views > 1000;
SELECT DisplayName FROM users WHERE Age BETWEEN 19 AND 65
SELECT COUNT(*) FROM posts AS T1 INNER JOIN users AS T2 ON T1.OwnerUserId = T2.Id WHERE T2.DisplayName = 'Jay Stevens' AND YEAR(T1.CreationDate) = 2010
SELECT T1.Id, T1.Title FROM posts AS T1 INNER JOIN users AS T2 ON T1.OwnerUserId = T2.Id WHERE T2.DisplayName = 'Harvey Motulsky' ORDER BY T1.ViewCount DESC LIMIT 1
SELECT T1.Id, T1.Title FROM posts AS T1 INNER JOIN users AS T2 ON T1.OwnerUserId = T2.Id ORDER BY T1.Score DESC LIMIT 1
SELECT AVG(Score) FROM posts WHERE OwnerUserId = (SELECT Id FROM users WHERE DisplayName = 'Stephen Turner')
SELECT DISTINCT T2.DisplayName FROM posts AS T1 INNER JOIN users AS T2 ON T1.OwnerUserId = T2.Id WHERE STRFTIME('%Y', T1.CreationDate) = '2011' AND T1.ViewCount > 20000 
SELECT T1.Id, T2.DisplayName FROM posts AS T1 INNER JOIN users AS T2 ON T1.OwnerUserId = T2.Id WHERE STRFTIME('%Y', T1.CreationDate) = '2010' ORDER BY T1.FavoriteCount DESC LIMIT 1
SELECT CAST(COUNT(CASE WHEN T2.Reputation > 1000 THEN 1 END) AS REAL) * 100 / COUNT(T1.Id) FROM posts AS T1 INNER JOIN users AS T2 ON T1.OwnerUserId = T2.Id WHERE strftime('%Y', T1.CreaionDate) = '2011'
SELECT CAST(COUNT(CASE WHEN Age BETWEEN 13 AND 19 THEN 1 END) AS REAL) * 100 / COUNT(Id) FROM users 
SELECT T1.ViewCount, T2.DisplayName FROM posts AS T1 INNER JOIN users AS T2 ON T1.LastEditorUserId = T2.Id WHERE T1.Title = 'Computer Game Datasets'
SELECT COUNT(*) FROM posts WHERE ViewCount > ( SELECT AVG(ViewCount) FROM posts )
SELECT COUNT(*) FROM comments WHERE PostId = ( SELECT Id FROM posts ORDER BY Score DESC LIMIT 1 )
SELECT COUNT(*) FROM posts WHERE ViewCount > 35000 AND CommentCount = 0
SELECT T2.DisplayName, T2.Location FROM posts AS T1 INNER JOIN users AS T2 ON T1.LastEditorUserId = T2.Id WHERE T1.Id = 183 ORDER BY T1.LastEditDate DESC LIMIT 1 
SELECT Name FROM badges AS T1 INNER JOIN users AS T2 ON T1.UserId = T2.Id WHERE T2.DisplayName = 'Emmett' ORDER BY T1.Date DESC LIMIT 1 
SELECT COUNT(Id) FROM users WHERE Age BETWEEN 19 AND 65 AND UpVotes > 5000 
SELECT strftime('%J', T2.Date) - strftime('%J', T1.CreationDate) AS TimeToGetBadge FROM users AS T1 INNER JOIN badges AS T2 ON T1.Id = T2.UserId WHERE T1.DisplayName = 'Zolomon' 
SELECT (SELECT COUNT(*) FROM posts WHERE OwnerUserId = (SELECT Id FROM users ORDER BY CreationDate DESC LIMIT 1)) AS NumberOfPosts, (SELECT COUNT(*) FROM comments WHERE UserId = (SELECT Id FROM users ORDER BY CreationDate DESC LIMIT 1)) AS NumberOfComments
SELECT T1.Text, T2.DisplayName FROM comments AS T1 INNER JOIN users AS T2 ON T1.UserId = T2.Id INNER JOIN posts AS T3 ON T1.PostId = T3.Id WHERE T3.Title = 'Analysing wind data with R' ORDER BY T1.CreationDate DESC LIMIT 1 
SELECT COUNT(DISTINCT UserId) FROM badges WHERE Name = 'Citizen Patrol'
SELECT COUNT(*) FROM posts WHERE Tags LIKE '%<careers>%'
SELECT Reputation, Views FROM users WHERE DisplayName = 'Jarrod Dixon'
SELECT (SELECT COUNT(*) FROM comments WHERE PostId = (SELECT Id FROM posts WHERE Title = 'Clustering 1D data')) AS CommentCount, (SELECT COUNT(*) FROM posts WHERE PostTypeId = 2 AND ParentId = (SELECT Id FROM posts WHERE Title = 'Clustering 1D data')) AS AnswerCount
SELECT CreationDate FROM users WHERE DisplayName = 'IrishStat'
SELECT COUNT(*) FROM votes WHERE BountyAmount >= 30
SELECT CAST(COUNT(CASE WHEN T2.Score >= 50 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T2.Id) FROM (SELECT UserId, MAX(Reputation) FROM users) AS T1 INNER JOIN posts AS T2 ON T1.UserId = T2.OwnerUserId 
SELECT COUNT(Id) FROM posts WHERE Score < 20
SELECT COUNT(Id) FROM tags WHERE Id < 15 AND Count <= 20 
SELECT ExcerptPostId, WikiPostId FROM tags WHERE TagName = 'sample'
SELECT T2.Reputation, T2.UpVotes FROM comments AS T1 INNER JOIN users AS T2 ON T1.UserId = T2.Id WHERE T1.Text = 'fine, you win :)';
SELECT T2.Text FROM posts AS T1 INNER JOIN comments AS T2 ON T1.Id = T2.PostId WHERE T1.Title = 'How can I adapt ANOVA for binary data?' 
SELECT T2.Text FROM posts AS T1 INNER JOIN comments AS T2 ON T1.Id = T2.PostId WHERE T1.ViewCount BETWEEN 100 AND 150 ORDER BY T2.Score DESC LIMIT 1
SELECT T1.CreationDate, T1.Age FROM users AS T1 INNER JOIN comments AS T2 ON T1.Id = T2.UserId WHERE T2.Text LIKE '%http://%'
SELECT COUNT(DISTINCT T1.PostId) FROM comments AS T1 INNER JOIN posts AS T2 ON T1.PostId = T2.Id WHERE T1.Score = 0 AND T2.ViewCount < 5
SELECT COUNT(T2.Score) FROM posts AS T1 INNER JOIN comments AS T2 ON T1.Id = T2.PostId WHERE T1.CommentCount = 1 AND T2.Score = 0
SELECT COUNT(DISTINCT T2.UserId) FROM comments AS T1 INNER JOIN users AS T2 ON T1.UserId = T2.Id WHERE T1.Score = 0 AND T2.Age = 40
SELECT T1.PostId, T2.Text FROM posts AS T1 INNER JOIN comments AS T2 ON T1.Id = T2.PostId WHERE T1.Title = 'Group differences on a five point Likert item'
SELECT T2.UpVotes FROM comments AS T1 INNER JOIN users AS T2 ON T1.UserId = T2.Id WHERE T1.Text = 'R is also lazy evaluated.'
SELECT T1.Text FROM comments AS T1 INNER JOIN users AS T2 ON T1.UserId = T2.Id WHERE T2.DisplayName = 'Harvey Motulsky'
SELECT T2.DisplayName FROM comments AS T1 INNER JOIN users AS T2 ON T1.UserId = T2.Id WHERE T1.Score BETWEEN 1 AND 5 AND T2.DownVotes = 0 
SELECT CAST(SUM(CASE WHEN T2.UpVotes = 0 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.UserId) FROM comments AS T1 INNER JOIN users AS T2 ON T1.UserId = T2.Id WHERE T1.Score BETWEEN 5 AND 10
SELECT T2.power_name FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.id = T2.hero_id INNER JOIN superpower AS T3 ON T2.power_id = T3.id WHERE T1.superhero_name = '3-D Man'
SELECT COUNT(DISTINCT T1.hero_id) FROM hero_power AS T1 INNER JOIN superpower AS T2 ON T1.power_id = T2.id WHERE T2.power_name = 'Super Strength'
SELECT COUNT(DISTINCT T1.id) FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.id = T2.hero_id INNER JOIN superpower AS T3 ON T2.power_id = T3.id WHERE T3.power_name = 'Super Strength' AND T1.height_cm > 200
SELECT T1.full_name FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.id = T2.hero_id GROUP BY T1.full_name HAVING COUNT(T2.power_id) > 15
SELECT COUNT(superhero.id) FROM superhero INNER JOIN colour ON superhero.eye_colour_id = colour.id WHERE colour.colour = 'Blue' 
SELECT T2.colour FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.skin_colour_id = T2.id WHERE T1.superhero_name = 'Apocalypse'
SELECT COUNT(T1.id) FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.eye_colour_id = T2.id INNER JOIN hero_power AS T3 ON T1.id = T3.hero_id INNER JOIN superpower AS T4 ON T3.power_id = T4.id WHERE T2.colour = 'Blue' AND T4.power_name = 'Agility'
SELECT superhero.superhero_name FROM superhero INNER JOIN colour AS eye_colour ON superhero.eye_colour_id = eye_colour.id INNER JOIN colour AS hair_colour ON superhero.hair_colour_id = hair_colour.id WHERE eye_colour.colour = 'Blue' AND hair_colour.colour = 'Blond'
SELECT COUNT(*) FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.publisher_id = T2.id WHERE T2.publisher_name = 'Marvel Comics'
SELECT T1.full_name FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.publisher_id = T2.id WHERE T2.publisher_name = 'Marvel Comics' ORDER BY T1.height_cm DESC LIMIT 1
SELECT T3.publisher_name FROM superhero AS T1 INNER JOIN publisher AS T3 ON T1.publisher_id = T3.id WHERE T1.superhero_name = 'Sauron'
SELECT COUNT(*) FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.eye_colour_id = T2.id INNER JOIN publisher AS T3 ON T1.publisher_id = T3.id WHERE T2.colour = 'Blue' AND T3.publisher_name = 'Marvel Comics'
SELECT AVG(T1.height_cm) FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.publisher_id = T2.id WHERE T2.publisher_name = 'Marvel Comics'
SELECT CAST(COUNT(CASE WHEN T4.power_name = 'Super Strength' THEN T1.id ELSE NULL END) AS REAL) * 100 / COUNT(T1.id) FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.publisher_id = T2.id INNER JOIN hero_power AS T3 ON T1.id = T3.hero_id INNER JOIN superpower AS T4 ON T3.power_id = T4.id WHERE T2.publisher_name = 'Marvel Comics'
SELECT COUNT(DISTINCT T1.id) FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.publisher_id = T2.id WHERE T2.publisher_name = 'DC Comics'
SELECT T3.publisher_name FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.id = T2.hero_id INNER JOIN publisher AS T3 ON T1.publisher_id = T3.id INNER JOIN attribute AS T4 ON T2.attribute_id = T4.id WHERE T4.attribute_name = 'Speed' ORDER BY T2.attribute_value ASC LIMIT 1
SELECT COUNT(T1.id) FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.eye_colour_id = T2.id INNER JOIN publisher AS T3 ON T1.publisher_id = T3.id WHERE T2.colour = 'Gold' AND T3.publisher_name = 'Marvel Comics'
SELECT T2.publisher_name FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.publisher_id = T2.id WHERE T1.superhero_name = 'Blue Beetle II'
SELECT COUNT(*) FROM superhero AS s INNER JOIN colour AS c ON s.hair_colour_id = c.id WHERE c.colour = 'Blond'
SELECT T1.superhero_name FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.id = T2.hero_id INNER JOIN attribute AS T3 ON T2.attribute_id = T3.id WHERE T3.attribute_name = 'Intelligence' ORDER BY T2.attribute_value ASC LIMIT 1
SELECT T2.race FROM superhero AS T1 INNER JOIN race AS T2 ON T1.race_id = T2.id WHERE T1.superhero_name = 'Copycat'
SELECT COUNT(DISTINCT superhero_id) FROM superhero INNER JOIN hero_attribute ON superhero.id = hero_attribute.hero_id INNER JOIN attribute ON hero_attribute.attribute_id = attribute.id WHERE attribute.attribute_name = 'Durability' AND hero_attribute.attribute_value < 50
SELECT T1.superhero_name FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.id = T2.hero_id INNER JOIN superpower AS T3 ON T2.power_id = T3.id WHERE T3.power_name = 'Death Touch'
SELECT COUNT(DISTINCT superhero.id) FROM superhero INNER JOIN gender ON superhero.gender_id = gender.id INNER JOIN hero_attribute ON superhero.id = hero_attribute.hero_id INNER JOIN attribute ON hero_attribute.attribute_id = attribute.id WHERE gender.gender = 'Female' AND attribute.attribute_name = 'Strength' AND hero_attribute.attribute_value = 100
SELECT T1.superhero_name FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.id = T2.hero_id GROUP BY T1.superhero_name ORDER BY COUNT(T2.power_id) DESC LIMIT 1
SELECT COUNT(T1.id) FROM superhero AS T1 INNER JOIN race AS T2 ON T1.race_id = T2.id WHERE T2.race = 'Vampire'
SELECT CAST(SUM(CASE WHEN T1.alignment = 'Bad' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T2.id) AS "percentage", COUNT(CASE WHEN T1.alignment = 'Bad' AND T3.publisher_name = 'Marvel Comics' THEN 1 ELSE 0 END) AS "number" FROM alignment AS T1 INNER JOIN superhero AS T2 ON T1.id = T2.alignment_id INNER JOIN publisher AS T3 ON T3.id = T2.publisher_id
SELECT (SELECT COUNT(*) FROM superhero WHERE publisher_id = (SELECT id FROM publisher WHERE publisher_name = 'Marvel Comics')) - (SELECT COUNT(*) FROM superhero WHERE publisher_id = (SELECT id FROM publisher WHERE publisher_name = 'DC Comics')) AS difference FROM superhero
SELECT id FROM publisher WHERE publisher_name = 'Star Trek'
SELECT AVG(attribute_value) FROM hero_attribute
SELECT COUNT(id) FROM superhero WHERE full_name IS NULL
SELECT T2.colour FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.eye_colour_id = T2.id WHERE T1.id = 75 
SELECT T2.power_name FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.id = T2.hero_id INNER JOIN superpower AS T3 ON T2.power_id = T3.id WHERE T1.superhero_name = 'Deathlok'
SELECT AVG(weight_kg) FROM superhero WHERE gender_id = 2 
SELECT T2.power_name FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.id = T2.hero_id INNER JOIN gender AS T3 ON T1.gender_id = T3.id WHERE T3.gender = 'Male' LIMIT 5 
SELECT T1.superhero_name FROM superhero AS T1 INNER JOIN race AS T2 ON T1.race_id = T2.id WHERE T2.race = 'Alien'
SELECT superhero_name FROM superhero WHERE height_cm BETWEEN 170 AND 190 AND eye_colour_id IS NULL 
SELECT T2.power_name FROM hero_power AS T1 INNER JOIN superpower AS T2 ON T1.power_id = T2.id WHERE T1.hero_id = 56
SELECT full_name FROM superhero AS T1 INNER JOIN race AS T2 ON T1.race_id = T2.id WHERE T2.race = 'Demi-God' LIMIT 5
SELECT COUNT(superhero_id) FROM superhero WHERE alignment_id = (SELECT id FROM alignment WHERE alignment = 'Bad')
SELECT T2.race FROM superhero AS T1 INNER JOIN race AS T2 ON T1.race_id = T2.id WHERE T1.weight_kg = 169
SELECT T2.colour FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.hair_colour_id = T2.id INNER JOIN race AS T3 ON T1.race_id = T3.id WHERE T1.height_cm = 185 AND T3.race = 'human'
SELECT T2.colour FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.eye_colour_id = T2.id ORDER BY T1.weight_kg DESC LIMIT 1
SELECT CAST(COUNT(CASE WHEN T2.publisher_name = 'Marvel Comics' THEN T1.id ELSE NULL END) AS REAL) * 100 / COUNT(T1.id) FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.publisher_id = T2.id WHERE T1.height_cm BETWEEN 150 AND 180
SELECT DISTINCT T1.full_name FROM superhero AS T1 INNER JOIN gender AS T2 ON T1.gender_id = T2.id WHERE T2.gender = 'M' AND T1.weight_kg > ( SELECT AVG(weight_kg) * 0.79 FROM superhero )
SELECT T2.power_name FROM hero_power AS T1 INNER JOIN superpower AS T2 ON T1.power_id = T2.id GROUP BY T2.power_name ORDER BY COUNT(T1.hero_id) DESC LIMIT 1
SELECT T2.attribute_name, T1.attribute_value FROM hero_attribute AS T1 INNER JOIN attribute AS T2 ON T1.attribute_id = T2.id INNER JOIN superhero AS T3 ON T1.hero_id = T3.id WHERE T3.superhero_name = 'Abomination'
SELECT T2.power_name FROM hero_power AS T1 INNER JOIN superpower AS T2 ON T1.power_id = T2.id WHERE T1.hero_id = 1
SELECT COUNT(DISTINCT T1.hero_id) FROM hero_power AS T1 INNER JOIN superpower AS T2 ON T1.power_id = T2.id WHERE T2.power_name = 'stealth'
SELECT T1.full_name FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.id = T2.hero_id INNER JOIN attribute AS T3 ON T2.attribute_id = T3.id WHERE T3.attribute_name = 'strength' ORDER BY T2.attribute_value DESC LIMIT 1
SELECT CAST(COUNT(CASE WHEN T2.id = 1 THEN T1.id ELSE NULL END) AS REAL) / COUNT(T1.id) FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.skin_colour_id = T2.id
SELECT COUNT(DISTINCT T1.id) FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.publisher_id = T2.id WHERE T2.publisher_name = 'Dark Horse Comics'
SELECT T1.superhero_name FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.id = T2.hero_id INNER JOIN attribute AS T3 ON T2.attribute_id = T3.id INNER JOIN publisher AS T4 ON T1.publisher_id = T4.id WHERE T3.attribute_name = 'durability' AND T4.publisher_name = 'Dark Horse Comics' ORDER BY T2.attribute_value DESC LIMIT 1
SELECT T2.colour FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.eye_colour_id = T2.id WHERE T1.full_name = 'Abraham Sapien'
SELECT T1.superhero_name FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.id = T2.hero_id INNER JOIN superpower AS T3 ON T2.power_id = T3.id WHERE T3.power_name = 'Flight'
SELECT T2.colour AS eye_colour, T3.colour AS hair_colour, T4.colour AS skin_colour FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.eye_colour_id = T2.id INNER JOIN colour AS T3 ON T1.hair_colour_id = T3.id INNER JOIN colour AS T4 ON T1.skin_colour_id = T4.id INNER JOIN gender AS T5 ON T1.gender_id = T5.id INNER JOIN publisher AS T6 ON T1.publisher_id = T6.id WHERE T5.gender = 'Female' AND T6.publisher_name = 'Dark Horse Comics'
SELECT T1.superhero_name, T2.publisher_name FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.publisher_id = T2.id WHERE T1.hair_colour_id = T1.skin_colour_id AND T1.hair_colour_id = T1.eye_colour_id
SELECT T2.race FROM superhero AS T1 INNER JOIN race AS T2 ON T1.race_id = T2.id WHERE T1.superhero_name = 'A-Bomb'
SELECT CAST(SUM(CASE WHEN T2.colour = 'Blue' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.gender_id) FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.eye_colour_id = T2.id WHERE T1.gender_id = (SELECT id FROM gender WHERE gender = 'Female')
SELECT T1.superhero_name, T3.race FROM superhero AS T1 INNER JOIN race AS T3 ON T1.race_id = T3.id WHERE T1.full_name = 'Charles Chandler'
SELECT T2.gender FROM superhero AS T1 INNER JOIN gender AS T2 ON T1.gender_id = T2.id WHERE T1.superhero_name = 'Agent 13' 
SELECT T1.superhero_name FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.id = T2.hero_id INNER JOIN superpower AS T3 ON T2.power_id = T3.id WHERE T3.power_name = 'Adaptation'
SELECT COUNT(power_id) FROM hero_power WHERE hero_id = (SELECT id FROM superhero WHERE superhero_name = 'Amazo')
SELECT T2.power_name FROM superhero AS T1 INNER JOIN hero_power AS T3 ON T1.id = T3.hero_id INNER JOIN superpower AS T2 ON T3.power_id = T2.id WHERE T1.full_name = 'Hunter Zolomon'
SELECT superhero.superhero_name, superhero.height_cm FROM superhero INNER JOIN colour ON superhero.eye_colour_id = colour.id WHERE colour.colour = 'Amber'
SELECT T1.superhero_name FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.eye_colour_id = T2.id INNER JOIN colour AS T3 ON T1.hair_colour_id = T3.id WHERE T2.colour = 'Black' AND T3.colour = 'Black'
SELECT T2.colour AS eye_colour FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.eye_colour_id = T2.id INNER JOIN colour AS T3 ON T1.skin_colour_id = T3.id WHERE T3.colour = 'Gold' 
SELECT superhero.full_name FROM superhero INNER JOIN race ON superhero.race_id = race.id WHERE race.race = 'Vampire'
SELECT T1.superhero_name FROM superhero AS T1 INNER JOIN alignment AS T2 ON T1.alignment_id = T2.id WHERE T2.alignment = 'Neutral'
SELECT COUNT(hero_id) FROM hero_attribute AS T1 INNER JOIN attribute AS T2 ON T1.attribute_id = T2.id WHERE T2.attribute_name = 'Strength' AND T1.attribute_value = ( SELECT MAX(attribute_value) FROM hero_attribute WHERE attribute_id = ( SELECT id FROM attribute WHERE attribute_name = 'Strength' ) )
SELECT T3.race, T4.alignment FROM superhero AS T1 INNER JOIN race AS T3 ON T1.race_id = T3.id INNER JOIN alignment AS T4 ON T1.alignment_id = T4.id WHERE T1.superhero_name = 'Cameron Hicks'
SELECT CAST(COUNT(CASE WHEN T2.gender = 'Female' THEN 1 ELSE NULL END) AS REAL) * 100 / COUNT(T1.publisher_name) FROM publisher AS T1 INNER JOIN superhero AS T2 ON T1.id = T2.publisher_id WHERE T1.publisher_name = 'Marvel Comics'
SELECT AVG(weight_kg) FROM superhero AS T1 INNER JOIN race AS T2 ON T1.race_id = T2.id WHERE T2.race = 'Alien';
SELECT (SUM(CASE WHEN T.full_name = 'Emil Blonsky' THEN T.weight_kg ELSE 0 END) - SUM(CASE WHEN T.full_name = 'Charles Chandler' THEN T.weight_kg ELSE 0 END)) AS weight_difference FROM superhero AS T
SELECT superhero_name, AVG(height_cm) FROM superhero GROUP BY superhero_name;
SELECT T2.power_name FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.id = T2.hero_id INNER JOIN superpower AS T3 ON T2.power_id = T3.id WHERE T1.superhero_name = 'Abomination'
SELECT COUNT(*) FROM superhero INNER JOIN race ON superhero.race_id = race.id INNER JOIN gender ON superhero.gender_id = gender.id WHERE race.race = 'god/eternal' AND gender.gender = 'Male'
SELECT T1.superhero_name FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.id = T2.hero_id INNER JOIN attribute AS T3 ON T2.attribute_id = T3.id WHERE T3.attribute_name = 'Speed' ORDER BY T2.attribute_value DESC LIMIT 1
SELECT COUNT(id) FROM superhero WHERE alignment_id = 3 
SELECT T2.attribute_name, T3.attribute_value FROM superhero AS T1 INNER JOIN attribute AS T2 ON T1.id = T2.id INNER JOIN hero_attribute AS T3 ON T1.id = T3.hero_id WHERE T1.superhero_name = '3-D Man'
SELECT T1.superhero_name FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.eye_colour_id = T2.id INNER JOIN colour AS T3 ON T1.hair_colour_id = T3.id WHERE T2.colour = 'Blue' AND T3.colour = 'Brown'
SELECT T2.publisher_name FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.publisher_id = T2.id WHERE T1.superhero_name IN ('Hawkman', 'Karate Kid', 'Speedy')
SELECT COUNT(id) FROM superhero WHERE publisher_id IS NULL 
SELECT CAST(SUM(CASE WHEN eye_colour_id = 7 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(id) AS percentage FROM superhero 
SELECT CAST(SUM(CASE WHEN gender_id = 1 THEN 1 ELSE 0 END) AS REAL) / SUM(CASE WHEN gender_id = 2 THEN 1 ELSE 0 END) FROM superhero 
SELECT superhero_name FROM superhero ORDER BY height_cm DESC LIMIT 1 
SELECT id FROM superpower WHERE power_name = 'cryokinesis'
SELECT superhero_name FROM superhero WHERE id = 294 
SELECT full_name FROM superhero WHERE weight_kg = 0 OR weight_kg IS NULL
SELECT T2.colour FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.eye_colour_id = T2.id WHERE T1.full_name = 'Karen Beecher-Duncan'
SELECT T3.power_name FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.id = T2.hero_id INNER JOIN superpower AS T3 ON T2.power_id = T3.id WHERE T1.full_name = 'Helen Parr'
SELECT T2.race FROM superhero AS T1 INNER JOIN race AS T2 ON T1.race_id = T2.id WHERE T1.weight_kg = 108 AND T1.height_cm = 188 
SELECT T2.publisher_name FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.publisher_id = T2.id WHERE T1.id = 38 
SELECT T3.race FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.id = T2.hero_id INNER JOIN race AS T3 ON T1.race_id = T3.id WHERE T2.attribute_value = ( SELECT MAX(attribute_value) FROM hero_attribute )
SELECT T1.alignment, T3.power_name FROM alignment AS T1 INNER JOIN superhero AS T2 ON T1.id = T2.alignment_id INNER JOIN hero_power AS T4 ON T2.id = T4.hero_id INNER JOIN superpower AS T3 ON T4.power_id = T3.id WHERE T2.superhero_name = 'Atom IV'
SELECT superhero.full_name FROM superhero INNER JOIN colour ON superhero.eye_colour_id = colour.id WHERE colour.colour = 'Blue' LIMIT 5 
SELECT AVG(attribute_value) FROM hero_attribute WHERE hero_id IN (SELECT id FROM superhero WHERE alignment_id = (SELECT id FROM alignment WHERE alignment = 'Neutral'))
SELECT T2.colour FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.skin_colour_id = T2.id INNER JOIN hero_attribute AS T3 ON T1.id = T3.hero_id WHERE T3.attribute_value = 100 
SELECT COUNT(*) FROM superhero WHERE alignment_id = 1 AND gender_id = 2
SELECT DISTINCT T2.superhero_name FROM hero_attribute AS T1 INNER JOIN superhero AS T2 ON T1.hero_id = T2.id WHERE T1.attribute_value BETWEEN 75 AND 80
SELECT T3.race FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.hair_colour_id = T2.id INNER JOIN race AS T3 ON T1.race_id = T3.id INNER JOIN gender AS T4 ON T1.gender_id = T4.id WHERE T2.colour = 'blue' AND T4.gender = 'male'
SELECT CAST(SUM(CASE WHEN T2.gender_id = 2 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.alignment_id) FROM superhero AS T1 INNER JOIN gender AS T2 ON T1.gender_id = T2.id WHERE T1.alignment_id = 2 
SELECT SUM(CASE WHEN T1.eye_colour_id = 7 THEN 1 ELSE 0 END) - SUM(CASE WHEN T1.eye_colour_id = 1 THEN 1 ELSE 0 END) AS dif FROM superhero AS T1 WHERE T1.weight_kg IS NULL OR T1.weight_kg = 0
SELECT T2.attribute_value FROM superhero AS T1 INNER JOIN hero_attribute AS T2 ON T1.id = T2.hero_id INNER JOIN attribute AS T3 ON T2.attribute_id = T3.id WHERE T1.superhero_name = 'Hulk' AND T3.attribute_name = 'Strength'
SELECT T2.power_name FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.id = T2.hero_id INNER JOIN superpower AS T3 ON T2.power_id = T3.id WHERE T1.superhero_name = 'Ajax'
SELECT COUNT(*) FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.skin_colour_id = T2.id INNER JOIN alignment AS T3 ON T1.alignment_id = T3.id WHERE T2.colour = 'Green' AND T3.alignment = 'Bad' 
SELECT COUNT(*) FROM superhero AS T1 INNER JOIN gender AS T2 ON T1.gender_id = T2.id INNER JOIN publisher AS T3 ON T1.publisher_id = T3.id WHERE T2.gender = 'Female' AND T3.publisher_name = 'Marvel Comics'
SELECT T1.superhero_name FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.id = T2.hero_id INNER JOIN superpower AS T3 ON T2.power_id = T3.id WHERE T3.power_name = 'Wind Control' ORDER BY T1.superhero_name ASC
SELECT T2.gender FROM superhero AS T1 INNER JOIN gender AS T2 ON T1.gender_id = T2.id INNER JOIN hero_power AS T3 ON T1.id = T3.hero_id INNER JOIN superpower AS T4 ON T3.power_id = T4.id WHERE T4.power_name = 'Phoenix Force'
SELECT T1.superhero_name FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.publisher_id = T2.id WHERE T2.publisher_name = 'DC Comics' ORDER BY T1.weight_kg DESC LIMIT 1
SELECT AVG(height_cm) FROM superhero AS T1 INNER JOIN race AS T2 ON T1.race_id = T2.id INNER JOIN publisher AS T3 ON T1.publisher_id = T3.id WHERE T2.race <> 'Human' AND T3.publisher_name = 'Dark Horse Comics'
SELECT COUNT(superhero.superhero_name) FROM superhero INNER JOIN hero_attribute ON superhero.id = hero_attribute.hero_id INNER JOIN attribute ON hero_attribute.attribute_id = attribute.id WHERE attribute.attribute_name = 'Speed' AND hero_attribute.attribute_value = 100
SELECT (SELECT COUNT(*) FROM superhero WHERE publisher_id = (SELECT id FROM publisher WHERE publisher_name = 'DC Comics')) - (SELECT COUNT(*) FROM superhero WHERE publisher_id = (SELECT id FROM publisher WHERE publisher_name = 'Marvel Comics')) AS difference FROM superhero
SELECT T2.attribute_name FROM hero_attribute AS T1 INNER JOIN attribute AS T2 ON T1.attribute_id = T2.id INNER JOIN superhero AS T3 ON T1.hero_id = T3.id WHERE T3.superhero_name = 'Black Panther' ORDER BY T1.attribute_value LIMIT 1
SELECT T2.colour FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.eye_colour_id = T2.id WHERE T1.superhero_name = 'Abomination'
SELECT superhero_name FROM superhero ORDER BY height_cm DESC LIMIT 1 
SELECT superhero_name FROM superhero WHERE full_name = 'Charles Chandler'
SELECT CAST(SUM(CASE WHEN T2.gender = 'Female' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.superhero_name) FROM superhero AS T1 INNER JOIN gender AS T2 ON T1.gender_id = T2.id INNER JOIN publisher AS T3 ON T1.publisher_id = T3.id WHERE T3.publisher_name = 'George Lucas'
SELECT CAST(SUM(CASE WHEN T4.alignment = 'Good' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.id) FROM superhero AS T1 INNER JOIN publisher AS T2 ON T1.publisher_id = T2.id INNER JOIN alignment AS T4 ON T1.alignment_id = T4.id WHERE T2.publisher_name = 'Marvel Comics'
SELECT COUNT(*) FROM superhero WHERE full_name LIKE 'John%'
SELECT hero_id FROM hero_attribute ORDER BY attribute_value LIMIT 1 
SELECT full_name FROM superhero WHERE superhero_name = 'Alien'
SELECT T1.full_name FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.eye_colour_id = T2.id WHERE T1.weight_kg < 100 AND T2.colour = 'Brown'
SELECT T2.attribute_name, T1.attribute_value FROM hero_attribute AS T1 INNER JOIN attribute AS T2 ON T1.attribute_id = T2.id INNER JOIN superhero AS T3 ON T1.hero_id = T3.id WHERE T3.superhero_name = 'Aquababy'
SELECT T1.weight_kg, T2.race FROM superhero AS T1 INNER JOIN race AS T2 ON T1.race_id = T2.id WHERE T1.id = 40
SELECT AVG(height_cm) FROM superhero AS T1 INNER JOIN alignment AS T2 ON T1.alignment_id = T2.id WHERE T2.alignment = 'Neutral'
SELECT T1.hero_id FROM hero_power AS T1 INNER JOIN superpower AS T2 ON T1.power_id = T2.id WHERE T2.power_name = 'Intelligence'
SELECT T2.colour FROM superhero AS T1 INNER JOIN colour AS T2 ON T1.eye_colour_id = T2.id WHERE T1.superhero_name = 'Blackwulf'
SELECT DISTINCT T3.power_name FROM superhero AS T1 INNER JOIN hero_power AS T2 ON T1.id = T2.hero_id INNER JOIN superpower AS T3 ON T2.power_id = T3.id WHERE T1.height_cm > 0.8 * ( SELECT AVG(height_cm) FROM superhero )
SELECT T1.driverRef FROM drivers AS T1 INNER JOIN qualifying AS T2 ON T1.driverId = T2.driverId WHERE T2.raceId = 18 ORDER BY T2.q1 DESC LIMIT 5 
SELECT drivers.surname FROM drivers INNER JOIN qualifying ON drivers.driverId = qualifying.driverId WHERE qualifying.raceId = 19 ORDER BY qualifying.q2 ASC LIMIT 1; 
SELECT T1.year FROM races AS T1 INNER JOIN circuits AS T2 ON T1.circuitId = T2.circuitId WHERE T2.location = 'Shanghai'
SELECT url FROM circuits WHERE name = 'Circuit de Barcelona-Catalunya'
SELECT races.name FROM races INNER JOIN circuits ON races.circuitId = circuits.circuitId WHERE circuits.country = 'Germany'
SELECT T1.name, T1.location, T1.country FROM circuits AS T1 INNER JOIN races AS T2 ON T1.circuitId = T2.circuitId INNER JOIN constructors AS T3 ON T2.raceId = T3.constructorId WHERE T3.name = 'Renault'
SELECT COUNT(raceId) FROM races INNER JOIN circuits ON races.circuitId = circuits.circuitId WHERE year = 2010 AND NOT (circuits.location IN ('Asia', 'Europe'))
SELECT races.name FROM races INNER JOIN circuits ON races.circuitId = circuits.circuitId WHERE circuits.country = 'Spain'
SELECT lat, lng FROM circuits WHERE name LIKE '%Australian Grand Prix%'
SELECT url FROM races INNER JOIN circuits ON races.circuitId = circuits.circuitId WHERE circuits.name = 'Sepang International Circuit'
SELECT races.time FROM races INNER JOIN circuits ON races.circuitId = circuits.circuitId WHERE circuits.name = 'Sepang International Circuit'
SELECT lat, lng FROM circuits WHERE name = 'Abu Dhabi Grand Prix'
SELECT T3.country FROM constructorResults AS T1 INNER JOIN constructors AS T2 ON T1.constructorId = T2.constructorId INNER JOIN circuits AS T3 ON T3.circuitId = T1.raceId WHERE T1.points = 1 AND T1.raceId = 24 
SELECT q1 FROM qualifying WHERE driverId = (SELECT driverId FROM drivers WHERE forename = 'Bruno' AND surname = 'Senna') AND raceId = 354
SELECT T1.nationality FROM drivers AS T1 INNER JOIN qualifying AS T2 ON T1.driverId = T2.driverId WHERE T2.q2 = '0:01:40' AND T2.raceId = 355
SELECT T1.number FROM drivers AS T1 INNER JOIN qualifying AS T2 ON T1.driverId = T2.driverId WHERE T2.q3 = '0:01:54' AND T2.raceId = 903
SELECT COUNT(T1.driverId) FROM results AS T1 INNER JOIN races AS T2 ON T1.raceId = T2.raceId WHERE T2.name = 'Bahrain Grand Prix' AND T2.year = 2007 AND T1.time IS NULL
SELECT T2.url FROM races AS T1 INNER JOIN seasons AS T2 ON T1.year = T2.year WHERE T1.raceId = 901 
SELECT COUNT(driverId) FROM results WHERE raceId = (SELECT raceId FROM races WHERE date = '2015-11-29') AND time IS NOT NULL 
SELECT T1.forename, T1.surname FROM drivers AS T1 INNER JOIN results AS T2 ON T1.driverId = T2.driverId WHERE T2.raceId = 592 AND T2.time IS NOT NULL ORDER BY T1.dob LIMIT 1
SELECT T1.url FROM drivers AS T1 INNER JOIN lapTimes AS T2 ON T1.driverId = T2.driverId WHERE T2.time = '0:01:27' AND T2.raceId = 161 
SELECT T2.nationality FROM results AS T1 INNER JOIN drivers AS T2 ON T1.driverId = T2.driverId WHERE T1.raceId = 933 ORDER BY T1.fastestLapSpeed DESC LIMIT 1
SELECT T1.lat, T1.lng FROM circuits AS T1 INNER JOIN races AS T2 ON T1.circuitId = T2.circuitId WHERE T2.name = 'Malaysian Grand Prix'
SELECT T2.url FROM constructorResults AS T1 INNER JOIN constructors AS T2 ON T1.constructorId = T2.constructorId WHERE T1.raceId = 9 ORDER BY T1.points DESC LIMIT 1 
SELECT q1 FROM qualifying WHERE driverId = (SELECT driverId FROM drivers WHERE forename = 'Lucas' AND surname = 'di Grassi') AND raceId = 345 
SELECT T2.nationality FROM qualifying AS T1 INNER JOIN drivers AS T2 ON T1.driverId = T2.driverId WHERE T1.q2 = '0:01:15' AND T1.raceId = 347
SELECT T1.code FROM drivers AS T1 INNER JOIN qualifying AS T2 ON T1.driverId = T2.driverId WHERE T2.raceId = 45 AND T2.q3 = '0:01:33'
SELECT T1.time FROM results AS T1 INNER JOIN drivers AS T2 ON T1.driverId = T2.driverId WHERE T2.surname = 'McLaren' AND T1.raceId = 743 
SELECT T1.forename, T1.surname FROM drivers AS T1 INNER JOIN results AS T2 ON T1.driverId = T2.driverId INNER JOIN races AS T3 ON T2.raceId = T3.raceId WHERE T3.name = 'San Marino Grand Prix' AND T3.year = 2006 AND T2.position = 2
SELECT T2.url FROM races AS T1 INNER JOIN seasons AS T2 ON T1.year = T2.year WHERE T1.raceId = 901 
SELECT COUNT(driverId) FROM results WHERE raceId IN (SELECT raceId FROM races WHERE date = '2015-11-29') AND statusId IN (SELECT statusId FROM status WHERE status = 'Finished')
SELECT T1.forename, T1.surname FROM drivers AS T1 INNER JOIN results AS T2 ON T1.driverId = T2.driverId WHERE T2.raceId = 872 AND T2.time IS NOT NULL ORDER BY T1.dob DESC LIMIT 1 
SELECT T2.forename, T2.surname FROM lapTimes AS T1 INNER JOIN drivers AS T2 ON T1.driverId = T2.driverId WHERE T1.raceId = 348 ORDER BY T1.time LIMIT 1 
SELECT T1.nationality FROM drivers AS T1 INNER JOIN results AS T2 ON T1.driverId = T2.driverId WHERE T2.fastestLapSpeed = ( SELECT MAX(fastestLapSpeed) FROM results )
SELECT (CAST(T1.fastestLapSpeed AS REAL) - CAST(T2.fastestLapSpeed AS REAL)) * 100 / CAST(T1.fastestLapSpeed AS REAL) AS percentage FROM results AS T1 INNER JOIN results AS T2 ON T1.driverId = T2.driverId WHERE T1.driverId = (SELECT driverId FROM drivers WHERE forename = 'Paul' AND surname = 'di Resta') AND T1.raceId = 853 AND T2.raceId = 854
SELECT CAST(SUM(CASE WHEN T2.time IS NOT NULL THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T2.driverId) FROM races AS T1 INNER JOIN results AS T2 ON T1.raceId = T2.raceId WHERE T1.date = '1983-07-16'
SELECT MIN(year) FROM races WHERE name = 'Singapore Grand Prix'
SELECT COUNT(raceId), name FROM races WHERE year = 2005 ORDER BY name DESC
SELECT name FROM races WHERE strftime('%Y-%m', date) = (SELECT strftime('%Y-%m', MIN(date)) FROM races)
SELECT name, date FROM races WHERE year = 1999 ORDER BY round DESC LIMIT 1
SELECT year FROM races GROUP BY year ORDER BY COUNT(raceId) DESC LIMIT 1 
SELECT T1.name FROM races AS T1 WHERE T1.year = 2017 AND T1.name NOT IN (SELECT T2.name FROM races AS T2 WHERE T2.year = 2000)
SELECT T1.country, T1.name, T1.location FROM circuits AS T1 INNER JOIN races AS T2 ON T1.circuitId = T2.circuitId WHERE T2.name = 'European Grand Prix' ORDER BY T2.year ASC LIMIT 1 
SELECT MAX(T1.year) FROM seasons AS T1 INNER JOIN races AS T2 ON T1.year = T2.year INNER JOIN circuits AS T3 ON T2.circuitId = T3.circuitId WHERE T3.name = 'Brands Hatch' AND T2.name = 'British Grand Prix'
SELECT COUNT(DISTINCT T3.year) FROM races AS T1 INNER JOIN circuits AS T2 ON T1.circuitId = T2.circuitId INNER JOIN seasons AS T3 ON T1.year = T3.year WHERE T2.name = 'Silverstone Circuit' AND T1.name = 'British Grand Prix'
SELECT T1.forename, T1.surname, T3.positionOrder FROM drivers AS T1 INNER JOIN results AS T3 ON T1.driverId = T3.driverId INNER JOIN races AS T2 ON T3.raceId = T2.raceId WHERE T2.year = 2010 AND T2.name = 'Singapore Grand Prix' ORDER BY T3.positionOrder
SELECT T1.forename, T1.surname, T2.points FROM drivers AS T1 INNER JOIN driverStandings AS T2 ON T1.driverId = T2.driverId ORDER BY T2.points DESC LIMIT 1 
SELECT drivers.forename, drivers.surname, results.points FROM results INNER JOIN drivers ON results.driverId = drivers.driverId INNER JOIN races ON results.raceId = races.raceId WHERE races.name = 'Chinese Grand Prix' AND races.year = 2017 ORDER BY results.points DESC LIMIT 3
SELECT T1.time, T2.forename, T2.surname, T3.name FROM lapTimes AS T1 INNER JOIN drivers AS T2 ON T1.driverId = T2.driverId INNER JOIN races AS T3 ON T1.raceId = T3.raceId WHERE T1.time = ( SELECT MIN(time) FROM lapTimes )
SELECT AVG(lapTimes.time) FROM lapTimes INNER JOIN drivers ON lapTimes.driverId = drivers.driverId INNER JOIN races ON lapTimes.raceId = races.raceId WHERE drivers.forename = 'Sebastian' AND drivers.surname = 'Vettel' AND races.name = 'Chinese Grand Prix' AND races.year = 2009
SELECT CAST(SUM(CASE WHEN T2.position > 1 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T2.position) FROM drivers AS T1 INNER JOIN results AS T2 ON T1.driverId = T2.driverId INNER JOIN races AS T3 ON T2.raceId = T3.raceId WHERE T1.surname = 'Hamilton' AND T3.year >= 2010 
SELECT T1.forename, T1.surname, T1.nationality, AVG(T2.points) FROM drivers AS T1 INNER JOIN driverStandings AS T2 ON T1.driverId = T2.driverId GROUP BY T1.driverId ORDER BY COUNT(T2.wins) DESC LIMIT 1 
SELECT forename, surname, STRFTIME('%Y', CURRENT_TIMESTAMP) - STRFTIME('%Y', dob) FROM drivers WHERE nationality = 'Japanese' ORDER BY dob DESC LIMIT 1
SELECT c.name, COUNT(r.raceId) as race_count FROM circuits c JOIN races r ON c.circuitId = r.circuitId WHERE r.year BETWEEN 1990 AND 2000 GROUP BY c.circuitId HAVING race_count = 4 
SELECT c.name AS circuit_name, c.location AS circuit_location, r.name AS race_name FROM circuits AS c INNER JOIN races AS r ON c.circuitId = r.circuitId WHERE c.country = 'USA' AND r.year = 2006
SELECT races.name, circuits.name, circuits.location FROM races INNER JOIN circuits ON races.circuitId = circuits.circuitId WHERE strftime('%m', races.date) = '09' AND strftime('%Y', races.date) = '2005';
SELECT races.name FROM results INNER JOIN drivers ON results.driverId = drivers.driverId INNER JOIN races ON results.raceId = races.raceId WHERE drivers.surname = 'Yoong' AND results.position < 10;
SELECT COUNT(T1.raceId) FROM results AS T1 INNER JOIN drivers AS T2 ON T1.driverId = T2.driverId INNER JOIN races AS T3 ON T1.raceId = T3.raceId INNER JOIN circuits AS T4 ON T3.circuitId = T4.circuitId WHERE T2.forename = 'Michael' AND T2.surname = 'Schumacher' AND T4.name = 'Sepang International Circuit' AND T1.points = (SELECT MAX(points) FROM results)
SELECT T1.name, T1.year FROM races AS T1 INNER JOIN results AS T2 ON T1.raceId = T2.raceId INNER JOIN drivers AS T3 ON T2.driverId = T3.driverId WHERE T3.surname = 'Schumacher' AND T3.forename = 'Michael' ORDER BY T2.fastestLapTime LIMIT 1
SELECT AVG(T2.points) FROM drivers AS T1 INNER JOIN results AS T2 ON T1.driverId = T2.driverId INNER JOIN races AS T3 ON T2.raceId = T3.raceId WHERE T1.forename = 'Eddie' AND T1.surname = 'Irvine' AND T3.year = 2000
SELECT T1.year, T1.name, T3.points FROM races AS T1 INNER JOIN results AS T2 ON T1.raceId = T2.raceId INNER JOIN driverStandings AS T3 ON T2.driverId = T3.driverId INNER JOIN drivers AS T4 ON T3.driverId = T4.driverId WHERE T4.surname = 'Hamilton' ORDER BY T1.year LIMIT 1
SELECT races.name, circuits.country, races.date FROM races INNER JOIN circuits ON races.circuitId = circuits.circuitId WHERE races.year = 2017 ORDER BY races.date
SELECT T1.name, T1.year, T2.location, MAX(T3.laps) FROM races AS T1 INNER JOIN circuits AS T2 ON T1.circuitId = T2.circuitId INNER JOIN results AS T3 ON T1.raceId = T3.raceId GROUP BY T1.raceId ORDER BY T3.laps DESC LIMIT 1
SELECT CAST(SUM(CASE WHEN T1.country = 'Germany' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.raceId) FROM circuits AS T1 INNER JOIN races AS T2 ON T1.circuitId = T2.circuitId WHERE T2.name = 'European Grand Prix'
SELECT lat, lng FROM circuits WHERE name = 'Silverstone Circuit'
SELECT `name`, `lat` FROM `circuits` WHERE `name` IN ('Silverstone Circuit', 'Hockenheimring', 'Hungaroring') ORDER BY `lat` DESC LIMIT 1 
SELECT circuitRef FROM circuits WHERE name = 'Marina Bay Street Circuit'
SELECT `country` FROM `circuits` ORDER BY `alt` DESC LIMIT 1 
SELECT COUNT(driverId) FROM drivers WHERE code IS NULL
SELECT c.country FROM drivers AS d INNER JOIN circuits AS c ON d.driverId = c.circuitId ORDER BY d.dob ASC LIMIT 1 
SELECT surname FROM drivers WHERE nationality = 'Italian'
SELECT url FROM drivers WHERE forename = 'Anthony' AND surname = 'Davidson'
SELECT driverRef FROM drivers WHERE forename = 'Lewis' AND surname = 'Hamilton'
SELECT c.name FROM races r INNER JOIN circuits c ON r.circuitId = c.circuitId WHERE r.name = 'Spanish Grand Prix' AND r.year = 2009 
SELECT DISTINCT year FROM races INNER JOIN circuits ON races.circuitId = circuits.circuitId WHERE circuits.name = 'Silverstone Circuit'
SELECT races.url, races.name, races.date, races.time FROM races INNER JOIN circuits ON races.circuitId = circuits.circuitId WHERE circuits.name = 'Silverstone Circuit'
SELECT races.time FROM races INNER JOIN circuits ON races.circuitId = circuits.circuitId WHERE races.year = 2010 AND circuits.name = 'Abu Dhabi Circuit'
SELECT COUNT(*) FROM races AS r INNER JOIN circuits AS c ON r.circuitId = c.circuitId WHERE c.country = 'Italy'
SELECT date FROM races WHERE circuitId = (SELECT circuitId FROM circuits WHERE name = 'Barcelona-Catalunya')
SELECT T2.url FROM races AS T1 INNER JOIN circuits AS T2 ON T1.circuitId = T2.circuitId WHERE T1.name = 'Spanish Grand Prix' AND T1.year = 2009
SELECT MIN(fastestLapTime) FROM results AS T1 INNER JOIN drivers AS T2 ON T1.driverId = T2.driverId WHERE T2.forename = 'Lewis' AND T2.surname = 'Hamilton'
SELECT T1.forename, T1.surname FROM drivers AS T1 INNER JOIN results AS T2 ON T1.driverId = T2.driverId ORDER BY T2.fastestLapSpeed DESC LIMIT 1
SELECT T1.driverRef FROM drivers AS T1 INNER JOIN results AS T2 ON T1.driverId = T2.driverId INNER JOIN races AS T3 ON T2.raceId = T3.raceId WHERE T3.name = 'Australian Grand Prix' AND T3.year = 2008 AND T2.positionOrder = 1
SELECT T3.name FROM drivers AS T1 INNER JOIN results AS T2 ON T1.driverId = T2.driverId INNER JOIN races AS T3 ON T2.raceId = T3.raceId WHERE T1.forename = 'Lewis' AND T1.surname = 'Hamilton'
SELECT T1.name FROM races AS T1 INNER JOIN results AS T2 ON T1.raceId = T2.raceId INNER JOIN drivers AS T3 ON T2.driverId = T3.driverId WHERE T3.forename = 'Lewis' AND T3.surname = 'Hamilton' ORDER BY T2.rank ASC LIMIT 1
SELECT MAX(fastestLapSpeed) FROM results AS T1 INNER JOIN races AS T2 ON T1.raceId = T2.raceId WHERE T2.year = 2009 AND T2.name = 'Spanish Grand Prix'
SELECT DISTINCT year FROM races AS T1 INNER JOIN results AS T2 ON T1.raceId = T2.raceId INNER JOIN drivers AS T3 ON T2.driverId = T3.driverId WHERE T3.forename = 'Lewis' AND T3.surname = 'Hamilton'
SELECT T1.positionOrder FROM results AS T1 INNER JOIN drivers AS T2 ON T1.driverId = T2.driverId INNER JOIN races AS T3 ON T1.raceId = T3.raceId WHERE T2.forename = 'Lewis' AND T2.surname = 'Hamilton' AND T3.name = 'Australian Grand Prix' AND T3.year = 2008
SELECT T1.forename, T1.surname FROM drivers AS T1 INNER JOIN results AS T2 ON T1.driverId = T2.driverId INNER JOIN races AS T3 ON T2.raceId = T3.raceId WHERE T2.grid = 4 AND T3.year = 2008 AND T3.name = 'Australian Grand Prix'
SELECT COUNT(driverId) FROM results WHERE raceId IN (SELECT raceId FROM races WHERE year = 2008 AND name = 'Australian Grand Prix') AND time IS NOT NULL
SELECT MIN(T1.fastestLapTime) FROM results AS T1 INNER JOIN drivers AS T2 ON T1.driverId = T2.driverId INNER JOIN races AS T3 ON T1.raceId = T3.raceId WHERE T2.forename = 'Lewis' AND T2.surname = 'Hamilton' AND T3.name = 'Australian Grand Prix' AND T3.year = 2008 
SELECT T1.time FROM results AS T1 INNER JOIN races AS T2 ON T1.raceId = T2.raceId INNER JOIN drivers AS T3 ON T1.driverId = T3.driverId WHERE T2.year = 2008 AND T2.name = 'Australian Grand Prix' AND T1.positionOrder = 2
SELECT T2.forename, T2.surname, T2.url FROM results AS T1 INNER JOIN drivers AS T2 ON T1.driverId = T2.driverId INNER JOIN races AS T3 ON T1.raceId = T3.raceId WHERE T3.year = 2008 AND T3.name = 'Australian Grand Prix' AND T1.time LIKE '%:%:%.%'
SELECT COUNT(T1.driverId) FROM drivers AS T1 INNER JOIN results AS T2 ON T1.driverId = T2.driverId INNER JOIN races AS T3 ON T2.raceId = T3.raceId WHERE T1.nationality = 'American' AND T3.year = 2008 AND T3.name = 'Australian Grand Prix'
SELECT COUNT(DISTINCT T1.driverId) FROM results AS T1 INNER JOIN races AS T2 ON T1.raceId = T2.raceId INNER JOIN drivers AS T3 ON T1.driverId = T3.driverId WHERE T2.year = 2008 AND T2.name = 'Australian Grand Prix' AND T1.time IS NOT NULL AND (SELECT COUNT(*) FROM results AS T4 WHERE T4.driverId = T3.driverId) > 0
SELECT SUM(points) FROM results WHERE driverId = (SELECT driverId FROM drivers WHERE forename = 'Lewis' AND surname = 'Hamilton')
SELECT AVG(SUBSTR(fastestLapTime, 4, 2) + SUBSTR(fastestLapTime, 1, 2) * 60 + SUBSTR(fastestLapTime, 7, 3) / 1000) FROM results INNER JOIN drivers ON results.driverId = drivers.driverId WHERE drivers.forename = 'Lewis' AND drivers.surname = 'Hamilton'
SELECT CAST(SUM(CASE WHEN time IS NOT NULL THEN 1 ELSE 0 END) AS REAL) / COUNT(raceId) FROM results WHERE raceId IN (SELECT raceId FROM races WHERE year = 2008 AND name = 'Australian Grand Prix')
SELECT (CAST(strftime('%s', T1.time) - strftime('%s', T2.time) AS REAL) / strftime('%s', T2.time)) * 100 AS percentage_faster FROM (SELECT time FROM results WHERE raceId = (SELECT raceId FROM races WHERE year = 2008 AND name = 'Australian Grand Prix') AND positionOrder = 1) AS T1, (SELECT time FROM results WHERE raceId = (SELECT raceId FROM races WHERE year = 2008 AND name = 'Australian Grand Prix') AND positionOrder = (SELECT MAX(positionOrder) FROM results WHERE raceId = (SELECT raceId FROM races WHERE year = 2008 AND name = 'Australian Grand Prix'))) AS T2
SELECT COUNT(*) FROM circuits WHERE country = 'Australia' AND location = 'Melbourne'
SELECT lat, lng FROM circuits WHERE country = 'USA'
SELECT COUNT(driverId) FROM drivers WHERE nationality = 'British' AND strftime('%Y', dob) > '1980' 
SELECT AVG(points) FROM constructorResults WHERE constructorId IN (SELECT constructorId FROM constructors WHERE nationality = 'British')
SELECT name FROM constructors WHERE constructorId = (SELECT constructorId FROM constructorStandings ORDER BY points DESC LIMIT 1)
SELECT T1.name FROM constructors AS T1 INNER JOIN constructorResults AS T2 ON T1.constructorId = T2.constructorId WHERE T2.points = 0 AND T2.raceId = 291
SELECT COUNT(T1.constructorId) FROM constructors AS T1 INNER JOIN constructorResults AS T2 ON T1.constructorId = T2.constructorId WHERE T1.nationality = 'Japanese' AND T2.points = 0 GROUP BY T1.constructorId HAVING COUNT(T2.raceId) = 2
SELECT name FROM constructors WHERE constructorId IN (SELECT constructorId FROM constructorStandings WHERE position = 1)
SELECT COUNT(DISTINCT constructors.constructorId) FROM constructors INNER JOIN results ON constructors.constructorId = results.constructorId WHERE constructors.nationality = 'French' AND results.laps > 50
SELECT CAST(SUM(CASE WHEN T1.time IS NOT NULL THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.driverId) FROM results AS T1 INNER JOIN drivers AS T2 ON T1.driverId = T2.driverId INNER JOIN races AS T3 ON T1.raceId = T3.raceId WHERE T2.nationality = 'Japanese' AND T3.year BETWEEN 2007 AND 2009
SELECT T1.year, AVG(T3.milliseconds) / 1000 FROM seasons AS T1 INNER JOIN results AS T2 ON T1.year = T2.raceId INNER JOIN lapTimes AS T3 ON T2.driverId = T3.driverId WHERE T2.position = 1 AND T3.time IS NOT NULL GROUP BY T1.year 
SELECT drivers.forename, drivers.surname FROM drivers INNER JOIN results ON drivers.driverId = results.driverId WHERE STRFTIME('%Y', drivers.dob) > '1975' AND results.rank = 2
SELECT COUNT(driverId) FROM drivers WHERE nationality = 'Italian' AND driverId NOT IN (SELECT driverId FROM results WHERE time IS NOT NULL)
SELECT T2.forename, T2.surname FROM results AS T1 INNER JOIN drivers AS T2 ON T1.driverId = T2.driverId ORDER BY T1.fastestLapTime ASC LIMIT 1
SELECT fastestLap FROM results AS T1 INNER JOIN races AS T2 ON T1.raceId = T2.raceId INNER JOIN driverStandings AS T3 ON T1.driverId = T3.driverId WHERE T2.year = 2009 AND T3.position = 1 AND T1.fastestLapTime IS NOT NULL ORDER BY T1.fastestLapTime ASC LIMIT 1;
SELECT AVG(fastestLapSpeed) FROM results WHERE raceId IN (SELECT raceId FROM races WHERE name = 'Spanish Grand Prix' AND year = 2009)
SELECT races.name, races.year FROM results INNER JOIN races ON results.raceId = races.raceId WHERE results.milliseconds IS NOT NULL ORDER BY results.milliseconds ASC LIMIT 1
SELECT CAST(SUM(CASE WHEN strftime('%Y', T2.dob) < '1985' AND T1.lap > 50 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.driverId) FROM lapTimes AS T1 INNER JOIN drivers AS T2 ON T1.driverId = T2.driverId INNER JOIN races AS T3 ON T1.raceId = T3.raceId WHERE T3.year BETWEEN 2000 AND 2005
SELECT COUNT(T1.driverId) FROM drivers AS T1 INNER JOIN lapTimes AS T2 ON T1.driverId = T2.driverId WHERE T1.nationality = 'French' AND T2.milliseconds < 120000 
SELECT code FROM drivers WHERE nationality = 'American'
SELECT raceId FROM races WHERE year = 2009; 
SELECT COUNT(DISTINCT driverId) FROM results WHERE raceId = 18 
SELECT driverId, nationality FROM drivers ORDER BY dob DESC LIMIT 3; SELECT COUNT(driverId) FROM drivers WHERE nationality = 'Dutch' AND driverId IN (SELECT driverId FROM drivers ORDER BY dob DESC LIMIT 3);
SELECT driverRef FROM drivers WHERE forename = 'Robert' AND surname = 'Kubica'
SELECT COUNT(driverId) FROM drivers WHERE nationality = 'Australian' AND strftime('%Y', dob) = '1980'
SELECT T1.forename, T1.surname FROM drivers AS T1 INNER JOIN lapTimes AS T2 ON T1.driverId = T2.driverId WHERE T1.nationality = 'German' AND STRFTIME('%Y', T1.dob) BETWEEN '1980' AND '1990' ORDER BY T2.time ASC LIMIT 3
SELECT driverRef FROM drivers WHERE nationality = 'German' ORDER BY dob ASC LIMIT 1
SELECT T1.driverId, T1.code FROM drivers AS T1 INNER JOIN results AS T2 ON T1.driverId = T2.driverId WHERE STRFTIME('%Y', T1.dob) = '1971' AND T2.fastestLapTime IS NOT NULL ORDER BY T2.fastestLapTime LIMIT 1
SELECT T1.forename, T1.surname, T1.dob, T2.time FROM drivers AS T1 INNER JOIN lapTimes AS T2 ON T1.driverId = T2.driverId WHERE T1.nationality = 'Spanish' AND STRFTIME('%Y', T1.dob) < '1982' ORDER BY T2.time DESC LIMIT 10 
SELECT year FROM races WHERE raceId IN (SELECT raceId FROM results WHERE fastestLapTime IS NOT NULL) ORDER BY year DESC LIMIT 1
SELECT T1.year FROM races AS T1 INNER JOIN lapTimes AS T2 ON T1.raceId = T2.raceId ORDER BY T2.time ASC LIMIT 1
SELECT driverId FROM lapTimes WHERE lap = 1 ORDER BY time ASC LIMIT 5 
SELECT COUNT(T1.resultId) FROM results AS T1 WHERE T1.raceId BETWEEN 50 AND 100 AND T1.statusId = 2 AND T1.time IS NOT NULL 
SELECT COUNT(circuitId), location, lat, lng FROM circuits WHERE country = 'Austria' GROUP BY location, lat, lng 
SELECT raceId FROM results WHERE time IS NOT NULL GROUP BY raceId ORDER BY COUNT(*) DESC LIMIT 1 
SELECT T1.driverRef, T1.dob, T1.nationality FROM drivers AS T1 INNER JOIN qualifying AS T2 ON T1.driverId = T2.driverId WHERE T2.q2 IS NOT NULL AND T2.raceId = 23
SELECT races.year, races.name, races.date, races.time FROM qualifying INNER JOIN drivers ON qualifying.driverId = drivers.driverId INNER JOIN races ON qualifying.raceId = races.raceId WHERE drivers.dob = (SELECT MAX(dob) FROM drivers) ORDER BY races.date ASC LIMIT 1
SELECT COUNT(DISTINCT driverId) FROM results AS T1 INNER JOIN drivers AS T2 ON T1.driverId = T2.driverId WHERE T2.nationality = 'American' AND T1.statusId = 2
SELECT T2.name, T2.url FROM constructorResults AS T1 INNER JOIN constructors AS T2 ON T1.constructorId = T2.constructorId WHERE T2.nationality = 'Italian' ORDER BY T1.points DESC LIMIT 1 
SELECT T2.url FROM constructorStandings AS T1 INNER JOIN constructors AS T2 ON T1.constructorId = T2.constructorId GROUP BY T1.constructorId ORDER BY SUM(T1.wins) DESC LIMIT 1 
SELECT T1.forename, T1.surname FROM drivers AS T1 INNER JOIN lapTimes AS T2 ON T1.driverId = T2.driverId INNER JOIN races AS T3 ON T2.raceId = T3.raceId WHERE T3.name = 'French Grand Prix' AND T2.lap = 3 ORDER BY T2.time DESC LIMIT 1 
SELECT T1.name, T2.milliseconds FROM races AS T1 INNER JOIN lapTimes AS T2 ON T1.raceId = T2.raceId WHERE T2.lap = 1 ORDER BY T2.milliseconds ASC LIMIT 1
SELECT AVG(T1.fastestLapTime) FROM results AS T1 INNER JOIN races AS T2 ON T1.raceId = T2.raceId WHERE T2.name = 'United States Grand Prix' AND T2.year = 2006 AND T1.rank < 11 
SELECT T1.driverId, T1.forename, T1.surname, AVG(T2.duration) AS avg_duration FROM drivers AS T1 INNER JOIN pitStops AS T2 ON T1.driverId = T2.driverId WHERE T1.nationality = 'German' AND STRFTIME('%Y', T1.dob) BETWEEN '1980' AND '1985' GROUP BY T1.driverId ORDER BY avg_duration ASC LIMIT 5
SELECT T2.forename, T2.surname, T1.time FROM results AS T1 INNER JOIN drivers AS T2 ON T1.driverId = T2.driverId INNER JOIN races AS T3 ON T1.raceId = T3.raceId WHERE T3.name = 'Canadian Grand Prix' AND T3.year = 2008 AND T1.positionOrder = 1 
SELECT T2.constructorRef, T2.url FROM results AS T1 INNER JOIN constructors AS T2 ON T1.constructorId = T2.constructorId INNER JOIN races AS T3 ON T1.raceId = T3.raceId WHERE T3.year = 2009 AND T3.name = 'Singapore Grand Prix' ORDER BY T1.time ASC LIMIT 1
SELECT forename, surname, dob FROM drivers WHERE nationality = 'Austrian' AND strftime('%Y', dob) BETWEEN '1981' AND '1991'
SELECT forename || ' ' || surname AS full_name, url, dob FROM drivers WHERE nationality = 'German' AND STRFTIME('%Y', dob) BETWEEN '1971' AND '1985' ORDER BY dob DESC
SELECT location, country, lat, lng FROM circuits WHERE name = 'Hungaroring'
SELECT T2.name, T2.nationality, MAX(T1.points) AS score FROM constructorResults AS T1 INNER JOIN constructors AS T2 ON T1.constructorId = T2.constructorId INNER JOIN races AS T3 ON T1.raceId = T3.raceId WHERE T3.name = 'Monaco Grand Prix' AND T3.year BETWEEN 1980 AND 2010 GROUP BY T2.constructorId ORDER BY score DESC LIMIT 1
SELECT AVG(T1.points) FROM results AS T1 INNER JOIN drivers AS T2 ON T1.driverId = T2.driverId INNER JOIN races AS T3 ON T1.raceId = T3.raceId WHERE T2.forename = 'Lewis' AND T2.surname = 'Hamilton' AND T3.name = 'Turkish Grand Prix'
SELECT CAST(COUNT(raceId) AS REAL) / 10 FROM races WHERE date BETWEEN '2000-01-01' AND '2010-12-31'
SELECT nationality FROM drivers GROUP BY nationality ORDER BY COUNT(nationality) DESC LIMIT 1 
SELECT wins FROM driverStandings WHERE points = (SELECT points FROM driverStandings ORDER BY points DESC LIMIT 1 OFFSET 90)
SELECT r.name FROM races AS r INNER JOIN results AS res ON r.raceId = res.raceId ORDER BY res.fastestLapTime ASC LIMIT 1
SELECT circuitId, location, country FROM circuits WHERE circuitId IN (SELECT circuitId FROM races ORDER BY date DESC LIMIT 1)
SELECT T1.forename, T1.surname FROM drivers AS T1 INNER JOIN qualifying AS T2 ON T1.driverId = T2.driverId INNER JOIN races AS T3 ON T2.raceId = T3.raceId INNER JOIN circuits AS T4 ON T3.circuitId = T4.circuitId WHERE T3.year = 2008 AND T4.name = 'Marina Bay Street Circuit' AND T2.position = 1 
SELECT T1.forename, T1.surname, T1.nationality, T3.name FROM drivers AS T1 INNER JOIN results AS T2 ON T1.driverId = T2.driverId INNER JOIN races AS T3 ON T2.raceId = T3.raceId ORDER BY T1.dob DESC LIMIT 1 
SELECT COUNT(*) FROM results AS T1 INNER JOIN races AS T2 ON T1.raceId = T2.raceId WHERE T2.name = 'Canadian Grand Prix' AND T1.statusId = 3 GROUP BY T1.driverId ORDER BY COUNT(*) DESC LIMIT 1 
SELECT T1.forename, T1.surname, SUM(T2.wins) FROM drivers AS T1 INNER JOIN driverStandings AS T2 ON T1.driverId = T2.driverId GROUP BY T1.driverId, T1.forename, T1.surname ORDER BY T1.dob LIMIT 1 
SELECT MAX(milliseconds) FROM pitStops
SELECT MIN(time) FROM lapTimes 
SELECT MAX(duration) FROM pitStops WHERE driverId = (SELECT driverId FROM drivers WHERE forename = 'Lewis' AND surname = 'Hamilton')
SELECT T1.lap FROM pitStops AS T1 INNER JOIN drivers AS T2 ON T1.driverId = T2.driverId INNER JOIN races AS T3 ON T1.raceId = T3.raceId WHERE T2.forename = 'Lewis' AND T2.surname = 'Hamilton' AND T3.name = 'Australian Grand Prix' AND T3.year = 2011
SELECT T1.driverId, T2.duration FROM pitStops AS T1 INNER JOIN races AS T2 ON T1.raceId = T2.raceId WHERE T2.year = 2011 AND T2.name = 'Australian Grand Prix'
SELECT MIN(T1.time) FROM lapTimes AS T1 INNER JOIN drivers AS T2 ON T1.driverId = T2.driverId WHERE T2.forename = 'Lewis' AND T2.surname = 'Hamilton'
SELECT T2.forename, T2.surname FROM lapTimes AS T1 INNER JOIN drivers AS T2 ON T1.driverId = T2.driverId ORDER BY T1.time ASC LIMIT 1
SELECT T3.position FROM lapTimes AS T1 INNER JOIN drivers AS T2 ON T1.driverId = T2.driverId INNER JOIN circuits AS T3 ON T1.raceId = T3.circuitId WHERE T2.forename = 'Lewis' AND T2.surname = 'Hamilton' ORDER BY T1.time LIMIT 1 
SELECT MIN(T1.time) AS 'Lap Record' FROM lapTimes AS T1 INNER JOIN races AS T2 ON T1.raceId = T2.raceId INNER JOIN circuits AS T3 ON T2.circuitId = T3.circuitId WHERE T3.name = 'Austrian Grand Prix Circuit'
SELECT T1.name, MIN(T3.time) AS lap_record FROM circuits AS T1 INNER JOIN races AS T2 ON T1.circuitId = T2.circuitId INNER JOIN lapTimes AS T3 ON T2.raceId = T3.raceId WHERE T1.country = 'Italy' GROUP BY T1.name
SELECT T1.name, T1.date FROM races AS T1 INNER JOIN lapTimes AS T2 ON T1.raceId = T2.raceId INNER JOIN circuits AS T3 ON T1.circuitId = T3.circuitId WHERE T3.name = 'Austrian Grand Prix Circuit' ORDER BY T2.time ASC LIMIT 1
SELECT T2.duration FROM lapTimes AS T1 INNER JOIN pitStops AS T2 ON T1.raceId = T2.raceId AND T1.driverId = T2.driverId INNER JOIN races AS T3 ON T1.raceId = T3.raceId INNER JOIN circuits AS T4 ON T3.circuitId = T4.circuitId WHERE T4.name = 'Austrian Grand Prix Circuit' AND T1.time = (SELECT MIN(time) FROM lapTimes WHERE raceId = T1.raceId)
SELECT T1.lat, T1.lng FROM circuits AS T1 INNER JOIN lapTimes AS T2 ON T1.circuitId = T2.raceId WHERE T2.time = '1:29.488'
SELECT AVG(milliseconds) FROM pitStops WHERE driverId = (SELECT driverId FROM drivers WHERE forename = 'Lewis' AND surname = 'Hamilton')
SELECT AVG(milliseconds) FROM lapTimes AS T1 INNER JOIN races AS T2 ON T1.raceId = T2.raceId INNER JOIN circuits AS T3 ON T2.circuitId = T3.circuitId WHERE T3.country = 'Italy'
SELECT player_api_id FROM Player_Attributes ORDER BY overall_rating DESC LIMIT 1 
SELECT player_name, height FROM Player ORDER BY height DESC LIMIT 1 
SELECT preferred_foot FROM Player_Attributes ORDER BY potential ASC LIMIT 1 
SELECT COUNT(*) FROM Player_Attributes WHERE overall_rating >= 60 AND overall_rating <= 65 AND defensive_work_rate = 'low' 
SELECT player_api_id FROM Player_Attributes ORDER BY crossing DESC LIMIT 5
SELECT T2.name FROM Match AS T1 INNER JOIN League AS T2 ON T1.league_id = T2.id WHERE T1.season = '2015/2016' GROUP BY T2.name ORDER BY SUM(T1.home_team_goal + T1.away_team_goal) DESC LIMIT 1 
SELECT T2.team_long_name FROM Match AS T1 INNER JOIN Team AS T2 ON T1.home_team_api_id = T2.team_api_id WHERE T1.season = '2015/2016' GROUP BY T1.home_team_api_id ORDER BY SUM(CASE WHEN T1.home_team_goal < T1.away_team_goal THEN 1 ELSE 0 END) ASC LIMIT 1 
SELECT player_name FROM Player_Attributes INNER JOIN Player ON Player_Attributes.player_api_id = Player.player_api_id ORDER BY penalties DESC LIMIT 10
SELECT T1.team_long_name FROM Team AS T1 INNER JOIN (SELECT away_team_api_id, COUNT(*) AS wins FROM Match WHERE league_id IN (SELECT id FROM League WHERE name = 'Scotland Premier League') AND season = '2009/2010' AND away_team_goal > home_team_goal GROUP BY away_team_api_id ORDER BY wins DESC LIMIT 1) AS T2 ON T1.team_api_id = T2.away_team_api_id
SELECT team_long_name, buildUpPlaySpeed FROM Team_Attributes INNER JOIN Team ON Team_Attributes.team_api_id = Team.team_api_id ORDER BY buildUpPlaySpeed DESC LIMIT 4 
SELECT T2.name FROM Match AS T1 INNER JOIN League AS T2 ON T1.league_id = T2.id WHERE T1.season = '2015/2016' AND T1.home_team_goal = T1.away_team_goal GROUP BY T1.league_id ORDER BY COUNT(*) DESC LIMIT 1 
SELECT Player.player_name, Player.birthday, (strftime('%Y', 'now') - strftime('%Y', Player.birthday)) as age FROM Player INNER JOIN Player_Attributes ON Player.player_api_id = Player_Attributes.player_api_id WHERE Player_Attributes.sprint_speed >= 97 AND Player_Attributes.date BETWEEN '2013-01-01 00:00:00' AND '2015-12-31 00:00:00'
SELECT L.name, COUNT(M.id) AS total_matches FROM League AS L JOIN Match AS M ON L.id = M.league_id GROUP BY L.id ORDER BY total_matches DESC LIMIT 1 
SELECT AVG(height) FROM Player WHERE birthday >= '1990-01-01 00:00:00' AND birthday < '1996-01-01 00:00:00' 
SELECT player_api_id FROM Player_Attributes WHERE substr(date,1,4) = '2010' ORDER BY overall_rating DESC LIMIT 1 
SELECT team_fifa_api_id FROM Team_Attributes WHERE buildUpPlaySpeed BETWEEN 51 AND 59 
SELECT T2.team_long_name FROM Team_Attributes AS T1 INNER JOIN Team AS T2 ON T1.team_api_id = T2.team_api_id WHERE strftime('%Y', T1.date) = '2012' AND T1.buildUpPlayPassing > ( SELECT AVG(buildUpPlayPassing) FROM Team_Attributes WHERE buildUpPlayPassing IS NOT NULL )
SELECT CAST(SUM(CASE WHEN T2.preferred_foot = 'left' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.player_fifa_api_id) FROM Player AS T1 INNER JOIN Player_Attributes AS T2 ON T1.player_fifa_api_id = T2.player_fifa_api_id WHERE T1.birthday BETWEEN '1987-01-01 00:00:00' AND '1992-12-31 00:00:00'
SELECT T1.name, SUM(T2.home_team_goal + T2.away_team_goal) AS total_goals FROM League AS T1 INNER JOIN Match AS T2 ON T1.id = T2.league_id GROUP BY T1.name ORDER BY total_goals ASC LIMIT 5
SELECT CAST(SUM(T2.long_shots) AS REAL) / COUNT(T2.player_fifa_api_id) FROM Player AS T1 INNER JOIN Player_Attributes AS T2 ON T1.player_fifa_api_id = T2.player_fifa_api_id WHERE T1.player_name = 'Ahmed Samir Farag'
SELECT T1.player_name, AVG(T2.heading_accuracy) AS avg_heading_accuracy FROM Player AS T1 INNER JOIN Player_Attributes AS T2 ON T1.player_fifa_api_id = T2.player_fifa_api_id WHERE T1.height > 180 GROUP BY T1.player_name ORDER BY avg_heading_accuracy DESC LIMIT 10
SELECT T2.team_long_name, T1.chanceCreationPassing FROM Team_Attributes AS T1 INNER JOIN Team AS T2 ON T1.team_api_id = T2.team_api_id WHERE T1.buildUpPlayDribblingClass = 'Normal' AND T1.date >= '2014-01-01 00:00:00' AND T1.date <= '2014-12-31 23:59:59' AND T1.chanceCreationPassing < ( SELECT AVG(chanceCreationPassing) FROM Team_Attributes WHERE date >= '2014-01-01 00:00:00' AND date <= '2014-12-31 23:59:59' ) ORDER BY T1.chanceCreationPassing DESC
SELECT L.name FROM League AS L JOIN ( SELECT league_id, AVG(home_team_goal) AS avg_home_goals, AVG(away_team_goal) AS avg_away_goals FROM Match WHERE season = '2009/2010' GROUP BY league_id ) AS M ON L.id = M.league_id WHERE M.avg_home_goals > M.avg_away_goals
SELECT T1.team_short_name FROM Team AS T1 WHERE T1.team_long_name = 'Queens Park Rangers'
SELECT player_name FROM Player WHERE SUBSTR(birthday, 1, 4) = '1970' AND SUBSTR(birthday, 6, 2) = '10'; 
SELECT `attacking_work_rate` FROM `Player_Attributes` WHERE `player_api_id` = (SELECT `player_api_id` FROM `Player` WHERE `player_name` = 'Franco Zennaro') 
SELECT buildUpPlayPositioningClass FROM Team_Attributes WHERE team_api_id = (SELECT team_api_id FROM Team WHERE team_long_name = 'ADO Den Haag')
SELECT heading_accuracy FROM Player_Attributes WHERE player_api_id = (SELECT player_api_id FROM Player WHERE player_name = 'Francois Affolter') AND date = '2014-09-18 00:00:00' 
SELECT overall_rating FROM Player_Attributes WHERE player_api_id = (SELECT player_api_id FROM Player WHERE player_name = 'Gabriel Tamas') AND strftime('%Y', date) = '2011'
SELECT COUNT(*) FROM Match m JOIN League l ON m.league_id = l.id JOIN Country c ON l.country_id = c.id WHERE m.season = '2015/2016' AND l.name = 'Scotland Premier League' AND c.name = 'Scotland'
SELECT preferred_foot FROM Player_Attributes WHERE player_api_id IN (SELECT player_api_id FROM Player ORDER BY birthday DESC LIMIT 1)
SELECT player_name FROM Player WHERE player_api_id IN (SELECT player_api_id FROM Player_Attributes WHERE potential = (SELECT MAX(potential) FROM Player_Attributes))
SELECT COUNT(T1.id) FROM Player AS T1 INNER JOIN Player_Attributes AS T2 ON T1.player_api_id = T2.player_api_id WHERE T1.weight < 130 AND T2.preferred_foot = 'left'
SELECT T2.team_short_name FROM Team_Attributes AS T1 INNER JOIN Team AS T2 ON T1.team_api_id = T2.team_api_id WHERE T1.chanceCreationPassingClass = 'Risky' 
SELECT `defensive_work_rate` FROM `Player_Attributes` WHERE `player_api_id` = (SELECT `player_api_id` FROM `Player` WHERE `player_name` = 'David Wilson')
SELECT Player.birthday FROM Player INNER JOIN Player_Attributes ON Player.player_api_id = Player_Attributes.player_api_id ORDER BY Player_Attributes.overall_rating DESC LIMIT 1 
SELECT name FROM League WHERE country_id = (SELECT id FROM Country WHERE name = 'Netherlands')
SELECT AVG(home_team_goal) FROM Match AS M INNER JOIN Country AS C ON M.country_id = C.id WHERE C.name = 'Poland' AND M.season = '2010/2011'
SELECT T1.player_name, AVG(T2.finishing) AS avg_finishing FROM Player AS T1 INNER JOIN Player_Attributes AS T2 ON T1.player_api_id = T2.player_api_id WHERE T1.height IN ( SELECT MAX(height) FROM Player UNION SELECT MIN(height) FROM Player ) GROUP BY T1.player_name ORDER BY avg_finishing DESC LIMIT 1 
SELECT player_name FROM Player WHERE height > 180
SELECT COUNT(player_api_id) FROM Player WHERE strftime('%Y', birthday) > '1990'
SELECT COUNT(*) FROM Player WHERE player_name LIKE 'Adam%' AND weight > 170 
SELECT DISTINCT T2.player_name FROM Player_Attributes AS T1 INNER JOIN Player AS T2 ON T1.player_api_id = T2.player_api_id WHERE strftime('%Y', T1.date) BETWEEN '2008' AND '2010' AND T1.overall_rating > 80; 
SELECT potential FROM Player_Attributes WHERE player_api_id = (SELECT player_api_id FROM Player WHERE player_name = 'Aaron Doran'); 
SELECT player_name FROM Player WHERE preferred_foot = 'left' 
SELECT T1.team_long_name FROM Team AS T1 INNER JOIN Team_Attributes AS T2 ON T1.team_api_id = T2.team_api_id WHERE T2.buildUpPlaySpeedClass = 'Fast'
SELECT T1.buildUpPlayPassingClass FROM Team_Attributes AS T1 INNER JOIN Team AS T2 ON T1.team_api_id = T2.team_api_id WHERE T2.team_short_name = 'CLB'
SELECT T1.team_short_name FROM Team AS T1 INNER JOIN Team_Attributes AS T2 ON T1.team_api_id = T2.team_api_id WHERE T2.buildUpPlayPassing > 70 
SELECT AVG(T1.overall_rating) FROM Player_Attributes AS T1 INNER JOIN Player AS T2 ON T1.player_api_id = T2.player_api_id WHERE strftime('%Y', T1.date) BETWEEN '2010' AND '2015' AND T2.height > 170 
SELECT player_name FROM Player ORDER BY height ASC LIMIT 1 
SELECT T2.name FROM League AS T1 INNER JOIN Country AS T2 ON T1.country_id = T2.id WHERE T1.name = 'Italy Serie A' 
SELECT T2.team_short_name FROM Team_Attributes AS T1 INNER JOIN Team AS T2 ON T1.team_api_id = T2.team_api_id WHERE T1.buildUpPlaySpeed = 31 AND T1.buildUpPlayDribbling = 53 AND T1.buildUpPlayPassing = 32
SELECT AVG(overall_rating) FROM Player_Attributes WHERE player_api_id = (SELECT player_api_id FROM Player WHERE player_name = 'Aaron Doran')
SELECT COUNT(*) FROM Match AS M INNER JOIN League AS L ON M.league_id = L.id WHERE L.name = 'Germany 1. Bundesliga' AND strftime('%Y-%m', M.date) BETWEEN '2008-08' AND '2008-10'
SELECT T2.team_short_name FROM Match AS T1 INNER JOIN Team AS T2 ON T1.home_team_api_id = T2.team_api_id WHERE T1.home_team_goal = 10
SELECT player_name FROM Player_Attributes INNER JOIN Player ON Player_Attributes.player_api_id = Player.player_api_id WHERE potential = 61 ORDER BY balance DESC LIMIT 1 
SELECT (SELECT AVG(ball_control) FROM Player_Attributes WHERE player_api_id = (SELECT player_api_id FROM Player WHERE player_name = 'Abdou Diallo')) - (SELECT AVG(ball_control) FROM Player_Attributes WHERE player_api_id = (SELECT player_api_id FROM Player WHERE player_name = 'Aaron Appindangoye')) AS difference FROM Player_Attributes 
SELECT team_long_name FROM Team WHERE team_short_name = 'GEN'
SELECT player_name FROM Player WHERE player_name = 'Aaron Lennon' OR player_name = 'Abdelaziz Barrada' ORDER BY birthday LIMIT 1 
SELECT player_name FROM Player ORDER BY height DESC LIMIT 1 
SELECT COUNT(T1.player_api_id) FROM Player_Attributes AS T1 WHERE T1.preferred_foot = 'left' AND T1.attacking_work_rate = 'low' 
SELECT T2.name FROM League AS T1 INNER JOIN Country AS T2 ON T1.country_id = T2.id WHERE T1.name = 'Belgium Jupiler League'
SELECT League.name FROM League INNER JOIN Country ON League.country_id = Country.id WHERE Country.name = 'Germany'
SELECT player_name FROM Player WHERE player_api_id = ( SELECT player_api_id FROM Player_Attributes ORDER BY overall_rating DESC LIMIT 1 ) 
SELECT COUNT(DISTINCT player_api_id) FROM Player_Attributes WHERE strftime('%Y', birthday) < '1986' AND defensive_work_rate = 'high'
SELECT player_name, MAX(crossing) FROM Player_Attributes WHERE player_name IN ('Alexis', 'Ariel Borysiuk', 'Arouna Kone') GROUP BY player_name ORDER BY MAX(crossing) DESC LIMIT 1 
SELECT heading_accuracy FROM Player_Attributes WHERE player_api_id = (SELECT player_api_id FROM Player WHERE player_name = 'Ariel Borysiuk')
SELECT COUNT(DISTINCT T1.player_api_id) FROM Player AS T1 INNER JOIN Player_Attributes AS T2 ON T1.player_api_id = T2.player_api_id WHERE T1.height > 180 AND T2.volleys > 70;
SELECT player_name FROM Player WHERE id IN (SELECT player_api_id FROM Player_Attributes WHERE volleys > 70 AND dribbling > 70)
SELECT COUNT(M.id) FROM Match AS M INNER JOIN Country AS C ON M.country_id = C.id WHERE C.name = 'Belgium' AND M.season = '2008/2009' 
SELECT T1.long_passing FROM Player_Attributes AS T1 INNER JOIN Player AS T2 ON T1.player_api_id = T2.player_api_id ORDER BY T2.birthday ASC LIMIT 1 
SELECT COUNT(Match.id) FROM Match INNER JOIN League ON Match.league_id = League.id WHERE League.name = 'Belgium Jupiler League' AND strftime('%Y', Match.date) = '2009' AND strftime('%m', Match.date) = '04'
SELECT T2.name FROM (SELECT league_id, COUNT(*) AS num FROM Match WHERE season = '2008/2009' GROUP BY league_id) AS T1 INNER JOIN League AS T2 ON T1.league_id = T2.id ORDER BY T1.num DESC LIMIT 1 
SELECT AVG(overall_rating) FROM Player_Attributes WHERE player_api_id IN (SELECT player_api_id FROM Player WHERE strftime('%Y', birthday) < '1986')
SELECT (SELECT overall_rating FROM Player_Attributes WHERE player_api_id = (SELECT player_api_id FROM Player WHERE player_name = 'Ariel Borysiuk')) - (SELECT overall_rating FROM Player_Attributes WHERE player_api_id = (SELECT player_api_id FROM Player WHERE player_name = 'Paulin Puel')) AS DIFFERENCE 
SELECT AVG(T1.buildUpPlaySpeed) FROM Team_Attributes AS T1 INNER JOIN Team AS T2 ON T1.team_api_id = T2.team_api_id WHERE T2.team_long_name = 'Heart of Midlothian'
SELECT AVG(T1.overall_rating) FROM Player_Attributes AS T1 INNER JOIN Player AS T2 ON T1.player_api_id = T2.player_api_id WHERE T2.player_name = 'Pietro Marino' 
SELECT SUM(T1.crossing) FROM Player_Attributes AS T1 INNER JOIN Player AS T2 ON T1.player_api_id = T2.player_api_id WHERE T2.player_name = 'Aaron Lennox'
SELECT MAX(T2.chanceCreationPassing), T2.chanceCreationPassingClass FROM Team AS T1 INNER JOIN Team_Attributes AS T2 ON T1.team_api_id = T2.team_api_id WHERE T1.team_long_name = 'Ajax' GROUP BY T2.chanceCreationPassingClass ORDER BY T2.chanceCreationPassing DESC LIMIT 1 
SELECT preferred_foot FROM Player_Attributes WHERE player_api_id = (SELECT player_api_id FROM Player WHERE player_name = 'Abdou Diallo') LIMIT 1 
SELECT MAX(T1.overall_rating) FROM Player_Attributes AS T1 INNER JOIN Player AS T2 ON T1.player_api_id = T2.player_api_id WHERE T2.player_name = 'Dorlan Pabon' 
SELECT AVG(Match.away_team_goal) FROM Match INNER JOIN Team ON Match.away_team_api_id = Team.team_api_id INNER JOIN League ON Match.league_id = League.id INNER JOIN Country ON League.country_id = Country.id WHERE Team.team_long_name = 'Parma' AND Country.name = 'Italy'
SELECT T2.player_name FROM Player_Attributes AS T1 INNER JOIN Player AS T2 ON T1.player_api_id = T2.player_api_id WHERE T1.overall_rating = 77 AND T1.date = '2016-06-23' ORDER BY T2.birthday LIMIT 1 
SELECT T2.overall_rating FROM Player AS T1 INNER JOIN Player_Attributes AS T2 ON T1.player_api_id = T2.player_api_id WHERE T1.player_name = 'Aaron Mooy' AND T2.date = '2016-02-04 00:00:00'
SELECT T1.potential FROM Player_Attributes AS T1 INNER JOIN Player AS T2 ON T1.player_api_id = T2.player_api_id WHERE T2.player_name = 'Francesco Parravicini' AND T1.date = '2010-08-30 00:00:00'
SELECT T1.attacking_work_rate FROM Player_Attributes AS T1 INNER JOIN Player AS T2 ON T1.player_api_id = T2.player_api_id WHERE T2.player_name = 'Francesco Migliore' AND T1.date = '2015-05-01 00:00:00'
SELECT defensive_work_rate FROM Player_Attributes WHERE player_api_id = (SELECT player_api_id FROM Player WHERE player_name = 'Kevin Berigaud') AND `date` = '2013-02-22 00:00:00' 
SELECT date FROM Player_Attributes WHERE player_api_id = (SELECT player_api_id FROM Player WHERE player_name = 'Kevin Constant') ORDER BY crossing DESC LIMIT 1 
SELECT T2.buildUpPlaySpeedClass FROM Team AS T1 INNER JOIN Team_Attributes AS T2 ON T1.team_api_id = T2.team_api_id WHERE T1.team_long_name = 'Willem II' AND T2.date = '2012-02-22 00:00:00'
SELECT T2.buildUpPlayDribblingClass FROM Team AS T1 INNER JOIN Team_Attributes AS T2 ON T1.team_api_id = T2.team_api_id WHERE T1.team_short_name = 'LEI' AND T2.date = '2015-09-10 00:00:00'
SELECT T2.buildUpPlayPassingClass FROM Team AS T1 INNER JOIN Team_Attributes AS T2 ON T1.team_api_id = T2.team_api_id WHERE T1.team_long_name = 'FC Lorient' AND T2.date = '2010-02-22'
SELECT T1.chanceCreationPassingClass FROM Team_Attributes AS T1 INNER JOIN Team AS T2 ON T1.team_api_id = T2.team_api_id WHERE T2.team_long_name = 'PEC Zwolle' AND T1.date = '2013-09-20 00:00:00'
SELECT T2.chanceCreationCrossingClass FROM Team AS T1 INNER JOIN Team_Attributes AS T2 ON T1.team_api_id = T2.team_api_id WHERE T1.team_long_name = 'Hull City' AND T2.date = '2010-02-22 00:00:00'
SELECT T2.defenceAggressionClass FROM Team AS T1 INNER JOIN Team_Attributes AS T2 ON T1.team_api_id = T2.team_api_id WHERE T1.team_long_name = 'Hannover 96' AND T2.date = '2015-09-10 00:00:00'
SELECT AVG(T1.overall_rating) FROM Player_Attributes AS T1 INNER JOIN Player AS T2 ON T1.player_api_id = T2.player_api_id WHERE T2.player_name = 'Marko Arnautovic' AND T1.date BETWEEN '2007-02-22 00:00:00' AND '2016-04-21 00:00:00'
SELECT (CAST((SELECT overall_rating FROM Player_Attributes WHERE player_api_id = (SELECT player_api_id FROM Player WHERE player_name = 'Landon Donovan') AND date = '2013-07-12') AS REAL) - (SELECT overall_rating FROM Player_Attributes WHERE player_api_id = (SELECT player_api_id FROM Player WHERE player_name = 'Jordan Bowery') AND date = '2013-07-12')) / (SELECT overall_rating FROM Player_Attributes WHERE player_api_id = (SELECT player_api_id FROM Player WHERE player_name = 'Landon Donovan') AND date = '2013-07-12') * 100 AS percentage_difference FROM Player_Attributes LIMIT 1 
SELECT player_name FROM Player ORDER BY height DESC LIMIT 5 
SELECT player_api_id FROM Player ORDER BY weight DESC LIMIT 10
SELECT player_name FROM Player WHERE (STRFTIME('%Y', CURRENT_TIMESTAMP) - STRFTIME('%Y', birthday)) >= 35
SELECT SUM(home_team_goal) FROM Match WHERE home_player_1 IN (SELECT player_api_id FROM Player WHERE player_name = 'Aaron Lennon') OR home_player_2 IN (SELECT player_api_id FROM Player WHERE player_name = 'Aaron Lennon') OR home_player_3 IN (SELECT player_api_id FROM Player WHERE player_name = 'Aaron Lennon') OR home_player_4 IN (SELECT player_api_id FROM Player WHERE player_name = 'Aaron Lennon') OR home_player_5 IN (SELECT player_api_id FROM Player WHERE player_name = 'Aaron Lennon') OR home_player_6 IN (SELECT player_api_id FROM Player WHERE player_name = 'Aaron Lennon') OR home_player_7 IN (SELECT player_api_id FROM Player WHERE player_name = 'Aaron Lennon') OR home_player_8 IN (SELECT player_api_id FROM Player WHERE player_name = 'Aaron Lennon') OR home_player_9 IN (SELECT player_api_id FROM Player WHERE player_name = 'Aaron Lennon') OR home_player_
SELECT SUM(M.away_team_goal) FROM Match M JOIN Player P1 ON M.away_player_1 = P1.player_api_id JOIN Player P2 ON M.away_player_2 = P2.player_api_id WHERE P1.player_name = 'Daan Smith' OR P2.player_name = 'Filipe Ferreira'
SELECT SUM(home_team_goal) FROM Match AS T1 INNER JOIN Player AS T2 ON T1.home_player_1 = T2.player_api_id OR T1.home_player_2 = T2.player_api_id OR T1.home_player_3 = T2.player_api_id OR T1.home_player_4 = T2.player_api_id OR T1.home_player_5 = T2.player_api_id OR T1.home_player_6 = T2.player_api_id OR T1.home_player_7 = T2.player_api_id OR T1.home_player_8 = T2.player_api_id OR T1.home_player_9 = T2.player_api_id OR T1.home_player_10 = T2.player_api_id OR T1.home_player_11 = T2.player_api_id WHERE CAST((julianday('now') - julianday(T2.birthday)) / 365 AS INTEGER) <= 30
SELECT player_name FROM Player INNER JOIN Player_Attributes ON Player.player_api_id = Player_Attributes.player_api_id ORDER BY Player_Attributes.overall_rating DESC LIMIT 10
SELECT player_name FROM Player WHERE player_api_id IN (SELECT player_api_id FROM Player_Attributes WHERE potential = (SELECT MAX(potential) FROM Player_Attributes))
SELECT T1.player_name FROM Player AS T1 INNER JOIN Player_Attributes AS T2 ON T1.player_api_id = T2.player_api_id WHERE T2.attacking_work_rate = 'high' 
SELECT T1.player_name FROM Player AS T1 INNER JOIN Player_Attributes AS T2 ON T1.player_api_id = T2.player_api_id WHERE T2.finishing = 1 ORDER BY datetime(T1.birthday) ASC LIMIT 1
SELECT T1.player_name FROM Player AS T1 INNER JOIN Country AS T2 ON T1.country_id = T2.id WHERE T2.name = 'Belgium'
SELECT T1.player_name, T3.name AS country_name FROM Player_Attributes AS T1 INNER JOIN Player AS T2 ON T1.player_api_id = T2.player_api_id INNER JOIN Country AS T3 ON T2.country_id = T3.id WHERE T1.vision > 89; 
SELECT T1.name FROM Country AS T1 INNER JOIN Player AS T2 ON T1.id = T2.id GROUP BY T1.name ORDER BY AVG(T2.weight) DESC LIMIT 1 
SELECT T1.team_long_name FROM Team AS T1 INNER JOIN Team_Attributes AS T2 ON T1.team_api_id = T2.team_api_id WHERE T2.buildUpPlaySpeedClass = 'Slow'
SELECT T2.team_short_name FROM Team_Attributes AS T1 INNER JOIN Team AS T2 ON T1.team_api_id = T2.team_api_id WHERE T1.chanceCreationPassingClass = 'Safe' 
SELECT AVG(T1.height) FROM Player AS T1 INNER JOIN Country AS T2 ON T1.country_id = T2.id WHERE T2.name = 'Italy'
SELECT player_name FROM Player WHERE height > 180 ORDER BY player_name ASC LIMIT 3 
SELECT COUNT(*) FROM Player WHERE player_name LIKE 'Aaron%' AND birthday > '1990-01-01' 
SELECT (SELECT jumping FROM Player_Attributes WHERE player_api_id = 6) - (SELECT jumping FROM Player_Attributes WHERE player_api_id = 23) AS diff FROM Player_Attributes LIMIT 1; 
SELECT player_api_id FROM Player_Attributes WHERE preferred_foot = 'right' ORDER BY potential ASC LIMIT 3 
SELECT COUNT(player_api_id) FROM Player_Attributes WHERE crossing = (SELECT MAX(crossing) FROM Player_Attributes) AND preferred_foot = 'left' 
SELECT CAST(COUNT(CASE WHEN stamina > 80 AND strength > 80 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(*) FROM Player_Attributes 
SELECT T2.name FROM League AS T1 INNER JOIN Country AS T2 ON T1.country_id = T2.id WHERE T1.name = 'Poland Ekstraklasa' 
SELECT home_team_goal, away_team_goal FROM Match WHERE date LIKE '2008-09-24%' AND league_id = (SELECT id FROM League WHERE name = 'Belgian Jupiler League') 
SELECT sprint_speed, agility, acceleration FROM Player_Attributes WHERE player_api_id = (SELECT player_api_id FROM Player WHERE player_name = 'Alexis Blin')
SELECT T1.buildUpPlaySpeedClass FROM Team AS T2 INNER JOIN Team_Attributes AS T1 ON T2.team_api_id = T1.team_api_id WHERE T2.team_long_name = 'KSV Cercle Brugge' 
SELECT COUNT(*) FROM `Match` WHERE season = '2015/2016' AND league_id = (SELECT id FROM `League` WHERE name = 'Italian Serie A')
SELECT MAX(home_team_goal) AS highest_home_score FROM Match INNER JOIN League ON Match.league_id = League.id INNER JOIN Country ON League.country_id = Country.id WHERE Country.name = 'Netherlands' AND League.name = 'Eredivisie'
SELECT T1.finishing, T1.curve FROM Player_Attributes AS T1 INNER JOIN Player AS T2 ON T1.player_api_id = T2.player_api_id ORDER BY T2.weight DESC LIMIT 1 
SELECT T2.name FROM Match AS T1 INNER JOIN League AS T2 ON T1.league_id = T2.id WHERE T1.season = '2015/2016' GROUP BY T2.name ORDER BY COUNT(T1.id) DESC LIMIT 1 
SELECT T1.team_long_name FROM Team AS T1 INNER JOIN Match AS T2 ON T1.team_api_id = T2.away_team_api_id ORDER BY T2.away_team_goal DESC LIMIT 1 
SELECT T1.player_name FROM Player AS T1 INNER JOIN Player_Attributes AS T2 ON T1.player_api_id = T2.player_api_id ORDER BY T2.overall_rating DESC LIMIT 1 
SELECT CAST(SUM(CASE WHEN T1.height < 180 AND T2.strength > 70 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.id) FROM Player AS T1 INNER JOIN Player_Attributes AS T2 ON T1.player_api_id = T2.player_api_id 
SELECT SUM(CASE WHEN T1.Admission = '+' THEN 1 ELSE 0 END) AS InPatient, SUM(CASE WHEN T1.Admission = '-' THEN 1 ELSE 0 END) AS OutPatient, ABS(SUM(CASE WHEN T1.Admission = '+' THEN 1 ELSE 0 END) - SUM(CASE WHEN T1.Admission = '-' THEN 1 ELSE 0 END)) * 100 / COUNT(T1.ID) AS Deviation FROM Patient AS T1 WHERE T1.SEX = 'M'
SELECT CAST(SUM(CASE WHEN strftime('%Y', Birthday) > '1930' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(ID) AS percentage FROM Patient WHERE SEX = 'F'
SELECT (COUNT(DISTINCT ID) * 100.0 / (SELECT COUNT(DISTINCT ID) FROM Patient WHERE strftime('%Y', Birthday) BETWEEN '1930' AND '1940')) AS Percentage FROM Patient WHERE strftime('%Y', Birthday) BETWEEN '1930' AND '1940' AND Admission = '+'
SELECT CAST(SUM(CASE WHEN Admission = '+' THEN 1 ELSE 0 END) AS REAL) / SUM(CASE WHEN Admission = '-' THEN 1 ELSE 0 END) FROM Patient WHERE Diagnosis = 'SLE'
SELECT T1.Diagnosis, T2.Date FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T1.ID = 30609
SELECT T1.SEX, T1.Birthday, T2.`Examination Date`, T2.Symptoms FROM Patient AS T1 INNER JOIN Examination AS T2 ON T1.ID = T2.ID WHERE T1.ID = '163109'
SELECT T1.ID, T1.SEX, T1.Birthday FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T2.LDH > 500
SELECT ID, YEAR(CURRENT_TIMESTAMP) - YEAR(Birthday) AS age FROM Patient WHERE ID IN (SELECT ID FROM Examination WHERE RVVT = '+')
SELECT T1.ID, T1.SEX, T1.Diagnosis FROM Patient AS T1 INNER JOIN Examination AS T2 ON T1.ID = T2.ID WHERE T2.Thrombosis = 2
SELECT DISTINCT T1.ID FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE STRFTIME('%Y', T1.Birthday) = '1937' AND T2.`T-CHO` >= 250
SELECT T1.ID, T1.SEX, T1.Diagnosis FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T2.ALB < 3.5
SELECT CAST(SUM(CASE WHEN T1.SEX = 'F' AND (T2.TP < 6.0 OR T2.TP > 8.5) THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.ID) AS percentage FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID
SELECT AVG(T1.`aCL IgG`) FROM Examination AS T1 INNER JOIN Patient AS T2 ON T1.ID = T2.ID WHERE T2.Admission = '+' AND (strftime('%Y', 'now') - strftime('%Y', T2.Birthday)) >= 50
SELECT COUNT(T1.ID) FROM Patient AS T1 INNER JOIN Examination AS T2 ON T1.ID = T2.ID WHERE T1.SEX = 'F' AND STRFTIME('%Y', T1.Description) = '1997' AND T1.Admission = '-'
SELECT MIN(STRFTIME('%Y', `First Date`) - STRFTIME('%Y', Birthday)) AS Age FROM Patient
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Examination AS T2 ON T1.ID = T2.ID WHERE strftime('%Y', T2.`Examination Date`) = '1997' AND T2.Thrombosis = 1 AND T1.SEX = 'F'
SELECT MAX(STRFTIME('%Y', Birthday)) - MIN(STRFTIME('%Y', Birthday)) FROM Patient WHERE ID IN (SELECT ID FROM Laboratory WHERE TG >= 200)
SELECT T1.Symptoms, T1.Diagnosis FROM Examination AS T1 INNER JOIN Patient AS T2 ON T1.ID = T2.ID ORDER BY T2.Birthday DESC LIMIT 1
SELECT CAST(COUNT(T1.ID) AS REAL) / 12 FROM Laboratory AS T1 INNER JOIN Patient AS T2 ON T1.ID = T2.ID WHERE T2.SEX = 'M' AND T1.Date BETWEEN '1998-01-01' AND '1998-12-31'
SELECT MAX(T2.Date), STRFTIME('%Y', T1.`First Date`) - STRFTIME('%Y', T1.Birthday) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T1.Diagnosis = 'SJS' ORDER BY T1.Birthday ASC LIMIT 1
SELECT CAST(SUM(CASE WHEN T1.SEX = 'M' AND T2.UA <= 8.0 THEN 1 ELSE 0 END) AS REAL) / SUM(CASE WHEN T1.SEX = 'F' AND T2.UA <= 6.5 THEN 1 ELSE 0 END) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 LEFT JOIN Examination AS T2 ON T1.ID = T2.ID WHERE strftime('%Y', T2.`Examination Date`) - strftime('%Y', T1.`First Date`) >= 1
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Examination AS T2 ON T1.ID = T2.ID WHERE strftime('%Y', T2.`Examination Date`) BETWEEN '1990' AND '1993' AND strftime('%Y', T1.Birthday) > strftime('%Y', T2.`Examination Date`) - 18
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T1.SEX = 'M' AND T2.`T-BIL` > 2.0
SELECT Diagnosis FROM Examination WHERE `Examination Date` BETWEEN '1985-01-01' AND '1995-12-31' GROUP BY Diagnosis ORDER BY COUNT(Diagnosis) DESC LIMIT 1
SELECT AVG(strftime('%Y', '1991') - strftime('%Y', T2.Birthday)) FROM Laboratory AS T1 INNER JOIN Patient AS T2 ON T1.ID = T2.ID WHERE T1.Date BETWEEN '1991-10-01' AND '1991-10-31'
SELECT STRFTIME('%Y', T1.`Examination Date`) - STRFTIME('%Y', T2.Birthday) AS age, T1.Diagnosis FROM Examination AS T1 INNER JOIN Patient AS T2 ON T1.ID = T2.ID INNER JOIN Laboratory AS T3 ON T1.ID = T3.ID WHERE T3.HGB = (SELECT MAX(HGB) FROM Laboratory) LIMIT 1
SELECT ANA FROM Examination WHERE ID = 3605340 AND `Examination Date` = '1996-12-02'
SELECT CASE WHEN `T-CHO` < 250 THEN 'Normal' ELSE 'Above Normal' END AS `Cholesterol Status` FROM Laboratory WHERE ID = 2927464 AND Date = '1995-9-4'
SELECT T1.SEX FROM Patient AS T1 INNER JOIN Examination AS T2 ON T1.ID = T2.ID WHERE T2.Diagnosis = 'AORTITIS' ORDER BY T2.`Examination Date` ASC LIMIT 1
SELECT T2.`aCL IgM` FROM Patient AS T1 INNER JOIN Examination AS T2 ON T1.ID = T2.ID WHERE T1.Diagnosis = 'SLE' AND T1.Description = '1994-02-19' AND T2.`Examination Date` = '1993-11-12'
SELECT T1.SEX FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T2.Date = '1992-06-12' AND T2.GPT = 9
SELECT '1991' - STRFTIME('%Y', T2.Birthday) AS age FROM Laboratory AS T1 INNER JOIN Patient AS T2 ON T1.ID = T2.ID WHERE T1.UA = 8.4 AND T1.Date = '1991-10-21'
SELECT COUNT(T2.ID) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T1.`First Date` = '1991-06-13' AND T1.Diagnosis = 'SJS' AND strftime('%Y', T2.Date) = '1995'
SELECT T1.Diagnosis FROM Patient AS T1 INNER JOIN Examination AS T2 ON T1.ID = T2.ID WHERE T2.`Examination Date` = '1997-01-27' AND T2.Diagnosis = 'SLE' AND T1.`First Date` = (SELECT MIN(`First Date`) FROM Patient WHERE ID = T1.ID)
SELECT T1.Symptoms FROM Examination AS T1 INNER JOIN Patient AS T2 ON T1.ID = T2.ID WHERE T2.Birthday = '1959-03-01' AND T1.`Examination Date` = '1993-09-27'
SELECT CAST((SUM(CASE WHEN T2.Date LIKE '1981-11-%' THEN T2.`T-CHO` ELSE 0 END) - SUM(CASE WHEN T2.Date LIKE '1981-12-%' THEN T2.`T-CHO` ELSE 0 END)) AS REAL) * 100 / SUM(CASE WHEN T2.Date LIKE '1981-11-%' THEN T2.`T-CHO` ELSE 0 END) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T1.Birthday = '1959-02-18'
SELECT T1.ID FROM Patient AS T1 INNER JOIN Examination AS T2 ON T1.ID = T2.ID WHERE T1.Diagnosis = 'Behcet' AND STRFTIME('%Y', T2.`Examination Date`) BETWEEN '1997' AND '1997'
SELECT DISTINCT T1.ID FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T2.Date BETWEEN '1987-07-06' AND '1996-01-31' AND T2.GPT > 30 AND T2.ALB < 4
SELECT ID FROM Patient WHERE SEX = 'F' AND STRFTIME('%Y', Birthday) = '1964' AND Admission = '+'
SELECT COUNT(DISTINCT T1.ID) FROM Examination AS T1 INNER JOIN Patient AS T2 ON T1.ID = T2.ID WHERE T1.Thrombosis = 2 AND T1.`ANA Pattern` = 'S' AND T1.`aCL IgM` > ( SELECT AVG(`aCL IgM`) * 1.2 FROM Examination )
SELECT CAST(SUM(CASE WHEN UA <= 6.5 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(CASE WHEN `U-PRO` > 0 AND `U-PRO` < 30 THEN 1 ELSE NULL END) FROM Laboratory
SELECT CAST(SUM(CASE WHEN T1.Diagnosis = 'BEHCET' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.`First Date`) AS percentage FROM Patient AS T1 WHERE T1.SEX = 'M' AND strftime('%Y', T1.`First Date`) = '1981'
SELECT DISTINCT T1.ID FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T1.Admission = '-' AND strftime('%Y-%m', T2.Date) = '1991-10' AND T2.`T-BIL` < 2.0
SELECT COUNT(T1.ID) FROM Patient AS T1 INNER JOIN Examination AS T2 ON T1.ID = T2.ID WHERE T2.`ANA Pattern` != 'P' AND T1.SEX = 'F' AND YEAR(T1.Birthday) BETWEEN 1980 AND 1989
SELECT T1.SEX FROM Patient AS T1 INNER JOIN Examination AS T2 ON T1.ID = T2.ID INNER JOIN Laboratory AS T3 ON T1.ID = T3.ID WHERE T2.Diagnosis = 'PSS' AND T3.CRP > 2 AND T3.CRE = 1 AND T3.LDH = 123
SELECT AVG(T2.ALB) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T1.SEX = 'F' AND T2.PLT > 400 AND T1.Diagnosis = 'SLE'
SELECT Symptoms FROM Examination WHERE Diagnosis = 'SLE' GROUP BY Symptoms ORDER BY COUNT(*) DESC LIMIT 1
SELECT T1.`First Date`, T1.Diagnosis FROM Patient AS T1 WHERE T1.ID = 48473
SELECT COUNT(*) FROM Patient WHERE SEX = 'F' AND Diagnosis = 'APS'
SELECT COUNT(DISTINCT T2.ID) FROM Laboratory AS T1 INNER JOIN Patient AS T2 ON T1.ID = T2.ID WHERE strftime('%Y', T1.Date) = '1997' AND (T1.TP < 6 OR T1.TP > 8.5)
SELECT CAST(SUM(CASE WHEN Examination.Symptoms LIKE '%thrombocytopenia%' THEN 1 ELSE 0 END) AS REAL) * 100 / SUM(CASE WHEN Patient.Diagnosis LIKE '%SLE%' THEN 1 ELSE 0 END) AS percentage FROM Examination INNER JOIN Patient ON Examination.ID = Patient.ID
SELECT CAST(SUM(CASE WHEN T1.SEX = 'F' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.SEX) AS percentage FROM Patient AS T1 WHERE strftime('%Y', T1.Birthday) = '1980' AND T1.Diagnosis = 'RA'
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Examination AS T2 ON T1.ID = T2.ID WHERE T1.SEX = 'M' AND T2.`Examination Date` BETWEEN '1995-01-01' AND '1997-12-31' AND T2.Diagnosis = 'BEHCET' AND T1.Admission = '-'
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T1.SEX = 'F' AND T2.WBC < 3.5
SELECT DATEDIFF(`Examination Date`, `First Date`) AS days FROM Patient AS T1 INNER JOIN Examination AS T2 ON T1.ID = T2.ID WHERE T1.ID = 821298
SELECT CASE WHEN SEX = 'M' AND UA > 8.0 THEN 'Yes' WHEN SEX = 'F' AND UA > 6.5 THEN 'Yes' ELSE 'No' END AS 'Is_UA_Normal' FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T1.ID = 57266
SELECT DATE FROM Laboratory WHERE ID = 48473 AND GOT >= 60
SELECT T2.SEX, T2.Birthday FROM Laboratory AS T1 INNER JOIN Patient AS T2 ON T1.ID = T2.ID WHERE STRFTIME('%Y', T1.Date) = '1994' AND T1.GOT < 60
SELECT DISTINCT T1.ID FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T1.SEX = 'M' AND T2.GPT >= 60
SELECT T2.Diagnosis FROM Laboratory AS T1 INNER JOIN Patient AS T2 ON T1.ID = T2.ID WHERE T1.GPT > 60 ORDER BY T2.Birthday ASC
SELECT AVG(LDH) FROM Laboratory WHERE LDH < 500
SELECT T1.ID, YEAR(CURRENT_TIMESTAMP) - YEAR(T1.Birthday) AS Age FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T2.LDH BETWEEN 600 AND 800
SELECT T2.Admission FROM Laboratory AS T1 INNER JOIN Patient AS T2 ON T1.ID = T2.ID WHERE T1.ALP < 300
SELECT T1.ID, CASE WHEN T2.ALP < 300 THEN 'Yes' ELSE 'No' END AS ALP_Normal_Range FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T1.Birthday = '1982-04-01'
SELECT T1.ID, T1.SEX, T1.Birthday FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T2.TP < 6.0
SELECT T1.ID, T2.Date, T2.TP - 8.5 AS Deviation FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T1.SEX = 'F' AND T2.TP > 8.5
SELECT T1.ID, T1.Birthday FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T1.SEX = 'M' AND (T2.ALB <= 3.5 OR T2.ALB >= 5.5) ORDER BY T1.Birthday DESC
SELECT T1.ID, CASE WHEN T2.ALB BETWEEN 3.5 AND 5.5 THEN 'Normal' ELSE 'Abnormal' END AS Albumin_Level FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE strftime('%Y', T1.Birthday) = '1982'
SELECT (SELECT COUNT(*) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T1.SEX = 'F' AND T2.UA > 6.5) / (SELECT COUNT(*) FROM Patient WHERE SEX = 'F') * 100 AS percentage_female_UA_beyond_normal_range
SELECT AVG(T2.UA) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE (T1.SEX = 'M' AND T2.UA < 8.0) OR (T1.SEX = 'F' AND T2.UA < 6.5) GROUP BY T1.ID ORDER BY T2.Date DESC
SELECT T1.ID, T1.SEX, T1.Birthday FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T2.UN = 29
SELECT T1.ID, T1.SEX, T1.Birthday FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T1.Diagnosis = 'RA' AND T2.UN < 30
SELECT COUNT(T1.ID) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T1.SEX = 'M' AND T2.CRE >= 1.5
SELECT CASE WHEN SUM(CASE WHEN T2.SEX = 'M' THEN 1 ELSE 0 END) > SUM(CASE WHEN T2.SEX = 'F' THEN 1 ELSE 0 END) THEN 'True' ELSE 'False' END AS Result FROM Laboratory AS T1 INNER JOIN Patient AS T2 ON T1.ID = T2.ID WHERE T1.CRE >= 1.5
SELECT T1.ID, T1.SEX, T1.Birthday FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T2.`T-BIL` = ( SELECT MAX(`T-BIL`) FROM Laboratory )
SELECT Patient.SEX, COUNT(Laboratory.`T-BIL`) FROM Patient INNER JOIN Laboratory ON Patient.ID = Laboratory.ID WHERE Laboratory.`T-BIL` >= 2.0 GROUP BY Patient.SEX
SELECT T1.ID, T2.`T-CHO` FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T1.Birthday = ( SELECT MIN(Birthday) FROM Patient ) AND T2.`T-CHO` = ( SELECT MAX(`T-CHO`) FROM Laboratory )
SELECT CAST(SUM(strftime('%Y', 'now') - strftime('%Y', T2.Birthday)) AS REAL) / COUNT(T1.ID) FROM Laboratory AS T1 INNER JOIN Patient AS T2 ON T1.ID = T2.ID WHERE T2.SEX = 'M' AND T1.`T-CHO` >= 250
SELECT T1.ID, T1.Diagnosis FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T2.TG > 300
SELECT COUNT(T1.ID) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T2.TG >= 200 AND STRFTIME('%Y', CURRENT_TIMESTAMP) - STRFTIME('%Y', T1.Birthday) > 50
SELECT DISTINCT T1.ID FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T1.Admission = '-' AND T2.CPK < 250 
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T1.SEX = 'M' AND T2.CPK >= 250 AND strftime('%Y', T1.Birthday) BETWEEN '1936' AND '1956'
SELECT T1.ID, T1.SEX, YEAR(CURRENT_TIMESTAMP) - YEAR(T1.Birthday) AS age FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T2.GLU >= 180 AND T2.`T-CHO` < 250
SELECT T1.ID, T2.GLU FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE STRFTIME('%Y', T1.Description) = '1991' AND T2.GLU < 180
SELECT P.ID, P.SEX, P.Birthday FROM Patient AS P INNER JOIN Laboratory AS L ON P.ID = L.ID WHERE L.WBC <= 3.5 OR L.WBC >= 9.0 GROUP BY P.SEX ORDER BY P.Birthday ASC
SELECT T1.ID, T1.Diagnosis, STRFTIME('%Y', CURRENT_TIMESTAMP) - STRFTIME('%Y', T1.Birthday) AS age FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T2.RBC < 3.5
SELECT T1.ID, T1.SEX, (strftime('%Y', 'now') - strftime('%Y', T1.Birthday)) AS Age, T2.RBC, CASE WHEN T1.Admission = '+' THEN 'Admitted' ELSE 'Not Admitted' END AS Admission_Status FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T1.SEX = 'F' AND (strftime('%Y', 'now') - strftime('%Y', T1.Birthday)) >= 50 AND (T2.RBC <= 3.5 OR T2.RBC >= 6.0)
SELECT T1.ID, T1.SEX FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T1.Admission = '-' AND T2.HGB < 10
SELECT T1.ID, T1.SEX FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T1.Diagnosis = 'SLE' AND T2.HGB > 10 AND T2.HGB < 17 ORDER BY T1.Birthday ASC LIMIT 1
SELECT T1.ID, YEAR(CURRENT_TIMESTAMP) - YEAR(T1.Birthday) AS age FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T2.HCT >= 52 GROUP BY T1.ID HAVING COUNT(T2.ID) >= 2
SELECT AVG(HCT) FROM Laboratory WHERE Date LIKE '1991%' AND HCT < 29
SELECT (SELECT COUNT(ID) FROM Laboratory WHERE PLT < 100) AS LowerThanNormal, (SELECT COUNT(ID) FROM Laboratory WHERE PLT > 400) AS HigherThanNormal, (SELECT COUNT(ID) FROM Laboratory WHERE PLT < 100) - (SELECT COUNT(ID) FROM Laboratory WHERE PLT > 400) AS Difference FROM Laboratory WHERE PLT < 100 OR PLT > 400
SELECT T2.ID, T2.SEX, T2.Birthday, T2.Description, T2.`First Date`, T2.Admission, T2.Diagnosis FROM Laboratory AS T1 INNER JOIN Patient AS T2 ON T1.ID = T2.ID WHERE strftime('%Y', T1.Date) = '1984' AND (strftime('%Y', CURRENT_TIMESTAMP) - strftime('%Y', T2.Birthday)) < 50 AND T1.PLT BETWEEN 100 AND 400
SELECT CAST(SUM(CASE WHEN T2.SEX = 'F' AND T1.PT >= 14 THEN 1 ELSE 0 END) AS REAL) * 100 / SUM(CASE WHEN T1.PT >= 14 THEN 1 ELSE 0 END) AS percentage FROM Laboratory AS T1 INNER JOIN Patient AS T2 ON T1.ID = T2.ID WHERE (strftime('%Y', 'now') - strftime('%Y', T2.Birthday)) > 55
SELECT T1.ID FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE STRFTIME('%Y', T1.`First Date`) > '1992' AND T2.PT < 14
SELECT COUNT(*) FROM Examination WHERE `Examination Date` > '1997-01-01' AND APTT < 45
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Examination AS T2 ON T1.ID = T2.ID INNER JOIN Laboratory AS T3 ON T1.ID = T3.ID WHERE T3.APTT > 45 AND T2.Thrombosis = 3
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T1.SEX = 'M' AND T2.WBC BETWEEN 3.5 AND 9.0 AND (T2.FG <= 150 OR T2.FG >= 450)
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T1.Birthday > '1980-01-01' AND (T2.FG < 150 OR T2.FG > 450)
SELECT DISTINCT T2.Diagnosis FROM Laboratory AS T1 INNER JOIN Patient AS T2 ON T1.ID = T2.ID WHERE T1.`U-PRO` >= 30
SELECT T1.ID FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T2.`U-PRO` BETWEEN 0 AND 30 AND T1.Diagnosis = 'SLE'
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID INNER JOIN Examination AS T3 ON T1.ID = T3.ID WHERE T2.IGG < 900 AND T3.Symptoms = 'abortion'
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID INNER JOIN Examination AS T3 ON T1.ID = T3.ID WHERE T2.IGG BETWEEN 900 AND 2000 AND T3.Symptoms IS NOT NULL
SELECT T2.Diagnosis FROM Laboratory AS T1 INNER JOIN Patient AS T2 ON T1.ID = T2.ID WHERE T1.IGA BETWEEN 80 AND 500 ORDER BY T1.IGA DESC LIMIT 1
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T2.IGA BETWEEN 80 AND 500 AND strftime('%Y', T1.`First Date`) >= '1990'
SELECT T2.Diagnosis FROM Laboratory AS T1 INNER JOIN Patient AS T2 ON T1.ID = T2.ID WHERE T1.IGM NOT BETWEEN 40 AND 400 GROUP BY T2.Diagnosis ORDER BY COUNT(T2.Diagnosis) DESC LIMIT 1
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE (T2.CRP LIKE '+' OR T2.CRP LIKE '-' OR T2.CRP < 1.0) AND T1.Description IS NULL
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T2.CRP NOT IN('+-', '-') AND T2.CRP >= 1.0 AND (YEAR(CURDATE()) - YEAR(T1.Birthday)) < 18
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Examination AS T2 ON T1.ID = T2.ID INNER JOIN Laboratory AS T3 ON T1.ID = T3.ID WHERE T3.RA IN('-', '+-') AND T2.KCT = '+'
SELECT Diagnosis FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE strftime('%Y', T1.Birthday) > '1995' AND T2.RA IN('-', '+-')
SELECT ID FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T2.RF < 20 AND STRFTIME('%Y', DATE('now')) - STRFTIME('%Y', T1.Birthday) > 60
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID INNER JOIN Examination AS T3 ON T1.ID = T3.ID WHERE T2.RF < 20 AND T3.Thrombosis = 0
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Examination AS T2 ON T1.ID = T2.ID INNER JOIN Laboratory AS T3 ON T1.ID = T3.ID WHERE T3.C3 > 35 AND T2.`ANA Pattern` = 'P'
SELECT T1.ID FROM Patient AS T1 INNER JOIN Examination AS T2 ON T1.ID = T2.ID INNER JOIN Laboratory AS T3 ON T1.ID = T3.ID WHERE T3.HCT < 29 OR T3.HCT > 52 ORDER BY T2.`aCL IgA` DESC LIMIT 1
SELECT COUNT(DISTINCT T2.ID) FROM Examination AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T1.Thrombosis = 1 AND T2.C4 > 10
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T2.RNP IN ('-', '+-') AND T1.Admission = '+'
SELECT T1.Birthday FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T2.RNP NOT IN('-', '+-') ORDER BY T1.Birthday DESC LIMIT 1
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Examination AS T2 ON T1.ID = T2.ID INNER JOIN Laboratory AS T3 ON T1.ID = T3.ID WHERE T3.SM IN('-', '+-') AND T2.Thrombosis = 1
SELECT T1.ID FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T2.SM NOT IN('-', '+-') ORDER BY T1.Birthday DESC LIMIT 3
SELECT ID FROM Examination WHERE `Examination Date` >= '1997-01-01' AND SC170 IN('-', '+-')
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Examination AS T2 ON T1.ID = T2.ID INNER JOIN Laboratory AS T3 ON T1.ID = T3.ID WHERE T1.SEX = 'M' AND T2.Symptoms = 'Vertigo' AND T3.SC170 IN('-', '+-')
SELECT COUNT(DISTINCT ID) FROM Patient WHERE `First Date` < '1990-01-01' AND ID IN (SELECT ID FROM Laboratory WHERE SSA IN('-','+-'))
SELECT T1.ID FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T2.SSA NOT IN('-', '+-') ORDER BY T1.`First Date` ASC LIMIT 1
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Examination AS T2 ON T1.ID = T2.ID INNER JOIN Laboratory AS T3 ON T1.ID = T3.ID WHERE T2.Diagnosis = 'SLE' AND T3.SSB IN ('negative', '0')
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Examination AS T2 ON T1.ID = T2.ID INNER JOIN Laboratory AS T3 ON T1.ID = T3.ID WHERE T3.SSB IN('-', '+-') AND T2.Symptoms IS NOT NULL
SELECT COUNT(T1.ID) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T1.SEX = 'M' AND T2.CENTROMEA IN('-', '+-') AND T2.SSB IN('-', '+-')
SELECT DISTINCT T2.Diagnosis FROM Laboratory AS T1 INNER JOIN Patient AS T2 ON T1.ID = T2.ID WHERE T1.DNA >= 8 
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T2.DNA < 8 AND T1.Description IS NULL
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T2.`DNA-II` >= 8 AND T1.Admission = '+'
SELECT CAST(SUM(CASE WHEN T1.GOT >= 60 AND T2.Diagnosis = 'SLE' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.ID) FROM Laboratory AS T1 INNER JOIN Patient AS T2 ON T1.ID = T2.ID WHERE T1.GOT >= 60
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T1.SEX = 'M' AND T2.GOT < 60
SELECT MAX(T2.Birthday) FROM Laboratory AS T1 INNER JOIN Patient AS T2 ON T1.ID = T2.ID WHERE T1.GOT >= 60
SELECT T1.Birthday FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T2.GPT < 60 ORDER BY T2.GPT DESC LIMIT 3
SELECT COUNT(DISTINCT T2.ID) FROM Laboratory AS T1 INNER JOIN Patient AS T2 ON T1.ID = T2.ID WHERE T1.GOT < 60 AND T2.SEX = 'M'
SELECT `First Date` FROM Patient WHERE ID = ( SELECT ID FROM Laboratory WHERE LDH < 500 ORDER BY LDH DESC LIMIT 1 ) ORDER BY `First Date` ASC LIMIT 1
SELECT MAX(`First Date`) FROM Patient WHERE ID IN (SELECT ID FROM Laboratory WHERE LDH >= 500)
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T2.ALP >= 300 AND T1.Admission = '+'
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T1.Admission = '-' AND T2.ALP < 300
SELECT T2.Diagnosis FROM Laboratory AS T1 INNER JOIN Patient AS T2 ON T1.ID = T2.ID WHERE T1.TP < 6.0
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T1.Diagnosis = 'SJS' AND T2.TP > 6.0 AND T2.TP < 8.5
SELECT T1.`Examination Date` FROM Examination AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T2.ALB BETWEEN 3.5 AND 5.5 ORDER BY T2.ALB DESC LIMIT 1
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T1.SEX = 'M' AND T2.ALB >= 3.5 AND T2.ALB <= 5.5 AND T2.TP >= 6.0 AND T2.TP <= 8.5
SELECT T1.`aCL IgG`, T1.`aCL IgM`, T1.`aCL IgA` FROM Examination AS T1 INNER JOIN Patient AS T2 ON T1.ID = T2.ID INNER JOIN Laboratory AS T3 ON T2.ID = T3.ID WHERE T2.SEX = 'F' AND T3.UA <= 7.2 AND T3.UA >= 3.7 ORDER BY T3.UA DESC LIMIT 1
SELECT MAX(T1.ANA) FROM Examination AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T2.CRE < 1.5
SELECT T1.ID FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID INNER JOIN Examination AS T3 ON T1.ID = T3.ID WHERE T2.CRE < 1.5 ORDER BY T3.`aCL IgA` DESC LIMIT 1
SELECT COUNT(T1.ID) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID INNER JOIN Examination AS T3 ON T1.ID = T3.ID WHERE T2.`T-BIL` >= 2.0 AND T3.`ANA Pattern` LIKE '%P%'
SELECT T1.ANA FROM Examination AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T2.`T-BIL` = ( SELECT MAX(`T-BIL`) FROM Laboratory WHERE `T-BIL` < 2.0 ) LIMIT 1
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID INNER JOIN Examination AS T3 ON T1.ID = T3.ID WHERE T2.`T-CHO` >= 250 AND T3.KCT = '-'
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID INNER JOIN Examination AS T3 ON T1.ID = T3.ID WHERE T2.`T-CHO` < 250 AND T3.`ANA Pattern` = 'P'
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID INNER JOIN Examination AS T3 ON T1.ID = T3.ID WHERE T2.TG < 200 AND T3.Symptoms IS NOT NULL
SELECT T2.Diagnosis FROM Laboratory AS T1 INNER JOIN Patient AS T2 ON T1.ID = T2.ID WHERE T1.TG < 200 ORDER BY T1.TG DESC LIMIT 1
SELECT DISTINCT T1.ID FROM Patient AS T1 INNER JOIN Examination AS T2 ON T1.ID = T2.ID INNER JOIN Laboratory AS T3 ON T1.ID = T3.ID WHERE T2.Thrombosis = 0 AND T3.CPK < 250
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID INNER JOIN Examination AS T3 ON T1.ID = T3.ID WHERE T2.CPK < 250 AND (T3.KCT = '+' OR T3.RVVT = '+' OR T3.LAC = '+')
SELECT T1.Birthday FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T2.GLU > 180 ORDER BY T1.Birthday LIMIT 1
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID INNER JOIN Examination AS T3 ON T1.ID = T3.ID WHERE T2.GLU < 180 AND T3.Thrombosis = 0
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T1.Admission = '+' AND T2.WBC BETWEEN 3.5 AND 9.0
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T1.Diagnosis = 'SLE' AND T2.WBC BETWEEN 3.5 AND 9.0
SELECT DISTINCT T1.ID FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE (T2.RBC <= 3.5 OR T2.RBC >= 6.0) AND T1.Admission = '-'
SELECT COUNT(DISTINCT T1.ID) FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T2.PLT > 100 AND T2.PLT < 400 AND T1.Diagnosis IS NOT NULL
SELECT T1.ID, T2.PLT FROM Patient AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T1.Diagnosis = 'MCTD' AND T2.PLT > 100 AND T2.PLT < 400
SELECT AVG(L.PT) FROM Laboratory AS L INNER JOIN Patient AS P ON L.ID = P.ID WHERE P.SEX = 'M' AND L.PT < 14
SELECT COUNT(DISTINCT T1.ID) FROM Examination AS T1 INNER JOIN Laboratory AS T2 ON T1.ID = T2.ID WHERE T1.Thrombosis IN (1, 2) AND T2.PT < 14
SELECT T2.major_name FROM member AS T1 INNER JOIN major AS T2 ON T1.link_to_major = T2.major_id WHERE T1.first_name = 'Angela' AND T1.last_name = 'Sanders'
SELECT COUNT(m.member_id) FROM member AS m INNER JOIN major AS mj ON m.link_to_major = mj.major_id WHERE mj.college = 'College of Engineering'
SELECT T1.first_name, T1.last_name FROM member AS T1 INNER JOIN major AS T2 ON T1.link_to_major = T2.major_id WHERE T2.department = 'Art and Design'
SELECT COUNT(T1.link_to_member) FROM attendance AS T1 INNER JOIN event AS T2 ON T1.link_to_event = T2.event_id WHERE T2.event_name = "Women's Soccer"
SELECT M.phone FROM member AS M INNER JOIN attendance AS A ON M.member_id = A.link_to_member INNER JOIN event AS E ON A.link_to_event = E.event_id WHERE E.event_name = "Women's Soccer"
SELECT COUNT(T1.member_id) FROM member AS T1 INNER JOIN attendance AS T2 ON T1.member_id = T2.link_to_member INNER JOIN event AS T3 ON T2.link_to_event = T3.event_id WHERE T3.event_name = 'Women's Soccer' AND T1.t_shirt_size = 'Medium'
SELECT T.event_name FROM ( SELECT T1.event_name, COUNT(T2.link_to_event) AS num FROM event AS T1 INNER JOIN attendance AS T2 ON T1.event_id = T2.link_to_event GROUP BY T1.event_id ) T ORDER BY T.num DESC LIMIT 1 
SELECT major.college FROM member INNER JOIN major ON member.link_to_major = major.major_id WHERE member.position = 'Vice President'
SELECT T1.event_name FROM event AS T1 INNER JOIN attendance AS T2 ON T1.event_id = T2.link_to_event INNER JOIN member AS T3 ON T2.link_to_member = T3.member_id WHERE T3.first_name = 'Maya' AND T3.last_name = 'Mclean'
SELECT COUNT(T1.event_id) FROM event AS T1 INNER JOIN attendance AS T2 ON T1.event_id = T2.link_to_event INNER JOIN member AS T3 ON T2.link_to_member = T3.member_id WHERE T1.type = 'Student_Club' AND T3.first_name = 'Sacha' AND T3.last_name = 'Harrison' AND STRFTIME('%Y', T1.event_date) = '2019'
SELECT COUNT(*) FROM ( SELECT event_id FROM attendance GROUP BY event_id HAVING COUNT(link_to_member) > 10 ) T1 INNER JOIN event AS T2 ON T1.event_id = T2.event_id WHERE T2.type = 'Meeting'
SELECT T1.event_name FROM event AS T1 INNER JOIN attendance AS T2 ON T1.event_id = T2.link_to_event GROUP BY T1.event_id HAVING COUNT(T2.link_to_member) > 20 
SELECT CAST(COUNT(T1.event_id) AS REAL) / COUNT(DISTINCT T1.event_name) FROM event AS T1 INNER JOIN attendance AS T2 ON T1.event_id = T2.link_to_event WHERE T1.type = 'Meeting' AND strftime('%Y', T1.event_date) = '2020'
SELECT expense_description FROM expense ORDER BY cost DESC LIMIT 1
SELECT COUNT(T1.member_id) FROM member AS T1 INNER JOIN major AS T2 ON T1.link_to_major = T2.major_id WHERE T2.major_name = 'Environmental Engineering'
SELECT T2.first_name, T2.last_name FROM attendance AS T1 INNER JOIN member AS T2 ON T1.link_to_member = T2.member_id INNER JOIN event AS T3 ON T1.link_to_event = T3.event_id WHERE T3.event_name = 'Laugh Out Loud'
SELECT last_name FROM member WHERE link_to_major IN (SELECT major_id FROM major WHERE major_name = 'Law and Constitutional Studies')
SELECT T2.county FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.zip = T2.zip_code WHERE T1.first_name = 'Sherri' AND T1.last_name = 'Ramsey'
SELECT T2.college FROM member AS T1 INNER JOIN major AS T2 ON T1.link_to_major = T2.major_id WHERE T1.first_name = 'Tyler' AND T1.last_name = 'Hewitt'
SELECT SUM(T1.amount) FROM income AS T1 INNER JOIN member AS T2 ON T1.link_to_member = T2.member_id WHERE T2.position = 'Vice President' 
SELECT T2.spent FROM event AS T1 INNER JOIN budget AS T2 ON T1.event_id = T2.link_to_event WHERE T1.event_name = 'September Meeting' AND T2.category = 'Food'
SELECT zip_code.city, zip_code.state FROM member INNER JOIN zip_code ON member.zip = zip_code.zip_code WHERE member.position = 'President'
SELECT T1.first_name, T1.last_name FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.zip = T2.zip_code WHERE T2.state = 'Illinois'
SELECT T2.spent FROM event AS T1 INNER JOIN budget AS T2 ON T1.event_id = T2.link_to_event WHERE T1.event_name = 'September Meeting' AND T2.category = 'Advertisement'
SELECT T2.department FROM member AS T1 INNER JOIN major AS T2 ON T1.link_to_major = T2.major_id WHERE T1.last_name IN ('Pierce', 'Guidi')
SELECT SUM(T2.amount) FROM event AS T1 INNER JOIN budget AS T2 ON T1.event_id = T2.link_to_event WHERE T1.event_name = 'October Speaker'
SELECT T2.expense_description, T2.approved FROM event AS T1 INNER JOIN expense AS T2 ON T1.event_id = T2.link_to_event WHERE T1.event_name = 'October Meeting' AND T1.event_date = '2019-10-08'
SELECT AVG(cost) FROM expense WHERE link_to_member = (SELECT member_id FROM member WHERE first_name = 'Elijah' AND last_name = 'Allen') AND (strftime('%m', expense_date) = '09' OR strftime('%m', expense_date) = '10')
SELECT (SELECT SUM(budget.spent) FROM budget INNER JOIN event ON budget.link_to_event = event.event_id WHERE strftime('%Y', event.event_date) = '2019') - (SELECT SUM(budget.spent) FROM budget INNER JOIN event ON budget.link_to_event = event.event_id WHERE strftime('%Y', event.event_date) = '2020') AS difference FROM budget
SELECT location FROM event WHERE event_name = 'Spring Budget Review' 
SELECT T2.cost FROM event AS T1 INNER JOIN expense AS T2 ON T1.event_id = T2.link_to_event WHERE T1.event_name = 'Posters' AND T1.event_date = '2019-09-04'
SELECT remaining FROM budget WHERE category = 'Food' AND amount = ( SELECT MAX(amount) FROM budget WHERE category = 'Food' )
SELECT notes FROM income WHERE source = 'Fundraising' AND date_received = '2019-09-14'
SELECT COUNT(major_id) FROM major WHERE college = 'College of Humanities and Social Sciences'
SELECT phone FROM member WHERE first_name = 'Carlo' AND last_name = 'Jacobs'
SELECT T2.county FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.zip = T2.zip_code WHERE T1.first_name = 'Adela' AND T1.last_name = "O'Gallagher"
SELECT COUNT(*) FROM budget AS T1 INNER JOIN event AS T2 ON T1.link_to_event = T2.event_id WHERE T2.event_name = 'November Meeting' AND T1.remaining < 0
SELECT SUM(amount) FROM budget WHERE link_to_event = (SELECT event_id FROM event WHERE event_name = 'September Speaker')
SELECT T3.status FROM expense AS T1 INNER JOIN budget AS T2 ON T1.link_to_budget = T2.budget_id INNER JOIN event AS T3 ON T2.link_to_event = T3.event_id WHERE T1.expense_description = 'Post Cards, Posters' AND T1.expense_date = '2019-8-20'
SELECT T2.major_name FROM member AS T1 INNER JOIN major AS T2 ON T1.link_to_major = T2.major_id WHERE T1.first_name = 'Brent' AND T1.last_name = 'Thomason'
SELECT COUNT(T1.member_id) FROM member AS T1 INNER JOIN major AS T2 ON T1.link_to_major = T2.major_id WHERE T2.major_name = 'Human Development and Family Studies' AND T1.t_shirt_size = 'Large'
SELECT T2.type FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.zip = T2.zip_code WHERE T1.first_name = 'Christof' AND T1.last_name = 'Nielson'
SELECT major.major_name FROM member INNER JOIN major ON member.link_to_major = major.major_id WHERE member.position = 'Vice President'
SELECT T2.state FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.zip = T2.zip_code WHERE T1.first_name = 'Sacha' AND T1.last_name = 'Harrison'
SELECT T2.department FROM member AS T1 INNER JOIN major AS T2 ON T1.link_to_major = T2.major_id WHERE T1.position = 'President'
SELECT T1.date_received FROM income AS T1 INNER JOIN member AS T2 ON T1.link_to_member = T2.member_id WHERE T2.first_name = 'Connor' AND T2.last_name = 'Hilton' AND T1.source = 'Dues'
SELECT T2.first_name, T2.last_name FROM income AS T1 INNER JOIN member AS T2 ON T1.link_to_member = T2.member_id WHERE T1.source = 'Dues' ORDER BY T1.date_received ASC LIMIT 1 
SELECT CAST(SUM(CASE WHEN T1.category = 'Advertisement' AND T2.event_name = 'Yearly Kickoff' THEN T1.amount ELSE 0 END) AS REAL) / SUM(CASE WHEN T1.category = 'Advertisement' AND T2.event_name = 'October Meeting' THEN T1.amount ELSE 0 END) FROM budget AS T1 INNER JOIN event AS T2 ON T1.link_to_event = T2.event_id
SELECT CAST(SUM(CASE WHEN T2.category = 'Parking' THEN T1.amount ELSE 0 END) AS REAL) * 100 / SUM(T1.amount) FROM budget AS T1 INNER JOIN event AS T2 ON T1.link_to_event = T2.event_id WHERE T2.event_name = 'November Speaker'
SELECT SUM(cost) FROM expense WHERE expense_description = 'Pizza'
SELECT COUNT(DISTINCT city) FROM zip_code WHERE county = 'Orange' AND state = 'Virginia' 
SELECT department FROM major WHERE college = 'College of Humanities and Social Sciences'
SELECT T2.city, T2.county, T2.state FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.zip = T2.zip_code WHERE T1.first_name = 'Amy' AND T1.last_name = 'Firth'
SELECT T2.expense_description FROM budget AS T1 INNER JOIN expense AS T2 ON T1.budget_id = T2.link_to_budget ORDER BY T1.remaining ASC LIMIT 1
SELECT T1.first_name, T1.last_name FROM member AS T1 INNER JOIN attendance AS T2 ON T1.member_id = T2.link_to_member INNER JOIN event AS T3 ON T2.link_to_event = T3.event_id WHERE T3.event_name = 'October Meeting'
SELECT T.college FROM ( SELECT T2.college, COUNT(T1.member_id) AS num FROM member AS T1 INNER JOIN major AS T2 ON T1.link_to_major = T2.major_id GROUP BY T2.college ) T ORDER BY T.num DESC LIMIT 1 
SELECT T1.major_name FROM major AS T1 INNER JOIN member AS T2 ON T1.major_id = T2.link_to_major WHERE T2.phone = '809-555-3360'
SELECT T1.event_name FROM event AS T1 INNER JOIN budget AS T2 ON T1.event_id = T2.link_to_event ORDER BY T2.amount DESC LIMIT 1 
SELECT T1.expense_description FROM expense AS T1 INNER JOIN member AS T2 ON T1.link_to_member = T2.member_id WHERE T2.position = 'Vice President'
SELECT COUNT(T2.link_to_member) FROM event AS T1 INNER JOIN attendance AS T2 ON T1.event_id = T2.link_to_event WHERE T1.event_name = 'Women\'s Soccer'
SELECT T1.date_received FROM income AS T1 INNER JOIN member AS T2 ON T1.link_to_member = T2.member_id WHERE T2.first_name = 'Casey' AND T2.last_name = 'Mason'
SELECT COUNT(DISTINCT member_id) FROM member INNER JOIN zip_code ON member.zip = zip_code.zip_code WHERE zip_code.state = 'Maryland'
SELECT COUNT(event_id) FROM attendance WHERE link_to_member = (SELECT member_id FROM member WHERE phone = '954-555-6240')
SELECT T2.first_name, T2.last_name FROM major AS T1 INNER JOIN member AS T2 ON T1.major_id = T2.link_to_major WHERE T1.department = 'School of Applied Sciences, Technology and Education'
SELECT T1.event_name FROM event AS T1 INNER JOIN budget AS T2 ON T1.event_id = T2.link_to_event WHERE T1.status = 'Closed' ORDER BY (T2.spent / T2.amount) DESC LIMIT 1
SELECT COUNT(member_id) FROM member WHERE position = 'President'
SELECT T1.event_name FROM event AS T1 INNER JOIN budget AS T2 ON T1.event_id = T2.link_to_event ORDER BY T2.spent DESC LIMIT 1 
SELECT COUNT(event_id) FROM event WHERE type = 'Meeting' AND STRFTIME('%Y', event_date) = '2020'
SELECT SUM(spent) FROM budget WHERE category = 'Food'
SELECT first_name, last_name FROM member INNER JOIN attendance ON member.member_id = attendance.link_to_member GROUP BY member.member_id HAVING COUNT(attendance.link_to_event) > 7
SELECT M.first_name, M.last_name FROM member AS M INNER JOIN major AS MJ ON M.link_to_major = MJ.major_id INNER JOIN attendance AS A ON M.member_id = A.link_to_member INNER JOIN event AS E ON A.link_to_event = E.event_id WHERE MJ.major_name = 'Interior Design' AND E.event_name = 'Community Theater'
SELECT first_name, last_name FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.zip = T2.zip_code WHERE T2.city = 'Georgetown' AND T2.state = 'South Carolina'
SELECT SUM(T2.amount) FROM member AS T1 INNER JOIN income AS T2 ON T1.member_id = T2.link_to_member WHERE T1.first_name = 'Grant' AND T1.last_name = 'Gilmour'
SELECT T1.first_name, T1.last_name FROM member AS T1 INNER JOIN income AS T2 ON T1.member_id = T2.link_to_member WHERE T2.amount > 40
SELECT SUM(cost) FROM expense AS T1 INNER JOIN event AS T2 ON T1.link_to_event = T2.event_id WHERE T2.event_name = 'Yearly Kickoff' 
SELECT T2.first_name, T2.last_name FROM budget AS T1 INNER JOIN member AS T2 ON T1.link_to_member = T2.member_id INNER JOIN event AS T3 ON T1.link_to_event = T3.event_id WHERE T3.event_name = 'Yearly Kickoff' 
SELECT T1.first_name, T1.last_name, T2.source FROM member AS T1 INNER JOIN income AS T2 ON T1.member_id = T2.link_to_member ORDER BY T2.amount DESC LIMIT 1
SELECT T1.event_name FROM event AS T1 INNER JOIN expense AS T2 ON T1.event_id = T2.link_to_event ORDER BY T2.cost ASC LIMIT 1
SELECT CAST(SUM(CASE WHEN T1.event_name = 'Yearly Kickoff' THEN T2.cost ELSE 0 END) AS REAL) * 100 / SUM(T2.cost) FROM event AS T1 INNER JOIN expense AS T2 ON T1.event_id = T2.link_to_event
SELECT CAST(SUM(CASE WHEN major_name = 'Finance' THEN 1 ELSE 0 END) AS REAL) / SUM(CASE WHEN major_name = 'Physics' THEN 1 ELSE 0 END) FROM member INNER JOIN major ON member.link_to_major = major.major_id 
SELECT source FROM income WHERE STRFTIME('%Y-%m', date_received) = '2019-09' GROUP BY source ORDER BY SUM(amount) DESC LIMIT 1 
SELECT first_name, last_name, email FROM member WHERE position = 'Secretary' 
SELECT COUNT(*) FROM member AS T1 INNER JOIN major AS T2 ON T1.link_to_major = T2.major_id WHERE T2.major_name = 'Physics Teaching' 
SELECT COUNT(DISTINCT link_to_member) FROM attendance AS T1 INNER JOIN event AS T2 ON T1.link_to_event = T2.event_id WHERE T2.event_name = 'Community Theater' AND STRFTIME('%Y', T2.event_date) = '2019'
SELECT COUNT(T1.link_to_event), T4.major_name FROM attendance AS T1 INNER JOIN member AS T2 ON T1.link_to_member = T2.member_id INNER JOIN major AS T4 ON T2.link_to_major = T4.major_id WHERE T2.first_name = 'Luisa' AND T2.last_name = 'Guidi'
SELECT AVG(spent) FROM budget WHERE category = 'Food' AND event_status = 'Closed'
SELECT T1.event_name FROM event AS T1 INNER JOIN budget AS T2 ON T1.event_id = T2.link_to_event WHERE T2.category = 'Advertisement' ORDER BY T2.spent DESC LIMIT 1
SELECT CASE WHEN EXISTS ( SELECT 1 FROM "attendance" AS T1 INNER JOIN "event" AS T2 ON T1.link_to_event = T2.event_id INNER JOIN "member" AS T3 ON T1.link_to_member = T3.member_id WHERE T2.event_name = 'Women's Soccer' AND T3.first_name = 'Maya' AND T3.last_name = 'Mclean' ) THEN 'Yes' ELSE 'No' END AS "Did Maya Mclean attend the 'Women's Soccer' event?"
SELECT CAST(SUM(CASE WHEN type = 'Community Service' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(event_id) FROM event WHERE event_date BETWEEN '2019-01-01' AND '2019-12-31'
SELECT T2.cost FROM event AS T1 INNER JOIN expense AS T2 ON T1.event_id = T2.link_to_event WHERE T2.expense_description = 'Posters' AND T1.event_name = 'September Speaker'
SELECT t_shirt_size FROM member GROUP BY t_shirt_size ORDER BY COUNT(t_shirt_size) DESC LIMIT 1 
SELECT T1.event_name FROM event AS T1 INNER JOIN budget AS T2 ON T1.event_id = T2.link_to_event WHERE T1.status = 'Closed' AND T2.remaining < 0 ORDER BY T2.remaining ASC LIMIT 1
SELECT T2.expense_description, SUM(T2.cost) FROM event AS T1 INNER JOIN expense AS T2 ON T1.event_id = T2.link_to_event WHERE T1.event_name = 'October Meeting' AND T2.approved = 'Yes' GROUP BY T2.expense_description
SELECT category, amount FROM budget WHERE link_to_event = (SELECT event_id FROM event WHERE event_name = 'April Speaker') ORDER BY amount ASC
SELECT budget_id FROM budget WHERE category = 'Food' ORDER BY amount DESC LIMIT 1 
SELECT budget_id, amount FROM budget WHERE category = 'Advertising' ORDER BY amount DESC LIMIT 3 
SELECT SUM(T1.cost) FROM expense AS T1 WHERE T1.expense_description = 'Parking'
SELECT SUM(cost) FROM expense WHERE expense_date = '2019-08-20'
SELECT T1.first_name, T1.last_name, SUM(T2.cost) FROM member AS T1 INNER JOIN expense AS T2 ON T1.member_id = T2.link_to_member WHERE T1.member_id = 'rec4BLdZHS2Blfp4v'
SELECT T2.expense_description FROM member AS T1 INNER JOIN expense AS T2 ON T1.member_id = T2.link_to_member WHERE T1.first_name = 'Sacha' AND T1.last_name = 'Harrison'
SELECT DISTINCT T2.expense_description FROM member AS T1 INNER JOIN expense AS T2 ON T1.member_id = T2.link_to_member WHERE T1.t_shirt_size = 'X-Large'
SELECT T2.zip FROM expense AS T1 INNER JOIN member AS T2 ON T1.link_to_member = T2.member_id WHERE T1.cost < 50 
SELECT T1.major_name FROM major AS T1 INNER JOIN member AS T2 ON T1.major_id = T2.link_to_major WHERE T2.first_name = 'Phillip' AND T2.last_name = 'Cullen'
SELECT T1.position FROM member AS T1 INNER JOIN major AS T2 ON T1.link_to_major = T2.major_id WHERE T2.major_name = 'Business'
SELECT COUNT(*) FROM member AS T1 INNER JOIN major AS T2 ON T1.link_to_major = T2.major_id WHERE T2.major_name = 'Business' AND T1.t_shirt_size = 'Medium'
SELECT DISTINCT T1.type FROM event AS T1 INNER JOIN budget AS T2 ON T1.event_id = T2.link_to_event WHERE T2.remaining > 30
SELECT DISTINCT type FROM event WHERE location = 'MU 215'
SELECT T1.category FROM budget AS T1 INNER JOIN event AS T2 ON T1.link_to_event = T2.event_id WHERE T2.event_date = '2020-03-24T12:00:00'
SELECT T2.major_name FROM member AS T1 INNER JOIN major AS T2 ON T1.link_to_major = T2.major_id WHERE T1.position = 'Vice President'
SELECT CAST(SUM(CASE WHEN T1.major_name = 'Mathematics' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T2.member_id) FROM major AS T1 INNER JOIN member AS T2 ON T1.major_id = T2.link_to_major WHERE T2.position = 'Member'
SELECT DISTINCT type FROM event WHERE location = 'MU 215'
SELECT COUNT(*) FROM income WHERE amount = 50 
SELECT COUNT(member_id) FROM member WHERE position = 'Member' AND t_shirt_size = 'X-Large'
SELECT COUNT(major_id) FROM major WHERE college = 'College of Agriculture and Applied Sciences' AND department = 'School of Applied Sciences, Technology and Education'
SELECT T1.last_name, T2.department, T2.college FROM member AS T1 INNER JOIN major AS T2 ON T1.link_to_major = T2.major_id WHERE T2.major_name = 'Environmental Engineering'
SELECT T2.category FROM event AS T1 INNER JOIN budget AS T2 ON T1.event_id = T2.link_to_event WHERE T1.location = 'MU 215' AND T1.type = 'Guest Speaker' AND T2.spent = 0
SELECT T3.city, T3.state FROM member AS T1 INNER JOIN major AS T2 ON T1.link_to_major = T2.major_id INNER JOIN zip_code AS T3 ON T1.zip = T3.zip_code WHERE T2.department = 'Electrical and Computer Engineering' AND T1.position = 'Member'
SELECT T1.event_name FROM event AS T1 INNER JOIN attendance AS T2 ON T1.event_id = T2.link_to_event INNER JOIN member AS T3 ON T2.link_to_member = T3.member_id WHERE T1.type = 'Social' AND T3.position = 'Vice President' AND T1.location = '900 E. Washington St.'
SELECT T1.last_name, T1.position FROM member AS T1 INNER JOIN expense AS T2 ON T1.member_id = T2.link_to_member WHERE T2.expense_description = 'Pizza' AND T2.expense_date = '2019-09-10'
SELECT T2.last_name FROM attendance AS T1 INNER JOIN member AS T2 ON T1.link_to_member = T2.member_id INNER JOIN event AS T3 ON T1.link_to_event = T3.event_id WHERE T2.position = 'Member' AND T3.event_name = 'Women's Soccer'
SELECT CAST(SUM(CASE WHEN T2.amount = 50 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.member_id) FROM member AS T1 INNER JOIN income AS T2 ON T1.member_id = T2.link_to_member WHERE T1.t_shirt_size = 'Medium' AND T1.position = 'Member'
SELECT DISTINCT T2.country FROM zip_code AS T1 INNER JOIN country AS T2 ON T1.country_code = T2.code WHERE T1.type = 'PO Box'
SELECT zip_code FROM zip_code WHERE type = 'PO Box' AND county = 'San Juan Municipio' AND state = 'Puerto Rico'
SELECT event_name FROM event WHERE type = 'Game' AND status = 'Closed' AND event_date BETWEEN '2019-03-15' AND '2020-03-20'
SELECT T1.link_to_event FROM expense AS T1 INNER JOIN member AS T2 ON T1.link_to_member = T2.member_id WHERE T1.cost > 50
SELECT T1.first_name, T1.last_name, T3.event_name, T3.event_id FROM member AS T1 INNER JOIN expense AS T2 ON T1.member_id = T2.link_to_member INNER JOIN event AS T3 ON T2.link_to_budget = T3.event_id WHERE T2.approved = 'true' AND T2.expense_date BETWEEN '2019-01-10' AND '2019-11-19'
SELECT T2.college FROM member AS T1 INNER JOIN major AS T2 ON T1.link_to_major = T2.major_id WHERE T1.first_name = 'Katy' AND T1.link_to_major = 'rec1N0upiVLy5esTO'
SELECT T1.phone FROM member AS T1 INNER JOIN major AS T2 ON T1.link_to_major = T2.major_id WHERE T2.major_name = 'Business' AND T2.college = 'College of Agriculture and Applied Sciences'
SELECT T2.email FROM expense AS T1 INNER JOIN member AS T2 ON T1.link_to_member = T2.member_id WHERE T1.cost > 20 AND T1.expense_date BETWEEN '2019-09-10' AND '2019-11-19'
SELECT COUNT(T1.member_id) FROM member AS T1 INNER JOIN major AS T2 ON T1.link_to_major = T2.major_id WHERE T2.major_name = 'education' AND T2.college = 'College of Education & Human Services' AND T1.position = 'Member'
SELECT CAST(SUM(CASE WHEN remaining < 0 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(event_id) FROM budget INNER JOIN event ON budget.link_to_event = event.event_id 
SELECT event_id, location, status FROM event WHERE event_date BETWEEN '2019-11-01' AND '2020-03-31'
SELECT expense_description FROM expense GROUP BY expense_description HAVING AVG(cost) > 50
SELECT first_name, last_name FROM member WHERE t_shirt_size = 'X-Large'
SELECT CAST(SUM(CASE WHEN type = 'PO Box' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(zip_code) FROM zip_code
SELECT T1.event_name, T1.location FROM event AS T1 INNER JOIN budget AS T2 ON T1.event_id = T2.link_to_event WHERE T2.remaining > 0 
SELECT T1.event_name, T1.event_date FROM event AS T1 INNER JOIN expense AS T2 ON T1.event_id = T2.link_to_event WHERE T2.expense_description = 'Pizza' AND T2.cost > 50 AND T2.cost < 100
SELECT T2.first_name, T2.last_name, T4.major_name FROM expense AS T1 INNER JOIN member AS T2 ON T1.link_to_member = T2.member_id INNER JOIN major AS T4 ON T2.link_to_major = T4.major_id WHERE T1.cost > 100
SELECT T3.city, T3.county FROM event AS T1 INNER JOIN income AS T2 ON T1.event_id = T2.link_to_member INNER JOIN zip_code AS T3 ON T1.location = T3.zip_code GROUP BY T1.event_id HAVING COUNT(T2.income_id) > 40
SELECT T1.first_name, T1.last_name FROM member AS T1 INNER JOIN ( SELECT T2.link_to_member, SUM(T2.cost) AS total_cost FROM expense AS T2 INNER JOIN budget AS T3 ON T2.link_to_budget = T3.budget_id GROUP BY T2.link_to_member HAVING COUNT(DISTINCT T3.link_to_event) > 1 ) AS T4 ON T1.member_id = T4.link_to_member ORDER BY T4.total_cost DESC LIMIT 1
SELECT AVG(T2.cost) FROM member AS T1 INNER JOIN expense AS T2 ON T1.member_id = T2.link_to_member WHERE T1.position != 'Member'
SELECT T1.event_name FROM event AS T1 INNER JOIN budget AS T2 ON T1.event_id = T2.link_to_event INNER JOIN expense AS T3 ON T2.budget_id = T3.link_to_budget WHERE T2.category = 'Parking' AND T3.cost < ( SELECT AVG(T3.cost) FROM expense AS T3 INNER JOIN budget AS T2 ON T3.link_to_budget = T2.budget_id WHERE T2.category = 'Parking' )
SELECT CAST(SUM(T2.cost) AS REAL) * 100 / COUNT(T1.event_id) FROM event AS T1 INNER JOIN expense AS T2 ON T1.event_id = T2.link_to_event WHERE T1.type = 'Game'
SELECT T1.budget_id FROM budget AS T1 INNER JOIN expense AS T2 ON T1.budget_id = T2.link_to_budget WHERE T2.expense_description = 'Water, chips, cookies' ORDER BY T2.cost DESC LIMIT 1 
SELECT T1.first_name, T1.last_name FROM member AS T1 INNER JOIN expense AS T2 ON T1.member_id = T2.link_to_member ORDER BY T2.cost DESC LIMIT 5
SELECT T2.first_name, T2.last_name, T2.phone FROM expense AS T1 INNER JOIN member AS T2 ON T1.link_to_member = T2.member_id WHERE T1.cost > ( SELECT AVG(cost) FROM expense )
SELECT (CAST(SUM(CASE WHEN T2.state = 'Maine' THEN 1 ELSE 0 END) AS REAL) / COUNT(T1.position) * 100) - (CAST(SUM(CASE WHEN T2.state = 'Vermont' THEN 1 ELSE 0 END) AS REAL) / COUNT(T1.position) * 100) AS DIFFERENCE FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.zip = T2.zip_code WHERE T1.position = 'Member'
SELECT T2.major_name, T2.department FROM member AS T1 INNER JOIN major AS T2 ON T1.link_to_major = T2.major_id WHERE T1.first_name = 'Garrett' AND T1.last_name = 'Gerke'
SELECT T1.first_name, T1.last_name, T2.cost FROM member AS T1 INNER JOIN expense AS T2 ON T1.member_id = T2.link_to_member WHERE T2.expense_description = 'Water, Veggie tray, supplies'
SELECT T1.last_name, T1.phone FROM member AS T1 INNER JOIN major AS T2 ON T1.link_to_major = T2.major_id WHERE T2.major_name = 'Elementary Education'
SELECT T2.category, T2.amount FROM event AS T1 INNER JOIN budget AS T2 ON T1.event_id = T2.link_to_event WHERE T1.event_name = 'January Speaker' 
SELECT T1.event_name FROM event AS T1 INNER JOIN budget AS T2 ON T1.event_id = T2.link_to_event WHERE T2.category = 'Food'
SELECT T1.first_name, T1.last_name, T2.amount FROM member AS T1 INNER JOIN income AS T2 ON T1.member_id = T2.link_to_member WHERE T2.date_received = '2019-09-09'
SELECT T2.category FROM expense AS T1 INNER JOIN budget AS T2 ON T1.link_to_budget = T2.budget_id WHERE T1.expense_description = 'Posters'
SELECT T1.first_name, T1.last_name, T3.college FROM member AS T1 INNER JOIN major AS T3 ON T1.link_to_major = T3.major_id WHERE T1.position = 'Secretary'
SELECT T1.event_name, SUM(T3.spent) FROM event AS T1 INNER JOIN budget AS T2 ON T1.event_id = T2.link_to_event INNER JOIN expense AS T3 ON T2.budget_id = T3.link_to_budget WHERE T2.category = 'Speaker Gifts' GROUP BY T1.event_name
SELECT T1.city FROM zip_code AS T1 INNER JOIN member AS T2 ON T1.zip_code = T2.zip WHERE T2.first_name = 'Garrett' AND T2.last_name = 'Girke'
SELECT T1.first_name, T1.last_name, T1.position FROM member AS T1 INNER JOIN zip_code AS T2 ON T1.zip = T2.zip_code WHERE T2.city = 'Lincolnton' AND T2.state = 'North Carolina' AND T2.zip_code = 28092
SELECT COUNT(DISTINCT GasStationID) FROM gasstations WHERE Country = 'CZE' AND Segment = 'Premium'
SELECT CAST(SUM(IIF(Currency = 'EUR', 1, 0)) AS REAL) / SUM(IIF(Currency = 'CZK', 1, 0)) FROM customers
SELECT CustomerID FROM yearmonth WHERE Date BETWEEN '201201' AND '201212' ORDER BY Consumption ASC LIMIT 1
SELECT AVG(Consumption) / 12 FROM yearmonth WHERE Date BETWEEN '201301' AND '201312' AND CustomerID IN (SELECT CustomerID FROM customers WHERE Segment = 'SME')
SELECT T1.CustomerID FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.CustomerID = T2.CustomerID WHERE T1.Currency = 'CZK' AND T2.Date BETWEEN '201101' AND '201112' ORDER BY T2.Consumption DESC LIMIT 1
SELECT COUNT(DISTINCT CustomerID) FROM yearmonth WHERE Date BETWEEN '201201' AND '201212' AND Consumption < 30000 AND CustomerID IN (SELECT CustomerID FROM customers WHERE Segment = 'KAM')
SELECT (SELECT SUM(Consumption) FROM yearmonth AS T1 INNER JOIN customers AS T2 ON T1.CustomerID = T2.CustomerID WHERE T2.Currency = 'CZK' AND T1.Date BETWEEN '201201' AND '201212') - (SELECT SUM(Consumption) FROM yearmonth AS T1 INNER JOIN customers AS T2 ON T1.CustomerID = T2.CustomerID WHERE T2.Currency = 'EUR' AND T1.Date BETWEEN '201201' AND '201212')
SELECT STRFTIME('%Y', T1.Date) FROM "transactions_1k" AS T1 INNER JOIN customers AS T2 ON T1.CustomerID = T2.CustomerID WHERE T2.Currency = 'EUR' GROUP BY STRFTIME('%Y', T1.Date) ORDER BY SUM(T1.Amount) DESC LIMIT 1
SELECT Segment FROM yearmonth GROUP BY Segment ORDER BY SUM(Consumption) ASC LIMIT 1
SELECT SUBSTR(Date, 1, 4) AS Year FROM yearmonth WHERE Currency = 'CZK' GROUP BY Year ORDER BY SUM(Consumption) DESC LIMIT 1
SELECT SUBSTR(Date, 6, 2) AS Month, SUM(Consumption) AS Total_Consumption FROM yearmonth AS T1 INNER JOIN customers AS T2 ON T1.CustomerID = T2.CustomerID WHERE T2.Segment = 'SME' AND SUBSTR(T1.Date, 1, 4) = '2013' GROUP BY Month ORDER BY Total_Consumption DESC LIMIT 1
SELECT (SELECT AVG(T3.Consumption) FROM customers AS T1 INNER JOIN transactions_1k AS T2 ON T1.CustomerID = T2.CustomerID INNER JOIN yearmonth AS T3 ON T1.CustomerID = T3.CustomerID WHERE T1.Segment = 'SME' AND T1.Currency = 'CZK' AND SUBSTR(T3.Date, 1, 4) = '2013' ORDER BY T2.Amount ASC LIMIT 1) - (SELECT AVG(T3.Consumption) FROM customers AS T1 INNER JOIN transactions_1k AS T2 ON T1.CustomerID = T2.CustomerID INNER JOIN yearmonth AS T3 ON T1.CustomerID = T3.CustomerID WHERE T1.Segment = 'LAM' AND T1.Currency = 'CZK' AND SUBSTR(T3.Date, 1, 4) = '2013' ORDER BY T2.Amount ASC LIMIT 1) AS 'SME
SELECT Segment, (SUM(CASE WHEN SUBSTR(Date, 1, 4) = '2013' THEN Consumption ELSE 0 END) - SUM(CASE WHEN SUBSTR(Date, 1, 4) = '2012' THEN Consumption ELSE 0 END)) / SUM(CASE WHEN SUBSTR(Date, 1, 4) = '2012' THEN Consumption ELSE 0 END) * 100 AS PercentageIncrease FROM yearmonth AS T1 INNER JOIN customers AS T2 ON T1.CustomerID = T2.CustomerID WHERE T2.Currency = 'EUR' AND T2.Segment IN ('SME', 'LAM', 'KAM') AND SUBSTR(T1.Date, 1, 4) BETWEEN '2012' AND '2013' GROUP BY Segment ORDER BY PercentageIncrease DESC, PercentageIncrease ASC LIMIT 1,1
SELECT SUM(Consumption) FROM yearmonth WHERE CustomerID = 6 AND SUBSTR(Date, 1, 6) BETWEEN '201308' AND '201311'
SELECT ( SELECT COUNT(GasStationID) FROM gasstations WHERE Country = 'Czech Republic' AND Segment = 'discount' ) - ( SELECT COUNT(GasStationID) FROM gasstations WHERE Country = 'Slovakia' AND Segment = 'discount' ) AS Difference
SELECT (SELECT Consumption FROM yearmonth WHERE CustomerID = 7 AND Date = '201304') - (SELECT Consumption FROM yearmonth WHERE CustomerID = 5 AND Date = '201304') AS Consumption_Difference
SELECT (SELECT COUNT(DISTINCT CustomerID) FROM customers WHERE Segment = 'SME' AND Currency = 'Czech koruna') - (SELECT COUNT(DISTINCT CustomerID) FROM customers WHERE Segment = 'SME' AND Currency = 'Euro') AS MoreSMEs
SELECT T1.CustomerID FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.CustomerID = T2.CustomerID WHERE T1.Segment = 'LAM' AND T1.Currency = 'Euro' AND T2.Date = '201310' ORDER BY T2.Consumption DESC LIMIT 1
SELECT T1.CustomerID, T2.Consumption FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.CustomerID = T2.CustomerID WHERE T1.Segment = 'KAM' ORDER BY T2.Consumption DESC LIMIT 1
SELECT SUM(Consumption) FROM yearmonth WHERE Date = '201305' AND CustomerID IN (SELECT CustomerID FROM customers WHERE Segment = 'KAM')
SELECT CAST(SUM(CASE WHEN T2.Consumption > 46.73 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(*) FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.CustomerID = T2.CustomerID WHERE T1.Segment = 'LAM'
SELECT Country, COUNT(*) as NumberOfValueForMoneyStations FROM gasstations WHERE Segment = 'Value for Money' GROUP BY Country ORDER BY NumberOfValueForMoneyStations DESC
SELECT (CAST(SUM(CASE WHEN Currency = 'Euro' THEN 1 ELSE 0 END) AS REAL) / COUNT(*)) * 100 AS percentage FROM customers WHERE Segment = 'KAM'
SELECT CAST(SUM(CASE WHEN Consumption > 528.3 THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(CustomerID) FROM yearmonth WHERE Date = '201202'
SELECT CAST(SUM(CASE WHEN Segment = 'Premium' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(*) FROM gasstations WHERE Country = 'Slovakia'
SELECT CustomerID FROM yearmonth WHERE Date = '201309' ORDER BY Consumption DESC LIMIT 1
SELECT T1.Segment FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.CustomerID = T2.CustomerID WHERE T2.Date = '201309' GROUP BY T1.Segment ORDER BY SUM(T2.Consumption) ASC LIMIT 1
SELECT T1.CustomerID FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.CustomerID = T2.CustomerID WHERE T1.Segment = 'SME' AND T2.Date = '201206' ORDER BY T2.Consumption ASC LIMIT 1
SELECT MAX(Consumption) FROM yearmonth WHERE SUBSTR(Date, 1, 4) = '2012'
SELECT MAX(SUM(T2.Consumption) / 12) FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.CustomerID = T2.CustomerID WHERE T1.Currency = 'Euro'
SELECT T2.Description FROM "transactions_1k" AS T1 INNER JOIN products AS T2 ON T1.ProductID = T2.ProductID WHERE SUBSTR(T1.Date, 1, 6) = '201309'
SELECT DISTINCT T2.Country FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.GasStationID = T2.GasStationID WHERE SUBSTR(T1.Date, 1, 6) = '201306'
SELECT DISTINCT T2.ChainID FROM gasstations AS T2 INNER JOIN transactions_1k AS T1 ON T1.GasStationID = T2.GasStationID INNER JOIN customers AS T3 ON T1.CustomerID = T3.CustomerID WHERE T3.Currency = 'Euro'
SELECT DISTINCT T3.Description FROM "transactions_1k" AS T1 INNER JOIN customers AS T2 ON T1.CustomerID = T2.CustomerID INNER JOIN products AS T3 ON T1.ProductID = T3.ProductID WHERE T2.Currency = 'Euro'
SELECT AVG(Amount * Price) FROM "transactions_1k" WHERE Date LIKE '2012-01%'
SELECT COUNT(DISTINCT T1.CustomerID) FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.CustomerID = T2.CustomerID WHERE T1.Currency = 'Euro' AND T2.Consumption > 1000
SELECT DISTINCT T3.Description FROM "transactions_1k" AS T1 INNER JOIN gasstations AS T2 ON T1.GasStationID = T2.GasStationID INNER JOIN products AS T3 ON T1.ProductID = T3.ProductID WHERE T2.Country = 'CZE'
SELECT DISTINCT T2.Time FROM gasstations AS T1 INNER JOIN transactions_1k AS T2 ON T1.GasStationID = T2.GasStationID WHERE T1.ChainID = 11
SELECT COUNT(TransactionID) FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.GasStationID = T2.GasStationID WHERE T2.Country = 'CZE' AND T1.Price > 1000
SELECT COUNT(TransactionID) FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.GasStationID = T2.GasStationID WHERE T2.Country = 'CZE' AND T1.Date > '2012-01-01'
SELECT AVG(T1.Price * T1.Amount) AS AverageTotalPrice FROM "transactions_1k" AS T1 INNER JOIN gasstations AS T2 ON T1.GasStationID = T2.GasStationID WHERE T2.Country = 'CZE'
SELECT AVG(T4.Price) FROM customers AS T1 INNER JOIN "transactions_1k" AS T4 ON T1.CustomerID = T4.CustomerID WHERE T1.Currency = 'Euro'
SELECT T1.CustomerID FROM customers AS T1 INNER JOIN transactions_1k AS T2 ON T1.CustomerID = T2.CustomerID WHERE DATE(T2.Date) = '2012-08-25' GROUP BY T1.CustomerID ORDER BY SUM(T2.Price) DESC LIMIT 1
SELECT T2.Country FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.GasStationID = T2.GasStationID WHERE T1.Date = '2012-08-25' ORDER BY T1.Time ASC LIMIT 1
SELECT T1.Currency FROM customers AS T1 INNER JOIN "transactions_1k" AS T2 ON T1.CustomerID = T2.CustomerID WHERE T2.Date = '2012-08-24' AND T2.Time = '16:25:00'
SELECT T2.Segment FROM "transactions_1k" AS T1 INNER JOIN customers AS T2 ON T1.CustomerID = T2.CustomerID WHERE T1.Date = '2012-08-23' AND T1.Time = '21:20:00'
SELECT COUNT(TransactionID) FROM "transactions_1k" AS T1 INNER JOIN customers AS T2 ON T1.CustomerID = T2.CustomerID WHERE T2.Currency = 'EUR' AND DATE(T1.Date) = '2012-08-26' AND TIME(T1.Time) < '13:00:00'
SELECT Segment FROM customers ORDER BY CustomerID ASC LIMIT 1 
SELECT T2.Country FROM "transactions_1k" AS T1 INNER JOIN gasstations AS T2 ON T1.GasStationID = T2.GasStationID WHERE T1.Date = '2012-08-24' AND T1.Time = '12:42:00'
SELECT T1.ProductID FROM "transactions_1k" AS T1 WHERE T1.Date = '2012-08-23' AND T1.Time = '21:20:00'
SELECT T2.Date, T2.Consumption FROM transactions_1k AS T1 INNER JOIN yearmonth AS T2 ON T1.CustomerID = T2.CustomerID WHERE T1.Date = '2012-08-24' AND T1.Price = 124.05 AND STRFTIME('%Y-%m', T2.Date) = '2012-01'
SELECT COUNT(TransactionID) FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.GasStationID = T2.GasStationID WHERE T2.Country = 'CZE' AND T1.Date = '2012-08-26' AND T1.Time BETWEEN '08:00:00' AND '09:00:00'
SELECT T1.Currency FROM customers AS T1 INNER JOIN yearmonth AS T2 ON T1.CustomerID = T2.CustomerID WHERE T2.Consumption = 214582.17 AND T2.Date LIKE '201306%'
SELECT T2.Country FROM transactions_1k AS T1 INNER JOIN gasstations AS T2 ON T1.GasStationID = T2.GasStationID WHERE T1.CardID = 667467
SELECT T1.Country FROM customers AS T1 INNER JOIN "transactions_1k" AS T2 ON T1.CustomerID = T2.CustomerID WHERE T2.Date = '2012-08-24' AND T2.Amount = 548.4
SELECT CAST(SUM(CASE WHEN T2.Currency = 'EUR' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(T1.CustomerID) FROM "transactions_1k" AS T1 INNER JOIN customers AS T2 ON T1.CustomerID = T2.CustomerID WHERE T1.Date = '2012-08-25'
SELECT (CAST((SELECT Consumption FROM yearmonth WHERE CustomerID = (SELECT CustomerID FROM transactions_1k WHERE Date = '2012-08-24' AND Price = 634.8) AND Date LIKE '2012%') AS REAL) - (SELECT Consumption FROM yearmonth WHERE CustomerID = (SELECT CustomerID FROM transactions_1k WHERE Date = '2012-08-24' AND Price = 634.8) AND Date LIKE '2013%')) / (SELECT Consumption FROM yearmonth WHERE CustomerID = (SELECT CustomerID FROM transactions_1k WHERE Date = '2012-08-24' AND Price = 634.8) AND Date LIKE '2012%') AS DecreaseRate
SELECT T1.GasStationID FROM gasstations AS T1 INNER JOIN transactions_1k AS T2 ON T1.GasStationID = T2.GasStationID GROUP BY T1.GasStationID ORDER BY SUM(T2.Price * T2.Amount) DESC LIMIT 1
SELECT CAST(SUM(CASE WHEN Segment = 'premium' THEN 1 ELSE 0 END) AS REAL) * 100 / COUNT(*) FROM gasstations WHERE Country = 'SVK'
SELECT SUM(T2.Amount * T2.Price) FROM customers AS T1 INNER JOIN transactions_1k AS T2 ON T1.CustomerID = T2.CustomerID WHERE T1.CustomerID = 38508 AND strftime('%Y%m', T2.Date) = '201201'
SELECT T1.Description FROM products AS T1 INNER JOIN transactions_1k AS T2 ON T1.ProductID = T2.ProductID GROUP BY T1.Description ORDER BY SUM(T2.Amount) DESC LIMIT 5
SELECT T1.CustomerID, AVG(T2.Price / T2.Amount) AS AveragePricePerItem, T1.Currency FROM customers AS T1 INNER JOIN transactions_1k AS T2 ON T1.CustomerID = T2.CustomerID GROUP BY T1.CustomerID ORDER BY SUM(T2.Price) DESC LIMIT 1
SELECT T2.Country FROM "transactions_1k" AS T1 INNER JOIN gasstations AS T2 ON T1.GasStationID = T2.GasStationID WHERE T1.ProductID = 2 ORDER BY T1.Price DESC LIMIT 1
SELECT T3.CustomerID, T3.Consumption FROM transactions_1k AS T1 INNER JOIN products AS T2 ON T1.ProductID = T2.ProductID INNER JOIN yearmonth AS T3 ON T1.CustomerID = T3.CustomerID WHERE T2.ProductID = 5 AND T1.Price / T1.Amount > 29.00 AND T3.Date LIKE '201208%'
