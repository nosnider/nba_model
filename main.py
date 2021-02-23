from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import math

def get_schedule():
    url = 'https://www.basketball-reference.com/leagues/NBA_2021_games-february.html'
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    html = driver.page_source
    table = BeautifulSoup(html, 'html.parser').find(id='schedule')

    df_rows = []
    for row in table.find('tbody').find_all('tr'):
        try:
            game = {'date': row.find('th', {'data-stat': 'date_game'}).a.contents[0],
                    'start_time': row.find('td', {'data-stat': 'game_start_time'}).contents[0],
                    'visiting_team': row.find('td', {'data-stat': 'visitor_team_name'}).a.contents[0],
                    'visiting_score': row.find('td', {'data-stat': 'visitor_pts'}).contents[0],
                    'home_team': row.find('td', {'data-stat': 'home_team_name'}).a.contents[0],
                    'home_score': row.find('td', {'data-stat': 'home_pts'}).contents[0]}
            df_rows.append(game)

        except IndexError:
            game = {'date': row.find('th', {'data-stat': 'date_game'}).a.contents[0],
                    'start_time': row.find('td', {'data-stat': 'game_start_time'}).contents[0],
                    'visiting_team': row.find('td', {'data-stat': 'visitor_team_name'}).a.contents[0],
                    'visiting_score': row.find('td', {'data-stat': 'visitor_pts'}).contents,
                    'home_team': row.find('td', {'data-stat': 'home_team_name'}).a.contents[0],
                    'home_score': row.find('td', {'data-stat': 'home_pts'}).contents}
            df_rows.append(game)

        except AttributeError:
            continue

    driver.quit()
    return pd.DataFrame(df_rows)


def get_four_factors():
    url = "https://www.basketball-reference.com/leagues/NBA_2021.html#misc::none"
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    html = driver.page_source
    table = BeautifulSoup(html, 'html.parser').find(id='div_misc_stats')

    df_rows = []
    # loop through each row in table
    for row in table.find('tbody').find_all('tr'):
        df_cells = dict()

        # loop through each cell in each row
        for cell in row.find_all('td'):

            # if the cell has a hyperlink (e.g. for team name), there is a child element we need to check
            if len(cell.findChildren()) != 0:
                # column name
                key = cell.get_attribute_list('data-stat')[0]
                # cell value
                value = cell.a.contents[0]
                # add to dictionary as key value pair
                df_cells[key] = value

            # if not, we can simply take the contents of the cell
            else:
                key = cell.get_attribute_list('data-stat')[0]
                value = cell.contents[0]
                df_cells[key] = value


        df_rows.append(df_cells)
    driver.quit()
    return pd.DataFrame(df_rows).dropna()


df = get_four_factors()
print('ehllo')
