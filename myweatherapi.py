import urllib.request
import json

city = input('Enter a city: ')
units = "&units=metric"
api_uri = "http://api.openweathermap.org/data/2.5/weather?q="
api_key = "&APPID=21eebae5f56bdb09029a4e9985925702"


def results():
    print('The temperature in ' + data['name'] + ' is ' + str(data['main']['temp']) + 'C' + ' with '
          + data['weather'][0]['description'] + '.')


with urllib.request.urlopen(api_uri + city + units + api_key) as url:
    data = json.loads(url.read().decode())
    json_str = json.dumps(data)
    with open('myweatherapidata.json', 'w', encoding='utf8') as f:
        json.dump(data, f, indent=4)
        results()
