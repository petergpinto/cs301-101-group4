Skeleton file for project report

Title, Author(s)

Abstract: Briefly describe your problem, approach, and key results. Should be no more than 300 words.

Introduction (10%): Describe the problem you are working on, why it’s important, and an overview of your results

Related Work (10%): Discuss published work that relates to your project. How is your approach similar or different from others?

Data (10%): Describe the data you are working with for your project. What type of data is it? Where did it come from? How much data are you working with? Did you have to do any preprocessing, filtering, or other special treatment to use this data in your project?

The data in this project was collected using a program to scrape comments posted on Reddit.  The code collecting the data is running 24/7 on a cloud service, so the amount of data (and quality of predicitons) is always increasing.  At the time of writing, we have collected about 20 days worth of sentiment data.  

The source code for the data collection service is located [Here](https://github.com/petergpinto/cs301-101-group4/blob/master/data_gathering/comment_service.py).  To summarize the code briefly, it first loads several dictionaries in to memory containing information on tickers to attempt to match and common words to exclude from the matching process.  It then continually scans the subreddits listed [here](https://github.com/petergpinto/cs301-101-group4/blob/master/data_gathering/comment_service_resources/subreddit_list) for new comments.  Once it finds a new comment, it extracts the text body and tokenizes it using the NLTK python library.  Then sentiment scores are obtained using the VADER lexicon.  We then check each word in the comment to see if it is a ticker, if it is we will associate the sentiment score with that ticker.  Multiple tickers per comment are allowed.  The sentiment-ticker associations are then inserted into a local MySQL database along with some comment metadata for future reference.

Later, the sentiment values from each ticker are averaged in 10 minute windows and extracted from the database [shown here](https://github.com/petergpinto/cs301-101-group4/blob/master/queries/GMEquery.sql) resulting in the following:


<p align="center">
  <img src="https://github.com/petergpinto/cs301-101-group4/blob/master/graphs/GME/sentiment_forecast.png?raw=true" />
</p>

This graph is for the ticker "GME" similar graphs for 9 other tickers can be found in the [graphs folder](https://github.com/petergpinto/cs301-101-group4/tree/master/graphs) in this repository

Additionally, we also collect daily price data for each ticker used at a nightly interval.  That data is sourced from Yahoo Finance using the yfinance python library.  The code for this is shown [here](https://github.com/petergpinto/cs301-101-group4/blob/master/data_gathering/getHistoricalPrices.py)

Methods (30%): Discuss your approach for solving the problems that you set up in the introduction. Why is your approach the right thing to do? Did you consider alternative approaches? You should demonstrate that you have applied ideas and skills built up during the quarter to tackling your problem of choice. It may be helpful to include figures, diagrams, or tables to describe your method or compare it with other methods.

Two different models were produced to attempt to predict future prices.  The first model uses Facebook Prophet, which takes time-series data and attempts to extract trends and roll them forward to predict future values.  The second model is a neural network.  


Initially when implementing the neural network, we attempted to use a very large deep network. However, T=there was a major problem with this approach. The the amount of data we have is not yet large enough to train a model with a large number of parameters.  The model simply memorized the data points using its large number of parameters and lost any potential predictive power.  Therefore we significantly reduced the size of the model such that memorizing the data would not be possible.  We also made heavy use of regularization to help prevent the weights from becoming too large.  To tune the size of the network, we saved a single validation data point and slowly decreased the size of the network until the model was able to predict the unseen data point with a relatively small margin of error.  The final architecture of the neural network has two hidden layers, the first with 16 neurons and the second with 8 neurons

Experiments (30%): Discuss the experiments that you performed to demonstrate that your approach solves the problem. The exact experiments will vary depending on the project, but you might compare with previously published methods, perform an ablation study to determine the impact of various components of your system, experiment with different hyperparameters or architectural choices, use visualization techniques to gain insight into how your model works, discuss common failure modes of your model, etc. You should include graphs, tables, or other figures to illustrate your experimental results.

Conclusion (5%) Summarize your key results - what have you learned? Suggest ideas for future extensions or new applications of your ideas.
