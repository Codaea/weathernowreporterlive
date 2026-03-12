import pyfiglet
import blessed
from game import WeatherGame

term = blessed.Terminal()
# Render the figlet text for the heading bar
heading_bar = pyfiglet.figlet_format("WeatherNOW", font="slant")

# Display the heading bar at the top left
print(term.orangered(heading_bar))
print("A Game about the weather")

# start class that manages game
game = WeatherGame(weather_data_file="weather.csv")


