from __future__ import annotations # forward refrences for type hinting
from typing import List
from utils import clear_screen, input_valid_float, input_valid_condition
from instruments import Calendar, Cricket, EightBall, Jerry, Grandma,Rock
from weather_day import WeatherDay, WeatherCondition
import time
import math
import random
from datetime import datetime
import csv



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
        self.Grandma = Grandma()
        self.Rock = Rock()
        self.total_score = 0

        self.play()

    def play(self):
        """Main game loop. handles each day and adds score to total_score"""

        for i in range(self.game_length):
            clear_screen()
            print(f"Day {i+1} of {self.game_length}")

            # get weather from weather engine -> csv
            weather = self.weather_engine.get_day()

            # Generate Instrument readings from real weather for next day
            calendar = self.Calendar.format(weather.date, weather.season)
            cricket = self.Cricket.predict(weather)
            eightball = self.EightBall.predict()
            jerry = self.Jerry.predict(weather)
            grandma = self.Grandma.predict(weather)
            rock = self.Rock.predict(weather)

            # show the player the instrument readings and ask for a prediction
            clear_screen()
            print(f"Day {i+1} of {self.game_length}")
            print("******************")
            print(f"Date: {calendar}")
            print(f"# of cricket chirps in the last minute: {cricket}")
            print(f"EightBall Reading: {eightball}")
            print(f"Jerry's Personal Opinion: {jerry}")
            print(f"Grandma's Text: {grandma}")
            print(f"Weather Rock: {rock}")

            temp_prediction = input_valid_float("What is your prediction for the temperature tomorrow? ")
            condition_prediction = input_valid_condition("What is your prediction for the weather condition tomorrow? (sunny/cloudy/rainy/stormy/snowy) ")
            # score prediction
            temp_score = max(0, 100 - abs(temp_prediction - weather.tempature))
            condition_score = 100 if condition_prediction == weather.condition else 0
            score = temp_score + condition_score
            self.total_score += score
            print(f"Your temperature prediction was off by {abs(temp_prediction - weather.tempature)} degrees, giving you a score of {temp_score} for the temperature prediction.")
            print(f"Your condition prediction was {'correct' if condition_prediction == weather.condition else 'incorrect'}, giving you a score of {condition_score} for the condition prediction.")
            print(f"Your total score for the day is {score}.")
            print(f"Your total score so far is {self.total_score}.")
            
            input("Press enter to continue to the next day...")
            
            
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
                # Skip empty rows and CSV headers.
                if not row or row[0].strip().lower() == "date":
                    continue

                # Skip malformed rows instead of crashing the whole game.
                if len(row) < 4:
                    continue

                day_date = datetime.fromisoformat(row[0].strip())
                season = row[1].strip()
                temp = float(row[2].strip())
                condition = row[3].strip().lower()
                weather_day = WeatherDay(
                    tempature=temp,
                    condition=WeatherCondition(condition),
                    date=day_date,
                    season=season,
                )

                self.weather_days.append(weather_day)
            return
        return
