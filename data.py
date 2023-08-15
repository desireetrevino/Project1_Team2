import pandas as pd
import yfinance as yf
import dates

# symbols
symbols = {}
# hospitality
symbols["hospitality"] = "HST HLT MAR CHH H"
# telecom
symbols["telecom"] = "DTEGY VOD GTMEF TMUS T VZ"
# transportation
symbols["transportation"] = "AAL JBLU UNP JBHT MOTO"
# f&b
symbols["foodbev"] = "bmboy bud ko gis adm"

symbols["healthcare"] = "unh sny pfe mrna wba pfe"

symbols["banking"] = ""

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
#stocks_hist.to_csv('data/stocks.csv', index=False)


## ETFs

etf_tickers = "FTXN FTXH FTXO FTXG FTXL FTXR"