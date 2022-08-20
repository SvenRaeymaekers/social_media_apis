import os
from numpy import number
from general_operations import general_operations
from sentiment_analysis import sentiment_analysis
from tweepy_operations import tweepy_operations


token_file_path = "/python/twitter_folder/tokens.txt"

# below is the topic_id, this is the id that corresponds to the account that you would like to extract tweets from.
# you can extract this topic id by using Postman and sending a GET request to "https://api.twitter.com/2/users/by/username/Youtube"
account_name = "Cristiano"  # subject = "delijn", you have to extract this topic id based on the name of the account. can easily be found online how to do this.
number_of_tweets = 1000


def main():

    tokens = general_operations.read_required_API_tokens_from_text_file(token_file_path)

    # this is for API V2
    client = tweepy_operations.authenticate_tokens_and_return_api(tokens)

    # currently doesn't work
    account_id = general_operations.get_account_id_by_account_name(account_name, tokens["BEARER_TOKEN"])

    extracted_tweets = client.get_users_mentions(id=account_id, max_results=100, tweet_fields=["created_at", "author_id", "lang", "source", "public_metrics"])
    extracted_tweets = tweepy_operations.get_number_of_accountid_mentions(client, account_id=account_id, number_of_tweets=number_of_tweets)
    df = general_operations.convert_tweet_objects_to_dataframe(extracted_tweets)
    df = df[df["language"] == "en"]
    df = sentiment_analysis.add_sentiment_analysis(sentiment_analysis, df)

    df.to_excel(os.getcwd() + "/extracted_tweets.xlsx")
    return


if __name__ == "__main__":
    main()
