# Reddit Bots

In this project, I created a Reddit bot that posts and upvotes/downvotes political messages on a specific subreddit designed for my computer science course. My bot supports Joe Biden by upvoting messages that mention him favorably and downvoting messages that mention him negatively. My bot opposes prominent Republican figures, such as Donald Trump, Ted Cruz, Mitch McConnell, and Tucker Carlson, by posting either negative or sarcastic comments about them. 

</br> 

## My Favorite Thread
My bot was constantly interacting with bots created by other students, which resulted in some very funny threads involving my bot. Here is a link to my [favorite thread](https://old.reddit.com/r/cs40_2022fall/comments/z34rak/amazon_raised_10_billion_in_the_bond_markets/ixjwvjm/). I really liked how several of the replies to my comment also opposed Donald Trump. It made the thread seem more like a coherent discussion between human users about Trump's vices rather than a bunch of bots posting random comments. 
</br>

![This is my favorite thread](https://github.com/Kevinl0378/reddit-bot/blob/main/favorite_thread.png)
</br>

</br>

## Output of Running the `bot_counter.py` File
While working on this project, I was able to create an "army" of 5 bots. Each bot posted over 500 comments in the subreddit. Here are the results of running the `bot_counter.py` file on each of the 5 bots:
1. Bot #1
```
len(comments)= 1000
len(top_level_comments)= 100
len(replies)= 900
len(valid_top_level_comments)= 100
len(not_self_replies)= 900
len(valid_replies)= 900
========================================
valid_comments= 1000
========================================
```
2. Bot #2
```
len(comments)= 517
len(top_level_comments)= 59
len(replies)= 458
len(valid_top_level_comments)= 59
len(not_self_replies)= 458
len(valid_replies)= 458
========================================
valid_comments= 517
========================================
```
3. Bot #3
```
len(comments)= 624
len(top_level_comments)= 57
len(replies)= 567
len(valid_top_level_comments)= 57
len(not_self_replies)= 567
len(valid_replies)= 567
========================================
valid_comments= 624
========================================
```
4. Bot #4
```
len(comments)= 599
len(top_level_comments)= 121
len(replies)= 478
len(valid_top_level_comments)= 121
len(not_self_replies)= 478
len(valid_replies)= 478
========================================
valid_comments= 599
========================================
```
5. Bot #5
```
len(comments)= 589
len(top_level_comments)= 78
len(replies)= 511
len(valid_top_level_comments)= 78
len(not_self_replies)= 511
len(valid_replies)= 511
========================================
valid_comments= 589
========================================
```

</br>

## Score
I believe my score should be 40/30. I fulfilled all 3 required tasks: 
* I completed all 6 tasks in the `bot.py` file (<b>12 points total</b>) 
* I created this GitHub repository and satisfied each requirement in the instructions (<b>3 points</b>)
* My main bot (Bot #1) was able to make 1,000 valid comments (<b>10 points</b>) 

In addition to the required tasks, I completed all of the optional tasks:
* I created a `bot_submissions.py` file, which posted 357 unique submissions (both self-posts and link posts) to the class subreddit (<b>2 points</b>) 
* All 5 of my bots were able to post over 500 comments (<b>2 points</b>)
* Inside the `bot.py` file, I edited task 4 so that my bot would reply to the most highly upvoted comment in a thread (**2 points**)
* I created a `bot_vote.py` file, which utilized the TextBlob sentiment analysis library to upvote comments and submissions that mentioned Joe Biden favorably and downvote comments and submissions that mentioned him unfavorably. My code ran on 573 submission, as well as all of the comments within those submissions (**4 points**)
* I used the Markovify library to create a function inside of the `bot.py` file that generates the comments that my bot will post using a more sophisticated algorithm. The text that the Markovify library uses contains information about the Bipartisan Safer Communities Act, the Inflation Reduction Act, and the results of the recent midterm elections (**5 points**)
