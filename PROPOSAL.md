# cs301-101-group4

## Stock Market Estimation Using Social Media Sentiment

We will be following the outline of the [BTC Deep Forcasting project](https://pantelis.github.io/cs634/docs/common/projects/btc-forecasting/) with a few modifications.  
Firstly, we will be using the Reddit APIs rather than Twitter, since in personal experience they are more forgiving in terms of rate limiting.  Secondly, for the implementation of the price predictor, we will be primarily working with models discussed in class rather than RNN architectures.  This will include models such as Deep Neural Networks, Random Forests, and Boosting methods.  We will investigate which models covered in class best represent the data and tweak them to improve performance.

We will do this for 10 unique ticker symbols which will be chosen based on the number of mentions we are able to collect.  GME for example is likely to be the most mentioned, and therefore have the most data making it a good selection.

## Original Proposal below

This project will attempt to establish a correlation between the sentiment of social media posts and the future stock market price.  It is our belief that by extracting the sentiment from posts discussing various market securities a predictive model can be built.  

For this project, we will be collecting our own data by scraping comments and posts off of social media sites and running them through well established sentiment analysis methods to generate sentiment scores.  We will most likely use python NLTK<sub>1</sub> for this.  The published work associated with NLTK is also a good source of information for working with the algorithms.  Since collecting a large enough amount of data is necessary for this project, it is important to begin collecting quickly.

This data collection will happen on a cloud service setup to watch for posts mentioning relevant information.  After initial analysis, the data will be put into a database for further analysis.  Once sufficient data is collected, we will attempt to build a predictive model using the sentiment scores as model inputs and the next day’s prices as outputs.  At this point, we will analyze the collected data and select appropriate models based on what is appropriate for the collected data. We expect that a model with some level of predictive power can be built, although it is unlikely that accuracy will be extremely high.  After the model is built we can definitively test the outputs by generating a prediction for a future day and then comparing it after we can collect the new price data.

1. Bird, Steven, Edward Loper and Ewan Klein (2009), _Natural Language Processing with Python._ O’Reilly Media Inc.
