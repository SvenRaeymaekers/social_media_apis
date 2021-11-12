from psaw import PushshiftAPI
import datetime
import re


def main():

    api = PushshiftAPI()

    start_time = int(datetime.datetime(2021, 11,1).timestamp())

    submissions = api.search_submissions(after=start_time,
                                         subreddit='wallstreetbets',
                                         filter=['url', 'author', 'title', 'subreddit'],
                                         #limit=250
                                         )

    mentions_of_particular_stock = {}

    for submission in submissions:

        words = submission.title.split()
        # print(words)

        cashtags = list(
            set(filter(lambda word: word.upper().startswith('$'), words)))

        if len(cashtags) > 0:
            #print(cashtags)
            #print(submission.title)
            #print('\n')
        

            pattern = re.compile("^\$[a-zA-Z]{2,5}$")
            
            for tag in cashtags:
                tag = tag.upper()
                if pattern.match(tag):
                    if mentions_of_particular_stock.get(tag) is not None:
                        mentions_of_particular_stock[tag] += 1
                    else:
                        mentions_of_particular_stock[tag] = 1

    sorted_mentions = sorted(mentions_of_particular_stock.items(),key= lambda x: x[1], reverse=True)
    for i in sorted_mentions:
        print(f'{i[0]} has been mentioned {i[1]} times')

    return


if __name__ == "__main__":
    main()
