import sqlite3

con = sqlite3.connect('predictions.db')
cur = con.cursor()
cur.execute('''CREATE TABLE predictions (game_id text, date text, home_team text, away_team text, factor_1 real, 
factor_2 real, factor_3 real, factor_4 real, line real)''')
con.commit()
con.close()
