import requests
import authorization as auth_file
import pandas as pd

CLIENT_ID = "twNex_1QnnWiLkrvIoi9EQ"
PRIVATE_KEY = "kyvWgSXifCF9JUA9OCH5nH4gnci2pA"

GRANT_TYPE = 'password'

USERNAME = 'Svekzo'
PASSWORD_FILE_NAME = 'pw.txt'


def main():

    # our
    headers = auth_file.authorization_class.request_OATH_token(CLIENT_ID,
                                                               PRIVATE_KEY=PRIVATE_KEY, PASSWORD_FILE_NAME=PASSWORD_FILE_NAME, USERNAME=USERNAME, GRANT_TYPE=GRANT_TYPE)
    print(headers)
    req = make_request(headers)
    print(req.json())

    req = requests.get('https://oauth.reddit.com/r/python/hot', headers=headers, params={'limit':100})
    print("\n\n")

    df = pd.DataFrame()

    
    print(req.json()['data']['children'][0]['data'].keys())
    for post in req.json()['data']['children']:
        df = df.append({
            'subreddit': post['data']['subreddit'],
            'title': post['data']['title'],
            'selftext': post['data']['selftext'],
            'upvote_ratio': post['data']['upvote_ratio'],
            'ups': post['data']['ups'],
            'downs': post['data']['downs'],
            'score': post['data']['score']
        }, ignore_index=True)
    print(df)
    



    return




def make_request(headers):
    return requests.get('https://oauth.reddit.com/api/v1/me',headers=headers)
    
if __name__ == "__main__":
    main()
