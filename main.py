"""
Analysis of Unemployment Rate in the United States
Authors: Divyaang Agarwal, Ankita Khiratkar
"""

import pandas as pd
import os
import numpy as np


def import_bls_excel(directory: str, file_name: str) -> pd.DataFrame:
    """
    The function reads data from given directory path and excel file name and converts it into a pandas Dataframe in the
    required format having Year and Month an index. This function gets called from the get_bls_data_merged function.
    :param directory: location of directory in which files are stored
    :param file_name: name of the file to read
    :return: dataframe of the requested excel sheet with index as Year and Month

    >>> import_bls_excel('./Data/BLS/Age/', '16-19 yrs.xlsx')   # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
                      16-19 yrs
    Year   Month
    1948.0 Jan          8.5
           Feb         10.0
           Mar         10.5
           Apr          9.5
           May          7.0
    ...                 ...
    2021.0 Aug         11.2
           Sep         11.5
           Oct         11.9
           Nov          NaN
           Dec          NaN
    <BLANKLINE>
    [888 rows x 1 columns]

    >>> import_bls_excel('./Data/BLS/Age/', '16-19 yrs')   # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    FileNotFoundError: [Errno 2] No such file or directory: './Data/BLS/Age/16-19 yrs'
    """
    # Loading the dataset from the specified directory path
    df = pd.read_excel(directory+file_name, dtype={'Year': 'Int16'}, skiprows=12)
    column = file_name.replace('.xlsx', '')
    # Creating a blank Data Frame with the required columns
    df_new = pd.DataFrame(columns=['Year', 'Month', column])
    # Extracting the column name from the existing data data frame
    colnames = list(df.columns)
    colnames.remove('Year')
    # Iterating through each row in the existing data frame
    for index in df.index:
        row = df.loc[index]
        # Iterating through each column value in the existing data frame
        # Adding them to the new data frame row wise
        for col in colnames:
            df_new.loc[len(df_new.index)] = [row['Year'], col, row[col]]
    return df_new.set_index(['Year', 'Month'])


def get_bls_data_merged(dir_path: str, df_merge: pd.DataFrame) -> pd.DataFrame:
    """
    This function merges the data from all the files in the given directory into one dataframe
    :param dir_path: path of the directory where the excel sheets are stored
    :param df_merge: base pandas dataframe to which all the files in the given directory are to be merged
    :return: dataframe containing the merged data from all the data files having index as Year and Month

    >>> get_bls_data_merged('./Data/BLS/Age/', get_bls_dummy([2020, 2021]))   # doctest: +NORMALIZE_WHITESPACE
                16-19 yrs  20 yrs. & over, Men  20 yrs. & over, Women
    Year Month
    2020 Jan         12.6                  3.1                    3.2
         Feb         11.5                  3.2                    3.1
         Mar         14.1                  4.1                    4.0
         Apr         32.1                 13.1                   15.5
         May         29.6                 11.6                   13.9
         Jun         22.6                 10.2                   11.3
         Jul         19.1                  9.4                   10.4
         Aug         16.4                  8.0                    8.3
         Sep         16.3                  7.3                    7.7
         Oct         14.0                  6.7                    6.5
         Nov         13.9                  6.6                    6.2
         Dec         16.0                  6.4                    6.3
    2021 Jan         14.8                  6.0                    6.0
         Feb         13.9                  6.0                    5.9
         Mar         13.0                  5.8                    5.7
         Apr         12.3                  6.1                    5.6
         May          9.6                  5.9                    5.4
         Jun          9.9                  5.9                    5.5
         Jul          9.6                  5.4                    5.0
         Aug         11.2                  5.1                    4.8
         Sep         11.5                  4.7                    4.2
         Oct         11.9                  4.3                    4.4
         Nov          NaN                  NaN                    NaN
         Dec          NaN                  NaN                    NaN

    >>> get_bls_data_merged('./Data/BLS/Ethnicity/', get_bls_dummy([1980, 2020])) # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
                Asian  Black or African American  Hispanic or Latino  White
    Year Month
    1980 Jan      NaN                       13.0                 8.7    5.5
         Feb      NaN                       12.9                 8.9    5.5
         Mar      NaN                       12.9                 9.2    5.6
         Apr      NaN                       13.8                10.4    6.1
         May      NaN                       14.4                10.1    6.6
    ...           ...                        ...                 ...    ...
    2020 Aug     10.6                       12.8                10.5    7.4
         Sep      8.8                       12.0                10.3    7.0
         Oct      7.6                       10.8                 8.8    6.0
         Nov      6.7                       10.3                 8.4    5.9
         Dec      5.9                        9.9                 9.3    6.0
    <BLANKLINE>
    [492 rows x 4 columns]


    >>> get_bls_data_merged('./Data/BLS/Ages', get_bls_dummy([2019, 2020])) # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    FileNotFoundError: [WinError 3] The system cannot find the path specified: './Data/BLS/Ages'
    """

    # Iterating through all the files present in the specified directory
    for name in os.listdir(dir_path):
        # Transforming each of the file to the required format
        new_df = import_bls_excel(directory=dir_path, file_name=name)
        # Merging all the files to a single data frame
        df_merge = pd.merge(df_merge, new_df, left_index=True, right_index=True, how='left')
    return df_merge


def get_bls_dummy(date_range: list) -> pd.DataFrame:
    """
    This function creates an empty dataframe which serves as the base to merge the data from all the files into one
    Dataframe. Some files do not have values for all the months. So the dataframe output from this function serves as a
    base for merging all the files into one.
    :param date_range: list containing start and end year
    :return: Empty dataframe with index as Year and Month

    >>> get_bls_dummy([2020, 2021])
    Empty DataFrame
    Columns: []
    Index: [(2020, Jan), (2020, Feb), (2020, Mar), (2020, Apr), (2020, May), (2020, Jun), (2020, Jul), (2020, Aug), (2020, Sep), (2020, Oct), (2020, Nov), (2020, Dec), (2021, Jan), (2021, Feb), (2021, Mar), (2021, Apr), (2021, May), (2021, Jun), (2021, Jul), (2021, Aug), (2021, Sep), (2021, Oct), (2021, Nov), (2021, Dec)]

    >>> get_bls_dummy([2021, 2021])
    Empty DataFrame
    Columns: []
    Index: [(2021, Jan), (2021, Feb), (2021, Mar), (2021, Apr), (2021, May), (2021, Jun), (2021, Jul), (2021, Aug), (2021, Sep), (2021, Oct), (2021, Nov), (2021, Dec)]

    >>> get_bls_dummy([2023, 2022])
    Empty DataFrame
    Columns: []
    Index: []
    """
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df_def = []
    # Iterating through each year between the given start and end year
    for i in range(date_range[0], date_range[1]+1):
        # Pairing each year with all the months
        for m in months:
            df_def.append([i, m])
    # Creating a new dataframe and setting Year and month as the index
    df_def = pd.DataFrame(data=df_def, columns=['Year', 'Month'])
    df_def.set_index(['Year', 'Month'], inplace=True)
    return df_def


def process_unemployment_underemployed(sheet_name: str) -> pd.DataFrame:
    """
    This function reads the specified sheet from the specified excel file and returns a dataframe with Date
    as the index
    :param sheet_name: name of the required sheet in the input excel file
    :return: dataframe containing the required columns  Date as the index

    >>> process_unemployment_underemployed('ch1_unemployment')    # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
                Recent graduates  College graduates
    Date
    1990-01-01             3.381              2.270
    1990-02-01             3.039              2.206
    1990-03-01             3.136              2.165
    1990-04-01             3.565              2.186
    1990-05-01             3.861              2.198
    ...                      ...                ...
    2021-05-01             6.093              3.603
    2021-06-01             6.089              3.522
    2021-07-01             6.077              3.316
    2021-08-01             5.765              3.144
    2021-09-01             5.433              2.915
    <BLANKLINE>
    [381 rows x 2 columns]

    >>> process_unemployment_underemployed('ch1_unemployed')    # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    ValueError: Worksheet named 'ch1_unemployed' not found
    """
    # Reading the specified sheet from the specified excel file
    df_unemp_underemp = pd.read_excel('./Data/unemployed_vs_underemployed/labor-market-for-recent-college-grads.xlsx',
                                  sheet_name=sheet_name,
                                  usecols=['Date', 'Recent graduates', 'College graduates'], skiprows=13, skipfooter=2)
    df_unemp_underemp.set_index('Date', inplace=True)
    return df_unemp_underemp


def get_job_loss_gain_df(path: str) -> pd.DataFrame:
    """
    This function reads the data from the specified csv file and calculates the percentage change in job losses/gains
    on the quarterly basis for all the states.
    :param path: path of the csv file from which data is to be read
    :return: dataframe containing data read from the csv file with State as index and columns containing the calculated
    percentage changes in job losses/gains

    >>> get_job_loss_gain_df(path='./Data/BLS state job gains and losses/Gross_job_losses.csv')    # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
                          Mar 2019  Mar 2020  ...  % Change Q1 19-20  % Change Q1 20-21
    State                                     ...
    Alabama                  89711     96778  ...           7.877518          -4.826510
    Alaska                   22374     24694  ...          10.369179         -12.278286
    ...
    Wisconsin               122749    134817  ...           9.831445         -16.664812
    Wyoming                  16697     20365  ...          21.968018         -18.605451
    <BLANKLINE>
    [51 rows x 5 columns]

    >>> get_job_loss_gain_df(path='./Data/BLS state job gains and losses/Gross_job.csv')    # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    FileNotFoundError: [Errno 2] No such file or directory: './Data/BLS state job gains and losses/Gross_job.csv'
    """
    # Reading the csv file to a dataframe
    df_jobs = pd.read_csv(path, index_col='State', usecols=['State', 'Mar 2019', 'Mar 2020', 'Mar 2021'])
    # Iterating through each column in the data frame
    for col in df_jobs.columns:
        # Removing the commas from the number and changing their data type to int
        df_jobs[col] = df_jobs[col].str.replace(',', '').astype(int)
    # Calculating the percentage change in job losses/gains
    df_jobs['% Change Q1 19-20'] = ((df_jobs['Mar 2020'] - df_jobs['Mar 2019'])/df_jobs['Mar 2019']) * 100
    df_jobs['% Change Q1 20-21'] = ((df_jobs['Mar 2021'] - df_jobs['Mar 2020'])/df_jobs['Mar 2020']) * 100
    return df_jobs


def get_gdp_unemployment_df(path_gdp: str, path_unemp: str) -> pd.DataFrame:
    """
    This functions reads and merges data sets for GDP and Unemployment and returns a dataframe with Year as the index
    :param path_gdp: path of the excel file to be read for GDP data
    :param path_unemp: path of the csv file to be read for unemployment data
    :return: dataframe containing merged data sets of GDP and unemployment with Year as index and all the required columns

    >>> get_gdp_unemployment_df('./Data/GDP and Unemployment/GDP.xls', './Data/GDP and Unemployment/Unemployment.csv')  # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
             GDP(Trillion $)  ... % Unemployed Total Youth (Ages 15-24)
    Year                  ...
    1991        6.158129  ...                                13.336
    ...
    2016       18.745076  ...                                10.337
    <BLANKLINE>
    [26 rows x 7 columns]

    >>> get_gdp_unemployment_df('./Data/GDP and Unemployment/GDP.xls', './Data/GDP and Unemployment/Unemployed.csv')    # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
    ...
    FileNotFoundError: [Errno 2] No such file or directory: './Data/GDP and Unemployment/Unemployed.csv'
    """
    # Reading the GDP data from the given path
    df_gdp = pd.read_excel(path_gdp, skiprows=3, index_col='Country Name')
    # Extracting the rows for United States and transposing the dataframe
    df_gdp = df_gdp[df_gdp.index == 'United States'].transpose().iloc[3:]
    df_gdp.index.names = ['Year']
    # Setting the columns name of the dataframe
    df_gdp.columns = ['GDP(Trillion $)']
    # Changing the unit of the GDP to trillion dollars
    df_gdp['GDP(Trillion $)'] = df_gdp['GDP(Trillion $)'] / (10 ** 12)

    # Reading the unemployment data from the given path
    df_unemployment = pd.read_csv(path_unemp)
    # Transposing the dataframe
    df_unemployment = df_unemployment.transpose().iloc[2:, :6]
    # Setting the columns name of the dataframe
    df_unemployment.columns = df_unemployment.iloc[0]
    df_unemployment = df_unemployment.iloc[3:, ]
    df_unemployment.columns = ['% Unemployed Female',
                               '% Unemployed Male',
                               '% Unemployed Total',
                               '% Unemployed Female Youth (Ages 15-24)',
                               '% Unemployed Male Youth (Ages 15-24)',
                               '% Unemployed Total Youth (Ages 15-24)']
    # Setting the index of the dataframe
    df_unemployment.index.names = ['Year']
    # Changing the index values to the required format
    df_unemployment.index = df_unemployment.index.str.split('[').str[0].str.strip()

    # Merging the GDP and the unemployment data
    df_merge = pd.merge(df_gdp,
                        df_unemployment,
                        left_index=True,
                        right_index=True,
                        how='inner')
    return df_merge


def get_party_colour(party_list: list) -> list:
    """
    This function returns a list of the color corresponding to the input political party list
    :param party_list: list of the political parties in the data set
    :return: a list of colours corresponding to the input political party list

    >>> df_umemp = import_bls_excel(directory='./Data/Political Party and Unemployment/', file_name='Unemployment Rate.xlsx')
    >>> df_umemp = df_umemp.groupby('Year')['Unemployment Rate'].mean().round(2)

    >>> df_president = pd.read_csv('./Data/Political Party and Unemployment/US presidents.csv', dtype={'Years (after inauguration)':'Int16'}, names=['Year', 'President', 'Party'], index_col='Year', skiprows=1)

    >>> df_president_unemp = pd.merge(df_umemp, df_president, left_index=True, right_index=True, how='inner')

    >>> get_party_colour(df_president_unemp['Party'])     # doctest: +ELLIPSIS
    ['Green', 'Green', 'Green', ... 'Blue', 'Blue', 'Blue', 'Blue']
    """
    colour_list = []
    # Iterating through the all the input political parties list
    for party in party_list:
        # Assigning colours according to the political party
        if party == 'Republican':
            colour_list.append('Blue')
        elif party == 'Democrat':
            colour_list.append('Green')
        else:
            colour_list.append('Red')
    return colour_list


def get_state_region_pop_df(path_1: str, path_2: str) -> pd.DataFrame:
    """
    This function reads the data files for state population and regions and merges them into one dataframe with State
    as index
    :param path_1: path of the population file to be read
    :param path_2: path of the region file to be read
    :return: dataframe having merged data of the population and region files with State as index

    >>> get_state_region_pop_df('./Data/State Population/statewise population.csv', './Data/State Population/state_region_division.csv')    # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
                                  2010      2011  ...     Region            Division
    State                                     ...
    Alaska                  713982    722349  ...       West             Pacific
    Alabama                4785514   4799642  ...      South  East South Central
    ...
    West Virginia          1854265   1856606  ...      South      South Atlantic
    Wyoming                 564531    567491  ...       West            Mountain
    <BLANKLINE>
    [51 rows x 13 columns]

    >>> get_state_region_pop_df('./Data/State Population/statewise populate.csv', './Data/State Population/state_region_divi.csv')  # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
    ...
    FileNotFoundError: [Errno 2] No such file or directory: './Data/State Population/statewise populate.csv'
    """
    # Reading the state population data
    df_state_pop = pd.read_csv(path_1,
                              usecols=['NAME', 'POPESTIMATE2010', 'POPESTIMATE2011',
                                       'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014',
                                       'POPESTIMATE2015', 'POPESTIMATE2016', 'POPESTIMATE2017',
                                       'POPESTIMATE2018', 'POPESTIMATE2019', 'POPESTIMATE2020'])
    df_state_pop.columns = ['State', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
    # df_region_pop = df_state_pop.loc[:4]
    df_state_pop = df_state_pop.loc[5:]
    df_state_pop.set_index('State', inplace=True)

    # Reading the State region data
    df_state_reg = pd.read_csv(path_2,
                              index_col='State',
                              usecols=['State', 'Region', 'Division'])

    # Return the merged state unemployment and region dataframe
    return pd.merge(df_state_pop, df_state_reg, left_index=True, right_index=True, how='right')


def invert_state_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    The input dataframe contains a seperate column for population for each year, this function create a new dataframe
    containing population for all the years into a single column
    :param df: dataframe containing State, Region, Division, and population for all the years
    :return: dataframe containing population for all the years into a single column

    >>> df_state_region = get_state_region_pop_df('./Data/State Population/statewise population.csv', './Data/State Population/state_region_division.csv')
    >>> invert_state_df(df_state_region)    # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
               State Region  Division  Year  Population
    0     Alaska   West   Pacific  2010      713982
    1     Alaska   West   Pacific  2011      722349
    ...
    559  Wyoming   West  Mountain  2019      580116
    560  Wyoming   West  Mountain  2020      582328
    <BLANKLINE>
    [561 rows x 5 columns]
    """
    # Creating a new dataframe with columns as per the requirements
    df_state_inv = pd.DataFrame(columns=['State', 'Region', 'Division', 'Year', 'Population'])
    # Iterating through all the rows in the input dataframe
    for i in df.index:
        current_row = df.loc[i]
        # Iterating through all the required years
        for y in ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']:
            # Adding the state population data to the new dataframe row wise
            df_state_inv.loc[len(df_state_inv.index)] = [i, current_row['Region'], current_row['Division'], y, current_row[y]]
    df_state_inv = df_state_inv.astype({"Year": int, "Population": int})
    return df_state_inv


def correct_rate_values(x: str) -> float:
    """
    This function takes a string value and converts it into an appropriate float value
    :param x: string
    :return: string converted into float value

    >>> correct_rate_values('9.7')
    9.7

    >>> correct_rate_values('-')
    nan
    """
    # Checking if the input value is of float data type
    if not isinstance(x, float):
        x = x.strip()
        if x == '-':
            x = np.nan
        else:
            x = float(x)
    return x


def get_state_umemp_df(path: str) -> pd.DataFrame:  # Can be made faster using Numba
    """
    The input data set has unemployment rate of all months for all years as sepearte columns for every state.
    This function reads the data from the specified csv file and transforms the unemployment rate into a single column
    :param path: path of the csv file containing the state unemployment data
    :return: dataframe containing statewise unemployment data

    >>> get_state_umemp_df(path='./Data/Unemployment Rates for States/state_unemployment_11_21.csv')    # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
                    State       Date  Rate  Year
    0         Alabama 2011-10-01   9.2  2011
    1         Alabama 2011-11-01   8.9  2011
    ...
    6290  Puerto Rico 2021-09-01   8.3  2021
    6291  Puerto Rico 2021-10-01   8.0  2021
    <BLANKLINE>
    [6290 rows x 4 columns]

    >>> get_state_umemp_df(path='./Data/Unemployment Rates for States/state_unemployment_11.csv')    # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    FileNotFoundError: [Errno 2] No such file or directory: './Data/Unemployment Rates for States/state_unemployment_11.csv'
    """
    df_state_emp = pd.read_csv(path, index_col='State')
    # Creating a new dataframe with columns as per requirements
    df_state_emp_inv = pd.DataFrame(columns=['State', 'Date', 'Rate'])
    # Iterating through each row in the input dataframe
    for i in df_state_emp.index:
        current_row = df_state_emp.loc[i]
        # Iterating through each column in the input dataframe
        for d in list(df_state_emp.columns):
            # Adding the state unemployment data to the new dataframe row wise
            df_state_emp_inv.loc[len(df_state_emp_inv.index)] = [i, d, current_row[d]]

    # Extracting the Year from the Date column
    df_state_emp_inv['Date'] = pd.to_datetime(df_state_emp_inv['Date'])
    df_state_emp_inv['Year'] = df_state_emp_inv['Date'].dt.year
    # Correcting the unemployment rate values
    df_state_emp_inv['Rate'] = df_state_emp_inv['Rate'].apply(correct_rate_values)
    df_state_emp_inv.dropna(inplace=True)

    return df_state_emp_inv
