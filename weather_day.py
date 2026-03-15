from __future__ import annotations

from datetime import datetime
from enum import Enum


class WeatherCondition(Enum):
    SUNNY = "sunny"
    CLOUDY = "cloudy"
    RAINY = "rainy"
    STORMY = "stormy"
    SNOWY = "snowy"


# Abstracted object to avoid circular import issues
class WeatherDay:
    def __init__(self, tempature: float, condition: WeatherCondition, date: datetime, season: str):
        self.tempature = tempature
        self.condition = condition
        self.date = date
        self.season = season

    def __str__(self):
        return f"Temperature: {self.tempature}, Condition: {self.condition.value}"