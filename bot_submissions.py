import praw
import random
import argparse
import time 

parser = argparse.ArgumentParser()
parser.add_argument('bot_name')
args = parser.parse_args()
bot_name = args.bot_name

reddit = praw.Reddit(bot_name)
redditor = reddit.redditor(name = bot_name)


already_posted = []

while True:

    # Getting the submission
    submissions = list(reddit.subreddit("worldnews+PoliticalDiscussion").hot(limit=None))   
    submission = random.choice(submissions)

    # Submission information
    print('submission=', submission)
    print('submission.title=', submission.title)
    print('submission.url=', submission.url)
    print('submission.selftext=', submission.selftext)

    # Posting the submission
    if submission.title not in already_posted:
        if submission.selftext:
            reddit.subreddit("cs40_2022fall").submit(title=submission.title, selftext=submission.selftext)
            print('posted a self-post')
            already_posted.append(submission.title)
        else:     
            reddit.subreddit("cs40_2022fall").submit(title=submission.title, url=submission.url)
            print('posted a link post')
            already_posted.append(submission.title)
    else:
        print('this has already been posted') 
    
    print('Number of submissions posted=', len(already_posted))

    time.sleep(30)


# calculate the number of unique submissions
submissions = list(redditor.submissions.new(limit=None))

unique_submissions = []
for submission in submissions:
    if submission.title not in unique_submissions:
        unique_submissions.append(submission.title)

print("len(unique_submissions)=", len(unique_submissions))

# Output: len(unique_submissions)= 357
