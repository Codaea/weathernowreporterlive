from weather_day import WeatherCondition

def ask_yes_no(prompt):
    """enforce yes or no response. 
    Yes is true, no is false"""
    while True:
        user_input = input(prompt+ " (y/n): ").lower().strip()[0]

        if user_input == 'y':
            return True
        elif user_input == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'. ")

def clear_screen():
    """Clears the terminal screen."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
def clamp(value: int, min_val:int, max_val:int) -> int:
    """Clamps Value between two numbers"""
    return max(min_val, min(value, max_val))

def input_valid_float(prompt: str) -> float:
    """Prompt until a valid float is entered, then return it."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def input_valid_condition(prompt:str ) -> WeatherCondition:
    while True:
        try:
            return WeatherCondition(input(prompt).lower().strip())
        except ValueError:
            print("Invalid input. Please enter a weather condition")