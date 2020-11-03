from datetime import datetime
import os
import pytz
import requests
import math

API_KEY = 'b08146856b184d819a56dba5765f7490'
API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}')


def query_api(city):
    try:
        data = requests.get(API_URL.format(city, API_KEY)).json()

        return data

    except Exception as exc:
        print(exc)
        data = None
        return data
