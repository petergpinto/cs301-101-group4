SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));
select ticker, timestamp,  avg(sentiment) from ticker_mentions where ticker="TSLA" group by UNIX_TIMESTAMP(timestamp) DIV 600;
