import random
from typing import List
from datetime import date, datetime
from game import WeatherDay
# File that handles weather instruments

class Calendar:
    def format(self, date: date, season: str):
        """Formats the date and season into string representations that can be used for predictions."""
        return f"{date.strftime('%B %d, %Y')} - {season}"

class EightBall:
    def __init__(self):
        """The eightball instrument is just a random phrase. There is no influence from anything."""
        self.responses = [
            "It is certain",
            "It is decidedly so",
            "Without a doubt",
            "Yes definitely",
            "You may rely on it",
            "As I see it, yes",
            "Most likely",
            "Outlook good",
            "Yes",
            "Signs point to yes",
            "Reply hazy try again",
            "Ask again later",
            "Better not tell you now",
            "Cannot predict now",
            "Concentrate and ask again",
            "Don't count on it",
            "My reply is no",
            "My sources say no",
            "Outlook not so good",
            "Very doubtful"
        ] # List pulled from https://magic-8ball.com/magic-8-ball-answers/
        return

    def predict(self) -> str:
        """Generate the random reading of the eight ball. returns 1 of 20 random pre-written responses"""
        index = random.randint(0, len(self.responses)-1)
        if index < 10:
            # leaning positive
            pass
        elif index < 15:
            # leaning neutral
            pass
        else:
            # leaning negative
            pass

        return self.responses[index]

class Cricket:
    def __init__(self, days_inacurate: List[int]):
        """Initializes cricket with a list of days that it will be off by a large amount. Monday is zero, sunday is 6"""
        self.days_inacurate = days_inacurate
        return
    
    def predict(self, weather_day: WeatherDay) -> int:
        temp = weather_day.tempature

        if weather_day.date.weekday() in self.days_inacurate:
            # if is inacurate, calculate cricket with a random tempature
            temp = random.randint(-10, 110)

        # Formula https://en.wikipedia.org/wiki/Dolbear%27s_law
        # Temp = 50 + ((N - 40) / 4) where N is the number of chirps in the past minute
        # Solving for n gives  Temp+50*4 + 40 = N where N is the number of chirps in the past minute

        num_chirps = (temp + 50)*4 + 40

        # TODO: would it be fun to rearrange this into dots so they have to count?
        
        return int(num_chirps) # temp caussed float math, round off to be a int.
        # crickets can't chirp a fraction of time
        

class Jerry:
    pass

class Rock:
    """Predicts the previous day's weather. On the inital start, there is no previous day. in this case, weather stone shows as no weather"""
    def __init__(self):
        self.previous_weather_day: WeatherDay|None = None
        return

    def predict(self, weather_day: WeatherDay) -> str:
        """Predicts the weather for the next day. If there is no previous day, it predicts that there is a rock."""
    
        if self.previous_weather_day == None:
            prediction = "There is a rock"

        elif self.previous_weather_day.condition == "sunny":
            prediction = "The rock is warm"
        elif self.previous_weather_day.condition == "cloudy":
            prediction = "The rock does not cast a shadow"
        elif self.previous_weather_day.condition == "rainy":
            prediction = "The rock is wet"
        elif self.previous_weather_day.condition == "stormy":
            prediction = "The rock is very wet"
        elif self.previous_weather_day.condition == "snowy":
            prediction = "The rock is white"
        else:
            prediction = "The rock is confused" # we shouldn't be able to get here

        # Set current day to previous, for next prediction

        return prediction