import tweepy, os, sys

client = tweepy.Client(
    consumer_key=os.environ["X_API_KEY"],
    consumer_secret=os.environ["X_API_SECRET"],
    access_token=os.environ["X_ACCESS_TOKEN"],
    access_token_secret=os.environ["X_ACCESS_TOKEN_SECRET"],
)

def post_tweet(text: str):
    client.create_tweet(text=text)

if __name__ == "__main__":
    post_tweet(sys.argv[1])