import pandas as pd

schedule = pd.read_pickle("./schedule.pkl")
four_factors = pd.read_pickle("./four_factors.pkl")

todays_games = schedule.loc[schedule['date_game'] == '2021-02-24']
game = todays_games.iloc[8]
home_four_factors = four_factors[four_factors['team_name'] == game['visitor_team_name']]
away_four_factors = four_factors[four_factors['team_name'] == game['home_team_name']]
matchup = away_four_factors.append(home_four_factors)
matchup['factor1'] = (matchup['efg_pct'] - matchup['opp_efg_pct']) * 100
matchup['factor2'] = (matchup['opp_tov_pct'] - matchup['tov_pct'])
matchup['factor3'] = (matchup['orb_pct'] - (100 - matchup['drb_pct']))
matchup['factor4'] = (matchup['ft_rate'] - matchup['opp_ft_rate'])
matchup = matchup[['factor1', 'factor2', 'factor3', 'factor4']]
matchup.diff(axis=0).loc[1]
#matchup.loc['spread'] = matchup.loc
pass