from general_operations import general_operations
from tweepy_operations import tweepy_operations


token_file_path = "/python/twitter_folder/tokens.txt"

# below is the topic_id, this is the id that corresponds to the account that you would like to extract tweets from.
# you can extract this topic id by using Postman and sending a GET request to "https://api.twitter.com/2/users/by/username/Youtube"
account_name = "Youtube"  # subject = "delijn", you have to extract this topic id based on the name of the account. can easily be found online how to do this.


def main():

    tokens = general_operations.read_required_API_tokens_from_text_file(token_file_path)

    # this is for API V2
    api = tweepy_operations.authenticate_tokens_and_return_api(tokens)
    account_id = general_operations.get_account_id_by_account_name(account_name)

    extracted_tweets = api.get_users_mentions(id=account_id, max_results=100, tweet_fields=["created_at", "author_id", "lang", "source", "public_metrics"])

    df = general_operations.convert_tweet_objects_to_dataframe(extracted_tweets)

    df.to_excel("extracted_tweets.xlsx")
    return


if __name__ == "__main__":
    main()
