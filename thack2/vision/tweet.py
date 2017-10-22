import twitter

def tweet(s):
    api = twitter.Api(consumer_key='77h8AAr1WUk1djkhZeBukwMBz',
                      consumer_secret='PysMgbrw9D4qhEzQXyQ0VEtjdVd3E12SYRRb9iBywTo9BRQ68E',
                      access_token_key='194338134-VJPU8sFr2sxkQblHAedGSmbofXu9tG3gSQINlpCA',
                      access_token_secret='ZYJCKG8RU5X37KsEmQrDcpBm5Q044Jw1CQmRJvWxGwbb1')

    print(api.VerifyCredentials())

    #@TorontoPolice
    status = api.PostUpdate(s)
    print(status.text)
