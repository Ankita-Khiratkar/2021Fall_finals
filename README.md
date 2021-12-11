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
        <li><a href="#hypothesis-1">Hypothesis 1: Unemployment Rate - Age</a></li>
        <li><a href="#hypothesis-2">Hypothesis 2: Unemployment Rate - Race</a></li>
        <li><a href="#hypothesis-3">Hypothesis 3: Unemployment Rate - Education Level</a></li>
        <li><a href="#hypothesis-4">Hypothesis 4: Unemployment Rate - Duration</a></li>
        <li><a href="#hypothesis-5">Hypothesis 5: Unemployed vs Underemployed</a></li>
        <li><a href="#hypothesis-6">Hypothesis 6: Percent Change in Job Losses and Job Gains during the Covid-19 pandemic</a></li>
        <li><a href="#hypothesis-7">Hypothesis 7: Relation between GDP and Unemployment Rate</a></li>
        <li><a href="#hypothesis-8">Hypothesis 8: Relation between President's Political Party and Unemployment Rate</a></li>
        <li><a href="#hypothesis-9">Hypothesis 9: Relation between Population and the Unemployment Rate</a></li>
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


### Hypothesis 1: Unemployment Rate - Age
>Null Hypothesis: Unemployment rate in the United States is independent of Age
>
>Alternative Hypothesis: Unemployment rate in the United States is NOT independent of Age

<img alt="Unemployment Rate in the United States - Age" src="./images/Unemployment Rate in the United States - Age.png" title="Unemployment Rate in the United States - Age"/>

<strong>Observation:</strong><br>
- From the above plot, we observe that the unemployment rate is inversely proportional to the age group. Higher the age group, lower is the unemployment rate.

- Unemployment rate is highest for the age group 16 to 24 years followed by 25 to 34 years, then 35 to 44 years, then 45 to 54 years, followed by 55 to 64 years, and lastly 65 years and above.

- Therefore, we conclude that unemployment rate is not independent of age and reject the null hypothesis.
 
<strong>Analyzing Unemployment Rate in the United States with respect to Age during the Great Recession and the Covid-19 pandemic</strong><br>

<img alt="Analyzing Unemployment Rate in the United States with respect to Age during the Great Recession and the Covid-19 pandemic" src="./images/CvsR_Unemployment Rate in the United States - Age.png" title="Analyzing Unemployment Rate in the United States with respect to Age during the Great Recession and the Covid-19 pandemic"/>
<strong>Observation:</strong><br>

- The unemployment rate increased for all age groups during the Great Recession period (December 2007 – June 2009).

- Due to the Great Recesion, age group 25 to 34 years, 35 to 44 years, and 45 to 54 years seems to be more affected as compared to other age groups.

- The unemployment rate for all age groups reached their all time high after the Covid-19 outbreak in early 2020.

- The effect of the Great Recession was more dominant as compared to the effect of the Covid-19 pandemic on the unemployment rate. As we notice that for all age groups, the unemployment rate took a much longer time to come down after the Great Recession as compared to the Covid-19 pandemic.


### Hypothesis 2: Unemployment Rate - Race
>Null Hypothesis: Unemployment rate in the United States is independent of Race
>
>Alternative Hypothesis: Unemployment rate in the United States is NOT independent of Race

<img alt="Unemployment Rate in the United States - Race" src="./images/Unemployment Rate in the United States - Race.png" title="Unemployment Rate in the United States - Race"/>

<strong>Observation:</strong><br>
- Ideally, the umployment rate should be independent of race but from the plot above we infer that the unemployment rate is always highest for Black/Africans Americans and lowest for Asian people. This trend is consistent throughout the timeline- the unemployment rate is highest for Black Americans followed by Hispanic or Latino then White and then Asians.

- Therefore, we can say that unemployemt rate is not independent of race and we reject the null hypothesis.

<strong>Analyzing Unemployment Rate in the United States with respect to Race during the Great Recession and the Covid-19 pandemic</strong><br>

<img alt="Analyzing Unemployment Rate in the United States with respect to Race during the Great Recession and the Covid-19 pandemic" src="./images/CvsR_Unemployment Rate in the United States - Race.png" title="Analyzing Unemployment Rate in the United States with respect to Race during the Great Recession and the Covid-19 pandemic"/>
<strong>Observation:</strong><br>

- The umployment rate increased for all Races during the Great Recession (December 2007 – June 2009).

- The umployment rate for all Races reached their all time high after the Covid-19 outbreak in early 2020.

- We observed that for all Races, the unemployment rate took a much longer time to come down after the Great Recession as compared to the Covid-19 pandemic.



### Hypothesis 3: Unemployment Rate - Education Level
>Null Hypothesis: Unemployment rate in the United States is independent of Education Level
>
>Alternative Hypothesis: Unemployment rate in the United States is NOT independent of Education Level

<img alt="Unemployment Rate in the United States - Education Level" src="./images/Unemployment Rate in the United States - Education Level.png" title="Unemployment Rate in the United States - Education Level"/>

<strong>Observation:</strong><br>
- From the plot above, we infer that the unemployment rate is inversely related to the education level. Unemployment rate is lower for people having the higher level of education.

- The trend of unemployment rate with respect to education level is consistent throughout the timeline- the unemployment rate is highest for people having less than a high school degree or diploma followed by high school graduates (no college) followed by some college or associate degree and lastly, bachelor's degree and higher.

- Thus, we conclude that unemployment rate is dependent on education level and we reject the null hypothesis.

<strong>Analyzing Unemployment Rate in the United States with respect to Education Level during the Great Recession and the Covid-19 pandemic</strong><br>

<img alt="Analyzing Unemployment Rate in the United States with respect to Education Level during the Great Recession and the Covid-19 pandemic" src="./images/CvsR_Unemployment Rate in the United States - Education Level.png" title="Analyzing Unemployment Rate in the United States with respect to Education Level during the Great Recession and the Covid-19 pandemic"/>
<strong>Observation:</strong><br>

- The uemployment rate increased for all Education Levels during the Great Recession (December 2007 – June 2009).

- The unemployment rate for all Education Level groups reached their all time high after the Covid-19 outbreak in early 2020.

- During both, the Great Recession and the Covid-19 pandemic, the rise in unemployment rate for people having less than a high school diploma was higher as compared to other categories.

- The effect of the Covid-19 pandemic on the unemployment rate was more severe as compared to the Great Recession. But, the unemployment rate took a much longer time to come down after the Great Recession as compared to the Covid-19 pandemic.

### Hypothesis 4: Unemployment Rate - Duration
>Null Hypothesis: Duration for which people are unemployed is independent of time
>
>Alternative Hypothesis: Duration for which people are unemployed is NOT independent of time

<img alt="Unemployment in the United States - Duration" src="./images/Unemployment in the United States - Duration.png" title="Unemployment in the United States - Duration"/>

<strong>Observation:</strong><br>
- From the plot above we can clearly see that duartion for which people are unemployed is dependent on time. Thus we reject the null hypothesis.

<strong>Analyzing the duration for which people are unemployed in the United States during the Great Recession and the Covid-19 pandemic</strong><br>

<img alt="Analyzing the duration for which people are unemployed in the United States during the Great Recession and the Covid-19 pandemic" src="./images/CvsR_Unemployment in the United States - Duration.png" title="Analyzing the duration for which people are unemployed in the United States during the Great Recession and the Covid-19 pandemic"/>
<strong>Observation:</strong><br>

- We observe that, after the Great Recession, most of the people were unemployed for 15 weeks and over.

- During the Covid-19 pandemic, the number of people were mostly unemployed for 5 to 14 weeks was much higher than the number of people unemployed for 15 weeks and over.

- The duration for which people were unemployed was less during the Covid-19 pandemic but the number of people affected was higher during the Covid-19 pandemic as compared to the Great Recession.

### Hypothesis 5: Unemployed vs Underemployed
>Null Hypothesis: Graduates in the United States prefer to be underemployed rather than staying unemployed
>
>Alternative Hypothesis: Graduates in the United States prefer to be unemployed rather than being underemployed

<img alt="Unemployement and Underemployment rate in the United States" src="./images/Unemployement and Underemployment rate in the United States.png" title="Unemployement and Underemployment rate in the United States"/>

<strong>Observation:</strong><br>
- From the plot, the rate of unemployment and underemployment for recent graduates is always high as compared to others. 

- If we compare the unemployment rate and underemployment rate for graduates, we can say that graduates in the United States prefer to be underemployed rather than stay unemployed. Hence, we can accept the null hypothesis.

### Hypothesis 6: Percent Change in Job Losses and Job Gains during the Covid-19 pandemic
>Null Hypothesis: Percent change in Job Losses and Job Gain is independent of state
>
>Alternative Hypothesis: Percent change in Job Losses and Job Gain is NOT independent of state

Note: For this analysis we have taken data for the first quarter of 2019, 2020 and 2021 for all the states in the United States.

<img alt="Percent change in job losses" src="./images/Percent change in job losses.png" title="Percent change in job losses"/>
<img alt="Percent change in job gains" src="./images/Percent change in job gains.png" title="Percent change in job gains"/>

<strong>Observation:</strong><br>
- From the plots above, we can clearly infer that both the job losses and job gains are dependent on state. For example, percent change in job losses is very large for Washington and very small for Mississippi. Similiarly, the percent change for job gains is very large for Minnesota and very small for Tennessee.

- Thus, we can conclude that Percent change in Job Losses and Job Gain is dependent on state and reject the null hypothesis.

- Also, we notice that there was a decline in percent change for job gain (or increase in percent change for job losses) for the duration March 2019 - March 2020 for almost all the states in the United States due to the Covid-19 pandemic outbreak. In the period March 2020 - March 2021, we see that almost all the states showed increase in the number of jobs i.e. increase in the percent change for job gain (or decline in percent change for job losses).

### Hypothesis 7: Relation between GDP and Unemployment Rate
>Null Hypothesis: There is NO relationship between Gross Domestic Product (GDP) and Unemployment Rate
>
>Alternative Hypothesis: There is relationship between Gross Domestic Product (GDP) and Unemployment Rate

<img alt="GDP and Unemployment Rate in the United States" src="./images/GDP and Unemployment Rate in the United States.png" title="GDP and Unemployment Rate in the United States"/>

<strong>Observation:</strong><br>

- From the above plot, we observe that the unemployment rate is inversely related to the GDP. Notice, whenever the GDP increases and the unemployment rate decreases.

- Around 2003 and during the Great Recession in 2008, there was a slight decrease in the GDP of United States and during both the times we notice that the unemployment rate increases.

- Thus, we conclude that there is a relationship between the Gross Domestic Product (GDP) and the Unemployment Rate, and we reject the null hypothesis.

### Hypothesis 8: Relation between President's Political Party and Unemployment Rate
>Null Hypothesis: There is NO relationship between President's Political Party and the Unemployment Rate
>
>Alternative Hypothesis: There is relationship between President's Political Party and the Unemployment Rate

<img alt="President's Political Party and the Unemployment Rate" src="./images/President's Political Party and the Unemployment Rate.png" title="President's Political Party and the Unemployment Rate"/>
In the above plot, Blue colour represents the Republican Party and Green colour represents the Democratic Party

<strong>Observation:</strong><br>

- Though there are many factors that contribute to the Unemployment rate in the country, from the above plot we notice that most of the times when Democratic Party's President was in power, the unemployment rate reduced. But, there are also some instances when the unemployment rate increased under Democratic Party like in the year 1961, 1980, and 2009.

- While in the rule of Republican party, we observe that the unemployment rate trend is random.

- Thus, we can say that there is no relationship between the President's Political Party and the Unemployment Rate in the United States and we accept the null hypothesis.

### Hypothesis 9: Relation between Population and the Unemployment Rate
>Null Hypothesis: There is NO relationship between the population and the Unemployment Rate
>
>Alternative Hypothesis: There is relationship between the population and the Unemployment Rate

<img alt="Unemployment rate and population regionwise" src="./images/Unemployment rate and population in the Midwest States.png" title="Unemployment rate and population regionwise"/>
<img alt="Unemployment rate and population regionwise" src="./images/Unemployment rate and population in the Northeast States.png" title="Unemployment rate and population regionwise"/>
<img alt="Unemployment rate and population regionwise" src="./images/Unemployment rate and population in the South States.png" title="Unemployment rate and population regionwise"/>
<img alt="Unemployment rate and population regionwise" src="./images/Unemployment rate and population in the West States.png" title="Unemployment rate and population regionwise"/>

<strong>Observation:</strong><br>

- The barplot above represents the mean of the unemployment rates of all states in a region and sum of the population (x10^7) for all the states in that region. 

- From the barplot above we notice that in Midwest and Northeast region there is not much significant change in population over the years (2011-2020) while for South and West region there is a notable increase in population in these years. But we notice that for all the regions the unemployment rate decreases from 2011 to 2019. Thus, we conclude that there is no significant relation between the population and the unemployment rate and thus, we accept the null hypothesis.

- In 2020, due to the Covid-19 pandemic there is a rise in the unemployment rate for all the regions in the United States.

<strong>Analyzing the Unemployment Rate in the States of United States - Regionwise from 2011 to 2020</strong><br>

<img alt="Boxplot for Unemployment Rate in the States of United States - Regionwise" src="./images/Boxplot for Unemployment Rate in the States of United States - Regionwise.png" title="Boxplot for Unemployment Rate in the States of United States - Regionwise"/>
<strong>Observation:</strong><br>

- In each boxplot above, each data point is the unemployment rate for a state in a particular region for a particular year. For example, the data points for the orange boxplot in the South region would be the unemployment rates for the states in the south region for the year 2012.

- We can clearly infer from the above plot that for all the regions the boxplot shifts downwards, i.e. the unemployment rate decreases from 2011 to 2019, in 2020 we se a huge surge in the unemployment rate due to the outbreak of the Covid-19 pandemic.

- Unemployment rate increased the maximum for states in the Northeast region and minimum for states in Midwest due to the Covid-19 pandemic.

## Data Sources
* https://data.bls.gov/PDQWeb/ln
* https://www.bls.gov/opub/ted/2021/job-gains-and-losses-by-state-from-march-2019-to-march-2021.htm
* https://data.worldbank.org/indicator/NY.GDP.MKTP.CD?end=2020&locations=US&start=1960&view=chart
* https://databank.worldbank.org/source/world-development-indicators%23
* https://www.theguardian.com/news/datablog/2012/oct/15/us-presidents-listed#data
* https://github.com/cphalpert/census-regions/blob/master/us%20census%20bureau%20regions%20and%20divisions.csv
* https://www.census.gov/programs-surveys/popest/technical-documentation/research/evaluation-estimates/2020-evaluation-estimates/2010s-state-total.html
* https://www.newyorkfed.org/research/college-labor-market/index.html#/overview
* https://www.bls.gov/charts/state-employment-and-unemployment/state-unemployment-rates-animated.htm

## Contribution
