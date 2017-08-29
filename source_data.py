from functools import wraps
from DB_Manager import DB
import tweet
import requests
import xmltodict
from bs4 import BeautifulSoup

from pprint import pprint
"""
Hold the classes designed to extract and return the necessary results for new and old posts
"""

#TODO: module to validate, check and update sqlite db
#TODO: module to send a tweet out
#TODO: pyvideo


class Decorators:
    @classmethod
    def check_sql(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            DB("PlanetPython", "@planetpython")
            return func(*args, **kwargs)
        return wrapper


class PlanetPython:
    """
    Get the new posts from the PlanetPython RSS feed and scrape the historical feeds
    Typically this site has new content daily, up to 3 new posts a day
    """

    def __init__(self):
        self.source = "PlanetPython"
        self.twitter_handle = "@planetpython"


    @Decorators.check_sql
    def __call__(self):
        xml_dict = xmltodict.parse(self.rss_feed)
        for item in xml_dict['rss']['channel']['item']:
            if DB.add_new_content('PlanetPython', item['link'], item['title'], item['link']):
                tweet.generate('PlanetPython', item['link'])
                #only tweet one post per cron task

        #TODO: If no new tweets, return an old one from the archive (true or false?)

    @property
    def rss_feed(self):
        xml = requests.get('http://planetpython.org/rss20.xml').text
        return xml

class PyVideo:
    """
    Get the new videos from PvVideo.org
    Typically this site has new content weekly, often with bulk uploads
    """

    def __init__(self):
        self.source = "PyVideo"
        self.twitter_handle = "@PyvideoOrg"

    #@Decorators.check_sql
    def __call__(self):
        td_list = self.github_rows('https://github.com/pyvideo/data')
        event_list = []
        for event in td_list:
            td_list2 = self.github_rows('https://github.com/pyvideo/data/tree/master/{}/videos'.format(event))
            for video_json in td_list2:
                if video_json[-5:] == ".json":
                    html = requests.get(
                        'https://github.com/pyvideo/data/tree/master/{}/videos/{}'.format(event, video_json))
                    event_list.append(video_json)
                    print(video_json)
                    #DB.add_new_video()
                #break
            #print(event_list)

    @staticmethod
    def github_rows(url):
        html = requests.get(url)
        list_of_row_names = []
        if html.status_code == 200:
            soup = BeautifulSoup(html.text, "lxml")
            list_of_row_names = soup.findAll("td", { "class" : "content" })
            list_of_row_names = [td.text.strip() for td in list_of_row_names]
        return list_of_row_names
