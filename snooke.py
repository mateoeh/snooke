#!/usr/bin/env python3
# Usage: ./snooke.py [praw.ini section]

import praw
import random
import string
import sys

config_section = sys.argv[1] if len(sys.argv) > 1 else "default"
reddit = praw.Reddit(config_section, user_agent="snooke")
redditor = reddit.user.me()

for comment in redditor.comments.new(limit=None):
    message = f"Nuking comment {comment.id}: {comment.body}"
    if len(message) > 80: message = message[:79-3] + "..."
    print(message)

    rand = "".join(random.choices(string.ascii_letters + string.digits, k=64))
    comment.edit(rand)
    comment.delete()

for post in redditor.submissions.new(limit=None):
    message = f"Nuking post {post.id}: {post.title}"
    if len(message) > 80: message = message[:79-3] + "..."
    print(message)

    rand = "".join(random.choices(string.ascii_letters + string.digits, k=64))
    try:
        post.edit(rand)
    except praw.exceptions.APIException:
        pass  # Non-editable
    post.delete()

print("Done.")
