# Python_Web_Scraping
This is a python script that scraps the data of vacation rent service named as vrbo and stores that data in mysql database.


# Project Features
* Scrap properties like hotel name, sleeping, bedrooms, bathrooms ,locations etc.
* Stores the above properties into mysql database


## How the run the scripts 

``` bash
# install and configure python 

# Install mysql and mysql connector and configure it
To install mysql connector run -
sudo apt-get install python3-mysql.connector
* For me I have installed used Xampp server
```
# Database table design
| Location   | Hotel Name | Sleeping | Bedrooms | Bathroom |
|------------|------------|----------|----------|----------|
| usa        | str        | 6        | 4        | 3        |
| florida    | str1       | 5        | 3        | 2        |
| ochen city | str3       | 4        | 2        | 2        |
| user4      | x4         | y4       |          |          |
| user5      | x5         | y5       |          |          |