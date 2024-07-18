from __future__ import print_function
import praw
import prawcore
import time
import os
import logging
from config import (
    REDDIT_CLIENT_ID,
    REDDIT_CLIENT_SECRET,
    REDDIT_PASSWORD,
    REDDIT_USERNAME,
    REDDIT_USER_AGENT,
    TARGET_SUBREDDIT,
    TARGET_STRING,
    REPLY_MESSAGE,
    SLEEP_DURATION
)
# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Function to handle rate limit with exponential backoff
def handle_rate_limit(api_exception, retry_attempts=3):
    for attempt in range(retry_attempts):
        retry_after = api_exception.response.headers.get('Retry-After')
        if retry_after:
            retry_after = int(retry_after)
            logger.info(f'Rate limited. Retrying after {retry_after} seconds.')
            time.sleep(retry_after)
            return
        else:
            logger.info('Rate limited. Retrying after 5 seconds.')
            time.sleep(5)
            return
    logger.error('Rate limit exceeded. Exiting program.')
    exit()

# Function to log in to Reddit
def bot_login():
    logger.info('Logging in to Reddit...')

    try:
        reddit = praw.Reddit(
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_CLIENT_SECRET,
            password=REDDIT_PASSWORD,
            user_agent=REDDIT_USER_AGENT,
            username=REDDIT_USERNAME
        )
        logger.info('Logged in to Reddit.')
        return reddit
    except prawcore.exceptions.OAuthException as e:
        logger.error('Error logging in to Reddit. Check your credentials.')
        raise e
    except Exception as e:
        logger.exception('An error occurred while logging in to Reddit.')
        raise e
    
# Function to run the bot
def run_bot(reddit, comments_replied_to):
    logger.info('Running bot...')

    # Get the subreddit
    subreddit = reddit.subreddit(TARGET_SUBREDDIT)

    # Get the comments
    comments = subreddit.stream.comments()

    # Loop through comments
    for comment in comments:
        # Check if the comment contains the target string
        if TARGET_STRING in comment.body.lower() and comment.id not in comments_replied_to:
            logger.info(f'Found comment with ID: {comment.id}')
            logger.info(f'Comment body: {comment.body}')

            # Reply to the comment
            try:
                comment.reply(REPLY_MESSAGE)
                logger.info('Replied to comment.')
                comments_replied_to.append(comment.id)
                with open('comments_replied_to.txt', 'a') as f:
                    f.write(comment.id + '\n')
            except prawcore.exceptions.Forbidden as e:
                logger.error('Error replying to comment. Forbidden.')
            except prawcore.exceptions.NotFound as e:
                logger.error('Error replying to comment. Not found.')
            except prawcore.exceptions.ServerError as e:
                logger.error('Error replying to comment. Server error.')
            except prawcore.exceptions.RequestException as e:
                logger.error('Error replying to comment. Request exception.')
            except prawcore.exceptions.ResponseException as e:
                logger.error('Error replying to comment. Response exception.')
            except Exception as e:
                logger.exception('An error occurred while replying to comment.')

        # Sleep for a while
        time.sleep(SLEEP_DURATION)

# Function to process comments
def process_comments():
    logger.info('Processing comments...')

    # Load comments replied to
    if not os.path.isfile('comments_replied_to.txt'):
        comments_replied_to = []
    else:
        with open('comments_replied_to.txt', 'r') as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split('\n')
            comments_replied_to = list(filter(None, comments_replied_to))

    # Log in to Reddit
    reddit = bot_login()

    # Run the bot
    run_bot(reddit, comments_replied_to)

# Function to process a single comment
def process_single_comment(comment_id):
    logger.info(f'Processing single comment with ID: {comment_id}')

    # Log in to Reddit
    reddit = bot_login()

    # Get the comment
    comment = reddit.comment(id=comment_id)

    # Check if the comment contains the target string
    if TARGET_STRING in comment.body.lower():
        logger.info(f'Found comment with ID: {comment.id}')
        logger.info(f'Comment body: {comment.body}')

        # Reply to the comment
        try:
            comment.reply(REPLY_MESSAGE)
            logger.info('Replied to comment.')
        except prawcore.exceptions.Forbidden as e:
            logger.error('Error replying to comment. Forbidden.')
        except prawcore.exceptions.NotFound as e:
            logger.error('Error replying to comment. Not found.')
        except prawcore.exceptions.ServerError as e:
            logger.error('Error replying to comment. Server error.')
        except prawcore.exceptions.RequestException as e:
            logger.error('Error replying to comment. Request exception.')
        except prawcore.exceptions.ResponseException as e:
            logger.error('Error replying to comment. Response exception.')
        except Exception as e:
            logger.exception('An error occurred while replying to comment.')
    else:
        logger.info('Comment does not contain target string.')

#Function to get saved comments
def get_saved_comments():
    logger.info('Getting saved comments...')

    # Load comments replied to
    if not os.path.isfile('comments_replied_to.txt'):
        comments_replied_to = []
    else:
        with open('comments_replied_to.txt', 'r') as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split('\n')
            comments_replied_to = list(filter(None, comments_replied_to))

    return comments_replied_to

# Main block to run the bot
if __name__ == '__main__':
    reddit = bot_login()
    comments_replied_to = get_saved_comments()
    run_bot(reddit, comments_replied_to)
    logger.info(f'Number of comments replied to: {len(comments_replied_to)}')

    # Run the bot in an infinite loop
    while True:
        try:
            run_bot(reddit, comments_replied_to)
        except Exception as e:
            logger.exception('An error occurred while running the bot.')
            handle_rate_limit(e)
            continue
        time.sleep(SLEEP_DURATION)
