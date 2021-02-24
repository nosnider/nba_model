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

    # loop through every row in table
    for row in table.find('tbody').find_all('tr'):
        df_cells = dict()

        # loop through each cell
        for cell in row.children:

            try:
                value = cell.get_text()
                key = cell.get_attribute_list('data-stat')[0]
            except AttributeError:
                continue

            df_cells[key] = value

        df_rows.append(df_cells)

    driver.quit()

    df = pd.DataFrame(df_rows)
    df = df[(df.date_game != 'Date')]
    return df


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
                value = cell.a.get_text()
                # add to dictionary as key value pair
                df_cells[key] = value

            # if not, we can simply take the contents of the cell
            else:
                key = cell.get_attribute_list('data-stat')[0]
                value = cell.get_text()
                df_cells[key] = value

        df_rows.append(df_cells)

    driver.quit()
    return pd.DataFrame(df_rows).dropna()


four_facts = get_four_factors()
schedule = get_schedule()