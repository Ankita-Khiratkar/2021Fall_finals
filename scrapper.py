import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrape_table(i, path):
    """

    :param path:
    :param i:
    :return:
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


def scrape_state_unemp(res_path):
    """

    :param res_path:
    :return:
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
