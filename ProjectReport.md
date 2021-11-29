<h1 align="center">
Stock Market Estimation Using Social Media Sentiment, Peter Pinto & Darius Karoon
</h1>

<h3 align='center'>
<a href='https://mediaspace.njit.edu/media/Kaltura+Capture+recording+-+November+28th+2021%2C+8A00A44+pm/1_lk6g88qa'>Video Presentation</a>
</h3>

<h2 align="center">
  Abstract
</h2>
  
We were tasked with creating a price predictor that establishes a connection between social media posts and furture stock prices. The implementation of the predictor involved the use of the Deep Neural Networks and Facebook Prophet models. The tickers used to test this model were AMC, AMD, BBBY, F, GME, NVDA, PLTR, PROG, TSLA, X. The measure of accuracy is whether or not the model correctly predicts the rise or fall of the price of a certain stock. Most of the results from the days, 11/18/21 through 11/22/21, not only had numbers that were in close proximity to the closing price, but also had numbers that indicated the correct direction predicted by the model.

<h2 align="center">
Introduction
</h2>

As more people invest themselves in the stock market due to the continuous rise of the internet, there is also an increasing demand for accurate forsight into future stock prices. Currently, there is competition between dozens of companies who try to advertise their success of their stock prediction software. However, the ability to get good predictions on prices is extremely difficult because the future is unpredictable, which makes the public distrustful of majority of their software. Since stock prices are heavily affected by human emotion, it also plays a huge role in the judgement of future stock prices. Therefore the most efficient way to analyze emotion in association with the stock market is to analyze posts on social media. For instance, Reddit is an immensely popular platform where people from all over the world discuss about any topic; and there is a major community on the platform that focuses on stocks and trading. 

With that being said, one of the most recent forms of stock prediction is known as machine learning. In this project, two of the many methods of machine learning used to analyze comments of subreddits are Deep Neural Networks and Facebook Prophet. The sentiment analysis DNN allows the predictor's performance The most popular stock predictors are those with As mentioned previously, the main indicator of accuracy is the model's ability to predict whether or not a specific stock's price rises or falls. Furthermore Based on the tests, it seems as though the higher the stock price, the more difficult to predict correctly. For instance, the highest stock, TSLA, with an average price of $1,130.10 over the course of three days, had more inaccurate results than smaller stocks like PROG with an average price of $4.55. 

<h2 align="center">
Related Work
</h2>

The following are some other projects that attempt to predict stock prices using machine learning:

https://towardsdatascience.com/is-it-possible-to-predict-stock-prices-with-a-neural-network-d750af3de50b

https://www.datacamp.com/community/tutorials/lstm-python-stock-market

https://www.hindawi.com/journals/complexity/2020/6622927/

https://scholar.google.com/scholar?q=stock+prediction+machine+learning&hl=en&as_sdt=0&as_vis=1&oi=scholart

The key difference between these projects and ours is the use of social media sentiment scores as an additional input to the machine learning models.  This additional data allows for more meaningful predictions in theory.

<h2 align="center">
Data
</h2>

The data in this project was collected using a program to scrape comments posted on Reddit.  The code collecting the data is running 24/7 on a cloud service, so the amount of data (and quality of predicitons) is always increasing.  At the time of writing, we have collected about 20 days worth of sentiment data.  

The source code for the data collection service is located [Here](https://github.com/petergpinto/cs301-101-group4/blob/master/data_gathering/comment_service.py).  To summarize the code briefly, it first loads several dictionaries in to memory containing information on tickers to attempt to match and common words to exclude from the matching process.  It then continually scans the subreddits listed [here](https://github.com/petergpinto/cs301-101-group4/blob/master/data_gathering/comment_service_resources/subreddit_list) for new comments.  Once it finds a new comment, it extracts the text body and tokenizes it using the NLTK python library.  Then sentiment scores are obtained using the VADER lexicon.  We then check each word in the comment to see if it is a ticker, if it is we will associate the sentiment score with that ticker.  Multiple tickers per comment are allowed.  The sentiment-ticker associations are then inserted into a local MySQL database along with some comment metadata for future reference.

Later, the sentiment values from each ticker are averaged in 10 minute windows and extracted from the database [shown here](https://github.com/petergpinto/cs301-101-group4/blob/master/queries/GMEquery.sql) resulting in the following:


<p align="center">
  <img src="https://github.com/petergpinto/cs301-101-group4/blob/master/graphs/GME/sentiment_forecast.png?raw=true" />
</p>

This graph is for the ticker "GME" similar graphs for 9 other tickers can be found in the [graphs folder](https://github.com/petergpinto/cs301-101-group4/tree/master/graphs) in this repository

Additionally, we also collect daily price data for each ticker used at a nightly interval.  That data is sourced from Yahoo Finance using the yfinance python library.  The code for this is shown [here](https://github.com/petergpinto/cs301-101-group4/blob/master/data_gathering/getHistoricalPrices.py)

<h2 align="center">
Methods
</h2>

Two different models were produced to attempt to predict future prices.  The first model uses Facebook Prophet, which takes time-series data and attempts to extract trends and roll them forward to predict future values.  The second model is a neural network.  

The approach with Facebook Prophet involved two parts.  First, we build a model of sentiments and have the model predict sentiments for the future.  Second, we extract the sentiment outputs of the first model and add them as an additional regressor to a model attempting to predict prices.  We built the model in this way because the primary data that we are collecting is the sentiment data.

Initially when implementing the neural network, we attempted to use a very large deep network. However, there was a major problem with this approach. The amount of data we have is not yet large enough to train a model with a large number of parameters.  The model simply memorized the data points using its large number of parameters and lost any potential predictive power. Therefore we significantly reduced the size of the model such that memorizing the data would not be possible.  We also made heavy use of regularization to help prevent the weights from becoming too large.  To tune the size of the network, we saved a single validation data point and slowly decreased the size of the network until the model was able to predict the unseen data point with a relatively small margin of error.  The final architecture of the neural network has two densely connected hidden layers, the first with 16 neurons and the second with 8 neurons.

<h2 align="center">
Experiments
</h2>

For each of the ten tickers, the stock neural network code is manually run ten times. This is a three to five minute process per ticker, so in order to properly test this, we had to leave plenty of time for testing before the market opened at 9:30am EST. Once the number was obtained, the number goes into the results table awaiting the comparison of the closing price at 4:00pm EST. Once the neural network was tested, the Facebook Prophet code was run once per ticker at an average time of three to five minutes per ticker. This process would provide the confidence interval for future values of each ticker.

<h3 align="center">
  Neural Network Experiments
</h3>

The code for the Neural Network experiments can be found [here](https://github.com/petergpinto/cs301-101-group4/blob/master/notebooks/Stock_neural_network.ipynb)

These are the experimental results for the Neural Network model.  They were generated by running the code before 9:30am (market open time) and produced a predicted close value for that day.  A prediciton is considered successful here if the predicted price movement is in the same direction as the true price movement

<p align="center">
  <img src="https://github.com/petergpinto/cs301-101-group4/blob/master/graphs/predictions.png?raw=true" />
</p>

There were many successful predictions to come out of this model, as well as some unsuccessful ones.  Overall, this model was better than 50/50 at predicting the direction of price movement

<h3 align="center">
  Facebook Prophet Experiments
</h3>

The code for the Facebook Prophet experiments can be found [here](https://github.com/petergpinto/cs301-101-group4/blob/master/notebooks/Stocks_Facebook_Prophet.ipynb)

The following data is for the ticker "GME"

<p align="center">
  <img src="https://github.com/petergpinto/cs301-101-group4/blob/master/graphs/GME/forecast.png?raw=true" />
</p>

<p align="center">
  <img src="https://github.com/petergpinto/cs301-101-group4/blob/master/graphs/GME/components.png?raw=true" />
</p>

<p align="center">
  <img src="https://github.com/petergpinto/cs301-101-group4/blob/master/graphs/GME/sentiment_forecast.png?raw=true" />
</p>



<h2 align="center">
Conclusion
</h2>

Overall, the analysis of the stock market subreddits is an effective method of predicting future stock prices. Throughout a three day period, the ratio of predictions that went in the right direction to predictions that went in the wrong direction is 3 to 2. If stocks in the stock market are mainly driven by human emotion, then gathering data should be heavily based on human emotion as well. 





