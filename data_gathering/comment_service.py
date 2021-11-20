#!/usr/bin/python3

import praw
import hashlib
import os
import sys
import subprocess
import re
import mysql.connector
import nltk

#Non working client secrets
reddit = praw.Reddit(client_id='',
    client_secret='',
    user_agent=''
)

mydb = mysql.connector.connect(host='localhost', user='mentions', password='StockMentions123!', database="cs301data")

#Load ticker into set
#Load company names into set
symbols = set()
companyNames = dict()

#A csv file with company names, we use these to attempt to assign a ticker to a comment, even if it is not explicitly mentioned
import csv
with open("relevant_ticker_data.csv") as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			pass
		else:
			symbols.add(row[0].strip())
			companyNames[row[0]] = row[1].lower()
		line_count += 1

#Don't attempt to match common words to ticker symbols
exclude_words = []
with open("exclude_words") as fp:
	lines = fp.readlines()
	for line in lines:
		exclude_words.append(line.strip())

def checkWord(word):
	symbol = word
	if symbol in symbols:
		return {symbol.upper():1}
	word = word.lower()
	relations = {}	
	for sym in companyNames.keys():
		if word in companyNames[sym]:
			relations[sym] = (len(word)/len(companyNames[sym]))
	return relations

cursor = mydb.cursor()

#We can't check all subreddits, but we can look at new comments being posted in specific ones
subs = ""
with open("subreddit_list") as fp:
	lines = fp.readlines()
	for line in lines:
		subs += line.strip()
		subs += "+"
subs = subs[:-1]

from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

while True:
	try:
		for comment in reddit.subreddit(subs).stream.comments():
			words = nltk.word_tokenize( ''.join(BeautifulSoup(comment.body_html).findAll(text=True)) ) 
			sentiment = sid.polarity_scores(comment.body)
			relations = {}
			for word in words:
				rels = checkWord(word.strip())
				if len(rels) > 0 and len(rels) < 10:
					relations.update(rels)
			if (len(relations) > 0):
				for symbol in relations.keys():
					try:
						sqlquery = "INSERT INTO ticker_mentions (ticker, strength, author, timestamp, sentiment, permalink, domain) values ('%s', '%s', '%s', FROM_UNIXTIME('%s'), '%s', '%s', 'reddit.com')"
						val = (symbol.upper(), relations[symbol], str(comment.author), comment.created_utc, sentiment['compound'], comment.permalink)
						cursor.execute(sqlquery % val)
					except Exception as e:
						print('non-unique ', e)	
						
			
			print(comment.created_utc, comment.author, sid.polarity_scores(comment.body))
			mydb.commit()
	except KeyboardInterrupt:
		print("Keyboard Interupt")
		exit()
	else:
		print("Connection Error")

