from html.parser import HTMLParser
import urllib.request

# Import HTML from a URL
location = "https://www.vrbo.com/vacation-rentals/usa/maryland/eastern-shore/ocean-city"
url = urllib.request.urlopen(
    "https://www.vrbo.com/vacation-rentals/usa/maryland/eastern-shore/ocean-city")
html = url.read().decode()
url.close()


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
        # init query tag
        tag = self.query[0]

        # init attr query
        attr = self.query[1]

        # init query output
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


# data extraction logic
hotelsList = find(content=html, query=[
    'div', ('class', 'CommonRatioCard__description'), 'text'])
WebParser.results = []
roomDescription = find(content=html, query=[
    'div', ('class', 'CommonRatioCard__subcaption'), 'text'])
WebParser.results = []
priceList = find(content=html, query=[
    'span', ('class', 'CommonRatioCard__price__amount'), 'text'])
WebParser.results = []
print(location[38:41]+" "+location[42:50])
# Extracting Sleeping rooms , Bedrooms, bathRooms from facilities list
sleepingRooms = []
bedRooms = []
bathRooms = []
for i in range(0, len(roomDescription)):
    allFacilities = roomDescription[i]
    print(allFacilities)
    # Slice sleeping, bedroom, & bathroom
    sleepingRooms.append(allFacilities[7:9])
    bedRooms.append(allFacilities[11:13])
    bathRooms.append(allFacilities[24:26])
print(hotelsList[0])

for i in range(0, len(sleepingRooms)):
    print("slepping room : "+sleepingRooms[i]+" Bedrooms:  "+bedRooms[i]+" Bathrooms : "+bathRooms[i]);

# Storing data in database
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
isDatabaseCreated = 0
if(mydb.is_connected()):
    print("Connected with database successfully")
    try:
        cursor = mydb.cursor()
        cursor.execute("SHOW DATABASES")
        if isDatabaseCreated == 0:
            cursor.execute("CREATE DATABASE vrboHotelData")
            print("Database created")
            isDatabaseCreated=1
        #cursor.execute("CREATE DATABASE abc")
        #print("Database created")
        mySql_Create_Table_Query = """CREATE TABLE vrbohoteldata (
                                         Id int(11) NOT NULL,
                                         Name varchar(250) NOT NULL,
                                         Price float NOT NULL,
                                         Purchase_date Date NOT NULL,
                                         PRIMARY KEY (Id)) """
        print("Hotel Data Table created successfully ")
        # insert
        mySql_insert_query1 = """INSERT INTO vrbohoteldata (Id, Name, Price, Purchase_date) 
                                 VALUES 
                                 (15, 'Lenovo ThinkPad P71', 6459, '2019-08-14') """

        cursor.execute(mySql_insert_query1)
        mydb.commit()
        print(cursor.rowcount, "Record inserted successfully into Laptop table")

    except mysql.connector.Error as error:
        print("Failed to create table in MySQL: {}".format(error))
    finally:
        if mydb.is_connected():
            mydb.close()
            print("MySQL connection is closed")
