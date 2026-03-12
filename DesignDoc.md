# Design Doc (DO NOT READ IF YOU ARE PLAYING, LOGIC IS DETAILED!!)

A game where the player has to use their intuition to guess the weather for the following day.

## Pillars

**Intuition** - The players are using not statistics and graphs to predict the weather, but rather medival instruments, and luck

## Main Mechanics

The game is TUI based, being turn taken.

### Gameplay Loop

Player is presented with current conditions, via a variety of "weather instruments". From this data, they must attempt to make an accurate predection of the weather for the following day. Points are awarded for "closeness" to the actual weather event.

### Weather Instruments

- Calendar (What season it is, [spring winter summer fall]), 7 Day seasons, 28 day years.
- Cricket Counter - Keeping track of tempature [Based on Dolbears Law](https://en.wikipedia.org/wiki/Dolbear%27s_law)
- Grandma's Knee - Low Barometric before storms reduce fluid pressure in joints.
- Magic 8 Ball - [Magic 8 Ball Answers](https://magic-8ball.com/magic-8-ball-answers/)
- Jerrys Opinion - 15 Percent Accurate On Even days of the game
- Rock - Keeps track of previous days weather

---- Keep/Cut Line ----

- Psychic
- Groundhog - Does Phil see his shadow?
- Not So Magic Dice (D20)

### Logic Paths

We generate a true weather object for the day, and then create the instruments readings. The readings are a "Window" into the actual weather outside.

#### Classes + Patterns

WeatherGame handles the cycle of generating a weatherEngine at the begninning and moving everything after it. It generates instrument readings to the user, who then interacts with it. They respond in the Forcast object, and are then scored by the Forcast class based on accuracy.

It handles everything game related, so a ssh version can be made with leaderboards and etc.

Weatherday class/object handles individual thing. WeatherEngine keeps track of all previous days, and handles generating to the season. WeatherEngine has support to generate a report of all days, and

Each Instrument is a Class, where it has a read method for the WeatherDay object and returns a noisy signal for the month. 

### Forcast Components

- Tempature
- Conditions (Sunny, Cloudy, Rainy, Snowy)

#### Scoring



## Visual Style/Audio

Its A Terminal based game, so theres not that much to do. I'm thinking possibly ASCII art for mini cards for each day, if time permits.

## Story

You are the child of your prodigal father, a master weatherman. He recently arrested for weatherfraud and has been placed on administrative leave. You must step up to the job, and carry on (the better parts) of your fathers legacy. 

The Weatherstation is fresh out of money, after the last volcano destroyed the previous HiTech TM Weather station, so you must make do with shitty instruments


## Timeline

Done by sunday.
