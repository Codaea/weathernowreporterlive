from __future__ import annotations # forward refrences for type hinting
from typing import List
from utils import clear_screen, clamp
from instruments import Calendar, Cricket, EightBall, Jerry, Rock
import time
import math
import random
from datetime import date, datetime
import csv
from enum import Enum



class WeatherGame:
    def __init__(self, game_length=7*4, weather_data_file="weather_data.csv"):
        self.game_length = game_length
        self.weather_data_file = weather_data_file

        # ask player if they have played before
        self.has_played_before = input("Have you played before? (y/n): ").lower().split()[0][0] == 'y'
        self.tutorial()
        
        # initialize the weather engine
        self.weather_engine = WeatherEngine(weather_data_file=self.weather_data_file)
        # initalize instruments
        self.Calendar = Calendar()
        self.Cricket = Cricket(days_inacurate=[0, 6]) # Mondays and Sundays are inacurate
        self.EightBall = EightBall()
        self.Jerry = Jerry()
        self.Rock = Rock()
        
        # Main game loop
        for i in range(game_length):
            clear_screen()
            print(f"Day {i+1} of {game_length}")

            # get weather from weather engine -> csv
            weather = self.weather_engine.get_day()

            # Generate Instrument readings from real weather for next day
            self.Calendar.format(weather.date, weather.season)
            self.Cricket.predict(weather)
            self.EightBall.predict()
            self.Jerry.predict(weather)
            self.Rock.predict(weather)
            # score prediction

    def tutorial(self):
        """Displays intro and story if the player has not played before. displays on the has_played_before variable"""
        if not self.has_played_before:
            print()
            print("""You are the child of your prodigal father, a master weatherman. 
He was recently arrested for weatherfraud by the WCC (Weather Communications Commission) 
and has been placed on paid administrative leave to a remote jail in hawaii. 
You must step up to the family buisness, and carry on (The better parts) of your 
fathers legacy.""")
            time.sleep(2)
            print()
            print("""Due to the legal trouble the station is in though, 
the HiTech Weather 5000 (Patent Pending) was repossesed by the bank, 
so your going to have to make do without any (good) instruments. 
                  """)
            time.sleep(2)
            print("Welcome to WeatherNOW! In this game, you will be a weather reporter trying to predict the weather for the next week. Each day, you will be given some information about the current weather and you will have to make a prediction for the next day. Your score will be based on how accurate your predictions are. Good luck!")

# A single days weather
class WeatherDay:
    def __init__(self, tempature: float, condition: WeatherCondition, date: date, season: str):
        self.tempature = tempature
        self.condition = condition
        self.date = date
        self.season = season

    def __str__(self):
        """Debug function for printing to string"""
        return f"Temperature: {self.tempature}, Condition: {self.condition.value}"
    
    pass

# Define an Enum for weather conditions
class WeatherCondition(Enum):
    SUNNY = "sunny"
    CLOUDY = "cloudy"
    RAINY = "rainy"
    STORMY = "stormy"
    SNOWY = "snowy"

class WeatherEngine:
    def __init__(self, weather_data_file: str = "weather_data.csv"):
        self.weather_data_file = weather_data_file
        
        # read in weather csv data and store it in a list of WeatherDay objects
        self.weather_days: List[WeatherDay] = []
        self.read_weather_data()
        self.current_day = 0
        
    def get_day(self):
        """return a weather object for the next object in line for the weather day."""
        weather = self.weather_days[self.current_day]
        self.current_day += 1
        return weather
        

    def read_weather_data(self):
        """Reads in weather data from a csv file and stores it in a list of WeatherDay objects.
        The csv file should have the following format:
        date,season,tempature,condition.
        date should be ISO 8601 Format YYYY-MM-DD"""
        with open(self.weather_data_file, 'r') as f:
            # read the data and store it in a list of WeatherDay objects
            reader = csv.reader(f, delimiter=',')

            for row in reader:
                date = datetime.fromisoformat(row[0])
                season = row[1]
                temp = float(row[2])
                condition = row[3]
                weather_day = WeatherDay(tempature=temp, condition=WeatherCondition(condition), date=date, season=season)

                self.weather_days.append(weather_day)
            return
        return
# Player prediction object
class Forcast:
    def __init__(self, tempature: float, condition: WeatherCondition):
        self.tempature = tempature
        self.condition = condition

    def score(self, weather_day: WeatherDay):
        # handles scoring from the weather day.
        pass
