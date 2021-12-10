# Python_Web_Scraping
This is a python script that scraps the data of vacation rent service named as vrbo and stores that data in mysql database.


##### Project Features
* Scrap properties like hotel name, sleeping, bedrooms, bathrooms ,locations etc.
* Stores the above properties into mysql database
* Prevented inserting duplicate hotel name into the database

# Prerequisites
* Mysql
* Python 3
* Xampp(if mysql installation failed)
* install and configure python 
* Install mysql connector 
To install mysql connector run -
``` 
sudo apt-get install python3-mysql.connector
```

# How the run the scripts 
One can run the script in two ways
# Procedure One
After creating a database 
``` bash
import the vrbo_hotel_info_table.sql file to retrive all tha hotel data
```
The above sql  script will store all the data in your system database

# Procedure Two
If the above methods doesn,t work then,
``` 
run vrboDatabase.py script
The above script will create a vrbo_hotel_info_table in the database
``` bash
Then run the main.py script to store the scraped data
```


##### Database Table Structure
| ID             | Location       | Hotel_Name | Sleeping  | Bedroom | Bathroom | Price |
|----------------|----------------|------------|-----------|---------|----------|-------|
| uhg87-888-a7.  | Usa-Maryland   | Hotel One  | 10        | 3       | 2        | $60   |
| uhg87-888-a8.  | Usa-Maryland   | Hotel Two  | 6         | 2       | 3        | $127  |
| uhg87-888-a9.  | Usa-Maryland   | Hotel Three | 8         | 2       | 4        | $109  |
| uhg87-888-a10. | Usa-Maryland   | Hotel Four | 7         | 1       | 2        | $92   |
| uhg87-888-a11. | Usa-Maryland   | Hotel Five | 5         | 5       | 3        | $116  |
 | uhg87-88-a11.  | Usa-Maryland  |  Hotel Six | 2         | 4       | 1        | $225  |