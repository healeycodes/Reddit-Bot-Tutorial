import os
import praw
import argparse

# setup argparse
parser = argparse.ArgumentParser(description='Reply to certain Reddit comments')
parser.add_argument('--search', dest='search',
                    help='Search for these comma-delimited phrases. E.g., "one phrase, another phrase"')
parser.add_argument('--reply', dest='reply',
                    help='Reply to target comments with this phrase')
args = parser.parse_args()

# our search phrases, also works with a single word
search = [phrase.strip() for phrase in args.search.split(',')]
# our reply
reply = args.reply

# reddit instance
reddit = praw.Reddit(client_id=os.environ['CLIENTID'],
                     client_secret=os.environ['CLIENTSECRET'],
                     user_agent='Reddit bot tutorial v0.1-1',
                     username=os.environ['CLIENTUSER'],
                     password=os.environ['CLIENTPASS'])

# an endless stream of comments
for comment in reddit.subreddit('all').stream.comments():
    for phrase in search:
        if phrase in comment.body:
            comment.reply(reply)
            # for debugging
            print(f'Replied to {comment.id}!')
            break
