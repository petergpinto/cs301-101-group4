#!/usr/bin/python2

import yfinance as yf
import pandas as pd
import datetime

tickers = ['AMC', 'AMD', 'BBBY', 'F', 'GME', 'NVDA', 'PLTR', 'PROG', 'TSLA', 'X']
today = datetime.datetime.today()
lastyear = today+datetime.timedelta(days=-365)

for ticker in tickers:
	t = yf.Ticker(ticker)
	historical = t.history(start=lastyear, end=today, interval='1d')
	historical.to_csv('/var/www/html/'+ticker+'historical.csv')
