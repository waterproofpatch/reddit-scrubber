"""
Delete comments for a given reddit account.
"""
import praw

from typing import Any
import requests
import time


def get_comment_ids(me: Any):
    comments = list(me.comments.new(limit=1000))
    comments_deleted = 0
    while comments:
        for comment in comments:
            print(f"Deleting {comment.id}")
            comment.delete()
            comments_deleted += 1
            time.sleep(2) # to prevent rate limiting
        print("Requesting more comments...")
        comments = list(me.comments.new(limit=1000))
    print(f"Done. Deleted {comments_deleted} comments.")

def delete_comments(comment_ids):
    for comment_id in comment_ids:
        comment = reddit.comment(id=comment_id)
        comment.delete()
        time.sleep(2)  # To prevent rate limiting

if __name__ == "__main__":
    # Initialize the Reddit instance
    reddit = praw.Reddit(client_id=os.env['client_id'],
                         client_secret=os.env['client_secret'],
                         password=os.env['password'],
                         user_agent=os.env['user_agent'],
                         username=os.env['username'])
    me = reddit.user.me()
    # Get comment ids
    comment_ids = get_comment_ids(me)

