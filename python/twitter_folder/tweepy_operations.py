

class tweepy_operations:
     
     # This is for twitter API V1.1
    def get_recent_mentions_of_username(api, username,number_of_tweets):
        # number_of_tweets can not be larger than 200 (see documentation)
        recent_tweets = api.mentions_timeline(name=username,count=number_of_tweets)
        return recent_tweets


    
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