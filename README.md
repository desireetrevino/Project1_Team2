# Project1_Team2
Project 1 repository for Team 2 - University of Pennsylvania Data Science Bootcamp
Team members: Crystal Lucas, Desiree Trevino, Jacob Field, Rajib Maji, Theresa Bravo, Vishnu Pillai

Code that gets data and generates csv files: data.py
Jupyter Notebook with final presentation: present.ipynb
CSV files with data for individual stocks and EFTs: inside data folder

Bar charts were adapted from "Analyzing World Stock Indices Performances with Python"
https://towardsdatascience.com/analyzing-world-stock-indices-performance-in-python-610df6a578f

List of companies and ETFs (tickers) we used:

ETFs:
* FTXL - First Trust Nasdaq Semiconductor ETF
* FTXR - First Trust Nasdaq Transportation ETF
* FTXH - First Trust Nasdaq Pharmaceuticals ETF
* FTXO - First Trust Nasdaq Bank ETF
* FTXN - First Trust Nasdaq Oil & Gas ETF
* FTXG - First Trust Nasdaq Food & Beverage ETF

Banking:
* WFC - Wells Fargo & Company
* HSBC - HSBC Holdings plc
* SAN - Banco Santander S.A.
* JPM - JPMorgan Chase & Co.
* C - Citigroup Inc.
  
Hospitality:
* HST - Host Hotels & Resorts Inc.
* HLT - Hilton Worldwide Holdings Inc.
* MAR - Marriot International Inc.
* CHH - Choice Hotels International Inc.
* H - Hyatt Hotels Corporation
  
Telecom:
* DTEGY - Deutsche Telekom AG
* VOD - Vodafone Group Public Limited Company
* GTMEF - Globe Telecom Inc.
* TMUS - T-Mobile US, Inc.
* T - AT&T Inc.
* VZ - Verizon Communications Inc.
  
Transportation:
* AAL - American Airlines Group Inc.
* JBLU - JetBlue Airways Corporation
* UNP - Union Pacific Corporation
* JBHT - J.B. Hunt Transport Services Inc.
* MOTO - SmartETFs Smart Transportation & Technology ETF
  
Food and Beverage:
* BMBOY - Grupo Bimbo, S.A.B. de C.V.
* BUD - Anheuser-Busch InVeb SA/NB
* KO - The Coca-Cola Company
* GIS - General Mills, Inc.
* ADM - Archer-Daniels-Midland Company
  
Healthcare:
* UNH - UnitedHealth Group Incorporated
* SNY - Sanofi
* PFE - Pfizer Inc.
* MRNA - Moderna, Inc.
* WBA - Walgreens Boots Alliance, Inc.

We had to access multiple years of data (2018-2023) for a variety of ETF’s. To do this we pulled data from yahoo finance and used a library (yfinance) that handles API calls directly, therefore we didn’t have to handle the API call. This call can be found in our data document within the notebook. We made DataFrames to store and analyze the large data sets and then saved those to CSV files. We chose this library because it supplies clean data, therefore our cleaning process was minimal. We used Pandas to read the CSV files back into the notebook which automatically converted most of the number data for us. However, the date column did not convert automatically and was pulled as string so we had to convert that as datetime. We used this data to build bar and line graphs to visualize our findings, which we will go into more detail about... (to Rajib)
