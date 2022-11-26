import praw
import random
import datetime
import time
import argparse
import markovify

# FIXME:
# copy your generate_comment function from the madlibs assignment here

madlibs = [
    "[PERSON] is in the pocket of [CORPORATIONS]. Never have I ever seen someone so [CORRUPT]. [PLEASE], for the sake of [OUR_COUNTRY], lock [PERSON] up!",
    "[PERSON] is [IN_LOVE] with [RUSSIA]. Are we [SURE] that he isn't a secret [AGENT] for them? It would [NOT_SURPRISE] me.",
    "I just received a [TEXT_MESSAGE] from [PERSON] asking for my [FINANCIAL_SUPPORT]. I can't believe [PERSON] takes the time to personally [ENGAGE] with each and every one of his [SUPPORTERS]! I also got a [TEXT_MESSAGE] asking about my car's extended warranty. Do you guys think it's worth renewing?",
    "[MOTIVATIONAL] quote of the day: [PERSON] once said: \"There's an old [SAYING] in [STATE_1] — I know it's in [STATE_2], probably in [STATE_1] — that says: [FOOL] me once, shame on you; [FOOL] me — you can't get [FOOL]ed again.\"",
    "[PERSON] has [TOLD] so many lies in the past [YEAR]. If I had a [DOLLAR] for every lie that he has [TOLD], I could buy [TWITTER]!",
    "[PERSON] doesn't want what's best for [OUR_COUNTRY]. He only cares about [KEEPING] his [POWER], [SERVING] the interests of his corporate overlords, and [BLOCKING] the Democrats' agenda."
    ]

replacements = {
    'PERSON' : ['Donald Trump', 'Ted Cruz', 'Mitch McConnell', 'Tucker Carlson'],
    'CORPORATIONS' : ['Corporate America', 'major corporations', 'the wealthy', 'the elite'],
    'CORRUPT' : ['corrupt', 'crooked', 'unethical', 'rotten', 'nefarious' ],
    'PLEASE' : ['Please', 'I beg'],
    'OUR_COUNTRY' : ['our country', 'our democracy', 'our nation', 'America'], 
    'IN_LOVE': ['in love', 'obsessed', 'infatuated'],
    'RUSSIA' : ['Russia', 'China', 'Saudi Arabia'], 
    'SURE' : ['sure', 'certain', 'positive', 'confident'], 
    'AGENT' : ['agent', 'operative', 'spy'], 
    'NOT_SURPRISE' : ['not surprise', 'not shock', 'make a lot of sense to'], 
    'TEXT_MESSAGE' : ['message', 'letter', 'text'], 
    'FINANCIAL_SUPPORT' : ['financial support', 'credit card information', 'bank account information'],
    'ENGAGE' : ['engage', 'interact', 'connect', 'communicate'], 
    'SUPPORTERS' : ['supporters', 'followers'], 
    'MOTIVATIONAL' : ['Motivational', 'Inspirational'], 
    'SAYING' : ['saying', 'adage', 'proverb', 'aphorism'],
    'STATE_1' : ['California', 'Tennessee', 'Florida', 'Alaska', 'Georgia', 'Virginia'], 
    'STATE_2' : ['Texas', 'Ohio', 'Michigan', 'New York', 'Oregon', 'Indiana'],
    'FOOL' : ['fool', 'trick', 'hoodwink'],
    'TOLD' : ['told', 'fabricated', 'made up', 'concocted'], 
    'YEAR' : ['year', 'two years', 'four years', 'six years'], 
    'DOLLAR' : ['dollar', 'quarter', 'dime', 'five-dollar bill'], 
    'TWITTER' : ['Twitter', 'a new house', '10 cars', 'a Taylor Swift concert ticket'], 
    'KEEPING' : ['keeping', 'maintaining', 'preserving'],
    'POWER' : ['power', 'influence', 'authority'], 
    'SERVING' : ['serving', 'protecting', 'carrying out', 'looking after'], 
    'BLOCKING' : ['blocking', 'interrupting', 'disrupting']
    }

def generate_comment():
    madlib = random.choice(madlibs)
    for replacement in replacements.keys():
        madlib = madlib.replace('['+replacement+']', random.choice(replacements[replacement]))    
    return madlib 


def generate_markovify():
    with open('markovify.txt') as f:    # 'markovify.txt' contains text about the Bipartisan Safer Communities Act, the Inflation Reduction Act, and the results of the recent midterm elections
        text = f.read()
    texts = text.split('\n\n')
    # building the markovify model 
    model_gun_legislation = markovify.Text(texts[0])
    model_climate_health_care = markovify.Text(texts[1])
    model_midterm_elections = markovify.Text(texts[2])
    model_combination = markovify.combine([model_gun_legislation, model_climate_health_care, model_midterm_elections], [1, 1, 3])
    # generating the text of my comments
    text = ''
    for i in range(5):
        sentence = model_combination.make_sentence(tries=50, state_size=7) + ' '
        word_list = sentence.split()
        if len(word_list) >= 7 and len(word_list) < 30:
            text += sentence
    return(text)  


# FIXME:
# connect to reddit 
parser = argparse.ArgumentParser()
parser.add_argument('bot_name')
parser.add_argument('--markovify', nargs='?', const=True)
args = parser.parse_args()
bot_name = args.bot_name

reddit = praw.Reddit(bot_name)

# FIXME:
# select a "home" submission in the /r/cs40_2022fall subreddit to post to,
# and put the url below
#
# HINT:
# The default submissions are going to fill up VERY quickly with comments from other students' bots.
# This can cause your code to slow down considerably.
# When you're first writing your code, it probably makes sense to make a submission
# that only you and 1-2 other students are working with.
# That way, you can more easily control the number of comments in the submission.

submission_url = 'https://old.reddit.com/r/cs40_2022fall/comments/z29aff/alex_jones_hit_with_965_million_verdict_in_2nd/'
submission = reddit.submission(url=submission_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once

while True:    

    # determine whether the bot will use the Markovify algorithm or the MadLibs algorithm to generate the comment
    if args.markovify:
        generate_text = generate_markovify()
    else:
        generate_text = generate_comment()

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions

    print('Before .replace_more()')
    submission.comments.replace_more(limit=None) 
    print('After .replace_more()')

    all_comments = submission.comments.list()
    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    for comment in all_comments:
        if comment.author != bot_name:
            not_my_comments.append(comment)
    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)
    print('has_not_commented=', has_not_commented)

    if has_not_commented:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # a top level comment is created when you reply to a post instead of a message
    
        #submission.reply(generate_comment())
        submission.reply(generate_text)
        pass

    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        comments_without_replies = []
        for comment in not_my_comments:
            if len(comment.replies.list()) == 0:
                comments_without_replies.append(comment)
            else:
                has_replied = False
                for reply in comment.replies.list():
                    if reply.author == bot_name:
                        has_replied = True
                if has_replied == False:
                    comments_without_replies.append(comment)
        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly;
        # many students struggle with getting a large number of "valid comments"
        print('len(comments_without_replies)=',len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;3
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message
        '''
        try:
            comment = random.choice(comments_without_replies)
            try:
                comment.reply(generate_comment())
            except praw.exceptions.APIException:
                print('this comment has been deleted') 
        except IndexError:
            pass
        '''
        # Reply to the most highly upvoted comment
        try: 
            most_upvoted_comment = None
            highest_score = 0
            for comment in comments_without_replies:
                if comment.score > highest_score:
                    most_upvoted_comment = comment
                    highest_score = comment.score
            print("Most upvoted comment: ", most_upvoted_comment.body)
            most_upvoted_comment.reply(generate_text)
        except AttributeError:
            print('there are no comments to reply to in this submission')
            pass
        except praw.exceptions.APIException:
            print('this comment has been deleted')
            pass


    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submission

    submissions = []
    for submission in reddit.subreddit("cs40_2022fall").hot(limit=5): 
        submissions.append(submission)
    submission = random.choice(submissions)
    pass

    # We sleep just for 1 second at the end of the while loop.
    # This doesn't avoid rate limiting
    # (since we're not sleeping for a long period of time),
    # but it does make the program's output more readable.
    time.sleep(1) 