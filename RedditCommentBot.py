import praw
import datetime as dt
from praw.models import MoreComments
import Constants
import csv
import time
from datetime import date, datetime
import random

class Reddit_comment_bot():

    def __init__(self):
        self.reddit = praw.Reddit(client_id= Constants.CLIENT_ID, 
                     client_secret=Constants.SECRET, 
                     user_agent=Constants.USER_AGENT, 
                     username=Constants.USER, 
                     password=Constants.PWD)
        pass


    def read_comments(self, submission):
        make_comment = False
        comment = ""
        for top_level_comment in submission.comments:
            if isinstance(top_level_comment, MoreComments):
                continue
                    #print(top_level_comment.body)
            comment = top_level_comment.body.lower()
            if Constants.SEARCH_PHRASE in comment and len(comment) < Constants.COMMENT_LENGTH:
                make_comment = True
                for second_level_comment in top_level_comment.replies:
                    user = second_level_comment.author_fullname
                    if user == Constants.USER:
                        make_comment = False
                        break
                return make_comment, top_level_comment
        return make_comment, None



    def main(self):
        
        comment_made = False
        didnt_comment = True
        while comment_made == False:
            sr = random.choice(Constants.SUB_REDDIT_SEARCH_LIST)
            print(sr)
            subreddit = self.reddit.subreddit(sr)
            for s in subreddit.hot(limit=Constants.SUBMISSION_SEARCH_LIMIT):
                submission = self.reddit.submission(id=s.id)
                make_comment, comment = self.read_comments(submission)
                if make_comment:
                    print("Post Title: " + s.title)
                    print("Comment Responded to: " + comment.body)
                    comment.reply("To Infinity and Beyond!")
                    print("COMMENTED!")
                    comment_made = True
                    
                if comment_made:
                    break
        



if __name__ == "__main__":
    x = Reddit_comment_bot()
    x.main()