import pandas as pd

schedule = pd.read_pickle("./schedule.pkl")
four_factors = pd.read_pickle("./four_factors.pkl")

todays_games = schedule.loc[schedule['date_game'] == '2021-02-24']
game = todays_games.iloc[8]
home_four_factors = four_factors[four_factors['team_name'] == game['visitor_team_name']]
away_four_factors = four_factors[four_factors['team_name'] == game['home_team_name']]
matchup = home_four_factors.append(away_four_factors)

matchup['factor1'] = (matchup['efg_pct'] - matchup['opp_efg_pct']) * 100
matchup['factor2'] = (matchup['opp_tov_pct'] - matchup['tov_pct'])
pass
