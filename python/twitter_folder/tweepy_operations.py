import tweepy
from tweepy import tweet

import pandas as pd
from general_operations import general_operations


class tweepy_operations:

    global token_file_path
    token_file_path = "/python/twitter_folder/tokens.txt"

    def get_tweepy_client():
        tokens = general_operations.read_required_API_tokens_from_text_file(token_file_path)

        # this is for API V2
        client = tweepy_operations.authenticate_tokens_and_return_api(tokens)
        return tokens, client

    # This is for twitter API V1.1
    def get_recent_mentions_of_username(api, username, number_of_tweets):
        # number_of_tweets can not be larger than 200 (see documentation)
        recent_tweets = api.mentions_timeline(name=username, count=number_of_tweets)
        return recent_tweets

    def get_number_of_tweets_mentioning_account_id(client, account_id, number_of_tweets):
        tweets = []
        for tweet in tweepy.Paginator(client.get_users_mentions, id=account_id, max_results=100, tweet_fields=["id", "source", "lang", "text", "created_at", "author_id", "public_metrics"]).flatten(limit=number_of_tweets):
            tweets.append(tweet)
        
        return tweets

    def authenticate_tokens_and_return_api(tokens):
        auth = tweepy.OAuthHandler(tokens["CONSUMER_KEY"], tokens["CONSUMER_SECRET"])
        auth.set_access_token(tokens["ACCESS_TOKEN"], tokens["ACCESS_TOKEN_SECRET"])
        return tweepy.Client(bearer_token=tokens["BEARER_TOKEN"])

    # This is for twitter API V1.1
    def print_user_info(api, username):
        user = api.get_user(screen_name=username)
        print("Printing friends of user:" + user.screen_name)
        for friend in user.friends():
            print(friend.screen_name)
        print(f"Number of {user.screen_name} followers: {user.followers_count}")
        return

    def get_mentions_of_user(api, user_id):
        # you have to look this user_id up by the postman Twitter API V2
        # environment, with corresponding keys. Then send a user lookup request
        # with the correct twitter username
        mentions = api.get_users_mentions(id=user_id)
        return mentions
