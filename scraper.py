"""
Analysis of Unemployment Rate in the United States
Authors: Divyaang Agarwal, Ankita Khiratkar
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import os


def scrape_table(i: int, path: str):
    """
    This function scrapes data from the below mentioned website and store them in the folder with specified file name
    as input
    :param i: table number specified on the website; used to scrape the particular table
    0: job gains table; 1: job losses table
    :param path: name of the csv file where scraped data is stored
    :return: None

    >>> scrape_table(0, './ScraperDoctestFiles/job_gains.csv')
    >>> if 'job_gains.csv' in os.listdir('./ScraperDoctestFiles/'): print('data scraped successfully')
    data scraped successfully

    >>> scrape_table(1, './ScraperDoctestFiles/job_losses.csv')
    >>> if 'job_losses.csv' in os.listdir('./ScraperDoctestFiles/'): print('data scraped successfully')
    data scraped successfully
    """
    response = requests.get(
        'https://www.bls.gov/opub/ted/2021/job-gains-and-losses-by-state-from-march-2019-to-march-2021.htm')
    html_text = response.text
    data = BeautifulSoup(html_text, 'html.parser')

    tables = data.find_all(class_='article-table')
    table_data = []

    for row in tables[i].find_all('tr'):
        row_list = []
        for value in row.stripped_strings:
            row_list.append(value)
        table_data.append(row_list)

    df = pd.DataFrame(data=table_data[1:],
                      columns=table_data[0])
    df.set_index('State', inplace=True)
    df.dropna(how='all', inplace=True)
    df.to_csv(path)


def scrape_state_unemp(res_path: str):
    """
    This function scrapes data from the below mentioned website and store them in the folder with specified file name
    as input
    :param res_path: name of the csv file where scraped data is stored
    :return: None
    >>> scrape_state_unemp('./ScraperDoctestFiles/state_unemployment_11_21.csv')
    >>> if 'state_unemployment_11_21.csv' in os.listdir('./ScraperDoctestFiles/'): print('data scraped successfully')
    data scraped successfully
    """
    response = requests.get(
        'https://www.bls.gov/charts/state-employment-and-unemployment/state-unemployment-rates-animated.htm')
    html_text = response.text
    data = BeautifulSoup(html_text, 'html.parser')

    table = data.find(id='lau_rc_unmapanim')
    table_data = []
    for row in table.find_all('tr'):
        row_list = []
        for value in row.stripped_strings:
            row_list.append(value)
        table_data.append(row_list)
    df = pd.DataFrame(data=table_data[1:],
                      columns=table_data[0])
    df.set_index('State', inplace=True)
    df.to_csv(res_path)
