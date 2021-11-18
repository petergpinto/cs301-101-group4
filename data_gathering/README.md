## comment_service.py

This python script runs continuously to fetch and analyze new comments that are posted on reddit.  After the sentiments are analyzed and scores produced, the data is inserted into a local MySQL database which can be queried at a later time

## comment_service.service

A systemd service file that manages comment_service.py

Running the python script in this way makes sure that the script stays alive and running even in the case of errors (network connectivity, rate limiting)

## crontab.txt

This file documents the crontab that runs on the data gathering server.  The MySQL server is queried every 5 minutes for new sentiment values which are output to /var/ww/html for distribution via HTTP.  This allows for the python learning notebooks to always fetch the newest data easily

## getHistoricalPrices.py

This python script downloads historical data from Yahoo Finance using the yfinance python library.  It runs once every day at midnight outputs daily quote information in csv format

# mysql_table.sql

The description of the table that holds the data in the MySQL database