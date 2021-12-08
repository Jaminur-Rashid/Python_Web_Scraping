###################################################################
# This script scrapes some location, hotel name, sleeping room etc.
# from vrbo website and stores that data in mysql database
# Author : Jaminur Rashid
# Date   : 7-12-2021
###################################################################
from html.parser import HTMLParser
import urllib.request
import mysql.connector
import uuid
import re
#from vrboDatabase import *

# Import HTML from a URL
location = "https://www.vrbo.com/vacation-rentals/usa/maryland/eastern-shore/ocean-city"
vrboURL = urllib.request.urlopen(
    "https://www.vrbo.com/vacation-rentals/usa/maryland/eastern-shore/ocean-city")
html = vrboURL.read().decode()
vrboURL.close()


class WebParser(HTMLParser):
    # search query
    query = []

    # search result match
    match = {}

    # results list
    results = []

    # handle opening tag
    def handle_starttag(self, tag, attr):
        self.match['name'] = tag
        self.match['attr'] = attr

    # handle data within a tag
    def handle_data(self, data):
        # initialize query tag
        tag = self.query[0]

        # initialize attr query
        attr = self.query[1]

        # initialize query output
        text = self.query[-1]

        try:
            # found tag name
            if self.match['name'] == tag:
                # attributes are not specified in query
                if not len(attr):
                    # on tag text node query
                    if text == 'text':
                        self.results.append(data)

                    # on tag attrbute data query
                    else:
                        # loop over attributes list
                        for item in self.match['attr']:
                            # init attr key and value
                            key = item[0]
                            val = item[1]

                            # query output is within attr's key
                            if text == key:
                                self.results.append(val)

                # attributes are specified in query
                else:
                    # loop over attributes list
                    for item in self.match['attr']:
                        # init available attr key and value
                        key = item[0]
                        val = item[1]

                        # init query attr key and value
                        q_key = attr[0]
                        q_val = attr[1]

                        # match key and value pairs
                        if q_key == key and q_val == val:
                            # on tag text node query
                            if text == 'text':
                                self.results.append(data)

                            # on tag attrbute data query
                            else:
                                # loop over attributes list
                                for item in self.match['attr']:
                                    # init attr key and value
                                    key = item[0]
                                    val = item[1]

                                    # query output is within attr's key
                                    if text == key:
                                        self.results.append(val)

        except:
            pass

    # handle closing tag
    def handle_endtag(self, tag):
        # reset result match after matching closing tag
        self.match = {}

# parse content


def find(content, query):
    # create parser instance
    parser = WebParser()

    # init query
    parser.query = query

    # find matching results
    parser.feed(str(content))

    # close parser
    parser.close()

    # return results
    return parser.results


# extracting data
hotelsList = find(content=html, query=[
    'div', ('class', 'CommonRatioCard__description'), 'text'])
WebParser.results = []
roomDescription = find(content=html, query=[
    'div', ('class', 'CommonRatioCard__subcaption'), 'text'])
WebParser.results = []
priceList = find(content=html, query=[
    'span', ('class', 'CommonRatioCard__price__amount'), 'text'])
WebParser.results = []
location_name=(location[38:41]+" "+location[42:50])


# Extracting Sleeping rooms , Bedrooms, bathRooms from facilities list
sleepingRooms = []
bedRooms = []
bathRooms = []

for i in range(0, len(roomDescription)):
    room_quantity = re.findall("\d+", roomDescription[i]) #extracts only number from string
    # store extracted rooms information into separate list
    sleepingRooms.append(room_quantity[0])
    bedRooms.append(room_quantity[1])
    bathRooms.append(room_quantity[2])
# show extracted data
for i in range(0, len(roomDescription)):
    if i == 0:
        print("Location is : "+location_name)
        print("Data of hotel " + str(i + 1) + " is : ")
        print(" Sleeping room  : " + sleepingRooms[i] + " Bedrooms:  " + bedRooms[i] + " Bathrooms : " + bathRooms[i]);
        print(" Hotel Title is: " + hotelsList[i]);
        print(" Price is      : " + priceList[i]);
    else :
        print("Data of hotel " + str(i + 1) + " is : ")
        print(" Sleeping room  : " + sleepingRooms[i] + " Bedrooms:  " + bedRooms[i] + " Bathrooms : " + bathRooms[i]);
        print(" Hotel Title is: " + hotelsList[i]);
        print(" Price is      : " + priceList[i]);


# Function that return a unique id


def get_unique_id():
    u_id = uuid.uuid1()
    return (u_id)

# Storing data in database

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="vrboDatabase"
)

isDatabaseCreated = 0
if(mydb.is_connected()):
    cursor = mydb.cursor()
    try:
        for i in range(0, len(roomDescription)):
            mySql_insert_query = """INSERT IGNORE INTO vrbo_hotel_info_table (Id, Location, Hotel_Name, Sleeping, Bedroom, Bathroom) 
                                               VALUES 
                                               (%s,%s,%s,%s,%s,%s) """
            # call get_unique_id function to get unique id
            unique_id = str(get_unique_id())
            table_values = (unique_id, location_name, "Check_Hotel", sleepingRooms[i], bedRooms[i], bathRooms[i])
            cursor.execute(mySql_insert_query, table_values)
            mydb.commit()
        print("Data Inserted Successfully")

    except mysql.connector.Error as error:
        print("Failed to insert record into vrbo_hotel_info table {}".format(error))
    finally:
        if mydb.is_connected():
            mydb.close()
            print("MySQL connection is closed")

