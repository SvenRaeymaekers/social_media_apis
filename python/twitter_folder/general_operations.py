from distutils.log import error
from socketserver import BaseRequestHandler
import pandas as pd
import os
import requests
from sentiment_analysis import sentiment_analysis
import numpy as np


class general_operations:

    global twitter_url
    twitter_url = r"https://api.twitter.com/2/users/by/username/"

    def read_required_API_tokens_from_text_file(tokens_file_path):
        """
            Function that reads the API tokens from your personal file
            returns: a dict including your keys
        """
        tokens = {}
        dir = os.getcwd()

        with open(dir + tokens_file_path, "r") as f:
            for line in f:
                token, token_value = line.partition("=")[::2]
                tokens[token.strip()] = str(token_value.strip())
        return tokens

    def get_account_id_by_account_name(account_name, BEARER_TOKEN):

        """
        Function that takes a twitter account name and makes a http-request to retrieve the ID of the twitter account 
        returns ID of the twitter account name
        """

        http_url = twitter_url + account_name
        Authorization_value = "Bearer {}".format(BEARER_TOKEN)
        response = requests.get(http_url, headers={"Authorization": Authorization_value})
        if response.status_code != 200:
            print("Something went wrong trying to get the account ID of the account you provided. Please check if the name you provided is correct.")
            quit()
        else:
            response_body_json = response.json()
            # extract the ID of the account
            return response_body_json["data"]["id"]

    def convert_tweet_objects_to_dataframe(tweets):
        # this function converts the tweet objects and stores them in a dataframe.

        """
        Function that converts the tweepy tweet objects to a dataframe.
        returns dataframe with tweets
        """
        df = pd.DataFrame(columns=["tweet_id", "source", "language", "text", "created_at", "author_id", "likes", "replies", "retweets", "quote_count"])
        for tweet in tweets:
            data = tweet.data
            df.loc[-1] = [
                data["id"],
                data["source"],
                data["lang"],
                data["text"],
                data["created_at"],
                data["author_id"],
                data["public_metrics"]["like_count"],
                data["public_metrics"]["reply_count"],
                data["public_metrics"]["retweet_count"],
                data["public_metrics"]["quote_count"],
            ]  # adding a row
            df.index = df.index + 1  # shifting index
            df = df.sort_index()  # sorting by index
        return df

    def retrieve_top_10_tweets_negative_or_positive(tweets_dataframe, sentiment):
        """
        Function that takes a dataframe of tweets & a sentiment argument which can be 'Positive' or 'Negative'.
        it returns the most positive or negative tweets.

        """

        if sentiment != "Positive" and sentiment != "Negative":
            raise Exception("The function retrieve_top_10_tweets_negative_or_positive requires a sentiment argument of 'negative' or 'positive' .")
        tweets_dataframe = tweets_dataframe.sort_values("sentiment_polarity")
        if sentiment == "Positive":
            return tweets_dataframe.tail(10)
        else:
            return tweets_dataframe.head(10)
