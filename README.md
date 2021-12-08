# Analysis of Unemployment Rate in the United States

Authors: Ankita Khiratkar (aak13), Divyaang Agarwal (dagarw5)

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#description">Description</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#analysis">Analysis</a>
      <ul>
        <li><a href="#hypothesis-1">Hypothesis 1</a></li>
        <li><a href="#hypothesis-2">Hypothesis 2</a></li>
        <li><a href="#hypothesis-3">Hypothesis 3</a></li>
        <li><a href="#hypothesis-4">Hypothesis 4</a></li>
        <li><a href="#hypothesis-5">Hypothesis 5</a></li>
        <li><a href="#hypothesis-6">Hypothesis 6</a></li>
        <li><a href="#hypothesis-7">Hypothesis 7</a></li>
        <li><a href="#hypothesis-8">Hypothesis 8</a></li>
        <li><a href="#hypothesis-9">Hypothesis 9</a></li>
      </ul>
    </li>
    <li><a href="#data-sources">Data Sources</a></li>
  </ol>
</details>

## Description

## Getting Started

### Prerequisites

### Installation
1. Open the command terminal in the required folder and clone the repository using command
``` 
git clone https://github.com/Ankita-Khiratkar/2021Fall_finals.git
```
OR<br>
Download the zip folder from the browser using this link
```
https://github.com/Ankita-Khiratkar/2021Fall_finals/archive/refs/heads/main.zip
```
2. Open and run file Final_Project.ipynb in Jupyter Notebook

## Analysis


### Hypothesis 1
>Null Hypothesis: Unemployment rate in the United States is independent of Age
>
>Alternative Hypothesis: Unemployment rate in the United States is NOT independent of Age

<img alt="Unemployment Rate in the United States - Age" src="./images/Unemployment Rate in the United States - Age.png" title="Unemployment Rate in the United States - Age"/>

<strong>Observation:</strong><br>
- From the above plot, we observe that the unemployment rate is inversely proportional to the age group. Higher the age group, lower is the unemployment rate.

- Unemployment rate is highest for the age group 16 to 24 years followed by 25 to 34 years, then 35 to 44 years, then 45 to 54 years, followed by 55 to 64 years, and lastly 65 years and above.

- Therefore, we conclude that unemployment rate is not independent of age and reject the null hypothesis.

### Hypothesis 2
>Null Hypothesis: Unemployment rate in the United States is independent of Race
>
>Alternative Hypothesis: Unemployment rate in the United States is NOT independent of Race

<img alt="Unemployment Rate in the United States - Race" src="./images/Unemployment Rate in the United States - Race.png" title="Unemployment Rate in the United States - Race"/>

<strong>Observation:</strong><br>
- Ideally, the umployment rate should be independent of race but from the plot above we infer that the unemployment rate is always highest for Black/Africans Americans and lowest for Asian people. This trend is consistent throughout the timeline- the unemployment rate is highest for Black Americans followed by Hispanic or Latino then White and then Asians.

- Therefore, we can say that unemployemt rate is not independent of race and we reject the null hypothesis.


### Hypothesis 3
>Null Hypothesis: Unemployment rate in the United States is independent of Education Level
>
>Alternative Hypothesis: Unemployment rate in the United States is NOT independent of Education Level

<img alt="Unemployment Rate in the United States - Education Level" src="./images/Unemployment Rate in the United States - Education Level.png" title="Unemployment Rate in the United States - Education Level"/>

<strong>Observation:</strong><br>
- From the plot above, we infer that the unemployment rate is inversely related to the education level. Unemployment rate is lower for people having the higher level of education.

- The trend of unemployment rate with respect to education level is consistent throughout the timeline- the unemployment rate is highest for people having less than a high school degree or diploma followed by high school graduates (no college) followed by some college or associate degree and lastly, bachelor's degree and higher.

- Thus, we conclude that unemployment rate is dependent on education level and we reject the null hypothesis.

### Hypothesis 4
>Null Hypothesis: Duration for which people are unemployed is independent of time
>
>Alternative Hypothesis: Duration for which people are unemployed is NOT independent of time

<img alt="Unemployment in the United States - Duration" src="./images/Unemployment in the United States - Duration.png" title="Unemployment in the United States - Duration"/>

<strong>Observation:</strong><br>
- From the plot above we can clearly see that duartion for which people are unemployed is dependent on time. Thus we reject the null hypothesis.

### Hypothesis 5

### Hypothesis 6

### Hypothesis 7

### Hypothesis 8

### Hypothesis 9

## Data Sources
1. https://data.bls.gov/PDQWeb/ln
2. https://www.bls.gov/opub/ted/2021/job-gains-and-losses-by-state-from-march-2019-to-march-2021.htm
3. https://data.worldbank.org/indicator/NY.GDP.MKTP.CD?end=2020&locations=US&start=1960&view=chart
4. https://databank.worldbank.org/source/world-development-indicators%23
5. https://www.theguardian.com/news/datablog/2012/oct/15/us-presidents-listed#data
6. https://github.com/cphalpert/census-regions/blob/master/us%20census%20bureau%20regions%20and%20divisions.csv
7. https://www.census.gov/programs-surveys/popest/technical-documentation/research/evaluation-estimates/2020-evaluation-estimates/2010s-state-total.html
8. https://www.newyorkfed.org/research/college-labor-market/index.html#/overview
9. https://www.bls.gov/charts/state-employment-and-unemployment/state-unemployment-rates-animated.htm



