CREATE TABLE IF NOT EXISTS `ticker_mentions` (
	ticker varchar(10),
	strength real,
	author varchar(100),
	timestamp datetime,
	PRIMARY KEY (ticker,timestamp,author)
	);

