import requests
from bs4 import BeautifulSoup

coorDict = {
    "Rome": "42 12",
    "New York": "40 -74",
    "Los Angeles": "34 -118",
    "Ottawa": "45 -75",
    "Beijing": "40 116",
    "Tokyo": "35 139",
    "Canberra": "-35 149",
    "London": "51 0",
    "Cairo": "30 31",
    "New Delhi": "28 77",
    "Cape Town": "-34 18",
    "Brasilia": "-15 -48",
    "Moscow": "55 37",
    "Lagos": "6 3",
    "Addis Ababa": "9 38",
    "Rabat": "34 6",
    "Dakar": "14 17",
    "Buenos Aires": "-35 -58",
    "Lima": "-12 -77",
    "Mexico City": "19 -99",
    "Auckland": "-37 174",
    "Berlin": "52 13",
    "San Francisco": "37 -122",
    "Chicago": "42 -87",
    "Havana": "23 -82",
    "Madrid": "40 -3",
    "Istanbul": "41 29",
    "Doha": "25 51",
    "Islamabad": "33 73",
    "Shangai": "31 121",
    "Kyoto": "35 135",
    "Taipei": "25 121",
    "Tehran": "34 51    ",
    "Ulan Bator": "48 107",
    "Helsinki": "60 25"
}

def forecast():
    print( "The forecast tool is starting!" )
    
    measSelect = input( "Choose the measures to use for the results (fahrenheit or celsius)[f/c]: " )
    if measSelect == "f":
        measures = "us12"
    elif measSelect == "c":
        measures = "ca12"
    else:
        measures = "ca12"
    
    coord1 = input( "Insert the coordinates of the place you want to pin\n" )
    coord2 = input()
    coordinates = coord1 + "," + coord2
    
    url = "https://darksky.net/forecast/" + coordinates + "/" + measures + "/en"
    page = requests.get( url )
    
    soup = BeautifulSoup( page.content, "html.parser" )
    
    tag1 = soup.find_all( class_="num swip humidity__value" )
    humidity = "Humidity: " + tag1[0].string
    tag2 = soup.find_all( class_="summary swap" )
    summary = "Conditions: " + tag2[0].string
    tag3 = soup.find_all( class_="feels-like-text" )
    feeling = "Feels like: " + tag3[0].string
    tag4 = soup.find_all( class_="low-temp-text" )
    low = "Lowest: " + tag4[0].string
    tag5 = soup.find_all( class_="high-temp-text" )
    high = "Highest: " + tag5[0].string
    print( summary + "\n" + feeling + "\n" + low + "\n" + high + "\n" + humidity )
    
    start()

def start():
    print( "Welcome to the Weather Forecast provider!" )
    command = input( "Type \"go\" to start or \"help\" for further commands: " )
    if command == "go":
        forecast()
    elif command == "help":
        print( "Commands:\ngo - start the forecast\ninfo - get information about this weather forecast\ncoordinates - find coordinates for a city" )
        start()
    elif command == "info":
        print( "This tool gets all the information from www.darksky.net" )
        start()
    elif command == "coordinates":
        town = input( "Get the coordinates of a city from a list of 30+ cities: " )
        print( coorDict[town] )
        start()
    elif command == "exit":
        print( "Bye!" )
    print( "Closing the weather forecast tool!" )

start()