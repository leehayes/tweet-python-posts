"""
Hold the classes designed to extract and return the necessary results for new and old posts
"""

#TODO: dbader

class PlanetPython:
    """
    Get the new posts from the PlanetPython RSS feed and scrape the historical feeds
    """
    def __init__(self):
        #check for sqlite db, if not there, create one and upload archive.

        #go to RSS feed and get most recent posts http://planetpython.org/rss20.xml

        #Look for posts that are not in db, using url as UID, if new add to db and tweet

        #If no new tweets, return an old one from the archive