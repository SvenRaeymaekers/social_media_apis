
import requests


class authorization_class:

    def request_OATH_token(CLIENT_ID, PRIVATE_KEY, PASSWORD_FILE_NAME, USERNAME, GRANT_TYPE):
        # function that requests the OATH2.0 Bearer token from reddit.

        auth = requests.auth.HTTPBasicAuth(CLIENT_ID, PRIVATE_KEY)

        with open(PASSWORD_FILE_NAME, 'r') as f:
            pw = f.read()

        data = {
            'grant_type': GRANT_TYPE,
            'username': USERNAME,
            'password': pw
        }

        # setup our headers
        headers = {'User-Agent': 'MyAPI/0.0.1'}

        res = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth,
                            data=data, headers=headers)
        print(res.text)
        TOKEN = res.json()['access_token']

        headers['Authorization'] = f'bearer {TOKEN}'
        return headers
