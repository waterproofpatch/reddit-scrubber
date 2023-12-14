"""
Delete comments for a given reddit account.
"""
import os
from typing import Any
import requests
import time

import praw



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
    reddit = praw.Reddit(client_id=os.environ['client_id'],
                         client_secret=os.environ['client_secret'],
                         password=os.environ['password'],
                         user_agent=os.environ['user_agent'],
                         username=os.environ['username'])
    me = reddit.user.me()
    # Get comment ids
    comment_ids = get_comment_ids(me)

