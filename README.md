# Summary
Simple script to predict NBA spreads based on [Four Factors applied by murrayyyyy](https://docs.google.com/document/d/1mN4zhW5-i2GAzL56dSfrTR8bSRFEDIXfZZdyJpeQ0lc/edit).

Statistics and schedules are scraped from www.basketballreference.com and www.nba.com respectively

# Installation
- Download from source
- Run ```$ pip install -r requirements.txt``` in root directory
- Run ```$ python main.py```

# Interpreting Output
The script will output all games for today's date and their predicted spreads. Negative values indicate an advantage to the home team, while positive values indicate an advantage to the away team. This is a bit different than traditional spreads where negative values indicate an advantage to the Vegas favorite.
