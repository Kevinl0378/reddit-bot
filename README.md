# Reddit Bots

In this project, I created a Reddit bot that posts and upvotes/downvotes political messages on a specific subreddit designed for my computer science course. My bot supports Joe Biden by upvoting messages that mention him favorably and downvoting messages that mention him negatively. My bot opposes prominent Republican figures, such as Donald Trump, Ted Cruz, Mitch McConnell, and Tucker Carlson, by posting either negative or sarcastic comments about them. 

My bot was constantly interacting with bots created by other students, which resulted in some very funny threads involving my bot. Here is a link to my [favorite thread](https://old.reddit.com/r/cs40_2022fall/comments/z34rak/amazon_raised_10_billion_in_the_bond_markets/ixjwvjm/).
</br>
[*IMAGE SCREENSHOT OF THREAD*]
</br>
I really liked how several of the replies to my comment also opposed Donald Trump. It made the thread seem more like a coherent discussion between human users about Trump's vices rather than a bunch of bots posting random comments. 

</br>

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
</br>

<h2>Score</h2>
I believe my score should be 40/30. I fulfilled all 3 required tasks. I completed all 6 tasks in the `bot.py` file (<b>12 points total</b>). I created this GitHub repository and satisfied each requirement in the instructions (<b>3 points</b>). My main bot (Bot #1) was able to make 1,000 valid comments (<b>10 points</b>). In addition to the required tasks, I completed all of the optional tasks. I created a `bot_submissions.py` file, which posted 357 unique submissions (both self-posts and link posts) to the class subreddit (<b>2 points</b>). All 5 of my bots were able to post over 500 comments (<b>2 points</b>).  
