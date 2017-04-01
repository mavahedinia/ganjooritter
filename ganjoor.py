import tweepy, json, requests

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

ganjoorJson = requests.get(url='http://c.ganjoor.net/beyt-json.php').text
ganjoorData = json.loads(ganjoorJson)
text = ganjoorData['m1'] + u'\n' + ganjoorData['m2'] + u'\n#' + ganjoorData['poet'].replace(u' ', u'_') + u'\n#گنجور'

api.update_status(text)
