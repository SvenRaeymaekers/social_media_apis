import re
from textblob import TextBlob
import numpy as np


class sentiment_analysis:
    def clean_tweet(self, tweet):
        """
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        """
        return " ".join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        return TextBlob(tweet).sentiment

    def add_sentiment_analysis(self, df):
        # function that adds a new column in a dataframe with the sentiment analysis of the text of the tweet in the dataframe field.

        df = df.reset_index()
        df["sentiment_polarity"] = ""
        df["sentiment_subjectivity"] = ""
        for index, row in df.iterrows():
            df.at[index, "sentiment_polarity"] = self.get_tweet_sentiment(self, self.clean_tweet(self, df.loc[index, "text"]))[0]
            df.at[index, "sentiment_subjectivity"] = self.get_tweet_sentiment(self, self.clean_tweet(self, df.loc[index, "text"]))[1]
        return df
