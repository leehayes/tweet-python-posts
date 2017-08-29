
import private
import tweepy
import sqlite3

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def send(msg):
  api = get_api(private.cfg)
  status = api.update_status(status=msg)

def generate(source, uid):
    conn = sqlite3.connect('Posts.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT count(*) FROM Posts WHERE Source = ? AND UID =?", (source, uid))
        data = cursor.fetchone()[0]
        # If this post doesn't exist, do not send a tweet
        if data == 0:
            return None
        else:
            cursor.execute("SELECT Twitter FROM Source WHERE Source = ?", (source,))
            handle = cursor.fetchone()[0]
            cursor.execute("SELECT * FROM Posts WHERE Source = ? AND UID =?", (source, uid))
            post = cursor.fetchone()
            title = post[1]
            link = post[2]

            msg = "{}\n{}\n{}\n{}".format(title, link, handle, "#python")

            if len(msg)>140:
                msg = "{}\n{}\n{}".format(link, handle, "#python")

            if len(msg) > 140:
                msg = "{}\n{}".format(link, handle)
                return None
            else:
                send(msg)