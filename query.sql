SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));
select ticker, timestamp,  avg(sentiment), FLOOR(UNIX_TIMESTAMP(timestamp)/(10*60)) as timekey from ticker_mentions where ticker="GME" group by timekey;
