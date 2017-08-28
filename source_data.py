from functools import wraps
import DB_Manager
import requests
import xmltodict
from pprint import pprint
"""
Hold the classes designed to extract and return the necessary results for new and old posts
"""

#TODO: module to validate, check and update sqlite db
#TODO: module to send a tweet out
#TODO: dbader
#TODO: pyvideo


class Decorators:
    @classmethod
    def check_sql(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            DB_Manager.DB()
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

        xml_dict = xmltodict.parse(self.rss_feed)
        for item in xml_dict['rss']['channel']['item']:
            if DB_Manager.add_new_content('PlanetPython', item['link'], item['title'], item['link'])
                print("This was new content, send tweet")
                #only tweet one post per cron task
                break

        #If no new tweets, return an old one from the archive (true or false?)

    @property
    def rss_feed(self):
        xml = requests.get('http://planetpython.org/rss20.xml').text
        return xml

class DBader:
    """
    TBC
    """
    @Decorators.check_sql
    def __call__(self):
        print("Running DBader")
