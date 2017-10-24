"""Must provide authentication keys.
"""

import twitter

def tweet(s):
    api = twitter.Api(consumer_key='',
                      consumer_secret='',
                      access_token_key='',
                      access_token_secret='')

    print(api.VerifyCredentials())

    status = api.PostUpdate(s)
    print(status.text)
