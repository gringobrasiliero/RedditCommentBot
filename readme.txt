Description:
	-This is a bot that will search through Comments in Reddit Submissions, and will respond to a comment that includes a defined phrase.
	- The bot will only make ONE Comment per execution. 
	- The bot will not respond to the same comment twice.
	-There is a 15 minute wait time you must have in between making comments. (Reddit API Limitations)
		-This prevents people from making bots that spam the threads. 

SETUP:
	1) Go to https://www.reddit.com/prefs/apps to Create your Application for API Access:
		-Make sure to select the "Script" radio button
		-Gather all the details after creating. You will need the details for setup
		
	2) Run pip install -r requirements.txt in CMD

	3) Edit the Values in Constants.py
		
		#Reddit API Details 
		CLIENT_ID = 'CLIENT_ID'
		SECRET = 'YOUR_SECRET'
		USER_AGENT = 'USER_AGENT'
		USER = 'USER_NAME'
		PWD = 'PASSWORD'

		#Length of comments to look for (This allows you to have the bot to respond to comments that are less than the specified comment length)
		COMMENT_LENGTH = 100

		#Phrase you want bot to Comment on. The comment will only need to contain what you define
		SEARCH_PHRASE = "to the moon"

		#Bot will search through the Subreddits defined here in a random order. This is to help ensure that the Bot is making comments in a variety of Subreddits
		# I suggest adding a bigger list, so the bot is not only commenting on one subreddit. 
		SUB_REDDIT_SEARCH_LIST = ['wallstreetbets', 'stocks' ]

	4) run "python RedditCommentBot.py" in CMD to Execute

	5) Collect Karma =)



SUGGESTIONS:
	- After setup, have the program run on a CRONJOB (Linux), or Windows Task Scheduler (Windows) throughout the day, so you do not have to manually execute the program. 


