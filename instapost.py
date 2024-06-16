# Install instabot if you haven't already
#pip install instabot

# Import the necessary module from instabot
from instabot import Bot
import time
import random

# Create an instance of the Bot
bot = Bot()

# Log in to your Instagram account
bot.login(username="lok", password="password")

# Define the post's link where you want to comment
post_url = "https://www.instagram.com/reel/C8QxqIriwv1/?igsh=MXd5NXZmaDA1aTg5aQ=="

# Get the media ID from the post URL
media_id = bot.get_media_id_from_link(post_url)

# Define the specific comments
specific_comments = [
    "good"
]

# Repeat the specific comments to make a list of 50 comments
comments_to_post = (specific_comments * (50 // len(specific_comments) + 1))[:50]

# Post the comments
for comment in comments_to_post:
    bot.comment(media_id, comment)
    print(f"Commented: {comment}")
    time.sleep(random.randint(15, 30))  # Sleep for a random duration between 15 to 30 seconds

# Logout from the bot
bot.logout()
