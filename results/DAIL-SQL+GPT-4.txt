SELECT count(*) FROM singer
SELECT count(*) FROM singer
SELECT Name, Country, Age FROM singer ORDER BY Age DESC
SELECT Name, Country, Age FROM singer ORDER BY Age DESC
SELECT avg(Age) , min(Age) , max(Age) FROM singer WHERE Country = 'France'
SELECT avg(Age) , min(Age) , max(Age) FROM singer WHERE Country = 'France'
SELECT T1.Name, T1.Song_release_year FROM singer AS T1 ORDER BY T1.Age ASC LIMIT 1
SELECT Song_Name, Song_release_year FROM singer WHERE Age = (SELECT min(Age) FROM singer)
SELECT DISTINCT Country FROM singer WHERE Age > 20
SELECT DISTINCT Country FROM singer WHERE Age > 20
SELECT country , count(*) FROM singer GROUP BY country
SELECT Country , COUNT(*) FROM singer GROUP BY Country
SELECT Song_Name FROM singer WHERE Age > (SELECT AVG(Age) FROM singer) ORDER BY Song_Name
SELECT s.Song_Name FROM singer AS s WHERE s.Age > (SELECT avg(Age) FROM singer)
SELECT Location, Name FROM stadium WHERE Capacity BETWEEN 5000 AND 10000
SELECT Location, Name FROM stadium WHERE Capacity BETWEEN 5000 AND 10000
SELECT max(Capacity) , avg(Capacity) FROM stadium
SELECT avg(Capacity) , max(Capacity) FROM stadium
SELECT Name, Capacity FROM stadium ORDER BY Average DESC LIMIT 1
SELECT Name, Capacity FROM stadium ORDER BY Average DESC LIMIT 1
SELECT count(*) FROM concert WHERE Year IN ('2014', '2015')
SELECT count(*) FROM concert WHERE Year IN ('2014', '2015')
SELECT s.Name, count(c.concert_ID) FROM stadium s JOIN concert c ON s.Stadium_ID = c.Stadium_ID GROUP BY s.Name
SELECT T1.Name , count(*) FROM stadium AS T1 JOIN concert AS T2 ON T1.Stadium_ID = T2.Stadium_ID GROUP BY T1.Name
SELECT T1.Name, T1.Capacity FROM stadium AS T1 JOIN concert AS T2 ON T1.Stadium_ID = T2.Stadium_ID WHERE T2.Year >= '2014' GROUP BY T1.Stadium_ID ORDER BY count(*) DESC LIMIT 1
SELECT T1.Name, T1.Capacity FROM stadium AS T1 JOIN concert AS T2 ON T1.Stadium_ID = T2.Stadium_ID WHERE T2.Year > 2013 GROUP BY T1.Stadium_ID ORDER BY COUNT(*) DESC LIMIT 1
SELECT Year FROM concert GROUP BY Year ORDER BY count(*) DESC LIMIT 1
SELECT Year FROM concert GROUP BY Year ORDER BY count(*) DESC LIMIT 1
SELECT Name FROM stadium WHERE Stadium_ID NOT IN (SELECT Stadium_ID FROM concert)
SELECT Name FROM stadium WHERE Stadium_ID NOT IN (SELECT Stadium_ID FROM concert)
SELECT Country FROM singer WHERE Age > 40 INTERSECT SELECT Country FROM singer WHERE Age < 30
SELECT Name FROM stadium EXCEPT SELECT T1.Name FROM stadium AS T1 JOIN concert AS T2 ON T1.Stadium_ID = T2.Stadium_ID WHERE T2.Year = '2014'
SELECT Name FROM stadium WHERE Stadium_ID NOT IN (SELECT Stadium_ID FROM concert WHERE Year = '2014')
SELECT T2.concert_Name, T2.Theme, count(*) FROM singer_in_concert AS T1 JOIN concert AS T2 ON T1.concert_ID = T2.concert_ID GROUP BY T1.concert_ID
SELECT T1.concert_Name , T1.Theme , COUNT(*) FROM concert AS T1 JOIN singer_in_concert AS T2 ON T1.concert_ID = T2.concert_ID GROUP BY T1.concert_ID
SELECT T2.Name , COUNT(*) FROM singer_in_concert AS T1 JOIN singer AS T2 ON T1.Singer_ID = T2.Singer_ID GROUP BY T1.Singer_ID
SELECT T2.Name , count(*) FROM singer_in_concert AS T1 JOIN singer AS T2 ON T1.Singer_ID = T2.Singer_ID GROUP BY T2.Name
SELECT singer.Name FROM singer JOIN singer_in_concert ON singer.Singer_ID = singer_in_concert.Singer_ID JOIN concert ON singer_in_concert.concert_ID = concert.concert_ID WHERE concert.Year = '2014'
SELECT T2.Name FROM concert AS T1 JOIN singer_in_concert AS T3 ON T1.concert_ID = T3.concert_ID JOIN singer AS T2 ON T3.Singer_ID = T2.Singer_ID WHERE T1.Year = '2014'
SELECT Name, Country FROM singer WHERE Song_Name LIKE "%Hey%"
SELECT Name, Country FROM singer WHERE Song_Name LIKE "%Hey%"
SELECT T1.Name, T1.Location FROM stadium AS T1 JOIN concert AS T2 ON T1.Stadium_ID = T2.Stadium_ID WHERE T2.Year = '2014' INTERSECT SELECT T1.Name, T1.Location FROM stadium AS T1 JOIN concert AS T2 ON T1.Stadium_ID = T2.Stadium_ID WHERE T2.Year = '2015'
SELECT T1.Name, T1.Location FROM stadium AS T1 JOIN concert AS T2 ON T1.Stadium_ID = T2.Stadium_ID WHERE T2.Year = '2014' INTERSECT SELECT T1.Name, T1.Location FROM stadium AS T1 JOIN concert AS T2 ON T1.Stadium_ID = T2.Stadium_ID WHERE T2.Year = '2015'
SELECT count(*) FROM concert AS T1 JOIN stadium AS T2 ON T1.Stadium_ID = T2.Stadium_ID WHERE T2.Capacity = (SELECT max(Capacity) FROM stadium)
SELECT count(*) FROM concert AS T1 JOIN stadium AS T2 ON T1.Stadium_ID = T2.Stadium_ID WHERE T2.Capacity = (SELECT max(Capacity) FROM stadium)
SELECT count(*) FROM Pets WHERE weight > 10
SELECT count(*) FROM Pets WHERE weight > 10
SELECT weight FROM Pets WHERE PetType = 'dog' ORDER BY pet_age ASC LIMIT 1;
SELECT weight FROM Pets JOIN Has_Pet ON Pets.PetID = Has_Pet.PetID JOIN Student ON Has_Pet.StuID = Student.StuID WHERE PetType = 'dog' ORDER BY pet_age ASC LIMIT 1;
SELECT PetType , max(weight) FROM Pets GROUP BY PetType
SELECT PetType , max(weight) FROM Pets GROUP BY PetType
SELECT count(*) FROM Has_Pet AS T1 JOIN Student AS T2 ON T1.StuID = T2.StuID WHERE T2.Age > 20
SELECT count(*) FROM Has_Pet WHERE StuID IN (SELECT StuID FROM Student WHERE Age > 20)
SELECT count(*) FROM Student AS T1 JOIN Has_Pet AS T2 ON T1.StuID = T2.StuID JOIN Pets AS T3 ON T2.PetID = T3.PetID WHERE T1.Sex = 'F' AND T3.PetType = 'Dog'
SELECT count(*) FROM Has_Pet AS T1 JOIN Student AS T2 ON T1.StuID = T2.StuID JOIN Pets AS T3 ON T1.PetID = T3.PetID WHERE T2.Sex = 'F' AND T3.PetType = 'Dog'
SELECT count(DISTINCT PetType) FROM Pets
SELECT count(DISTINCT PetType) FROM Pets
SELECT T1.Fname FROM Student AS T1 JOIN Has_Pet AS T2 ON T1.StuID = T2.StuID JOIN Pets AS T3 ON T2.PetID = T3.PetID WHERE T3.PetType = "Cat" OR T3.PetType = "Dog"
SELECT Fname FROM Student WHERE StuID IN (SELECT StuID FROM Has_Pet WHERE PetID IN (SELECT PetID FROM Pets WHERE PetType IN ('cat', 'dog')))
SELECT Fname FROM Student WHERE StuID IN (SELECT StuID FROM Has_Pet WHERE PetID IN (SELECT PetID FROM Pets WHERE PetType = "Cat") INTERSECT SELECT StuID FROM Has_Pet WHERE PetID IN (SELECT PetID FROM Pets WHERE PetType = "Dog"))
SELECT Fname FROM Student WHERE StuID IN (SELECT StuID FROM Has_Pet WHERE PetID IN (SELECT PetID FROM Pets WHERE PetType = 'cat') INTERSECT SELECT StuID FROM Has_Pet WHERE PetID IN (SELECT PetID FROM Pets WHERE PetType = 'dog'))
SELECT Major, Age FROM Student WHERE StuID NOT IN (SELECT StuID FROM Has_Pet JOIN Pets ON Has_Pet.PetID = Pets.PetID WHERE PetType = 'Cat')
SELECT Major, Age FROM Student WHERE StuID NOT IN (SELECT StuID FROM Has_Pet JOIN Pets ON Has_Pet.PetID = Pets.PetID WHERE PetType = 'Cat')
SELECT StuID FROM Student WHERE StuID NOT IN (SELECT StuID FROM Has_Pet JOIN Pets ON Has_Pet.PetID = Pets.PetID WHERE PetType = 'cat')
SELECT StuID FROM Student EXCEPT SELECT T1.StuID FROM Has_Pet AS T1 JOIN Pets AS T2 ON T1.PetID = T2.PetID WHERE T2.PetType = 'cat'
SELECT Fname, Age FROM Student WHERE StuID IN (SELECT StuID FROM Has_Pet WHERE PetID IN (SELECT PetID FROM Pets WHERE PetType = 'Dog')) AND StuID NOT IN (SELECT StuID FROM Has_Pet WHERE PetID IN (SELECT PetID FROM Pets WHERE PetType = 'Cat'))
SELECT Fname FROM Student WHERE StuID IN (SELECT StuID FROM Has_Pet WHERE PetID IN (SELECT PetID FROM Pets WHERE PetType = 'Dog')) AND StuID NOT IN (SELECT StuID FROM Has_Pet WHERE PetID IN (SELECT PetID FROM Pets WHERE PetType = 'Cat'))
SELECT PetType, weight FROM Pets ORDER BY pet_age ASC LIMIT 1
SELECT PetType, weight FROM Pets ORDER BY pet_age ASC LIMIT 1
SELECT PetID, weight FROM Pets WHERE pet_age > 1
SELECT PetID, weight FROM Pets WHERE pet_age > 1
SELECT PetType , avg(pet_age) , max(pet_age) FROM Pets GROUP BY PetType
SELECT avg(pet_age) , max(pet_age) , PetType FROM Pets GROUP BY PetType
SELECT PetType , avg(weight) FROM Pets GROUP BY PetType
SELECT PetType , avg(weight) FROM Pets GROUP BY PetType
SELECT DISTINCT T1.Fname, T1.Age FROM Student AS T1 JOIN Has_Pet AS T2 ON T1.StuID = T2.StuID
SELECT DISTINCT T1.Fname, T1.Age FROM Student AS T1 JOIN Has_Pet AS T2 ON T1.StuID = T2.StuID
SELECT PetID FROM Has_Pet WHERE StuID = (SELECT StuID FROM Student WHERE LName = 'Smith')
SELECT PetID FROM Has_Pet JOIN Student ON Has_Pet.StuID = Student.StuID WHERE Student.LName = 'Smith'
SELECT Has_Pet.StuID , count(*) FROM Has_Pet JOIN Student ON Has_Pet.StuID = Student.StuID GROUP BY Has_Pet.StuID HAVING count(*) > 0
SELECT T1.StuID , count(*) FROM Has_Pet AS T1 JOIN Student AS T2 ON T1.StuID = T2.StuID GROUP BY T1.StuID
SELECT T1.Fname , T1.Sex FROM Student AS T1 JOIN Has_Pet AS T2 ON T1.StuID = T2.StuID GROUP BY T1.StuID HAVING count(*) > 1
SELECT Fname, Sex FROM Student AS S JOIN Has_Pet AS P ON S.StuID = P.StuID GROUP BY S.StuID HAVING count(*) > 1
SELECT LName FROM Student WHERE StuID IN (SELECT StuID FROM Has_Pet WHERE PetID IN (SELECT PetID FROM Pets WHERE PetType = 'cat' AND pet_age = 3))
SELECT S.LName FROM Student AS S JOIN Has_Pet AS HP ON S.StuID = HP.StuID JOIN Pets AS P ON HP.PetID = P.PetID WHERE P.PetType = 'cat' AND P.pet_age = 3;
SELECT avg(Age) FROM Student WHERE StuID NOT IN (SELECT StuID FROM Has_Pet)
SELECT avg(Age) FROM Student WHERE StuID NOT IN (SELECT StuID FROM Has_Pet)
SELECT count(*) FROM continents
SELECT count(*) FROM continents
SELECT T1.ContId , T1.Continent, count(*) FROM continents AS T1 JOIN countries AS T2 ON T1.ContId = T2.Continent GROUP BY T1.ContId
SELECT T1.ContId , T1.Continent, count(*) FROM continents AS T1 JOIN countries AS T2 ON T1.ContId = T2.Continent GROUP BY T1.ContId
SELECT count(*) FROM countries
SELECT count(*) FROM countries
SELECT car_makers.FullName, car_makers.Id, COUNT(model_list.Model) FROM car_makers JOIN model_list ON car_makers.Id = model_list.Maker GROUP BY car_makers.Id, car_makers.FullName
SELECT T1.Id, T1.FullName, COUNT(*) FROM car_makers AS T1 JOIN model_list AS T2 ON T1.Id = T2.Maker GROUP BY T1.Id, T1.FullName
SELECT Model FROM model_list WHERE Maker = (SELECT Maker FROM car_makers WHERE Country = (SELECT Country FROM cars_data ORDER BY Horsepower ASC LIMIT 1))
SELECT Model FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId JOIN model_list ON car_names.Model = model_list.Model WHERE Horsepower = ( SELECT MIN ( Horsepower ) FROM cars_data );
SELECT model FROM model_list WHERE ModelId IN (SELECT Id FROM cars_data WHERE Weight < (SELECT avg(Weight) FROM cars_data))
SELECT model FROM model_list WHERE Maker IN (SELECT Maker FROM car_names WHERE MakeId IN (SELECT Id FROM cars_data WHERE Weight < (SELECT AVG(Weight) FROM cars_data)));
SELECT Maker FROM car_makers WHERE Id IN (SELECT Maker FROM model_list WHERE ModelId IN (SELECT Model FROM car_names WHERE MakeId IN (SELECT Id FROM cars_data WHERE Year = 1970)))
SELECT DISTINCT T1.Maker FROM car_makers AS T1 JOIN model_list AS T2 ON T1.Id = T2.Maker JOIN car_names AS T3 ON T2.Model = T3.Model JOIN cars_data AS T4 ON T3.MakeId = T4.Id WHERE T4.Year = 1970
SELECT T1.Make , T1.Year FROM cars_data AS T1 JOIN car_names AS T2 ON T1.Id = T2.MakeId ORDER BY T1.Year ASC LIMIT 1
SELECT T1.Maker, T2.Year FROM car_makers AS T1 JOIN cars_data AS T2 ON T1.Id = T2.Id ORDER BY T2.Year ASC LIMIT 1
SELECT DISTINCT Model FROM model_list WHERE Maker IN (SELECT Id FROM car_makers WHERE Country IN (SELECT CountryId FROM countries WHERE Continent IN (SELECT ContId FROM continents))) AND ModelId IN (SELECT MakeId FROM cars_data WHERE Year > 1980)
SELECT DISTINCT T1.Model FROM model_list AS T1 JOIN cars_data AS T2 ON T1.ModelId = T2.Id WHERE T2.Year > 1980
SELECT T1.Continent , COUNT(*) FROM continents AS T1 JOIN countries AS T2 ON T1.ContId = T2.Continent JOIN car_makers AS T3 ON T2.CountryId = T3.Country GROUP BY T1.ContId
SELECT T1.Continent , COUNT(*) FROM continents AS T1 JOIN countries AS T2 ON T1.ContId = T2.Continent JOIN car_makers AS T3 ON T2.CountryId = T3.Country GROUP BY T1.Continent
SELECT countries.CountryName FROM car_makers JOIN countries ON car_makers.Country = countries.CountryId GROUP BY countries.CountryName ORDER BY COUNT(*) DESC LIMIT 1
SELECT T1.CountryName FROM countries AS T1 JOIN car_makers AS T2 ON T1.CountryId = T2.Country GROUP BY T1.CountryName ORDER BY count(*) DESC LIMIT 1
SELECT T1.FullName , COUNT(*) FROM car_makers AS T1 JOIN model_list AS T2 ON T1.Id = T2.Maker GROUP BY T1.FullName
SELECT car_makers.Id, car_makers.FullName, COUNT(model_list.Model) FROM car_makers JOIN model_list ON car_makers.Id = model_list.Maker GROUP BY car_makers.Id, car_makers.FullName
SELECT Accelerate FROM cars_data WHERE Id IN (SELECT MakeId FROM car_names WHERE Make = 'amc hornet sportabout (sw)')
SELECT Accelerate FROM cars_data WHERE Id IN (SELECT MakeId FROM car_names WHERE Make = 'amc hornet sportabout (sw)')
SELECT count(*) FROM car_makers AS T1 JOIN countries AS T2 ON T1.Country = T2.CountryId WHERE T2.CountryName = 'France'
SELECT count(DISTINCT Maker) FROM car_makers WHERE Country IN (SELECT CountryId FROM countries WHERE CountryName = 'France')
SELECT count(*) FROM model_list AS T1 JOIN car_makers AS T2 ON T1.Maker = T2.Id JOIN countries AS T3 ON T2.Country = T3.CountryId WHERE T3.CountryName = 'USA';
SELECT count(*) FROM model_list JOIN car_makers ON model_list.Maker = car_makers.Id JOIN countries ON car_makers.Country = countries.CountryId JOIN continents ON countries.Continent = continents.ContId WHERE continents.Continent = 'North America' AND countries.CountryName = 'United States';
SELECT avg(MPG) FROM cars_data WHERE Cylinders = 4
SELECT avg(MPG) FROM cars_data WHERE Cylinders = 4
SELECT MIN(Weight) FROM cars_data WHERE Cylinders = 8 AND Year = 1974
SELECT min(Weight) FROM cars_data WHERE Cylinders = 8 AND Year = 1974
SELECT car_makers.Maker , model_list.Model FROM car_makers JOIN model_list ON car_makers.Id = model_list.Maker
SELECT Maker , Model FROM model_list
SELECT countries.CountryId, countries.CountryName FROM countries JOIN car_makers ON countries.CountryId = car_makers.Country GROUP BY countries.CountryId, countries.CountryName
SELECT T1.CountryId, T1.CountryName FROM countries AS T1 JOIN car_makers AS T2 ON T1.CountryId = T2.Country GROUP BY T1.CountryId HAVING COUNT(*) >= 1
SELECT count(*) FROM cars_data WHERE Horsepower > 150
SELECT count(*) FROM cars_data WHERE Horsepower > 150
SELECT avg(Weight) , Year FROM cars_data GROUP BY Year
SELECT avg(Weight) , Year FROM cars_data GROUP BY Year
SELECT T2.CountryName FROM car_makers AS T1 JOIN countries AS T2 JOIN continents AS T3 ON T1.Country = T2.CountryId AND T2.Continent = T3.ContId WHERE T3.Continent = "Europe" GROUP BY T2.CountryName HAVING count(*) >= 3
SELECT CountryName FROM countries WHERE Continent IN (SELECT ContId FROM continents WHERE Continent = 'Europe') AND CountryId IN (SELECT Country FROM car_makers GROUP BY Country HAVING COUNT(Id) >= 3)
SELECT max(cars_data.Horsepower), car_names.Make FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE cars_data.Cylinders = 3
SELECT max(Horsepower), Make FROM cars_data AS T1 JOIN car_names AS T2 ON T1.Id = T2.MakeId WHERE Cylinders = 3
SELECT model FROM model_list JOIN cars_data ON model_list.ModelId = cars_data.Id ORDER BY MPG DESC LIMIT 1;
SELECT model FROM cars_data AS t1 JOIN model_list AS t2 ON t1.Id = t2.ModelId ORDER BY MPG DESC LIMIT 1
SELECT avg(Horsepower) FROM cars_data WHERE Year < 1980
SELECT avg(Horsepower) FROM cars_data WHERE Year < 1980
SELECT avg(Edispl) FROM cars_data AS T1 JOIN car_names AS T2 ON T1.Id = T2.MakeId JOIN model_list AS T3 ON T2.Model = T3.Model WHERE T3.Model = 'volvo'
SELECT avg(cars_data.Edispl) FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId JOIN model_list ON car_names.Model = model_list.Model JOIN car_makers ON model_list.Maker = car_makers.Id WHERE car_makers.Maker = 'volvo'
SELECT max(Accelerate) , Cylinders FROM cars_data GROUP BY Cylinders
SELECT max(Accelerate) , Cylinders FROM cars_data GROUP BY Cylinders
SELECT Model FROM model_list AS T1 JOIN car_names AS T2 ON T1.ModelId = T2.MakeId GROUP BY T1.Model ORDER BY COUNT(*) DESC LIMIT 1;
SELECT Model FROM model_list GROUP BY Model ORDER BY count(*) DESC LIMIT 1
SELECT count(*) FROM cars_data WHERE Cylinders > 4
SELECT count(*) FROM cars_data WHERE Cylinders > 4
SELECT count(*) FROM cars_data WHERE Year = 1980;
SELECT count(*) FROM cars_data WHERE Year = 1980
SELECT count(*) FROM model_list AS T1 JOIN car_makers AS T2 ON T1.Maker = T2.Id WHERE T2.FullName = "American Motor Company";
SELECT count(*) FROM car_makers AS T1 JOIN model_list AS T2 ON T1.Id = T2.Maker WHERE T1.Maker = "American Motor Company"
SELECT T1.Id, T1.FullName FROM car_makers AS T1 JOIN model_list AS T2 ON T1.Id = T2.Maker GROUP BY T1.Id HAVING COUNT(*) > 3
SELECT T2.Maker, T2.Id FROM model_list AS T1 JOIN car_makers AS T2 ON T1.Maker = T2.Id GROUP BY T1.Maker HAVING count(T1.ModelId) > 3;
SELECT DISTINCT T3.Model FROM car_makers AS T1 JOIN model_list AS T2 ON T1.Id = T2.Maker JOIN car_names AS T3 ON T2.ModelId = T3.MakeId JOIN cars_data AS T4 ON T3.MakeId = T4.Id WHERE T1.FullName = 'General Motors' OR T4.Weight > 3500
SELECT Model FROM model_list AS T1 JOIN car_makers AS T2 ON T1.Maker = T2.Id WHERE T2.Maker = 'General Motors' UNION SELECT T3.Model FROM cars_data AS T4 JOIN car_names AS T3 ON T4.Id = T3.MakeId WHERE T4.Weight > 3500
SELECT Year FROM cars_data WHERE Weight BETWEEN 3000 AND 4000
SELECT Year FROM cars_data WHERE Weight < 4000 INTERSECT SELECT Year FROM cars_data WHERE Weight > 3000
SELECT Horsepower FROM cars_data ORDER BY Accelerate DESC LIMIT 1
SELECT Horsepower FROM cars_data ORDER BY Accelerate DESC LIMIT 1
SELECT Cylinders FROM cars_data AS T1 JOIN car_names AS T2 ON T1.Id = T2.MakeId JOIN model_list AS T3 ON T2.Model = T3.Model WHERE T3.Model = 'volvo' ORDER BY T1.Accelerate ASC LIMIT 1;
SELECT Cylinders FROM cars_data AS T1 JOIN car_names AS T2 ON T1.Id = T2.MakeId JOIN model_list AS T3 ON T2.Model = T3.Model WHERE T3.Maker = (SELECT Id FROM car_makers WHERE Maker = 'volvo') ORDER BY T1.Accelerate ASC LIMIT 1;
SELECT COUNT(*) FROM cars_data WHERE Accelerate > (SELECT Accelerate FROM cars_data ORDER BY Horsepower DESC LIMIT 1)
SELECT count(*) FROM cars_data WHERE Accelerate > (SELECT Accelerate FROM cars_data ORDER BY Horsepower DESC LIMIT 1)
SELECT count(*) FROM (SELECT Country FROM car_makers GROUP BY Country HAVING count(*) > 2)
SELECT count(*) FROM (SELECT Country FROM car_makers GROUP BY Country HAVING count(*) > 2)
SELECT count(*) FROM cars_data WHERE Cylinders > 6
SELECT count(*) FROM cars_data WHERE Cylinders > 6;
SELECT T2.Model FROM cars_data AS T1 JOIN car_names AS T2 ON T1.Id = T2.MakeId WHERE T1.Cylinders = 4 ORDER BY T1.Horsepower DESC LIMIT 1;
SELECT T2.Model FROM cars_data AS T1 JOIN model_list AS T2 ON T1.Id = T2.ModelId WHERE T1.Cylinders = 4 ORDER BY T1.Horsepower DESC LIMIT 1;
SELECT MakeId, Make FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE Horsepower > (SELECT MIN(Horsepower) FROM cars_data) AND Cylinders <= 3
SELECT MakeId, Make FROM cars_data JOIN car_names ON cars_data.Id = car_names.MakeId WHERE Cylinders < 4 AND Horsepower > (SELECT MIN(Horsepower) FROM cars_data)
SELECT max(MPG) FROM cars_data WHERE Cylinders = 8 OR Year < 1980
SELECT max(MPG) FROM cars_data WHERE Cylinders = 8 OR Year < 1980
SELECT model_list.Model FROM model_list JOIN car_makers ON model_list.Maker = car_makers.Id JOIN cars_data ON model_list.ModelId = cars_data.Id WHERE cars_data.Weight < 3500 AND car_makers.Maker != 'Ford Motor Company'
SELECT model FROM model_list WHERE ModelId IN (SELECT MakeId FROM cars_data WHERE Weight < 3500) AND Maker NOT IN (SELECT Id FROM car_makers WHERE Maker = 'Ford')
SELECT CountryName FROM countries WHERE CountryId NOT IN (SELECT Country FROM car_makers)
SELECT CountryName FROM countries WHERE CountryId NOT IN (SELECT Country FROM car_makers)
SELECT T1.Id, T1.Maker FROM car_makers AS T1 JOIN model_list AS T2 ON T1.Id = T2.Maker GROUP BY T1.Id HAVING COUNT(*) >= 2 INTERSECT SELECT T1.Id, T1.Maker FROM car_makers AS T1 JOIN countries AS T2 ON T1.Country = T2.CountryId GROUP BY T2.CountryId HAVING COUNT(*) > 3
SELECT T1.Id, T1.Maker FROM car_makers AS T1 JOIN model_list AS T2 ON T1.Id = T2.Maker JOIN cars_data AS T3 ON T2.ModelId = T3.Id GROUP BY T1.Id HAVING COUNT(DISTINCT T2.Model) >= 2 AND COUNT(T3.Id) > 3
SELECT CountryId, CountryName FROM countries WHERE CountryId IN (SELECT Country FROM car_makers GROUP BY Country HAVING COUNT(Id) > 3) OR CountryId IN (SELECT Country FROM car_makers WHERE Id IN (SELECT Maker FROM model_list WHERE Model = 'fiat'))
SELECT CountryId, CountryName FROM countries WHERE CountryId IN (SELECT Country FROM car_makers GROUP BY Country HAVING COUNT(*) > 3) OR CountryId IN (SELECT Country FROM car_makers WHERE Id IN (SELECT Maker FROM model_list WHERE Model = 'Fiat'))
SELECT Country FROM airlines WHERE Airline = "JetBlue Airways"
SELECT Country FROM airlines WHERE Airline = "Jetblue Airways";
SELECT Abbreviation FROM airlines WHERE Airline = "JetBlue Airways"
SELECT Abbreviation FROM airlines WHERE Airline = "Jetblue Airways";
SELECT Airline, Abbreviation FROM airlines WHERE Country = "USA"
SELECT Airline, Abbreviation FROM airlines WHERE Country = 'USA'
SELECT AirportCode, AirportName FROM airports WHERE City = "Anthony"
SELECT AirportCode, AirportName FROM airports WHERE City = "Anthony"
SELECT count(*) FROM airlines
SELECT count(*) FROM airlines
SELECT count(*) FROM airports
SELECT count(*) FROM airports
SELECT count(*) FROM flights
SELECT count(*) FROM flights
SELECT Airline FROM airlines WHERE Abbreviation = 'UAL'
SELECT Airline FROM airlines WHERE Abbreviation = 'UAL'
SELECT count(*) FROM airlines WHERE Country = 'USA'
SELECT count(*) FROM airlines WHERE Country = 'USA'
SELECT City, Country FROM airports WHERE AirportName = 'Alton'
SELECT City, Country FROM airports WHERE AirportName = 'Alton'
SELECT AirportName FROM airports WHERE AirportCode = "AKO"
SELECT AirportName FROM airports WHERE AirportCode = 'AKO'
SELECT AirportName FROM airports WHERE City = "Aberdeen"
SELECT AirportName FROM airports WHERE City = "Aberdeen"
SELECT count(*) FROM flights WHERE SourceAirport = 'APG'
SELECT count(*) FROM flights WHERE SourceAirport = 'APG'
SELECT count(*) FROM flights WHERE DestAirport = "ATO"
SELECT count(*) FROM flights WHERE DestAirport = 'ATO'
SELECT count(*) FROM flights INNER JOIN airports ON flights.SourceAirport = airports.AirportCode WHERE airports.City = 'Aberdeen'
SELECT count(*) FROM flights WHERE SourceAirport = 'Aberdeen'
SELECT count(*) FROM flights WHERE DestAirport IN (SELECT AirportCode FROM airports WHERE City = 'Aberdeen')
SELECT count(*) FROM flights WHERE DestAirport IN (SELECT AirportCode FROM airports WHERE City = 'Aberdeen')
SELECT count(*) FROM flights AS F JOIN airports AS S ON F.SourceAirport = S.AirportCode JOIN airports AS D ON F.DestAirport = D.AirportCode WHERE S.City = 'Aberdeen' AND D.City = 'Ashley'
SELECT count(*) FROM flights WHERE SourceAirport = 'Aberdeen' AND DestAirport = 'Ashley'
SELECT count(*) FROM flights JOIN airlines ON flights.Airline = airlines.uid WHERE airlines.Airline = 'JetBlue Airways'
SELECT count(*) FROM flights AS F JOIN airlines AS A ON F.Airline = A.uid WHERE A.Airline = "Jetblue Airways"
SELECT count(*) FROM flights AS T1 JOIN airlines AS T2 ON T1.Airline = T2.uid WHERE T2.Airline = 'United Airlines' AND T1.DestAirport = 'ASY'
SELECT COUNT(*) FROM flights WHERE Airline = (SELECT uid FROM airlines WHERE Airline = "United Airlines") AND DestAirport = "ASY"
SELECT count(*) FROM flights AS t1 JOIN airlines AS t2 ON t1.Airline = t2.uid WHERE t2.Airline = 'United Airlines' AND t1.SourceAirport = 'AHD'
SELECT count(*) FROM flights WHERE Airline IN (SELECT uid FROM airlines WHERE Airline = 'United Airlines') AND SourceAirport = 'AHD'
SELECT count(*) FROM flights WHERE Airline IN (SELECT uid FROM airlines WHERE Airline = 'United Airlines') AND DestAirport IN (SELECT AirportCode FROM airports WHERE City = 'Aberdeen')
SELECT count(*) FROM flights WHERE Airline IN (SELECT uid FROM airlines WHERE Airline = 'United Airlines') AND DestAirport IN (SELECT AirportCode FROM airports WHERE City = 'Aberdeen')
SELECT City FROM airports JOIN flights ON airports.AirportCode = flights.DestAirport GROUP BY City ORDER BY count(*) DESC LIMIT 1;
SELECT City FROM airports JOIN flights ON airports.AirportCode = flights.DestAirport GROUP BY City ORDER BY COUNT(*) DESC LIMIT 1
SELECT City FROM airports JOIN flights ON airports.AirportCode = flights.SourceAirport GROUP BY City ORDER BY count(*) DESC LIMIT 1
SELECT City FROM airports JOIN flights ON airports.AirportCode = flights.SourceAirport GROUP BY flights.SourceAirport ORDER BY count(*) DESC LIMIT 1
SELECT SourceAirport FROM flights GROUP BY SourceAirport ORDER BY count(*) DESC LIMIT 1
SELECT SourceAirport FROM flights GROUP BY SourceAirport ORDER BY count(*) DESC LIMIT 1
SELECT SourceAirport FROM flights GROUP BY SourceAirport ORDER BY count(*) ASC LIMIT 1
SELECT SourceAirport FROM flights GROUP BY SourceAirport ORDER BY count(*) ASC LIMIT 1
SELECT Airline FROM flights GROUP BY Airline ORDER BY count(*) DESC LIMIT 1
SELECT Airline FROM flights GROUP BY Airline ORDER BY COUNT(*) DESC LIMIT 1
SELECT T1.Abbreviation, T1.Country FROM airlines AS T1 JOIN flights AS T2 ON T1.uid = T2.Airline GROUP BY T2.Airline ORDER BY count(*) ASC LIMIT 1
SELECT T1.Abbreviation, T1.Country FROM airlines AS T1 JOIN flights AS T2 ON T1.uid = T2.Airline GROUP BY T2.Airline ORDER BY count(*) ASC LIMIT 1
SELECT Airline FROM airlines WHERE uid IN (SELECT Airline FROM flights WHERE SourceAirport = 'AHD')
SELECT a.Airline FROM airlines AS a JOIN flights AS f ON a.uid = f.Airline WHERE f.SourceAirport = "AHD"
SELECT Airline FROM airlines AS T1 JOIN flights AS T2 ON T1.uid = T2.Airline WHERE T2.DestAirport = 'AHD'
SELECT a.Airline FROM airlines AS a JOIN flights AS f ON a.uid = f.Airline WHERE f.DestAirport = "AHD"
SELECT a.Airline FROM airlines AS a JOIN flights AS f ON a.uid = f.Airline WHERE f.SourceAirport IN ('APG', 'CVO') GROUP BY a.Airline HAVING COUNT(DISTINCT f.SourceAirport) = 2
SELECT Airline FROM airlines WHERE uid IN (SELECT Airline FROM flights WHERE SourceAirport = "APG" INTERSECT SELECT Airline FROM flights WHERE SourceAirport = "CVO")
SELECT Airline FROM airlines WHERE uid IN (SELECT Airline FROM flights WHERE SourceAirport = 'CVO') AND uid NOT IN (SELECT Airline FROM flights WHERE SourceAirport = 'APG')
SELECT a.Airline FROM airlines a JOIN flights f ON a.uid = f.Airline WHERE f.SourceAirport = 'CVO' AND a.uid NOT IN ( SELECT Airline FROM flights WHERE SourceAirport = 'APG' )
SELECT Airline FROM flights GROUP BY Airline HAVING count(*) >= 10
SELECT Airline FROM flights GROUP BY Airline HAVING count(*) >= 10
SELECT Airline FROM airlines WHERE uid IN (SELECT Airline FROM flights GROUP BY Airline HAVING COUNT(*) < 200)
SELECT T2.Airline FROM flights AS T1 JOIN airlines AS T2 ON T1.Airline = T2.uid GROUP BY T1.Airline HAVING count(T1.FlightNo) < 200;
SELECT FlightNo FROM flights WHERE Airline IN (SELECT uid FROM airlines WHERE Airline = "United Airlines")
SELECT FlightNo FROM flights JOIN airlines ON flights.Airline = airlines.uid WHERE airlines.Airline = "United Airlines"
SELECT FlightNo FROM flights WHERE SourceAirport = "APG"
SELECT FlightNo FROM flights WHERE SourceAirport = "APG";
SELECT FlightNo FROM flights WHERE DestAirport = "APG"
SELECT FlightNo FROM flights WHERE DestAirport = 'APG'
SELECT FlightNo FROM flights AS T1 JOIN airports AS T2 ON T1.SourceAirport = T2.AirportCode WHERE T2.City = "Aberdeen"
SELECT FlightNo FROM flights WHERE SourceAirport = "Aberdeen";
SELECT FlightNo FROM flights AS T1 JOIN airports AS T2 ON T1.DestAirport = T2.AirportCode WHERE T2.City = "Aberdeen"
SELECT FlightNo FROM flights WHERE DestAirport IN (SELECT AirportCode FROM airports WHERE City = 'Aberdeen')
SELECT count(*) FROM flights AS T1 JOIN airports AS T2 ON T1.DestAirport = T2.AirportCode WHERE T2.City IN ('Aberdeen', 'Abilene')
SELECT count(*) FROM flights WHERE DestAirport IN ('ABZ', 'ABI')
SELECT AirportName FROM airports WHERE AirportCode NOT IN (SELECT SourceAirport FROM flights UNION SELECT DestAirport FROM flights)
SELECT AirportName FROM airports WHERE AirportCode NOT IN (SELECT SourceAirport FROM flights) AND AirportCode NOT IN (SELECT DestAirport FROM flights)
SELECT count(*) FROM employee
SELECT count(*) FROM employee
SELECT Name FROM employee ORDER BY Age ASC
SELECT Name FROM employee ORDER BY Age ASC
SELECT City , COUNT(*) FROM employee GROUP BY City
SELECT City , count(*) FROM employee GROUP BY City
SELECT City FROM employee WHERE Age < 30 GROUP BY City HAVING count(*) > 1
SELECT City FROM employee WHERE Age < 30 GROUP BY City HAVING COUNT(*) > 1
SELECT count(*) , Location FROM shop GROUP BY Location
SELECT count(*) , Location FROM shop GROUP BY Location
SELECT Manager_name, District FROM shop ORDER BY Number_products DESC LIMIT 1
SELECT Manager_name, District FROM shop ORDER BY Number_products DESC LIMIT 1
SELECT min(Number_products) , max(Number_products) FROM shop
SELECT min(Number_products) , max(Number_products) FROM shop
SELECT Name, Location, District FROM shop ORDER BY Number_products DESC
SELECT Name, Location, District FROM shop ORDER BY Number_products DESC
SELECT Name FROM shop WHERE Number_products > (SELECT avg(Number_products) FROM shop)
SELECT Name FROM shop WHERE Number_products > (SELECT avg(Number_products) FROM shop)
SELECT T1.Name FROM employee AS T1 JOIN evaluation AS T2 ON T1.Employee_ID = T2.Employee_ID GROUP BY T1.Employee_ID ORDER BY COUNT(*) DESC LIMIT 1
SELECT T2.Name FROM evaluation AS T1 JOIN employee AS T2 ON T1.Employee_ID = T2.Employee_ID GROUP BY T2.Name ORDER BY COUNT(*) DESC LIMIT 1
SELECT T1.Name FROM employee AS T1 JOIN evaluation AS T2 ON T1.Employee_ID = T2.Employee_ID ORDER BY T2.Bonus DESC LIMIT 1
SELECT T1.Name FROM employee AS T1 JOIN evaluation AS T2 ON T1.Employee_ID = T2.Employee_ID ORDER BY T2.Bonus DESC LIMIT 1
SELECT Name FROM employee WHERE Employee_ID NOT IN (SELECT Employee_ID FROM evaluation)
SELECT Name FROM employee WHERE Employee_ID NOT IN (SELECT Employee_ID FROM evaluation)
SELECT T2.Name FROM hiring AS T1 JOIN shop AS T2 ON T1.Shop_ID = T2.Shop_ID GROUP BY T1.Shop_ID ORDER BY COUNT(*) DESC LIMIT 1
SELECT T2.Name FROM hiring AS T1 JOIN shop AS T2 ON T1.Shop_ID = T2.Shop_ID GROUP BY T2.Name ORDER BY COUNT(*) DESC LIMIT 1
SELECT Name FROM shop WHERE Shop_ID NOT IN (SELECT Shop_ID FROM hiring)
SELECT Name FROM shop WHERE Shop_ID NOT IN (SELECT Shop_ID FROM hiring)
SELECT t1.Name, count(*) FROM shop AS t1 JOIN hiring AS t2 ON t1.Shop_ID = t2.Shop_ID GROUP BY t1.Name
SELECT T1.Name , COUNT(*) FROM shop AS T1 JOIN hiring AS T2 ON T1.Shop_ID = T2.Shop_ID GROUP BY T1.Name
SELECT sum(Bonus) FROM evaluation
SELECT sum(Bonus) FROM evaluation
SELECT * FROM hiring
SELECT * FROM hiring
SELECT District FROM shop WHERE Number_products < 3000 INTERSECT SELECT District FROM shop WHERE Number_products > 10000
SELECT District FROM shop WHERE Number_products < 3000 INTERSECT SELECT District FROM shop WHERE Number_products > 10000
SELECT count(DISTINCT Location) FROM shop
SELECT count(DISTINCT Location) FROM shop
SELECT count(*) FROM Documents
SELECT count(*) FROM Documents
SELECT Document_ID , Document_Name , Document_Description FROM Documents
SELECT Document_ID, Document_Name, Document_Description FROM Documents
SELECT Document_Name, Template_ID FROM Documents WHERE Document_Description LIKE '%w%'
SELECT Document_Name, Template_ID FROM Documents WHERE Document_Description LIKE "%w%"
SELECT Document_ID, Template_ID, Document_Description FROM Documents WHERE Document_Name = "Robbin CV"
SELECT Document_ID, Template_ID, Document_Description FROM Documents WHERE Document_Name = "Robbin CV"
SELECT count(DISTINCT Template_ID) FROM Documents
SELECT count(DISTINCT Template_ID) FROM Documents
SELECT count(*) FROM Documents WHERE Template_ID IN (SELECT Template_ID FROM Templates WHERE Template_Type_Code = 'PPT')
SELECT count(*) FROM Documents AS D JOIN Templates AS T ON D.Template_ID = T.Template_ID JOIN Ref_Template_Types AS RTT ON T.Template_Type_Code = RTT.Template_Type_Code WHERE RTT.Template_Type_Description = "PPT"
SELECT Template_ID , count(*) FROM Documents GROUP BY Template_ID;
SELECT Template_ID , count(*) FROM Documents GROUP BY Template_ID
SELECT T1.Template_ID, T1.Template_Type_Code FROM Templates AS T1 JOIN Documents AS T2 ON T1.Template_ID = T2.Template_ID GROUP BY T1.Template_ID ORDER BY COUNT(*) DESC LIMIT 1
SELECT T1.Template_ID , T1.Template_Type_Code FROM Templates AS T1 JOIN Documents AS T2 ON T1.Template_ID = T2.Template_ID GROUP BY T1.Template_ID ORDER BY count(*) DESC LIMIT 1
SELECT Template_ID FROM Documents GROUP BY Template_ID HAVING count(*) > 1
SELECT Template_ID FROM Documents GROUP BY Template_ID HAVING COUNT(*) > 1
SELECT Template_ID FROM Templates EXCEPT SELECT Template_ID FROM Documents
SELECT Template_ID FROM Templates WHERE Template_ID NOT IN (SELECT Template_ID FROM Documents)
SELECT count(*) FROM Templates
SELECT count(*) FROM Templates
SELECT Template_ID , Version_Number , Template_Type_Code FROM Templates
SELECT Template_ID , Version_Number , Template_Type_Code FROM Templates
SELECT distinct(Template_Type_Code) FROM Templates
SELECT DISTINCT Template_Type_Code FROM Ref_Template_Types
SELECT Template_ID FROM Templates WHERE Template_Type_Code = "PP" OR Template_Type_Code = "PPT"
SELECT Template_ID FROM Templates WHERE Template_Type_Code IN ('PP', 'PPT')
SELECT count(*) FROM Templates WHERE Template_Type_Code = 'CV'
SELECT count(*) FROM Templates AS t1 JOIN Ref_Template_Types AS t2 ON t1.Template_Type_Code = t2.Template_Type_Code WHERE t2.Template_Type_Description = "CV"
SELECT Version_Number , Template_Type_Code FROM Templates WHERE Version_Number > 5
SELECT Version_Number, Template_Type_Code FROM Templates WHERE Version_Number > 5
SELECT Template_Type_Code , count(*) FROM Templates GROUP BY Template_Type_Code
SELECT Template_Type_Code , count(*) FROM Templates GROUP BY Template_Type_Code
SELECT Template_Type_Code FROM Templates GROUP BY Template_Type_Code ORDER BY count(*) DESC LIMIT 1
SELECT Template_Type_Code FROM Templates GROUP BY Template_Type_Code ORDER BY count(*) DESC LIMIT 1
SELECT Template_Type_Code FROM Templates GROUP BY Template_Type_Code HAVING COUNT(*) < 3
SELECT Template_Type_Code FROM Templates GROUP BY Template_Type_Code HAVING count(*) < 3
SELECT MIN(Version_Number), Template_Type_Code FROM Templates GROUP BY Template_Type_Code ORDER BY MIN(Version_Number) ASC LIMIT 1;
SELECT MIN(Version_Number), Template_Type_Code FROM Templates GROUP BY Template_Type_Code
SELECT T2.Template_Type_Code FROM Documents AS T1 JOIN Templates AS T2 ON T1.Template_ID = T2.Template_ID WHERE T1.Document_Name = "Data base"
SELECT T2.Template_Type_Code FROM Documents AS T1 JOIN Templates AS T2 ON T1.Template_ID = T2.Template_ID WHERE T1.Document_Name = "Data base"
SELECT T2.Document_Name FROM Templates AS T1 JOIN Documents AS T2 ON T1.Template_ID = T2.Template_ID WHERE T1.Template_Type_Code = "BK"
SELECT Document_Name FROM Documents AS D JOIN Templates AS T ON D.Template_ID = T.Template_ID WHERE T.Template_Type_Code = "BK"
SELECT t.Template_Type_Code, COUNT(d.Document_ID) FROM Ref_Template_Types t LEFT JOIN Templates te ON t.Template_Type_Code = te.Template_Type_Code LEFT JOIN Documents d ON te.Template_ID = d.Template_ID GROUP BY t.Template_Type_Code
SELECT T1.Template_Type_Code , count(*) FROM Ref_Template_Types AS T1 JOIN Templates AS T2 ON T1.Template_Type_Code = T2.Template_Type_Code JOIN Documents AS T3 ON T2.Template_ID = T3.Template_ID GROUP BY T1.Template_Type_Code
SELECT t2.Template_Type_Code FROM Documents AS t1 JOIN Templates AS t2 ON t1.Template_ID = t2.Template_ID GROUP BY t2.Template_Type_Code ORDER BY count(*) DESC LIMIT 1
SELECT Template_Type_Code FROM Templates JOIN Documents ON Templates.Template_ID = Documents.Template_ID GROUP BY Template_Type_Code ORDER BY COUNT(*) DESC LIMIT 1
SELECT Template_Type_Code FROM Ref_Template_Types EXCEPT SELECT T1.Template_Type_Code FROM Ref_Template_Types AS T1 JOIN Templates AS T2 ON T1.Template_Type_Code = T2.Template_Type_Code JOIN Documents AS T3 ON T2.Template_ID = T3.Template_ID
SELECT Template_Type_Code FROM Ref_Template_Types WHERE Template_Type_Code NOT IN (SELECT Template_Type_Code FROM Templates WHERE Template_ID IN (SELECT Template_ID FROM Documents))
SELECT Template_Type_Code , Template_Type_Description FROM Ref_Template_Types
SELECT Template_Type_Code , Template_Type_Description FROM Ref_Template_Types
SELECT Template_Type_Description FROM Ref_Template_Types WHERE Template_Type_Code = "AD"
SELECT Template_Type_Description FROM Ref_Template_Types WHERE Template_Type_Code = "AD"
SELECT Template_Type_Code FROM Ref_Template_Types WHERE Template_Type_Description = "Book"
SELECT Template_Type_Code FROM Ref_Template_Types WHERE Template_Type_Description = "Book"
SELECT DISTINCT Template_Type_Description FROM Ref_Template_Types WHERE Template_Type_Code IN (SELECT Template_Type_Code FROM Templates WHERE Template_ID IN (SELECT Template_ID FROM Documents))
SELECT DISTINCT Template_Type_Description FROM Ref_Template_Types INNER JOIN Templates ON Ref_Template_Types.Template_Type_Code = Templates.Template_Type_Code INNER JOIN Documents ON Templates.Template_ID = Documents.Template_ID
SELECT Template_ID FROM Templates AS T1 JOIN Ref_Template_Types AS T2 ON T1.Template_Type_Code = T2.Template_Type_Code WHERE T2.Template_Type_Description = "Presentation"
SELECT T1.Template_ID FROM Templates AS T1 JOIN Ref_Template_Types AS T2 ON T1.Template_Type_Code = T2.Template_Type_Code WHERE T2.Template_Type_Description = 'Presentation'
SELECT count(*) FROM Paragraphs;
SELECT count(*) FROM Paragraphs
SELECT count(*) FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.Document_ID = T2.Document_ID WHERE T2.Document_Name = 'Summer Show'
SELECT count(*) FROM Documents AS t1 JOIN Paragraphs AS t2 ON t1.Document_ID = t2.Document_ID WHERE t1.Document_Name = "Summer Show"
SELECT Other_Details FROM Paragraphs WHERE Paragraph_Text = "Korea"
SELECT Paragraph_Details FROM Paragraphs WHERE Paragraph_Text LIKE '%Korea%'
SELECT Paragraph_ID, Paragraph_Text FROM Paragraphs WHERE Document_ID IN (SELECT Document_ID FROM Documents WHERE Document_Name = 'Welcome to NY')
SELECT Paragraph_ID, Paragraph_Text FROM Paragraphs WHERE Document_ID IN (SELECT Document_ID FROM Documents WHERE Document_Name = 'Welcome to NY')
SELECT Paragraph_Text FROM Paragraphs AS T1 JOIN Documents AS T2 ON T1.Document_ID = T2.Document_ID WHERE T2.Document_Name = "Customer reviews"
SELECT Paragraph_Text FROM Paragraphs AS P JOIN Documents AS D ON P.Document_ID = D.Document_ID WHERE D.Document_Name = 'Customer reviews'
SELECT Document_ID , count(*) FROM Paragraphs GROUP BY Document_ID ORDER BY Document_ID
SELECT Document_ID, COUNT(*) FROM Paragraphs GROUP BY Document_ID ORDER BY Document_ID
SELECT T1.Document_ID, T1.Document_Name, COUNT(*) FROM Documents AS T1 JOIN Paragraphs AS T2 ON T1.Document_ID = T2.Document_ID GROUP BY T1.Document_ID, T1.Document_Name
SELECT T1.Document_ID , T1.Document_Name , count(*) FROM Documents AS T1 JOIN Paragraphs AS T2 ON T1.Document_ID = T2.Document_ID GROUP BY T1.Document_ID
SELECT Document_ID FROM Paragraphs GROUP BY Document_ID HAVING COUNT(*) >= 2
SELECT Document_ID FROM Paragraphs GROUP BY Document_ID HAVING count(*) >= 2
SELECT T1.Document_ID, T1.Document_Name FROM Documents AS T1 JOIN Paragraphs AS T2 ON T1.Document_ID = T2.Document_ID GROUP BY T1.Document_ID ORDER BY count(*) DESC LIMIT 1
SELECT T1.Document_ID , T1.Document_Name FROM Documents AS T1 JOIN Paragraphs AS T2 ON T1.Document_ID = T2.Document_ID GROUP BY T1.Document_ID ORDER BY count(*) DESC LIMIT 1
SELECT Document_ID FROM Paragraphs GROUP BY Document_ID ORDER BY count(*) LIMIT 1;
SELECT Document_ID FROM Paragraphs GROUP BY Document_ID ORDER BY count(*) ASC LIMIT 1
SELECT Document_ID FROM Documents WHERE Document_ID IN (SELECT Document_ID FROM Paragraphs GROUP BY Document_ID HAVING COUNT(Paragraph_ID) BETWEEN 1 AND 2)
SELECT Document_ID FROM Paragraphs GROUP BY Document_ID HAVING COUNT(*) BETWEEN 1 AND 2;
SELECT Document_ID FROM Paragraphs WHERE Paragraph_Text IN ('Brazil', 'Ireland')
SELECT Document_ID FROM Paragraphs WHERE Paragraph_Text LIKE '%Brazil%' INTERSECT SELECT Document_ID FROM Paragraphs WHERE Paragraph_Text LIKE '%Ireland%'
SELECT count(*) FROM teacher
SELECT count(*) FROM teacher
SELECT Name FROM teacher ORDER BY Age ASC
SELECT Name FROM teacher ORDER BY Age ASC
SELECT Age , Hometown FROM teacher
SELECT Age , Hometown FROM teacher
SELECT Name FROM teacher WHERE Hometown != "Little Lever Urban District"
SELECT Name FROM teacher WHERE Hometown != "Little Lever Urban District"
SELECT Name FROM teacher WHERE Age = "32" OR Age = "33"
SELECT Name FROM teacher WHERE Age = '32' OR Age = '33'
SELECT Hometown FROM teacher ORDER BY Age ASC LIMIT 1
SELECT Hometown FROM teacher ORDER BY Age ASC LIMIT 1
SELECT Hometown , COUNT(*) FROM teacher GROUP BY Hometown
SELECT Hometown , COUNT(*) FROM teacher GROUP BY Hometown
SELECT Hometown FROM teacher GROUP BY Hometown ORDER BY COUNT(*) DESC LIMIT 1
SELECT Hometown FROM teacher GROUP BY Hometown ORDER BY COUNT(*) DESC LIMIT 1
SELECT Hometown FROM teacher GROUP BY Hometown HAVING COUNT(*) >= 2
SELECT Hometown FROM teacher GROUP BY Hometown HAVING COUNT(*) >= 2
SELECT teacher.Name, course.Course FROM course_arrange JOIN teacher ON course_arrange.Teacher_ID = teacher.Teacher_ID JOIN course ON course_arrange.Course_ID = course.Course_ID
SELECT T2.Name , T1.Course FROM course AS T1 JOIN course_arrange AS T3 ON T1.Course_ID = T3.Course_ID JOIN teacher AS T2 ON T3.Teacher_ID = T2.Teacher_ID
SELECT T2.Name, T1.Course FROM course_arrange AS T1 JOIN teacher AS T2 ON T1.Teacher_ID = T2.Teacher_ID JOIN course AS T3 ON T1.Course_ID = T3.Course_ID ORDER BY T2.Name ASC
SELECT teacher.Name, course.Course FROM course_arrange JOIN teacher ON course_arrange.Teacher_ID = teacher.Teacher_ID JOIN course ON course_arrange.Course_ID = course.Course_ID ORDER BY teacher.Name ASC
SELECT T2.Name FROM course AS T1 JOIN course_arrange AS T3 ON T1.Course_ID = T3.Course_ID JOIN teacher AS T2 ON T3.Teacher_ID = T2.Teacher_ID WHERE T1.Course = 'Math'
SELECT T.Name FROM teacher AS T JOIN course_arrange AS CA ON T.Teacher_ID = CA.Teacher_ID JOIN course AS C ON CA.Course_ID = C.Course_ID WHERE C.Course = "Math"
SELECT T1.Name , COUNT(*) FROM teacher AS T1 JOIN course_arrange AS T2 ON T1.Teacher_ID = T2.Teacher_ID GROUP BY T1.Name
SELECT T2.Name , COUNT(*) FROM course_arrange AS T1 JOIN teacher AS T2 ON T1.Teacher_ID = T2.Teacher_ID GROUP BY T2.Name
SELECT T2.Name FROM course_arrange AS T1 JOIN teacher AS T2 ON T1.Teacher_ID = T2.Teacher_ID GROUP BY T1.Teacher_ID HAVING COUNT(*) >= 2
SELECT T2.Name FROM course_arrange AS T1 JOIN teacher AS T2 ON T1.Teacher_ID = T2.Teacher_ID GROUP BY T1.Teacher_ID HAVING COUNT(*) >= 2
SELECT Name FROM teacher WHERE Teacher_ID NOT IN (SELECT Teacher_ID FROM course_arrange)
SELECT Name FROM teacher WHERE Teacher_ID NOT IN (SELECT Teacher_ID FROM course_arrange)
SELECT count(*) FROM visitor WHERE Age < 30;
SELECT Name FROM visitor WHERE Level_of_membership > 4 ORDER BY Level_of_membership DESC
SELECT avg(Age) FROM visitor WHERE Level_of_membership <= 4
SELECT Name, Level_of_membership FROM visitor WHERE Level_of_membership > 4 ORDER BY Age DESC
SELECT Museum_ID , Name FROM museum ORDER BY Num_of_Staff DESC LIMIT 1
SELECT avg(Num_of_Staff) FROM museum WHERE Open_Year < '2009'
SELECT Open_Year , Num_of_Staff FROM museum WHERE Name = "Plaza Museum"
SELECT Name FROM museum WHERE Num_of_Staff > (SELECT min(Num_of_Staff) FROM museum WHERE Open_Year > '2010')
SELECT T1.ID, T1.Name, T1.Age FROM visitor AS T1 JOIN visit AS T2 ON T1.ID = T2.visitor_ID GROUP BY T2.visitor_ID HAVING COUNT(*) > 1
SELECT T2.ID, T2.Name, T2.Level_of_membership FROM visitor AS T2 JOIN visit AS T1 ON T2.ID = T1.visitor_ID GROUP BY T2.ID ORDER BY SUM(T1.Total_spent) DESC LIMIT 1
SELECT T1.Museum_ID , T1.Name FROM museum AS T1 JOIN visit AS T2 ON T1.Museum_ID = T2.Museum_ID GROUP BY T1.Museum_ID ORDER BY count(*) DESC LIMIT 1
SELECT Name FROM museum WHERE Museum_ID NOT IN (SELECT Museum_ID FROM visit)
SELECT T1.Name, T1.Age FROM visitor AS T1 JOIN visit AS T2 ON T1.ID = T2.visitor_ID ORDER BY T2.Num_of_Ticket DESC LIMIT 1
SELECT avg(Num_of_Ticket) , max(Num_of_Ticket) FROM visit
SELECT sum(Total_spent) FROM visit AS T1 JOIN visitor AS T2 ON T1.visitor_ID = T2.ID WHERE T2.Level_of_membership = 1
SELECT T1.Name FROM visitor AS T1 JOIN visit AS T2 JOIN museum AS T3 ON T1.ID = T2.visitor_ID AND T2.Museum_ID = T3.Museum_ID WHERE T3.Open_Year < '2009' INTERSECT SELECT T1.Name FROM visitor AS T1 JOIN visit AS T2 JOIN museum AS T3 ON T1.ID = T2.visitor_ID AND T2.Museum_ID = T3.Museum_ID WHERE T3.Open_Year > '2011'
SELECT count(*) FROM visitor WHERE ID NOT IN ( SELECT visitor_ID FROM visit WHERE Museum_ID IN (SELECT Museum_ID FROM museum WHERE Open_Year > '2010'))
SELECT count(*) FROM museum WHERE Open_Year > '2013' OR Open_Year < '2008'
SELECT count(*) FROM players
SELECT count(*) FROM players
SELECT count(*) FROM matches
SELECT count(*) FROM matches
SELECT first_name, birth_date FROM players WHERE country_code = "USA"
SELECT first_name, birth_date FROM players WHERE country_code = 'USA'
SELECT avg(loser_age) , avg(winner_age) FROM matches
SELECT avg(loser_age) , avg(winner_age) FROM matches
SELECT avg(winner_rank) FROM matches
SELECT avg(winner_rank) FROM matches
SELECT max(loser_rank) FROM matches
SELECT min(loser_rank) FROM matches
SELECT count(DISTINCT country_code) FROM players
SELECT COUNT(DISTINCT country_code) FROM players
SELECT count(DISTINCT loser_name) FROM matches
SELECT count(DISTINCT loser_name) FROM matches
SELECT tourney_name FROM matches GROUP BY tourney_name HAVING count(*) > 10;
SELECT tourney_name FROM matches GROUP BY tourney_name HAVING COUNT(*) > 10;
SELECT winner_name FROM matches WHERE year = 2013 INTERSECT SELECT winner_name FROM matches WHERE year = 2016
SELECT first_name, last_name FROM players WHERE player_id IN (SELECT winner_id FROM matches WHERE year = 2013 INTERSECT SELECT winner_id FROM matches WHERE year = 2016)
SELECT count(*) FROM matches WHERE year IN (2013, 2016);
SELECT count(*) FROM matches WHERE year IN (2013, 2016);
SELECT T2.country_code , T2.first_name FROM matches AS T1 JOIN players AS T2 ON T1.winner_id = T2.player_id WHERE T1.tourney_name = "WTA Championships" INTERSECT SELECT T2.country_code , T2.first_name FROM matches AS T1 JOIN players AS T2 ON T1.winner_id = T2.player_id WHERE T1.tourney_name = "Australian Open"
SELECT T1.first_name, T1.country_code FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'WTA Championships' INTERSECT SELECT T1.first_name, T1.country_code FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id WHERE T2.tourney_name = 'Australian Open'
SELECT first_name , country_code FROM players ORDER BY birth_date LIMIT 1
SELECT first_name , country_code FROM players ORDER BY birth_date LIMIT 1
SELECT first_name, last_name FROM players ORDER BY birth_date ASC
SELECT first_name, last_name FROM players ORDER BY birth_date
SELECT first_name, last_name FROM players WHERE hand = 'L' ORDER BY birth_date
SELECT first_name, last_name FROM players WHERE hand = 'L' ORDER BY birth_date
SELECT T1.first_name , T1.country_code FROM players AS T1 JOIN rankings AS T2 ON T1.player_id = T2.player_id GROUP BY T2.player_id ORDER BY sum(T2.tours) DESC LIMIT 1
SELECT first_name, country_code FROM players AS T1 JOIN rankings AS T2 ON T1.player_id = T2.player_id GROUP BY T1.player_id ORDER BY sum(T2.tours) DESC LIMIT 1
SELECT year FROM matches GROUP BY year ORDER BY count(*) DESC LIMIT 1
SELECT year FROM matches GROUP BY year ORDER BY COUNT(*) DESC LIMIT 1
SELECT T1.first_name, T1.last_name, T3.ranking_points FROM players AS T1 JOIN matches AS T2 ON T1.player_id = T2.winner_id JOIN rankings AS T3 ON T1.player_id = T3.player_id GROUP BY T2.winner_id ORDER BY count(*) DESC, T3.ranking_points DESC LIMIT 1
SELECT players.first_name, players.last_name, rankings.ranking_points FROM players JOIN matches ON players.player_id = matches.winner_id JOIN rankings ON players.player_id = rankings.player_id GROUP BY players.player_id ORDER BY COUNT(matches.winner_id) DESC, rankings.ranking_points DESC LIMIT 1
SELECT winner_name FROM matches WHERE winner_rank_points = (SELECT max(winner_rank_points) FROM matches WHERE tourney_name = 'Australian Open')
SELECT players.first_name, players.last_name FROM players JOIN matches ON players.player_id = matches.winner_id WHERE matches.tourney_name = 'Australian Open' ORDER BY matches.winner_rank_points DESC LIMIT 1
SELECT p1.first_name AS loser_first_name, p1.last_name AS loser_last_name, p2.first_name AS winner_first_name, p2.last_name AS winner_last_name FROM matches m JOIN players p1 ON m.loser_id = p1.player_id JOIN players p2 ON m.winner_id = p2.player_id WHERE m.minutes = (SELECT MAX(minutes) FROM matches);
SELECT T1.winner_name, T1.loser_name FROM matches AS T1 ORDER BY T1.minutes DESC LIMIT 1
SELECT players.first_name, avg(rankings.ranking) FROM players JOIN rankings ON players.player_id = rankings.player_id GROUP BY players.player_id, players.first_name;
SELECT players.first_name, AVG(rankings.ranking) FROM players JOIN rankings ON players.player_id = rankings.player_id GROUP BY players.first_name
SELECT sum(ranking_points) , first_name FROM rankings AS T1 JOIN players AS T2 ON T1.player_id = T2.player_id GROUP BY T2.first_name
SELECT sum(rankings.ranking_points) , players.first_name FROM players JOIN rankings ON players.player_id = rankings.player_id GROUP BY players.first_name
SELECT count(*) , country_code FROM players GROUP BY country_code
SELECT country_code , COUNT(*) FROM players GROUP BY country_code
SELECT country_code FROM players GROUP BY country_code ORDER BY count(*) DESC LIMIT 1
SELECT country_code FROM players GROUP BY country_code ORDER BY count(*) DESC LIMIT 1
SELECT country_code FROM players GROUP BY country_code HAVING count(*) > 50
SELECT country_code FROM players GROUP BY country_code HAVING count(*) > 50;
SELECT ranking_date, count(tours) FROM rankings GROUP BY ranking_date;
SELECT ranking_date , sum(tours) FROM rankings GROUP BY ranking_date
SELECT year, COUNT(*) FROM matches GROUP BY year
SELECT year , COUNT(*) FROM matches GROUP BY year
SELECT p.first_name, p.last_name, r.ranking FROM players p JOIN rankings r ON p.player_id = r.player_id JOIN matches m ON p.player_id = m.winner_id ORDER BY p.birth_date DESC LIMIT 3
SELECT players.first_name, players.last_name, rankings.ranking FROM players JOIN rankings ON players.player_id = rankings.player_id JOIN matches ON players.player_id = matches.winner_id ORDER BY players.birth_date DESC LIMIT 3;
SELECT count(DISTINCT winner_id) FROM matches WHERE tourney_name = "WTA Championships" AND winner_hand = "L"
SELECT count(*) FROM matches WHERE winner_hand = 'L' AND tourney_name = 'WTA Championships'
SELECT first_name, country_code, birth_date FROM players WHERE player_id = (SELECT winner_id FROM matches ORDER BY winner_rank_points DESC LIMIT 1)
SELECT first_name, country_code, birth_date FROM players WHERE player_id = (SELECT winner_id FROM matches ORDER BY winner_rank_points DESC LIMIT 1)
SELECT hand , count(*) FROM players GROUP BY hand
SELECT hand , count(*) FROM players GROUP BY hand
SELECT count(*) FROM ship WHERE disposition_of_ship = 'Captured';
SELECT name, tonnage FROM ship ORDER BY name DESC
SELECT name , date , result FROM battle
SELECT max(killed) , min(killed) FROM death
SELECT avg(injured) FROM death
SELECT T3.killed, T3.injured FROM ship AS T1 JOIN death AS T3 ON T1.id = T3.caused_by_ship_id WHERE T1.tonnage = 't'
SELECT name, result FROM battle WHERE bulgarian_commander != 'Boril'
SELECT DISTINCT T1.id, T1.name FROM battle AS T1 JOIN ship AS T2 ON T1.id = T2.lost_in_battle WHERE T2.ship_type = 'Brig'
SELECT T1.id , T1.name FROM battle AS T1 JOIN ship AS T2 ON T1.id = T2.lost_in_battle JOIN death AS T3 ON T2.id = T3.caused_by_ship_id GROUP BY T1.id HAVING SUM(T3.killed) > 10
SELECT T1.id, T1.name FROM ship AS T1 JOIN death AS T2 ON T1.id = T2.caused_by_ship_id GROUP BY T1.id ORDER BY sum(T2.injured) DESC LIMIT 1
SELECT DISTINCT name FROM battle WHERE bulgarian_commander = 'Kaloyan' AND latin_commander = 'Baldwin I'
SELECT count(DISTINCT result) FROM battle
SELECT count(DISTINCT id) FROM battle WHERE id NOT IN (SELECT lost_in_battle FROM ship WHERE tonnage = '225')
SELECT T1.name, T1.date FROM battle AS T1 JOIN ship AS T2 ON T1.id = T2.lost_in_battle WHERE T2.name = 'Lettice' OR T2.name = 'HMS Atalanta'
SELECT b.name, b.result, b.bulgarian_commander FROM battle AS b LEFT JOIN ship AS s ON b.id = s.lost_in_battle WHERE s.location != 'English Channel' OR s.location IS NULL
SELECT note FROM death WHERE note LIKE "%East%"
SELECT line_1 , line_2 FROM Addresses
SELECT line_1 , line_2 FROM Addresses;
SELECT count(*) FROM Courses
SELECT count(*) FROM Courses
SELECT course_description FROM Courses WHERE course_name = "Math"
SELECT course_description FROM Courses WHERE course_name LIKE "%math%"
SELECT zip_postcode FROM Addresses WHERE city = "Port Chelsea"
SELECT zip_postcode FROM Addresses WHERE city = "Port Chelsea"
SELECT T1.department_name, T1.department_id FROM Departments AS T1 JOIN Degree_Programs AS T2 ON T1.department_id = T2.department_id GROUP BY T1.department_id ORDER BY count(*) DESC LIMIT 1
SELECT T1.department_name, T1.department_id FROM Departments AS T1 JOIN Degree_Programs AS T2 ON T1.department_id = T2.department_id GROUP BY T1.department_id ORDER BY count(*) DESC LIMIT 1
SELECT count(DISTINCT department_id) FROM Degree_Programs
SELECT count(DISTINCT department_id) FROM Degree_Programs
SELECT count(DISTINCT degree_summary_name) FROM Degree_Programs
SELECT count(DISTINCT degree_summary_name) FROM Degree_Programs
SELECT count(*) FROM Degree_Programs WHERE department_id = (SELECT department_id FROM Departments WHERE department_name = 'engineering')
SELECT count(*) FROM Degree_Programs WHERE department_id = (SELECT department_id FROM Departments WHERE department_name = 'Engineering')
SELECT section_name, section_description FROM Sections
SELECT section_name, section_description FROM Sections
SELECT T1.course_id, T1.course_name FROM Courses AS T1 JOIN Sections AS T2 ON T1.course_id = T2.course_id GROUP BY T1.course_id HAVING count(T2.section_id) <= 2;
SELECT T1.course_id, T1.course_name FROM Courses AS T1 LEFT JOIN Sections AS T2 ON T1.course_id = T2.course_id GROUP BY T1.course_id HAVING count(T2.section_id) < 2;
SELECT section_name FROM Sections ORDER BY section_name DESC
SELECT section_name FROM Sections ORDER BY section_name DESC
SELECT T1.semester_id, T1.semester_name FROM Semesters AS T1 JOIN Student_Enrolment AS T2 ON T1.semester_id = T2.semester_id GROUP BY T1.semester_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT T1.semester_id, T1.semester_name FROM Semesters AS T1 JOIN Student_Enrolment AS T2 ON T1.semester_id = T2.semester_id GROUP BY T1.semester_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT department_description FROM Departments WHERE department_name LIKE "%computer%"
SELECT department_description FROM Departments WHERE department_name LIKE "%computer%"
SELECT T1.first_name, T1.middle_name, T1.last_name, T1.student_id FROM Students AS T1 JOIN Student_Enrolment AS T2 ON T1.student_id = T2.student_id GROUP BY T2.semester_id, T1.student_id HAVING COUNT(T2.degree_program_id) = 2
SELECT T1.first_name, T1.middle_name, T1.last_name, T1.student_id FROM Students AS T1 JOIN Student_Enrolment AS T2 ON T1.student_id = T2.student_id GROUP BY T1.student_id, T2.semester_id HAVING COUNT(DISTINCT T2.degree_program_id) = 2
SELECT T1.first_name, T1.middle_name, T1.last_name FROM Students AS T1 JOIN Student_Enrolment AS T2 ON T1.student_id = T2.student_id JOIN Degree_Programs AS T3 ON T2.degree_program_id = T3.degree_program_id WHERE T3.degree_summary_name LIKE "%Bachelor%"
SELECT first_name, middle_name, last_name FROM Students AS S JOIN Student_Enrolment AS SE ON S.student_id = SE.student_id JOIN Degree_Programs AS DP ON SE.degree_program_id = DP.degree_program_id WHERE DP.degree_summary_name LIKE '%Bachelors%'
SELECT T1.degree_summary_name FROM Degree_Programs AS T1 JOIN Student_Enrolment AS T2 ON T1.degree_program_id = T2.degree_program_id GROUP BY T1.degree_summary_name ORDER BY COUNT(*) DESC LIMIT 1
SELECT T1.degree_summary_name FROM Degree_Programs AS T1 JOIN Student_Enrolment AS T2 ON T1.degree_program_id = T2.degree_program_id GROUP BY T1.degree_summary_name ORDER BY COUNT(*) DESC LIMIT 1
SELECT T1.degree_program_id, T1.degree_summary_name FROM Degree_Programs AS T1 JOIN Student_Enrolment AS T2 ON T1.degree_program_id = T2.degree_program_id GROUP BY T1.degree_program_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT T1.degree_program_id, T1.degree_summary_name FROM Degree_Programs AS T1 JOIN Student_Enrolment AS T2 ON T1.degree_program_id = T2.degree_program_id GROUP BY T1.degree_program_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT T1.student_id, T1.first_name, T1.middle_name, T1.last_name, COUNT(*) AS number_of_enrollments FROM Students AS T1 JOIN Student_Enrolment AS T2 ON T1.student_id = T2.student_id GROUP BY T1.student_id ORDER BY number_of_enrollments DESC LIMIT 1
SELECT T1.first_name, T1.middle_name, T1.last_name, T1.student_id, COUNT(*) AS number_of_enrollments FROM Students AS T1 JOIN Student_Enrolment AS T2 ON T1.student_id = T2.student_id GROUP BY T1.student_id ORDER BY number_of_enrollments DESC LIMIT 1
SELECT semester_name FROM Semesters WHERE semester_id NOT IN (SELECT semester_id FROM Student_Enrolment)
SELECT T1.semester_name FROM Semesters AS T1 LEFT JOIN Student_Enrolment AS T2 ON T1.semester_id = T2.semester_id WHERE T2.student_id IS NULL
SELECT course_name FROM Courses WHERE course_id IN (SELECT course_id FROM Student_Enrolment_Courses)
SELECT T1.course_name FROM Courses AS T1 JOIN Student_Enrolment_Courses AS T2 ON T1.course_id = T2.course_id GROUP BY T1.course_name
SELECT T1.course_name FROM Courses AS T1 JOIN Student_Enrolment_Courses AS T2 ON T1.course_id = T2.course_id GROUP BY T1.course_name ORDER BY COUNT(*) DESC LIMIT 1
SELECT T1.course_name FROM Courses AS T1 JOIN Student_Enrolment_Courses AS T2 ON T1.course_id = T2.course_id GROUP BY T1.course_name ORDER BY COUNT(*) DESC LIMIT 1
SELECT T1.last_name FROM Students AS T1 JOIN Addresses AS T2 ON T1.current_address_id = T2.address_id LEFT JOIN Student_Enrolment AS T3 ON T1.student_id = T3.student_id WHERE T2.state_province_county = 'North Carolina' AND T3.degree_program_id IS NULL
SELECT T1.last_name FROM Students AS T1 JOIN Addresses AS T2 ON T1.current_address_id = T2.address_id WHERE T2.state_province_county = "North Carolina" AND T1.student_id NOT IN (SELECT student_id FROM Student_Enrolment)
SELECT T1.transcript_date , T1.transcript_id FROM Transcripts AS T1 JOIN Transcript_Contents AS T2 ON T1.transcript_id = T2.transcript_id GROUP BY T1.transcript_id HAVING count(*) >= 2
SELECT T1.transcript_date , T1.transcript_id FROM Transcripts AS T1 JOIN Transcript_Contents AS T2 ON T1.transcript_id = T2.transcript_id GROUP BY T1.transcript_id HAVING count(*) >= 2
SELECT cell_mobile_number FROM Students WHERE first_name = "Timmothy" AND last_name = "Ward"
SELECT cell_mobile_number FROM Students WHERE first_name = "Timmothy" AND last_name = "Ward"
SELECT first_name, middle_name, last_name FROM Students ORDER BY date_first_registered LIMIT 1
SELECT first_name, middle_name, last_name FROM Students ORDER BY date_first_registered LIMIT 1
SELECT first_name, middle_name, last_name FROM Students WHERE date_left IS NOT NULL ORDER BY date_left ASC LIMIT 1
SELECT first_name, middle_name, last_name FROM Students WHERE date_left IS NOT NULL ORDER BY date_left ASC LIMIT 1
SELECT first_name FROM Students WHERE current_address_id != permanent_address_id
SELECT first_name FROM Students WHERE current_address_id != permanent_address_id
SELECT T1.current_address_id, T2.line_1, T2.line_2, T2.line_3 FROM Students AS T1 JOIN Addresses AS T2 ON T1.current_address_id = T2.address_id GROUP BY T1.current_address_id ORDER BY COUNT(*) DESC LIMIT 1;
SELECT T1.address_id, T1.line_1, T1.line_2 FROM Addresses AS T1 JOIN Students AS T2 ON T1.address_id = T2.current_address_id OR T1.address_id = T2.permanent_address_id GROUP BY T1.address_id ORDER BY count(*) DESC LIMIT 1
SELECT avg(transcript_date) FROM Transcripts
SELECT avg(transcript_date) FROM Transcripts
SELECT transcript_date, other_details FROM Transcripts ORDER BY transcript_date ASC LIMIT 1
SELECT min(transcript_date), other_details FROM Transcripts ORDER BY transcript_date ASC LIMIT 1
SELECT count(*) FROM Transcripts;
SELECT count(*) FROM Transcripts
SELECT max(transcript_date) FROM Transcripts
SELECT transcript_date FROM Transcripts ORDER BY transcript_date DESC LIMIT 1
SELECT count(*) , T1.student_course_id FROM Student_Enrolment_Courses AS T1 JOIN Transcript_Contents AS T2 ON T1.student_course_id = T2.student_course_id GROUP BY T1.student_course_id ORDER BY count(*) DESC LIMIT 1
SELECT T1.course_id , T1.student_enrolment_id , count(*) FROM Student_Enrolment_Courses AS T1 JOIN Transcript_Contents AS T2 ON T1.student_course_id = T2.student_course_id GROUP BY T1.course_id ORDER BY count(*) DESC LIMIT 1
SELECT T1.transcript_date , T1.transcript_id FROM Transcripts AS T1 JOIN Transcript_Contents AS T2 ON T1.transcript_id = T2.transcript_id GROUP BY T1.transcript_id ORDER BY count(*) ASC LIMIT 1
SELECT transcript_date, transcript_id FROM Transcript_Contents JOIN Transcripts ON Transcript_Contents.transcript_id = Transcripts.transcript_id GROUP BY Transcript_Contents.transcript_id ORDER BY COUNT(*) ASC LIMIT 1
SELECT semester_name FROM Semesters WHERE semester_id IN (SELECT semester_id FROM Student_Enrolment WHERE degree_program_id IN (SELECT degree_program_id FROM Degree_Programs WHERE degree_summary_name = 'Master') INTERSECT SELECT semester_id FROM Student_Enrolment WHERE degree_program_id IN (SELECT degree_program_id FROM Degree_Programs WHERE degree_summary_name = 'Bachelor'))
SELECT semester_id FROM Student_Enrolment WHERE degree_program_id IN (SELECT degree_program_id FROM Degree_Programs WHERE degree_summary_name IN ('Masters', 'Bachelors')) GROUP BY semester_id HAVING COUNT(DISTINCT degree_program_id) = 2
SELECT count(DISTINCT current_address_id) FROM Students
SELECT DISTINCT T1.line_1, T1.line_2, T1.line_3, T1.city, T1.zip_postcode, T1.state_province_county, T1.country FROM Addresses AS T1 JOIN Students AS T2 ON T1.address_id = T2.current_address_id OR T1.address_id = T2.permanent_address_id
SELECT * FROM Students ORDER BY first_name DESC, middle_name DESC, last_name DESC
SELECT other_student_details FROM Students ORDER BY last_name DESC, first_name DESC
SELECT section_description FROM Sections WHERE section_name = "h"
SELECT section_description FROM Sections WHERE section_name = "h";
SELECT first_name FROM Students WHERE permanent_address_id IN (SELECT address_id FROM Addresses WHERE country = 'Haiti') OR cell_mobile_number = '09700166582'
SELECT first_name FROM Students WHERE permanent_address_id IN (SELECT address_id FROM Addresses WHERE country = "Haiti") OR cell_mobile_number = "09700166582"
SELECT Title FROM Cartoon ORDER BY Title ASC
SELECT Title FROM Cartoon ORDER BY Title ASC
SELECT Title FROM Cartoon WHERE Directed_by = "Ben Jones"
SELECT Title FROM Cartoon WHERE Directed_by = 'Ben Jones'
SELECT count(*) FROM Cartoon WHERE Written_by = "Joseph Kuhr"
SELECT count(*) FROM Cartoon WHERE Written_by = 'Joseph Kuhr'
SELECT Title, Directed_by FROM Cartoon ORDER BY Original_air_date
SELECT Title, Directed_by FROM Cartoon ORDER BY Original_air_date
SELECT Title FROM Cartoon WHERE Directed_by = "Ben Jones" OR Directed_by = "Brandon Vietti"
SELECT Title FROM Cartoon WHERE Directed_by = 'Ben Jones' OR Directed_by = 'Brandon Vietti'
SELECT Country , count(*) FROM TV_Channel GROUP BY Country ORDER BY count(*) DESC LIMIT 1;
SELECT Country , COUNT(*) FROM TV_Channel GROUP BY Country ORDER BY COUNT(*) DESC LIMIT 1
SELECT count(DISTINCT series_name) , count(DISTINCT Content) FROM TV_Channel
SELECT count(DISTINCT series_name) , count(DISTINCT Content) FROM TV_Channel
SELECT "Content" FROM "TV_Channel" WHERE "series_name" = "Sky Radio"
SELECT Content FROM TV_Channel WHERE series_name = "Sky Radio";
SELECT Package_Option FROM TV_Channel WHERE series_name = "Sky Radio"
SELECT Package_Option FROM TV_Channel WHERE series_name = "Sky Radio"
SELECT count(*) FROM TV_Channel WHERE Language = 'English';
SELECT count(*) FROM TV_Channel WHERE Language = "English"
SELECT Language , count(*) FROM TV_Channel GROUP BY Language ORDER BY count(*) ASC LIMIT 1;
SELECT Language, COUNT(*) as Channel_Count FROM TV_Channel GROUP BY Language ORDER BY Channel_Count ASC LIMIT 1;
SELECT Language , COUNT(*) FROM TV_Channel GROUP BY Language
SELECT Language , COUNT(*) FROM TV_Channel GROUP BY Language
SELECT T1.series_name FROM TV_Channel AS T1 JOIN Cartoon AS T2 ON T1.id = T2.Channel WHERE T2.Title = "The Rise of the Blue Beetle!"
SELECT T2.series_name FROM Cartoon AS T1 JOIN TV_Channel AS T2 ON T1.Channel = T2.id WHERE T1.Title = "The Rise of the Blue Beetle"
SELECT T1.Title FROM Cartoon AS T1 JOIN TV_Channel AS T2 ON T1.Channel = T2.id WHERE T2.series_name = "Sky Radio"
SELECT T1.Title FROM Cartoon AS T1 JOIN TV_Channel AS T2 ON T1.Channel = T2.id WHERE T2.series_name = "Sky Radio"
SELECT Episode FROM TV_series ORDER BY Rating
SELECT Episode FROM TV_series ORDER BY Rating
SELECT Episode, Rating FROM TV_series ORDER BY Rating DESC LIMIT 3
SELECT Episode, Rating FROM TV_series ORDER BY Rating DESC LIMIT 3
SELECT min(Share) , max(Share) FROM TV_series
SELECT max(Share) , min(Share) FROM TV_series
SELECT "Air_Date" FROM "TV_series" WHERE "Episode" = "A Love of a Lifetime"
SELECT Air_Date FROM TV_series WHERE Episode = "A Love of a Lifetime"
SELECT "Weekly_Rank" FROM "TV_series" WHERE "Episode" = "A Love of a Lifetime"
SELECT Weekly_Rank FROM TV_series WHERE Episode = "A Love of a Lifetime"
SELECT T1.series_name FROM TV_Channel AS T1 JOIN TV_series AS T2 ON T1.id = T2.Channel WHERE T2.Episode = "A Love of a Lifetime"
SELECT series_name FROM TV_Channel WHERE id IN (SELECT Channel FROM TV_series WHERE Episode = 'A Love of a Lifetime')
SELECT T2.Episode FROM TV_Channel AS T1 JOIN TV_series AS T2 ON T1.id = T2.Channel WHERE T1.series_name = "Sky Radio"
SELECT T2.Episode FROM TV_Channel AS T1 JOIN TV_series AS T2 ON T1.id = T2.Channel WHERE T1.series_name = "Sky Radio"
SELECT Directed_by , count(*) FROM Cartoon GROUP BY Directed_by
SELECT Directed_by , count(*) FROM Cartoon GROUP BY Directed_by
SELECT Production_code , Channel FROM Cartoon ORDER BY Original_air_date DESC LIMIT 1
SELECT Production_code , Channel FROM Cartoon ORDER BY Original_air_date DESC LIMIT 1
SELECT T1.Package_Option , T1.series_name FROM TV_Channel AS T1 WHERE T1.Hight_definition_TV = "Yes";
SELECT T1.Package_Option , T2.series_name FROM TV_Channel AS T1 JOIN TV_series AS T2 ON T1.id = T2.Channel WHERE T1.Hight_definition_TV = 'Yes'
SELECT DISTINCT T1.Country FROM TV_Channel AS T1 JOIN Cartoon AS T2 ON T1.id = T2.Channel WHERE T2.Written_by = "Todd Casey";
SELECT T1.Country FROM TV_Channel AS T1 JOIN Cartoon AS T2 ON T1.id = T2.Channel WHERE T2.Written_by = "Todd Casey"
SELECT Country FROM TV_Channel WHERE id NOT IN (SELECT Channel FROM Cartoon WHERE Written_by = 'Todd Casey')
SELECT Country FROM TV_Channel EXCEPT SELECT T1.Country FROM TV_Channel AS T1 JOIN Cartoon AS T2 ON T1.id = T2.Channel WHERE T2.Written_by = 'Todd Casey'
SELECT T1.series_name, T1.Country FROM TV_Channel AS T1 JOIN Cartoon AS T2 ON T1.id = T2.Channel WHERE T2.Directed_by IN ("Ben Jones", "Michael Chang")
SELECT T1.series_name, T1.Country FROM TV_Channel AS T1 JOIN Cartoon AS T2 ON T1.id = T2.Channel WHERE T2.Directed_by = "Ben Jones" INTERSECT SELECT T1.series_name, T1.Country FROM TV_Channel AS T1 JOIN Cartoon AS T2 ON T1.id = T2.Channel WHERE T2.Directed_by = "Michael Chang"
SELECT Pixel_aspect_ratio_PAR, Country FROM TV_Channel WHERE Language != "English"
SELECT Pixel_aspect_ratio_PAR, Country FROM TV_Channel WHERE Language != 'English'
SELECT Country FROM TV_Channel GROUP BY Country HAVING COUNT(id) > 2
SELECT Channel FROM TV_Channel GROUP BY Channel HAVING count(*) > 2;
SELECT id FROM TV_Channel WHERE id NOT IN (SELECT Channel FROM Cartoon WHERE Directed_by = 'Ben Jones')
SELECT id FROM TV_Channel WHERE id NOT IN (SELECT Channel FROM Cartoon WHERE Directed_by = 'Ben Jones')
SELECT "Package_Option" FROM "TV_Channel" WHERE "id" NOT IN (SELECT "Channel" FROM "Cartoon" WHERE "Directed_by" = 'Ben Jones')
SELECT Package_Option FROM TV_Channel WHERE id NOT IN (SELECT Channel FROM Cartoon WHERE Directed_by = 'Ben Jones')
SELECT count(*) FROM poker_player
SELECT count(*) FROM poker_player
SELECT Earnings FROM poker_player ORDER BY Earnings DESC
SELECT Earnings FROM poker_player ORDER BY Earnings DESC
SELECT Final_Table_Made , Best_Finish FROM poker_player
SELECT Final_Table_Made , Best_Finish FROM poker_player
SELECT avg(Earnings) FROM poker_player
SELECT avg(Earnings) FROM poker_player
SELECT money_rank FROM poker_player ORDER BY earnings DESC LIMIT 1
SELECT Money_Rank FROM poker_player ORDER BY Earnings DESC LIMIT 1
SELECT max(Final_Table_Made) FROM poker_player WHERE Earnings < 200000
SELECT max(Final_Table_Made) FROM poker_player WHERE Earnings < 200000
SELECT T2.Name FROM poker_player AS T1 JOIN people AS T2 ON T1.People_ID = T2.People_ID
SELECT T2.Name FROM poker_player AS T1 JOIN people AS T2 ON T1.People_ID = T2.People_ID
SELECT T2.Name FROM poker_player AS T1 JOIN people AS T2 ON T1.People_ID = T2.People_ID WHERE T1.Earnings > 300000
SELECT T2.Name FROM poker_player AS T1 JOIN people AS T2 ON T1.People_ID = T2.People_ID WHERE T1.Earnings > 300000
SELECT T2.Name FROM poker_player AS T1 JOIN people AS T2 ON T1.People_ID = T2.People_ID ORDER BY T1.Final_Table_Made ASC
SELECT T2.Name FROM poker_player AS T1 JOIN people AS T2 ON T1.People_ID = T2.People_ID ORDER BY T1.Final_Table_Made ASC
SELECT P2.Birth_Date FROM poker_player AS P1 JOIN people AS P2 ON P1.People_ID = P2.People_ID ORDER BY P1.Earnings ASC LIMIT 1
SELECT T2.Birth_Date FROM poker_player AS T1 JOIN people AS T2 ON T1.People_ID = T2.People_ID ORDER BY T1.Earnings ASC LIMIT 1
SELECT T1.Money_Rank FROM poker_player AS T1 JOIN people AS T2 ON T1.People_ID = T2.People_ID ORDER BY T2.Height DESC LIMIT 1
SELECT T1.Money_Rank FROM poker_player AS T1 JOIN people AS T2 ON T1.People_ID = T2.People_ID ORDER BY T2.Height DESC LIMIT 1
SELECT avg(T1.Earnings) FROM poker_player AS T1 JOIN people AS T2 ON T1.People_ID = T2.People_ID WHERE T2.Height > 200
SELECT avg(Earnings) FROM poker_player AS T1 JOIN people AS T2 ON T1.People_ID = T2.People_ID WHERE T2.Height > 200
SELECT T2.Name FROM poker_player AS T1 JOIN people AS T2 ON T1.People_ID = T2.People_ID ORDER BY T1.Earnings DESC
SELECT T2.Name FROM poker_player AS T1 JOIN people AS T2 ON T1.People_ID = T2.People_ID ORDER BY T1.Earnings DESC
SELECT Nationality , count(*) FROM people GROUP BY Nationality
SELECT Nationality , count(*) FROM people GROUP BY Nationality
SELECT Nationality FROM people GROUP BY Nationality ORDER BY COUNT(*) DESC LIMIT 1
SELECT Nationality FROM people GROUP BY Nationality ORDER BY COUNT(*) DESC LIMIT 1
SELECT Nationality FROM people GROUP BY Nationality HAVING COUNT(*) >= 2
SELECT Nationality FROM people GROUP BY Nationality HAVING COUNT(*) >= 2
SELECT Name, Birth_Date FROM people ORDER BY Name ASC
SELECT Name, Birth_Date FROM people ORDER BY Name
SELECT Name FROM people WHERE Nationality != "Russia"
SELECT Name FROM people WHERE Nationality != 'Russia'
SELECT Name FROM people WHERE People_ID NOT IN (SELECT People_ID FROM poker_player)
SELECT Name FROM people WHERE People_ID NOT IN (SELECT People_ID FROM poker_player)
SELECT count(DISTINCT Nationality) FROM people
SELECT count(DISTINCT Nationality) FROM people
SELECT count(DISTINCT state) FROM AREA_CODE_STATE
SELECT contestant_number, contestant_name FROM CONTESTANTS ORDER BY contestant_name DESC
SELECT vote_id , phone_number , state FROM VOTES
SELECT max(area_code) , min(area_code) FROM AREA_CODE_STATE
SELECT max(created) FROM VOTES WHERE state = 'CA'
SELECT contestant_name FROM CONTESTANTS WHERE contestant_name != 'Jessie Alloway'
SELECT DISTINCT state, created FROM VOTES
SELECT T1.contestant_number, T1.contestant_name FROM CONTESTANTS AS T1 JOIN VOTES AS T2 ON T1.contestant_number = T2.contestant_number GROUP BY T1.contestant_number HAVING COUNT(*) >= 2
SELECT T1.contestant_number, T1.contestant_name FROM CONTESTANTS AS T1 JOIN VOTES AS T2 ON T1.contestant_number = T2.contestant_number GROUP BY T1.contestant_number ORDER BY count(*) ASC LIMIT 1
SELECT count(*) FROM VOTES WHERE state IN ('NY', 'CA')
SELECT count(*) FROM CONTESTANTS WHERE contestant_number NOT IN (SELECT contestant_number FROM VOTES)
SELECT area_code FROM AREA_CODE_STATE JOIN VOTES ON AREA_CODE_STATE.state = VOTES.state GROUP BY area_code ORDER BY COUNT(*) DESC LIMIT 1;
SELECT T3.created, T3.state, T3.phone_number FROM CONTESTANTS AS T1 JOIN VOTES AS T3 ON T1.contestant_number = T3.contestant_number WHERE T1.contestant_name = 'Tabatha Gehling'
SELECT T1.area_code FROM AREA_CODE_STATE AS T1 JOIN VOTES AS T2 ON T1.state = T2.state JOIN CONTESTANTS AS T3 ON T2.contestant_number = T3.contestant_number WHERE T3.contestant_name = 'Tabatha Gehling' INTERSECT SELECT T1.area_code FROM AREA_CODE_STATE AS T1 JOIN VOTES AS T2 ON T1.state = T2.state JOIN CONTESTANTS AS T3 ON T2.contestant_number = T3.contestant_number WHERE T3.contestant_name = 'Kelly Clauss'
SELECT contestant_name FROM CONTESTANTS WHERE contestant_name LIKE "%Al%"
SELECT Name FROM country WHERE IndepYear > 1950
SELECT Name FROM country WHERE IndepYear > 1950
SELECT count(*) FROM country WHERE GovernmentForm LIKE "%Republic%"
SELECT count(*) FROM country WHERE GovernmentForm LIKE "%Republic%"
SELECT sum(SurfaceArea) FROM country WHERE Region = 'Caribbean'
SELECT sum(SurfaceArea) FROM country WHERE Region = 'Caribbean'
SELECT Continent FROM country WHERE Name = "Anguilla";
SELECT T1.Continent FROM country AS T1 JOIN city AS T2 ON T1.Code = T2.CountryCode WHERE T2.Name = "Anguilla";
SELECT Region FROM city JOIN country ON city.CountryCode = country.Code WHERE city.Name = "Kabul"
SELECT District FROM city WHERE Name = "Kabul";
SELECT Language FROM countrylanguage WHERE CountryCode = (SELECT Code FROM country WHERE Name = 'Aruba') ORDER BY Percentage DESC LIMIT 1;
SELECT Language FROM countrylanguage WHERE CountryCode = (SELECT Code FROM country WHERE Name = 'Aruba') AND IsOfficial = 'T'
SELECT Population , LifeExpectancy FROM country WHERE Name = 'Brazil'
SELECT Population, LifeExpectancy FROM country WHERE Name = 'Brazil'
SELECT Region, Population FROM country WHERE Name = "Angola"
SELECT Region, Population FROM country WHERE Name = "Angola";
SELECT avg(LifeExpectancy) FROM country WHERE Region = 'Central Africa'
SELECT avg(LifeExpectancy) FROM country WHERE Region = 'Central Africa'
SELECT `Name` FROM `country` WHERE `Continent` = 'Asia' ORDER BY `LifeExpectancy` ASC LIMIT 1;
SELECT Name FROM country WHERE Continent = 'Asia' ORDER BY LifeExpectancy ASC LIMIT 1
SELECT sum(Population) , max(GNP) FROM country WHERE Continent = 'Asia'
SELECT sum(Population) , max(GNP) FROM country WHERE Continent = 'Asia'
SELECT avg(LifeExpectancy) FROM country WHERE Continent = 'Africa' AND GovernmentForm LIKE '%Republic%'
SELECT avg(LifeExpectancy) FROM country WHERE Continent = 'Africa' AND GovernmentForm LIKE '%Republic%'
SELECT sum(SurfaceArea) FROM country WHERE Continent = 'Asia' OR Continent = 'Europe'
SELECT sum(SurfaceArea) FROM country WHERE Continent = 'Asia' OR Continent = 'Europe'
SELECT SUM(Population) FROM city WHERE District = "Gelderland"
SELECT sum(Population) FROM city WHERE District = 'Gelderland'
SELECT avg(GNP) , sum(Population) FROM country WHERE GovernmentForm = "US territory"
SELECT avg(GNP), sum(Population) FROM country WHERE GovernmentForm = "US Territory"
SELECT count(DISTINCT Language) FROM countrylanguage
SELECT count(DISTINCT Language) FROM countrylanguage
SELECT count(DISTINCT GovernmentForm) FROM country WHERE Continent = 'Africa'
SELECT count(DISTINCT GovernmentForm) FROM country WHERE Continent = 'Africa'
SELECT count(DISTINCT Language) FROM countrylanguage WHERE CountryCode = (SELECT Code FROM country WHERE Name = 'Aruba')
SELECT count(*) FROM countrylanguage WHERE CountryCode = (SELECT Code FROM country WHERE Name = 'Aruba')
SELECT COUNT(Language) FROM countrylanguage WHERE CountryCode = (SELECT Code FROM country WHERE Name = "Afghanistan") AND IsOfficial = 'T'
SELECT COUNT(Language) FROM countrylanguage WHERE CountryCode = (SELECT Code FROM country WHERE Name = "Afghanistan") AND IsOfficial = 'T'
SELECT T2.Name FROM countrylanguage AS T1 JOIN country AS T2 ON T1.CountryCode = T2.Code GROUP BY T1.CountryCode ORDER BY COUNT(*) DESC LIMIT 1;
SELECT T2.Name FROM countrylanguage AS T1 JOIN country AS T2 ON T1.CountryCode = T2.Code GROUP BY T2.Name ORDER BY COUNT(*) DESC LIMIT 1
SELECT T2.Continent FROM countrylanguage AS T1 JOIN country AS T2 ON T1.CountryCode = T2.Code GROUP BY T2.Continent ORDER BY COUNT(DISTINCT T1.Language) DESC LIMIT 1
SELECT Continent FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode GROUP BY Continent ORDER BY COUNT(DISTINCT Language) DESC LIMIT 1
SELECT count(*) FROM country AS C WHERE EXISTS (SELECT 1 FROM countrylanguage AS L1 WHERE L1.CountryCode = C.Code AND L1.Language = 'English') AND EXISTS (SELECT 1 FROM countrylanguage AS L2 WHERE L2.CountryCode = C.Code AND L2.Language = 'Dutch')
SELECT count(*) FROM countrylanguage WHERE Language IN ('English', 'Dutch')
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = 'English' INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = 'French'
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = 'English' INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = 'French'
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = 'English' AND T2.IsOfficial = 'T' INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = 'French' AND T2.IsOfficial = 'T'
SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = 'English' AND T2.IsOfficial = 'T' INTERSECT SELECT T1.Name FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = 'French' AND T2.IsOfficial = 'T'
SELECT count(DISTINCT T1.Continent) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = 'Chinese'
SELECT count(DISTINCT Continent) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = 'Chinese'
SELECT Region FROM country WHERE Code IN (SELECT CountryCode FROM countrylanguage WHERE Language IN ('English', 'Dutch'))
SELECT Region FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language IN ('Dutch', 'English') GROUP BY T1.Region;
SELECT T2.Name FROM countrylanguage AS T1 JOIN country AS T2 ON T1.CountryCode = T2.Code WHERE T1.Language IN ('English', 'Dutch') AND T1.IsOfficial = 'T'
SELECT `Name` FROM `country` WHERE `Code` IN (SELECT `CountryCode` FROM `countrylanguage` WHERE `Language` IN ('English', 'Dutch') AND `IsOfficial` = 'T')
SELECT Language FROM countrylanguage AS cl JOIN country AS c ON cl.CountryCode = c.Code WHERE c.Continent = 'Asia' GROUP BY cl.Language ORDER BY count(*) DESC LIMIT 1
SELECT Language FROM countrylanguage AS t1 JOIN country AS t2 ON t1.CountryCode = t2.Code WHERE t2.Continent = 'Asia' GROUP BY t1.Language ORDER BY count(*) DESC LIMIT 1
SELECT Language FROM countrylanguage WHERE CountryCode IN (SELECT Code FROM country WHERE GovernmentForm = 'Republic') GROUP BY Language HAVING COUNT(*) = 1
SELECT Language FROM countrylanguage WHERE CountryCode IN (SELECT Code FROM country WHERE GovernmentForm = 'Republic') GROUP BY Language HAVING COUNT(*) = 1
SELECT T1.Name FROM city AS T1 JOIN countrylanguage AS T2 ON T1.CountryCode = T2.CountryCode WHERE T2.Language = 'English' ORDER BY T1.Population DESC LIMIT 1;
SELECT T1.Name FROM city AS T1 JOIN countrylanguage AS T2 ON T1.CountryCode = T2.CountryCode WHERE T2.Language = 'English' ORDER BY T1.Population DESC LIMIT 1;
SELECT Name, Population, LifeExpectancy FROM country WHERE Continent = 'Asia' ORDER BY SurfaceArea DESC LIMIT 1;
SELECT Name, Population, LifeExpectancy FROM country WHERE Continent = 'Asia' ORDER BY SurfaceArea DESC LIMIT 1;
SELECT avg(LifeExpectancy) FROM country WHERE Code NOT IN (SELECT CountryCode FROM countrylanguage WHERE Language = 'English' AND IsOfficial = 'T')
SELECT avg(LifeExpectancy) FROM country WHERE Code NOT IN (SELECT CountryCode FROM countrylanguage WHERE Language = 'English' AND IsOfficial = 'T')
SELECT SUM(Population) FROM country WHERE Code NOT IN (SELECT CountryCode FROM countrylanguage WHERE Language = 'English')
SELECT sum(Population) FROM country WHERE Code NOT IN (SELECT CountryCode FROM countrylanguage WHERE Language = 'English')
SELECT Language FROM countrylanguage WHERE IsOfficial = 'T' AND CountryCode = (SELECT Code FROM country WHERE HeadOfState = 'Beatrix')
SELECT Language FROM countrylanguage WHERE IsOfficial = 'T' AND CountryCode = (SELECT Code FROM country WHERE HeadOfState = 'Beatrix')
SELECT count(DISTINCT Language) FROM countrylanguage WHERE CountryCode IN (SELECT Code FROM country WHERE IndepYear < 1930 AND IsOfficial = 'T')
SELECT count(DISTINCT Language) FROM countrylanguage AS T1 JOIN country AS T2 ON T1.CountryCode = T2.Code WHERE T2.IndepYear < 1930 AND T1.IsOfficial = 'T'
SELECT `Name` FROM `country` WHERE `SurfaceArea` > (SELECT max(`SurfaceArea`) FROM `country` WHERE `Continent` = 'Europe')
SELECT Name FROM country WHERE SurfaceArea > (SELECT max(SurfaceArea) FROM country WHERE Continent = 'Europe')
SELECT c1.Name FROM country AS c1 WHERE c1.Continent = 'Africa' AND c1.Population < ANY (SELECT c2.Population FROM country AS c2 WHERE c2.Continent = 'Asia')
SELECT T1.Name FROM country AS T1 WHERE T1.Continent = 'Africa' AND T1.Population < ANY (SELECT T2.Population FROM country AS T2 WHERE T2.Continent = 'Asia')
SELECT Name FROM country WHERE Continent = 'Asia' AND Population > (SELECT max(Population) FROM country WHERE Continent = 'Africa')
SELECT Name FROM country WHERE Continent = 'Asia' AND Population > (SELECT max(Population) FROM country WHERE Continent = 'Africa')
SELECT `Code` FROM `country` WHERE `Code` NOT IN (SELECT `CountryCode` FROM `countrylanguage` WHERE `Language` = 'English')
SELECT CountryCode FROM countrylanguage WHERE Language != 'English'
SELECT CountryCode FROM countrylanguage WHERE Language != 'English'
SELECT CountryCode FROM countrylanguage WHERE Language != 'English'
SELECT Code FROM country WHERE Code NOT IN (SELECT CountryCode FROM countrylanguage WHERE Language = 'English') AND GovernmentForm != 'Republic'
SELECT Code FROM country WHERE Code NOT IN (SELECT CountryCode FROM countrylanguage WHERE Language = 'English') AND GovernmentForm NOT LIKE '%Republic%'
SELECT city.Name FROM city JOIN country ON city.CountryCode = country.Code JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Continent = 'Europe' AND (countrylanguage.Language != 'English' OR countrylanguage.IsOfficial = 'F')
SELECT city.Name FROM city JOIN country ON city.CountryCode = country.Code JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Continent = 'Europe' AND (countrylanguage.Language != 'English' OR countrylanguage.IsOfficial = 'F')
SELECT DISTINCT city.Name FROM city JOIN country ON city.CountryCode = country.Code JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Continent = 'Asia' AND countrylanguage.Language = 'Chinese' AND countrylanguage.IsOfficial = 'T'
SELECT DISTINCT city.Name FROM city JOIN country ON city.CountryCode = country.Code JOIN countrylanguage ON country.Code = countrylanguage.CountryCode WHERE country.Continent = 'Asia' AND countrylanguage.Language = 'Chinese' AND countrylanguage.IsOfficial = 'T'
SELECT Name, IndepYear, SurfaceArea FROM country ORDER BY Population LIMIT 1
SELECT Name, IndepYear, SurfaceArea FROM country ORDER BY Population LIMIT 1
SELECT Population, Name, HeadOfState FROM country ORDER BY SurfaceArea DESC LIMIT 1
SELECT Name , Population, HeadOfState FROM country ORDER BY SurfaceArea DESC LIMIT 1
SELECT T1.Name, COUNT(T2.Language) AS NumberOfLanguages FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode GROUP BY T1.Name HAVING COUNT(T2.Language) >= 3
SELECT Country.Name, COUNT(CountryLanguage.Language) FROM Country JOIN CountryLanguage ON Country.Code = CountryLanguage.CountryCode GROUP BY Country.Name HAVING COUNT(CountryLanguage.Language) > 2;
SELECT District, count(*) FROM city WHERE Population > (SELECT avg(Population) FROM city) GROUP BY District
SELECT count(*) , District FROM city WHERE Population > (SELECT avg(Population) FROM city) GROUP BY District
SELECT GovernmentForm, SUM(Population) FROM country GROUP BY GovernmentForm HAVING AVG(LifeExpectancy) > 72
SELECT GovernmentForm, SUM(Population) FROM country GROUP BY GovernmentForm HAVING AVG(LifeExpectancy) > 72
SELECT avg(LifeExpectancy), sum(Population), Continent FROM country GROUP BY Continent HAVING avg(LifeExpectancy) < 72
SELECT Continent, SUM(Population), AVG(LifeExpectancy) FROM country GROUP BY Continent HAVING AVG(LifeExpectancy) < 72
SELECT Name, SurfaceArea FROM country ORDER BY SurfaceArea DESC LIMIT 5
SELECT Name, SurfaceArea FROM country ORDER BY SurfaceArea DESC LIMIT 5
SELECT Name FROM country ORDER BY Population DESC LIMIT 3
SELECT Name FROM country ORDER BY Population DESC LIMIT 3
SELECT Name FROM country ORDER BY Population ASC LIMIT 3
SELECT Name FROM country ORDER BY Population ASC LIMIT 3
SELECT count(*) FROM country WHERE Continent = 'Asia'
SELECT count(*) FROM country WHERE Continent = 'Asia'
SELECT Name FROM country WHERE Continent = "Europe" AND Population = 80000
SELECT Name FROM country WHERE Continent = 'Europe' AND Population = 80000
SELECT sum(Population) , avg(SurfaceArea) FROM country WHERE Continent = "North America" AND SurfaceArea > 3000
SELECT sum(Population) , avg(SurfaceArea) FROM country WHERE Continent = 'North America' AND SurfaceArea > 3000
SELECT Name FROM city WHERE Population BETWEEN 160000 AND 900000
SELECT Name FROM city WHERE Population BETWEEN 160000 AND 900000
SELECT Language FROM countrylanguage GROUP BY Language ORDER BY count(*) DESC LIMIT 1;
SELECT Language FROM countrylanguage GROUP BY Language ORDER BY count(*) DESC LIMIT 1
SELECT CountryCode, Language, max(Percentage) FROM countrylanguage GROUP BY CountryCode
SELECT T1.CountryCode, T1.Language FROM countrylanguage AS T1 JOIN ( SELECT CountryCode, MAX(Percentage) AS MaxPercentage FROM countrylanguage GROUP BY CountryCode ) AS T2 ON T1.CountryCode = T2.CountryCode AND T1.Percentage = T2.MaxPercentage
SELECT count(*) FROM country WHERE Code IN (SELECT CountryCode FROM countrylanguage WHERE Language = 'Spanish' ORDER BY Percentage DESC)
SELECT count(*) FROM country AS T1 JOIN countrylanguage AS T2 ON T1.Code = T2.CountryCode WHERE T2.Language = 'Spanish' AND T2.IsOfficial = 'T'
SELECT CountryCode FROM countrylanguage WHERE Language = 'Spanish' ORDER BY Percentage DESC
SELECT CountryCode FROM countrylanguage WHERE Language = 'Spanish' AND IsOfficial = 'T'
SELECT count(*) FROM conductor
SELECT count(*) FROM conductor
SELECT Name FROM conductor ORDER BY Age ASC
SELECT Name FROM conductor ORDER BY Age
SELECT Name FROM conductor WHERE Nationality != 'USA'
SELECT Name FROM conductor WHERE Nationality != 'USA'
SELECT Record_Company FROM orchestra ORDER BY Year_of_Founded DESC
SELECT Record_Company FROM orchestra ORDER BY Year_of_Founded DESC
SELECT avg(Attendance) FROM show
SELECT avg(Attendance) FROM show
SELECT max(Share) , min(Share) FROM performance WHERE Type != "Live final"
SELECT max(Share) , min(Share) FROM performance WHERE Type != "Live final"
SELECT count(DISTINCT Nationality) FROM conductor
SELECT count(DISTINCT Nationality) FROM conductor
SELECT Name FROM conductor ORDER BY Year_of_Work DESC
SELECT Name FROM conductor ORDER BY Year_of_Work DESC
SELECT Name FROM conductor ORDER BY Year_of_Work DESC LIMIT 1
SELECT Name FROM conductor ORDER BY Year_of_Work DESC LIMIT 1
SELECT T1.Name , T2.Orchestra FROM conductor AS T1 JOIN orchestra AS T2 ON T1.Conductor_ID = T2.Conductor_ID
SELECT T1.Name, T2.Orchestra FROM conductor AS T1 JOIN orchestra AS T2 ON T1.Conductor_ID = T2.Conductor_ID
SELECT T1.Name FROM conductor AS T1 JOIN orchestra AS T2 ON T1.Conductor_ID = T2.Conductor_ID GROUP BY T1.Name HAVING COUNT(DISTINCT T2.Orchestra_ID) > 1
SELECT T1.Name FROM conductor AS T1 JOIN orchestra AS T2 ON T1.Conductor_ID = T2.Conductor_ID GROUP BY T2.Conductor_ID HAVING COUNT(*) > 1
SELECT T1.Name FROM conductor AS T1 JOIN orchestra AS T2 ON T1.Conductor_ID = T2.Conductor_ID GROUP BY T1.Conductor_ID ORDER BY count(*) DESC LIMIT 1
SELECT T1.Name FROM conductor AS T1 JOIN orchestra AS T2 ON T1.Conductor_ID = T2.Conductor_ID GROUP BY T1.Name ORDER BY count(*) DESC LIMIT 1
SELECT DISTINCT T1.Name FROM conductor AS T1 JOIN orchestra AS T2 ON T1.Conductor_ID = T2.Conductor_ID WHERE T2.Year_of_Founded > 2008
SELECT DISTINCT T1.Name FROM conductor AS T1 JOIN orchestra AS T2 ON T1.Conductor_ID = T2.Conductor_ID WHERE T2.Year_of_Founded > 2008
SELECT Record_Company , COUNT(*) FROM orchestra GROUP BY Record_Company
SELECT Record_Company , count(*) FROM orchestra GROUP BY Record_Company
SELECT Major_Record_Format FROM orchestra GROUP BY Major_Record_Format ORDER BY COUNT(*) ASC
SELECT Major_Record_Format FROM orchestra GROUP BY Major_Record_Format ORDER BY COUNT(*) DESC
SELECT Record_Company FROM orchestra GROUP BY Record_Company ORDER BY COUNT(*) DESC LIMIT 1
SELECT Record_Company FROM orchestra GROUP BY Record_Company ORDER BY count(*) DESC LIMIT 1
SELECT Orchestra FROM orchestra WHERE Orchestra_ID NOT IN (SELECT Orchestra_ID FROM performance)
SELECT Orchestra FROM orchestra WHERE Orchestra_ID NOT IN (SELECT Orchestra_ID FROM performance)
SELECT Record_Company FROM orchestra WHERE Year_of_Founded < 2003 INTERSECT SELECT Record_Company FROM orchestra WHERE Year_of_Founded > 2003
SELECT Record_Company FROM orchestra WHERE Year_of_Founded < 2003 INTERSECT SELECT Record_Company FROM orchestra WHERE Year_of_Founded > 2003
SELECT count(*) FROM orchestra WHERE Major_Record_Format = "CD" OR Major_Record_Format = "DVD"
SELECT count(*) FROM orchestra WHERE Major_Record_Format = "CD" OR Major_Record_Format = "DVD"
SELECT Year_of_Founded FROM orchestra WHERE Orchestra_ID IN (SELECT Orchestra_ID FROM performance GROUP BY Orchestra_ID HAVING COUNT(*) > 1)
SELECT Year_of_Founded FROM orchestra AS T1 JOIN performance AS T2 ON T1.Orchestra_ID = T2.Orchestra_ID GROUP BY T1.Orchestra_ID HAVING COUNT(*) > 1
SELECT count(*) FROM Highschooler
SELECT count(*) FROM Highschooler
SELECT name , grade FROM Highschooler
SELECT name , grade FROM Highschooler
SELECT grade FROM Highschooler
SELECT Grade FROM Highschooler
SELECT grade FROM Highschooler WHERE name = "Kyle";
SELECT grade FROM Highschooler WHERE name = "Kyle"
SELECT name FROM Highschooler WHERE grade = 10
SELECT name FROM Highschooler WHERE grade = 10
SELECT ID FROM Highschooler WHERE name = "Kyle"
SELECT ID FROM Highschooler WHERE name = "Kyle";
SELECT count(*) FROM Highschooler WHERE grade IN (9, 10)
SELECT count(*) FROM Highschooler WHERE grade IN (9, 10)
SELECT grade , count(*) FROM Highschooler GROUP BY grade
SELECT grade , count(*) FROM Highschooler GROUP BY grade
SELECT grade FROM Highschooler GROUP BY grade ORDER BY COUNT(*) DESC LIMIT 1
SELECT grade FROM Highschooler GROUP BY grade ORDER BY count(*) DESC LIMIT 1
SELECT grade FROM Highschooler GROUP BY grade HAVING count(ID) >= 4
SELECT grade FROM Highschooler GROUP BY grade HAVING COUNT(*) >= 4
SELECT student_id , COUNT(*) FROM Friend GROUP BY student_id
SELECT student_id , count(*) FROM Friend GROUP BY student_id
SELECT H.name, COUNT(F.friend_id) FROM Highschooler H LEFT JOIN Friend F ON H.ID = F.student_id GROUP BY H.ID, H.name
SELECT T1.name , count(*) FROM Highschooler AS T1 JOIN Friend AS T2 ON T1.ID = T2.student_id GROUP BY T1.ID
SELECT T1.name FROM Highschooler AS T1 JOIN Friend AS T2 ON T1.ID = T2.student_id GROUP BY T1.ID ORDER BY count(*) DESC LIMIT 1
SELECT T1.name FROM Highschooler AS T1 JOIN Friend AS T2 ON T1.ID = T2.student_id GROUP BY T1.name ORDER BY COUNT(*) DESC LIMIT 1
SELECT T1.name FROM Highschooler AS T1 JOIN Friend AS T2 ON T1.ID = T2.student_id GROUP BY T1.ID HAVING COUNT(*) >= 3
SELECT T1.name FROM Highschooler AS T1 JOIN Friend AS T2 ON T1.ID = T2.student_id GROUP BY T1.ID HAVING COUNT(*) >= 3
SELECT T2.name FROM Friend AS T1 JOIN Highschooler AS T2 ON T1.friend_id = T2.ID WHERE T1.student_id = (SELECT ID FROM Highschooler WHERE name = 'Kyle')
SELECT T2.name FROM Friend AS T1 JOIN Highschooler AS T2 ON T1.friend_id = T2.ID WHERE T1.student_id IN (SELECT ID FROM Highschooler WHERE name = 'Kyle')
SELECT count(*) FROM Friend AS T1 JOIN Highschooler AS T2 ON T1.student_id = T2.ID WHERE T2.name = "Kyle"
SELECT count(*) FROM Friend AS T1 JOIN Highschooler AS T2 ON T1.student_id = T2.ID WHERE T2.name = "Kyle"
SELECT ID FROM Highschooler WHERE ID NOT IN (SELECT student_id FROM Friend)
SELECT ID FROM Highschooler EXCEPT SELECT student_id FROM Friend
SELECT name FROM Highschooler WHERE ID NOT IN (SELECT student_id FROM Friend)
SELECT name FROM Highschooler WHERE ID NOT IN (SELECT student_id FROM Friend)
SELECT T1.ID FROM Highschooler AS T1 JOIN Friend AS T2 ON T1.ID = T2.student_id JOIN Likes AS T3 ON T1.ID = T3.liked_id
SELECT T1.ID FROM Highschooler AS T1 JOIN Friend AS T2 ON T1.ID = T2.student_id JOIN Likes AS T3 ON T1.ID = T3.liked_id GROUP BY T1.ID
SELECT T1.name FROM Highschooler AS T1 JOIN Friend AS T2 ON T1.ID = T2.student_id JOIN Likes AS T3 ON T1.ID = T3.liked_id
SELECT T1.name FROM Highschooler AS T1 JOIN Friend AS T2 ON T1.ID = T2.student_id JOIN Likes AS T3 ON T1.ID = T3.liked_id
SELECT student_id , count(*) FROM Likes GROUP BY student_id
SELECT student_id , count(*) FROM Likes GROUP BY student_id
SELECT T1.name , count(*) FROM Likes AS T2 JOIN Highschooler AS T1 ON T2.student_id = T1.ID GROUP BY T2.student_id
SELECT T1.name , count(*) FROM Highschooler AS T1 JOIN Likes AS T2 ON T1.ID = T2.student_id GROUP BY T1.ID
SELECT T1.name FROM Highschooler AS T1 JOIN Likes AS T2 ON T1.ID = T2.liked_id GROUP BY T1.ID ORDER BY count(*) DESC LIMIT 1
SELECT T1.name FROM Highschooler AS T1 JOIN Likes AS T2 ON T1.ID = T2.liked_id GROUP BY T1.ID ORDER BY COUNT(*) DESC LIMIT 1
SELECT T1.name FROM Highschooler AS T1 JOIN Likes AS T2 ON T1.ID = T2.student_id GROUP BY T1.ID HAVING COUNT(*) >= 2
SELECT T1.name FROM Highschooler AS T1 JOIN Likes AS T2 ON T1.ID = T2.student_id GROUP BY T1.ID HAVING count(*) >= 2
SELECT T1.name FROM Highschooler AS T1 JOIN Friend AS T2 ON T1.ID = T2.student_id GROUP BY T1.name HAVING COUNT(T2.friend_id) >= 2 AND AVG(T1.grade) > 5
SELECT T1.name FROM Highschooler AS T1 JOIN Friend AS T2 ON T1.ID = T2.student_id GROUP BY T1.ID HAVING COUNT(T2.friend_id) >= 2 AND AVG(T1.grade) > 5
SELECT count(*) FROM Likes WHERE liked_id = (SELECT ID FROM Highschooler WHERE name = 'Kyle')
SELECT count(*) FROM Likes AS T1 JOIN Highschooler AS T2 ON T1.student_id = T2.ID WHERE T2.name = "Kyle"
SELECT avg(grade) FROM Highschooler WHERE ID IN (SELECT student_id FROM Friend)
SELECT avg(grade) FROM Highschooler WHERE ID IN (SELECT student_id FROM Friend)
SELECT min(grade) FROM Highschooler WHERE ID NOT IN (SELECT student_id FROM Friend)
SELECT MIN(grade) FROM Highschooler WHERE ID NOT IN (SELECT student_id FROM Friend)
SELECT DISTINCT O.state FROM Owners AS O JOIN Professionals AS P ON O.state = P.state
SELECT DISTINCT state FROM Owners INTERSECT SELECT DISTINCT state FROM Professionals
SELECT avg(age) FROM Dogs WHERE dog_id IN (SELECT dog_id FROM Treatments)
SELECT avg(age) FROM Dogs WHERE dog_id IN (SELECT dog_id FROM Treatments)
SELECT T1.professional_id, T1.last_name, T1.cell_number FROM Professionals AS T1 JOIN Treatments AS T2 ON T1.professional_id = T2.professional_id WHERE T1.state = 'Indiana' OR T1.professional_id IN (SELECT professional_id FROM Treatments GROUP BY professional_id HAVING COUNT(treatment_id) > 2)
SELECT `professional_id`, `last_name`, `cell_number` FROM `Professionals` WHERE `state` = 'Indiana' OR `professional_id` IN (SELECT `professional_id` FROM `Treatments` GROUP BY `professional_id` HAVING COUNT(`treatment_id`) > 2)
SELECT name FROM Dogs WHERE dog_id NOT IN (SELECT dog_id FROM Treatments GROUP BY dog_id HAVING SUM(cost_of_treatment) > 1000)
SELECT name FROM Dogs WHERE dog_id NOT IN (SELECT dog_id FROM Treatments GROUP BY dog_id HAVING SUM(cost_of_treatment) > 1000)
SELECT first_name FROM Professionals UNION SELECT first_name FROM Owners EXCEPT SELECT name FROM Dogs
SELECT first_name FROM Professionals UNION SELECT first_name FROM Owners EXCEPT SELECT name FROM Dogs
SELECT professional_id, role_code, email_address FROM Professionals WHERE professional_id NOT IN (SELECT professional_id FROM Treatments)
SELECT professional_id, role_code, email_address FROM Professionals WHERE professional_id NOT IN (SELECT professional_id FROM Treatments)
SELECT `owner_id`, `first_name`, `last_name` FROM `Owners` WHERE `owner_id` IN (SELECT `owner_id` FROM `Dogs` GROUP BY `owner_id` ORDER BY COUNT(*) DESC LIMIT 1)
SELECT owner_id, first_name, last_name FROM Owners WHERE owner_id = (SELECT owner_id FROM Dogs GROUP BY owner_id ORDER BY COUNT(*) DESC LIMIT 1)
SELECT T1.professional_id, T1.role_code, T1.first_name FROM Professionals AS T1 JOIN Treatments AS T2 ON T1.professional_id = T2.professional_id GROUP BY T1.professional_id HAVING COUNT(*) >= 2
SELECT T1.professional_id, T1.role_code, T1.first_name FROM Professionals AS T1 JOIN Treatments AS T2 ON T1.professional_id = T2.professional_id GROUP BY T1.professional_id HAVING COUNT(*) >= 2
SELECT breed_name FROM Breeds AS T1 JOIN Dogs AS T2 ON T1.breed_code = T2.breed_code GROUP BY T1.breed_name ORDER BY count(*) DESC LIMIT 1
SELECT t2.breed_name FROM Dogs AS t1 JOIN Breeds AS t2 ON t1.breed_code = t2.breed_code GROUP BY t2.breed_name ORDER BY count(*) DESC LIMIT 1
SELECT T1.owner_id, T1.last_name FROM Owners AS T1 JOIN Dogs AS T2 ON T1.owner_id = T2.owner_id JOIN Treatments AS T3 ON T2.dog_id = T3.dog_id GROUP BY T1.owner_id ORDER BY COUNT(*) DESC LIMIT 1
SELECT T1.owner_id, T1.last_name FROM Owners AS T1 JOIN Dogs AS T2 ON T1.owner_id = T2.owner_id JOIN Treatments AS T3 ON T2.dog_id = T3.dog_id GROUP BY T1.owner_id ORDER BY sum(T3.cost_of_treatment) DESC LIMIT 1
SELECT t1.treatment_type_description FROM Treatment_Types AS t1 JOIN Treatments AS t2 ON t1.treatment_type_code = t2.treatment_type_code GROUP BY t1.treatment_type_code ORDER BY sum(t2.cost_of_treatment) ASC LIMIT 1
SELECT T1.treatment_type_description FROM Treatment_Types AS T1 JOIN Treatments AS T2 ON T1.treatment_type_code = T2.treatment_type_code GROUP BY T1.treatment_type_code ORDER BY sum(cost_of_treatment) ASC LIMIT 1;
SELECT T1.owner_id, T1.zip_code FROM Owners AS T1 JOIN Dogs AS T2 ON T1.owner_id = T2.owner_id JOIN Treatments AS T3 ON T2.dog_id = T3.dog_id GROUP BY T1.owner_id ORDER BY sum(T3.cost_of_treatment) DESC LIMIT 1
SELECT T1.owner_id, T1.zip_code FROM Owners AS T1 JOIN Dogs AS T2 ON T1.owner_id = T2.owner_id JOIN Treatments AS T3 ON T2.dog_id = T3.dog_id GROUP BY T1.owner_id ORDER BY sum(T3.cost_of_treatment) DESC LIMIT 1
SELECT T1.professional_id, T1.cell_number FROM Professionals AS T1 JOIN Treatments AS T2 ON T1.professional_id = T2.professional_id GROUP BY T1.professional_id HAVING COUNT(DISTINCT T2.treatment_type_code) >= 2
SELECT professional_id, cell_number FROM Professionals WHERE professional_id IN (SELECT professional_id FROM Treatments GROUP BY professional_id HAVING COUNT(DISTINCT treatment_type_code) >= 2)
SELECT first_name, last_name FROM Professionals WHERE professional_id IN (SELECT professional_id FROM Treatments WHERE cost_of_treatment < (SELECT AVG(cost_of_treatment) FROM Treatments))
SELECT P.first_name, P.last_name FROM Professionals AS P JOIN Treatments AS T ON P.professional_id = T.professional_id WHERE T.cost_of_treatment < (SELECT AVG(cost_of_treatment) FROM Treatments)
SELECT T.date_of_treatment , P.first_name FROM Treatments AS T JOIN Professionals AS P ON T.professional_id = P.professional_id
SELECT T1.date_of_treatment , T2.first_name FROM Treatments AS T1 JOIN Professionals AS T2 ON T1.professional_id = T2.professional_id
SELECT T1.cost_of_treatment , T2.treatment_type_description FROM Treatments AS T1 JOIN Treatment_Types AS T2 ON T1.treatment_type_code = T2.treatment_type_code
SELECT T1.cost_of_treatment , T2.treatment_type_description FROM Treatments AS T1 JOIN Treatment_Types AS T2 ON T1.treatment_type_code = T2.treatment_type_code
SELECT T1.first_name, T1.last_name, T3.size_description FROM Owners AS T1 JOIN Dogs AS T2 ON T1.owner_id = T2.owner_id JOIN Sizes AS T3 ON T2.size_code = T3.size_code
SELECT T1.first_name , T1.last_name , T3.size_description FROM Owners AS T1 JOIN Dogs AS T2 ON T1.owner_id = T2.owner_id JOIN Sizes AS T3 ON T2.size_code = T3.size_code
SELECT T1.first_name , T2.name FROM Owners AS T1 JOIN Dogs AS T2 ON T1.owner_id = T2.owner_id
SELECT T1.first_name , T2.name FROM Owners AS T1 JOIN Dogs AS T2 ON T1.owner_id = T2.owner_id
SELECT Dogs.name, Treatments.date_of_treatment FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_id WHERE Dogs.breed_code = (SELECT breed_code FROM Dogs GROUP BY breed_code ORDER BY COUNT(*) ASC LIMIT 1)
SELECT Dogs.name, Treatments.date_of_treatment FROM Dogs JOIN Treatments ON Dogs.dog_id = Treatments.dog_id WHERE Dogs.breed_code = (SELECT breed_code FROM Dogs GROUP BY breed_code ORDER BY COUNT(*) ASC LIMIT 1)
SELECT Owners.first_name, Dogs.name FROM Dogs JOIN Owners ON Dogs.owner_id = Owners.owner_id WHERE Owners.state = 'Virginia'
SELECT T1.first_name, T2.name FROM Owners AS T1 JOIN Dogs AS T2 ON T1.owner_id = T2.owner_id WHERE T1.state = 'Virginia'
SELECT T1.date_arrived, T1.date_departed FROM Dogs AS T1 JOIN Treatments AS T2 ON T1.dog_id = T2.dog_id
SELECT T1.date_arrived, T1.date_departed FROM Dogs AS T1 JOIN Treatments AS T2 ON T1.dog_id = T2.dog_id
SELECT Owners.last_name FROM Owners JOIN Dogs ON Owners.owner_id = Dogs.owner_id ORDER BY Dogs.date_of_birth DESC LIMIT 1;
SELECT O.last_name FROM Owners O JOIN Dogs D ON O.owner_id = D.owner_id ORDER BY D.date_of_birth DESC LIMIT 1;
SELECT email_address FROM Professionals WHERE state = "Hawaii" OR state = "Wisconsin"
SELECT email_address FROM Professionals WHERE state = "Hawaii" OR state = "Wisconsin";
SELECT date_arrived, date_departed FROM Dogs;
SELECT date_arrived , date_departed FROM Dogs
SELECT count(DISTINCT dog_id) FROM Treatments
SELECT count(DISTINCT dog_id) FROM Treatments
SELECT COUNT(DISTINCT professional_id) FROM Treatments
SELECT COUNT(DISTINCT professional_id) FROM Treatments
SELECT role_code, street, city, state FROM Professionals WHERE city LIKE "%West%"
SELECT role_code, street, city, state FROM Professionals WHERE city LIKE "%West%"
SELECT first_name, last_name, email_address FROM Owners WHERE state LIKE "%North%"
SELECT first_name, last_name, email_address FROM Owners WHERE state LIKE "%North%"
SELECT count(*) FROM Dogs WHERE age < (SELECT avg(age) FROM Dogs)
SELECT count(*) FROM Dogs WHERE age < (SELECT avg(age) FROM Dogs)
SELECT cost_of_treatment FROM Treatments ORDER BY date_of_treatment DESC LIMIT 1
SELECT cost_of_treatment FROM Treatments ORDER BY date_of_treatment DESC LIMIT 1
SELECT count(*) FROM Dogs WHERE dog_id NOT IN (SELECT dog_id FROM Treatments)
SELECT count(*) FROM Dogs WHERE dog_id NOT IN (SELECT dog_id FROM Treatments)
SELECT count(*) FROM Owners WHERE owner_id NOT IN (SELECT owner_id FROM Dogs WHERE abandoned_yn != 'Y')
SELECT count(*) FROM Owners WHERE owner_id NOT IN (SELECT owner_id FROM Dogs WHERE date_adopted IS NULL AND date_departed IS NULL)
SELECT count(*) FROM Professionals WHERE professional_id NOT IN ( SELECT professional_id FROM Treatments )
SELECT count(*) FROM Professionals WHERE professional_id NOT IN (SELECT professional_id FROM Treatments)
SELECT name, age, weight FROM Dogs WHERE abandoned_yn = '1'
SELECT name, age, weight FROM Dogs WHERE abandoned_yn = '1'
SELECT avg(age) FROM Dogs
SELECT avg(age) FROM Dogs
SELECT max(age) FROM Dogs
SELECT Age FROM Dogs ORDER BY Age DESC LIMIT 1
SELECT charge_type , sum(charge_amount) FROM Charges GROUP BY charge_type
SELECT charge_type , charge_amount FROM Charges;
SELECT charge_type, charge_amount FROM Charges ORDER BY charge_amount DESC LIMIT 1
SELECT charge_amount FROM Charges ORDER BY charge_amount DESC LIMIT 1
SELECT email_address, cell_number, home_phone FROM Professionals
SELECT email_address , cell_number , home_phone FROM Professionals
SELECT B.breed_name, S.size_description FROM Breeds B, Sizes S
SELECT DISTINCT B.breed_name, S.size_description FROM Dogs AS D JOIN Breeds AS B ON D.breed_code = B.breed_code JOIN Sizes AS S ON D.size_code = S.size_code
SELECT T1.first_name , T2.treatment_type_description FROM Professionals AS T1 JOIN Treatments AS T2 ON T1.professional_id = T2.professional_id JOIN Treatment_Types AS T3 ON T2.treatment_type_code = T3.treatment_type_code
SELECT T2.first_name , T3.treatment_type_description FROM Treatments AS T1 JOIN Professionals AS T2 ON T1.professional_id = T2.professional_id JOIN Treatment_Types AS T3 ON T1.treatment_type_code = T3.treatment_type_code
SELECT count(*) FROM singer
SELECT count(*) FROM singer
SELECT Name FROM singer ORDER BY Net_Worth_Millions ASC
SELECT Name FROM singer ORDER BY Net_Worth_Millions ASC
SELECT Birth_Year , Citizenship FROM singer
SELECT Birth_Year , Citizenship FROM singer
SELECT Name FROM singer WHERE Citizenship != "France"
SELECT Name FROM singer WHERE Citizenship != 'French'
SELECT Name FROM singer WHERE Birth_Year = 1948 OR Birth_Year = 1949
SELECT Name FROM singer WHERE Birth_Year = 1948 OR Birth_Year = 1949
SELECT Name FROM singer ORDER BY Net_Worth_Millions DESC LIMIT 1
SELECT Name FROM singer ORDER BY Net_Worth_Millions DESC LIMIT 1
SELECT Citizenship , COUNT(*) FROM singer GROUP BY Citizenship
SELECT Citizenship , COUNT(*) FROM singer GROUP BY Citizenship
SELECT Citizenship FROM singer GROUP BY Citizenship ORDER BY COUNT(*) DESC LIMIT 1
SELECT Citizenship FROM singer GROUP BY Citizenship ORDER BY COUNT(*) DESC LIMIT 1
SELECT "Citizenship", max("Net_Worth_Millions") FROM singer GROUP BY "Citizenship"
SELECT Citizenship , max(Net_Worth_Millions) FROM singer GROUP BY Citizenship
SELECT T1.Title , T2.Name FROM song AS T1 JOIN singer AS T2 ON T1.Singer_ID = T2.Singer_ID
SELECT song.Title , singer.Name FROM song JOIN singer ON song.Singer_ID = singer.Singer_ID
SELECT DISTINCT Name FROM singer WHERE Singer_ID IN (SELECT Singer_ID FROM song WHERE Sales > 300000)
SELECT DISTINCT T1.Name FROM singer AS T1 JOIN song AS T2 ON T1.Singer_ID = T2.Singer_ID WHERE T2.Sales > 300000
SELECT singer.Name FROM singer JOIN song ON singer.Singer_ID = song.Singer_ID GROUP BY singer.Name HAVING COUNT(*) > 1
SELECT T1.Name FROM singer AS T1 JOIN song AS T2 ON T1.Singer_ID = T2.Singer_ID GROUP BY T1.Singer_ID HAVING COUNT(*) > 1
SELECT T1.Name , sum(T2.Sales) FROM singer AS T1 JOIN song AS T2 ON T1.Singer_ID = T2.Singer_ID GROUP BY T1.Name
SELECT T1.Name , sum(T2.Sales) FROM singer AS T1 JOIN song AS T2 ON T1.Singer_ID = T2.Singer_ID GROUP BY T1.Name
SELECT Name FROM singer WHERE Singer_ID NOT IN (SELECT Singer_ID FROM song)
SELECT Name FROM singer WHERE Singer_ID NOT IN (SELECT Singer_ID FROM song)
SELECT Citizenship FROM singer WHERE Birth_Year < 1945 INTERSECT SELECT Citizenship FROM singer WHERE Birth_Year > 1955
SELECT Citizenship FROM singer WHERE Birth_Year < 1945 INTERSECT SELECT Citizenship FROM singer WHERE Birth_Year > 1955
SELECT count(*) FROM Other_Available_Features
SELECT T1.feature_type_name FROM Ref_Feature_Types AS T1 JOIN Other_Available_Features AS T2 ON T1.feature_type_code = T2.feature_type_code WHERE T2.feature_name = "AirCon";
SELECT property_type_description FROM Ref_Property_Types WHERE property_type_code IN (SELECT property_type_code FROM Properties)
SELECT property_name FROM Properties WHERE (property_type_code IN (SELECT property_type_code FROM Ref_Property_Types WHERE property_type_description IN ('House', 'Apartment')) AND room_count > 1)