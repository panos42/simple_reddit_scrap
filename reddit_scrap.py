# You need to create a Reddit app in the link below
# https://www.reddit.com/prefs/apps
# Enter the name and description of your choice.
# In the redirect uri box, enter http://localhost:8080
import praw
import pandas as pd

reddit = praw.Reddit(client_id="[YOUR_CLIENT_ID]", client_secret="[YOUR_CLIENT_SECRET]", user_agent="[USER_AGENT_NAME]")
subreddit = reddit.subreddit("personalfinance")

# extract top 500 posts
posts = []
while len(posts) < 500:
    limit = min(100, 500 - len(posts))
    top_posts = subreddit.top("month", limit=limit, params={"after": posts[-1].name if posts else None})
    posts += list(top_posts)

# create dataframe
posts_dict = {"Title": [], "Post Text": [], "ID": [], "Score": [], "Total Comments": [], "Post URL": []}
for post in posts:
    posts_dict["Title"].append(post.title)
    posts_dict["Post Text"].append(post.selftext)
    posts_dict["ID"].append(post.id)
    posts_dict["Score"].append(post.score)
    posts_dict["Total Comments"].append(post.num_comments)
    posts_dict["Post URL"].append(post.url)

top_posts = pd.DataFrame(posts_dict)

# Display the name of the Subreddit
print("Display Name:", subreddit.display_name)

# Display the title of the Subreddit
print("Title:", subreddit.title)

# Display the description of the Subreddit
print("Description:", subreddit.description)

# save dataframe as csv
top_posts.to_csv("Top Posts.csv", index=True)


