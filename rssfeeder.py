
#implementing rss feed
import feedparser
url = "http://w1.weather.gov/xml/current_obs/KALB.rss"
feed = feedparser.parse( url )
print(feed.get("value"))