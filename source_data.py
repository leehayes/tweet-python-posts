from functools import wraps
import DB_Manager
"""
Hold the classes designed to extract and return the necessary results for new and old posts
"""

#TODO: module that is triggered by cron job
#TODO: module to validate, check and update sqlite db
#TODO: module to send a tweet out
#TODO: dbader
#TODO: pyvideo


class Decorators:
    @classmethod
    def check_sql(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            #check for sqlite db, if not there, create one and upload entire archive.
            print("checking sql")
            x = DB_Manager.DB()
            return func(*args, **kwargs)
        return wrapper


class PlanetPython:
    """
    Get the new posts from the PlanetPython RSS feed and scrape the historical feeds
    Typically this site has new content daily, up to 3 new posts a day
    """
    @Decorators.check_sql
    def __call__(self):
        print("Running PlanetPython")

        #go to RSS feed and get most recent posts http://planetpython.org/rss20.xml

        #Look for posts that are not in db, using url as UID, if new add to db and tweet

        #If no new tweets, return an old one from the archive


class DBader:
    """
    TBC
    """
    @Decorators.check_sql
    def __call__(self):
        print("Running DBader")
