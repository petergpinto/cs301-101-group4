select ticker,count(ticker) from ticker_mentions where strength=1 and ticker not in (select ticker from exclude) group by ticker order by count(ticker) desc limit 10;
