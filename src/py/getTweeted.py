
# This code simply takes in a user name and composes the twitter mention for that
# user with a unique URL.
# We might want to improve the message.

def getTweeted(username):
    message = 'Please consider participating in our short, univerity-affiliated study on how people express \
their identities on Twitter http:smallsocialsystems.com/asaf/AboutUs/'

    message += username

    return message
    
