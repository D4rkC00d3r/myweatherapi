# Introduction
"My Weather API" is a simple tool made in Python3 to check the weather from the OpenWeatherMaps database.

## Why I made it?
I am learning how to use Application Programming Interface's (API) within Python and how to handle the returned data in json.

## What can myweatherapi do?
With myweatherapi you are able to enter a city name and make an API request to get the weather now in that city.
## What does the json result look like?
The json below is returned from the OpenWeatherMaps server and I add some formatting to make it readable.

```json
  {
    "name": "London",
    "id": 2643743,
    "dt": 1494103800,
    "base": "stations",
    "clouds": {
        "all": 0
    },
    "sys": {
        "country": "GB",
        "id": 5091,
        "message": 0.008,
        "sunset": 1494099216,
        "type": 1,
        "sunrise": 1494044495
    },
    "visibility": 9000,
    "coord": {
        "lat": 51.51,
        "lon": -0.13
    },
    "wind": {
        "speed": 3.6,
        "deg": 350
    },
    "main": {
        "temp": 10.82,
        "temp_max": 12,
        "temp_min": 9,
        "pressure": 1015,
        "humidity": 76
    },
    "cod": 200,
    "weather": [
        {
            "main": "Haze",
            "icon": "50n",
            "description": "haze",
            "id": 721
        }
    ]
}
```
 * Example based on the city being set to London.

## What API am I using and why?
I am using the OpenWeatherMap API for current weather data. I chose this as it forced me to make a developer
account and obtain a API key. I then had to learn how to use the key, I also liked the returned json data as it had nested
objects that I would need to drill down into to construct the data for the user. https://openweathermap.org/current 

## How to use myweatherapi?
Simply clone or download the myweatherapi project and make the script executable with the following command;

```
sudo chmod +x myweatherapi.py
```
then to run myweatherapi simply type;
```
python3 myweatherapi.py
```
Below is an example of the console output.
![myweatherconsole](https://cloud.githubusercontent.com/assets/17799879/25776136/e6afa9ce-32ad-11e7-9445-87bcfc34c810.png)

## Additional notes
1. Each time you run the script check the myweatherapidata.json file to see it change depending on the city entered.
2. I have tried to make it as clean as passable adhering to PEP 8.

## Credits
The API belongs to https://openweathermap.org/

## Want to use or change my code?
That's awesome! Thanks, but please adhere to the GNU GENERAL PUBLIC LICENSE. For more information see the LICENSE.txt in the repo.

Enjoy. D4rkC00d3r :-)
