import pandas as pd

schedule = pd.read_pickle("./schedule.pkl")
four_factors = pd.read_pickle("./four_factors.pkl")

todays_games = schedule.loc[schedule['date_game'] == '2021-02-28']
game = todays_games.iloc[7]
away_four_factors = four_factors[four_factors['team_name'] == game['visitor_team_name']]
home_four_factors = four_factors[four_factors['team_name'] == game['home_team_name']]
matchup = away_four_factors.append(home_four_factors)
matchup.index = ('away', 'home')
matchup['factor1'] = (matchup['efg_pct'] - matchup['opp_efg_pct']) * 100
matchup['factor2'] = (matchup['tov_pct'] - matchup['opp_tov_pct'])
matchup['factor3'] = (matchup['orb_pct'] - (100 - matchup['drb_pct']))
matchup['factor4'] = (matchup['ft_rate'] - matchup['opp_ft_rate'])
matchup = matchup[['factor1', 'factor2', 'factor3', 'factor4']]
# TODO: investigate spread calculation
spread = matchup.iloc[1] - matchup.iloc[0]
line = (spread.factor1 * .40) + (spread.factor2 * .25) + (spread.factor3 * .20) + (spread.factor4 * .15)
line = line * 2
# matchup.loc['spread'] = matchup.loc
pass
