from flask import Flask
import requests
app = Flask(__name__)


@app.route('/')
def hello_world():
    return ' Hello! \n This is Open-Weather API \n You can check weather condition of your city by typing city and country code in URL. \n For example: \n \t " /London/UK " \n \t " /Karachi/PK " '


@app.route('/<city>/<country_code>')
def hello_shah(city, country_code):
    api_key = '9ef4115193d676f691ecd24950d18895'
    response = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={api_key}')
    result = response.json()
    return result


if __name__ == '__main__':
    app.run()
