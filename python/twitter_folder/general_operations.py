import pandas as pd
import os
import requests


class general_operations:

    global twitter_url
    twitter_url = r"https://api.twitter.com/2/users/by/username/"

    def read_required_API_tokens_from_text_file(tokens_file_path):
        tokens = {}
        dir = os.getcwd()

        with open(dir + tokens_file_path, "r") as f:
            for line in f:
                token, token_value = line.partition("=")[::2]
                tokens[token.strip()] = token_value
        return tokens

    def get_account_id_by_account_name(account_name):
        http_url = twitter_url + account_name
        account_info_json = requests.get(http_url)
        return account_info_json["data"]["id"]

    def convert_tweet_objects_to_dataframe(tweets):
        # this function converts the tweet objects and stores them in a dataframe.
        df = pd.DataFrame(columns=["tweet_id", "source", "language", "text", "topic_id", "created_at", "author_id", "likes", "replies", "retweets", "quote_count"])
        for tweet in tweets.data:
            df.loc[-1] = [
                tweet.id,
                tweet.source,
                tweet.lang,
                tweet.text,
                topic_id,
                pd.to_datetime(tweet.created_at).date(),
                tweet.author_id,
                tweet.public_metrics["like_count"],
                tweet.public_metrics["reply_count"],
                tweet.public_metrics["retweet_count"],
                tweet.public_metrics["quote_count"],
            ]  # adding a row
            df.index = df.index + 1  # shifting index
            df = df.sort_index()  # sorting by index
        return df
