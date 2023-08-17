# Project1_Team2
Project 1 repository for Team 2 - University of Pennsylvania Data Science Bootcamp

Code gets data and generates csv files: data.py
Jupyter Notebook with final presentation: present.ipynb
CSV files with data for individual stocks and EFTs: inside data folder

Bar charts were adapted from "Analyzing World Stock Indices Performances with Python"
https://towardsdatascience.com/analyzing-world-stock-indices-performance-in-python-610df6a578f

We had to access multiple years of data (2018-2023) for a variety of ETF’s. To do this we pulled data from yahoo finance and used a library (yfinance) that handles API calls directly, therefore we didn’t have to handle the API call. This call can be found in our data document within the notebook.
We made DataFrames to store and analyze the large data sets and then saved those to CSV files. We chose this library because it supplies clean data, therefore our cleaning process was minimal.  We used Pandas to read the CSV files back into the notebook which automatically converted most of the number data for us. However, the date column did not convert automatically and was pulled as string so we had to convert that as datetime. We used this data to build bar and line graphs to visualize our findings, which we will go into more detail about... (to Rajib)


List of companies (tickers) we used:
