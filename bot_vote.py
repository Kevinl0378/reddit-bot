import praw
import argparse
import time 
from textblob import TextBlob

parser = argparse.ArgumentParser()
parser.add_argument('bot_name')
args = parser.parse_args()
bot_name = args.bot_name

reddit = praw.Reddit(bot_name)

num_submissions_checked = 0

submissions_voted_on = {}
comments_voted_on = {}

num_comments_checked_each_submission = []

# Checking submissions
for submission in list(reddit.subreddit("cs40_2022fall").hot(limit=None)):
    if submission.likes == None:
        print('Currently checking:', submission.title)
        num_submissions_checked += 1
        if 'biden' in submission.title.lower():
            tb_submission_output = TextBlob(submission.title)
            if tb_submission_output.sentiment.polarity > 0:
                submission.upvote()
                submissions_voted_on[submission.title] = 'Upvoted'
            else:
                submission.downvote()
                submissions_voted_on[submission.title] = 'Downvoted'
        else:
            print('Joe Biden was not mentioned in this submission')
    else:
        print('you have already voted on this submissions')

    print('Before .replace_more()')
    submission.comments.replace_more(limit=None)
    print('After .replace_more()')
    all_comments = submission.comments.list()

    # Checking comments
    num_comments_checked = 0
    for comment in all_comments:
        if comment.likes == None:
            print('Currently checking:', comment.body)
            num_comments_checked += 1
            if 'biden' in comment.body.lower():
                tb_comment_output = TextBlob(comment.body)
                if tb_comment_output.sentiment.polarity > 0:
                    comment.upvote()
                    comments_voted_on[comment.id] = 'Upvoted'                  
                else:
                    comment.downvote()
                    comments_voted_on[comment.id] = 'Downvoted'  
            else:
                print('Joe Biden was not mentioned in this comment')
        else:
            print('you have already voted on this comment')

    # Statistics
    print()
    print('Number of comments checked on this submission:', num_comments_checked)
    print('Comments voted on so far:', comments_voted_on)
    print()
    print('Number of submissions checked so far:', num_submissions_checked)
    print('Submissions voted on so far:', submissions_voted_on)
    print()
    num_comments_checked_each_submission.append(num_comments_checked)
    print('Number of comments checked in each submission so far:', num_comments_checked_each_submission)

    time.sleep(5)

# Output: Number of submissions checked so far: 573





    
