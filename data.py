import pandas as pd
import yfinance as yf
import dates

## Stocks

# symbols
symbols = {}
symbols["hospitality"] = "HST HLT MAR CHH H"
symbols["telecom"] = "DTEGY VOD GTMEF TMUS T VZ"
symbols["transportation"] = "AAL JBLU UNP JBHT MOTO"
symbols["foodbev"] = "bmboy bud ko gis adm"
symbols["healthcare"] = "unh sny pfe mrna wba"
symbols["banking"] = "WFC HSBC SAN JPM C"

# Create filler df
stocks_hist = pd.DataFrame({"Stock": []})

# put ticker call together
for key, value in symbols.items():
    stocks = yf.Tickers(value)

    # loop stocks
    for ticker in stocks.tickers:
        df = stocks.tickers[ticker].history(start=dates.set_start,
                                            end=dates.set_end,
                                            period=dates.set_period)
        df["Stock"] = ticker
        df["Sector"] = key
        df = df.reset_index()

        stocks_hist = pd.merge(stocks_hist,
                               df,
                               how='outer')

print(stocks_hist.head())

# Export Stock Data to CSV
stocks_hist.to_csv('data/stocks.csv', index=False)


## ETFs

# symbols
etf_tickers = "FTXN FTXH FTXO FTXG FTXL FTXR"

# Create filler df
etf_hist = pd.DataFrame({"ETF": []})

# call Yahoo Finance
etfs = yf.Tickers(etf_tickers)

# loop etfs
for ticker in etfs.tickers:
    df = etfs.tickers[ticker].history(start=dates.set_start,
                                        end=dates.set_end,
                                        period=dates.set_period)
    df["ETF"] = ticker
    df = df.reset_index()

    etf_hist = pd.merge(etf_hist,
                        df,
                        how='outer')

print(etf_hist.head())
    
# Export ETF Data to CSV
etf_hist.to_csv('data/etf.csv', index=False)