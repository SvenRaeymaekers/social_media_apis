import tweepy
from tweepy import tweet
from tweepy_operations import tweepy_operations
import pandas as pd

CONSUMER_KEY = "C6sSMFKB33EiivNZ5I1j9c7UJ"
CONSUMER_SECRET = "dPrweSI9IyqVVHN10NldwYn5XKmkxJ7RFmYrAWvsKrUfRslb8o"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAJ%2FJVgEAAAAA7F%2F7hhrrDCSXWgUQWnrLQyHUFms%3DXvXPnwYP8Hw3YQqYREqzkkrGXs5y06DVUjMdsH08UckXeXAZqa"
ACCESS_TOKEN = "2736696627-EuTPG3gCMFYj9CXO5TFiARCoOq6BK1UObAbCJWw"
ACCESS_TOKEN_SECRET = "Qzpdded4LQIINX6QWFzUOFsAcSZT6UY9cY5kNsBmt9xrQ"


def main():

    # see tweepy doc, this is for API V1.1
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # this is for API V2
    api = tweepy.Client(bearer_token=BEARER_TOKEN)

    # for tweet in public_tweets:
    #    print(tweet.text + "\n")

    # user = api.get_user(screen_name='raeymaekersss')
    topic_id = 32851079  # delijn
    tweets_of_subject = api.get_users_mentions(
        id=topic_id, max_results=100, tweet_fields=['created_at', 'author_id', 'lang', 'source', 'public_metrics'])

    df = pd.DataFrame(columns=['tweet_id', 'source', 'language', 'text',
                      'topic_id', 'created_at', 'author_id', 'likes', 'replies', 'retweets', 'quote_count'])
    for tweet in tweets_of_subject.data:

        df.loc[-1] = [tweet.id, tweet.source, tweet.lang, tweet.text, topic_id,
                      pd.to_datetime(tweet.created_at).date(
                      ), tweet.author_id, tweet.public_metrics['like_count'],
                      tweet.public_metrics['reply_count'], tweet.public_metrics['retweet_count'], tweet.public_metrics['quote_count']]  # adding a row
        df.index = df.index + 1  # shifting index
        df = df.sort_index()  # sorting by index

    df.to_excel("extracted_tweets.xlsx")
    return


if __name__ == "__main__":
    main()
()
