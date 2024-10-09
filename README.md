# Socioeconomic Determinants of Life Expectancy: A Global Analysis

This project investigates the relationships between life expectancy and key socioeconomic factors, such as GDP per capita, education levels, BMI, alcohol consumption, and population size across countries and regions. By analyzing global data from 2000 to 2015, the project aims to understand how economic, health, and educational factors impact life expectancy and to provide insights for public health policies.

## Table of Contents

- [Introduction](#introduction)
- [Data Sources](#data-sources)
- [Methodology](#methodology)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Limitations](#limitations)
- [Contributors](#contributors)
- [License](#license)

## Introduction

Life expectancy is a critical indicator of population health and well-being. This project explores the complex relationships between life expectancy and several key socioeconomic factors using a global dataset. By applying statistical techniques like correlation analysis, hypothesis testing, and regression modeling, we aim to provide insights into the factors that contribute most to life expectancy variations across countries.

## Data Sources

The dataset used in this project includes life expectancy data from multiple years (2000-2015) and various regions around the world. It also contains socioeconomic factors such as:

- **Life Expectancy**: [WHO Life Expectancy Data](https://www.who.int/data/gho/data/indicators/indicator-details/GHO/life-expectancy-at-birth-(years))
- **Alcohol Consumption**: [WHO Alcohol Consumption Data](https://www.who.int/data/gho/data/indicators/indicator-details/GHO/alcohol-recorded-per-capita-(15-)-consumption-(in-litres-of-pure-alcohol))
- **BMI**: [NCD Risk Factor Collaboration BMI Data](https://www.ncdrisc.org/data-downloads-adiposity.html)
- **GDP per capita**: [World Bank GDP Data](https://data.worldbank.org/indicator/NY.GDP.PCAP.CD?most_recent_year_desc=true)
- **Population**: [World Bank Population Data](https://data.worldbank.org/indicator/SP.POP.TOTL?most_recent_year_desc=true)
- **Years of Schooling**: [Our World in Data Schooling Data](https://ourworldindata.org/grapher/mean-years-of-schooling-long-run)

## Methodology

The project uses statistical methods to explore the relationships between life expectancy and other socioeconomic variables:

1. **Correlation Analysis**: Measures the strength and direction of associations between variables.
2. **Statistical Hypothesis Testing**: Independent two-sample t-tests and Mann-Whitney U tests are used to assess significant differences.
3. **Regression Modeling**: Ordinary Least Squares (OLS) regression is applied to understand how key factors (GDP, education, BMI, etc.) predict life expectancy.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/AdamZlr/Statistical-Theory.git
    ```
2. Install the required dependencies using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

### Dependencies

- `numpy`
- `pandas`
- `matplotlib`
- `scipy`
- `statsmodels`
- `seaborn`
- `scikit-learn`

Ensure that these packages are installed by using the `requirements.txt` file.

## Usage

Once the repository is cloned and dependencies installed, you can run the analysis by running all cells in the notebook in order.
