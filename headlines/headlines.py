from flask import Flask
from flask import render_template

import feedparser

app = Flask(__name__, template_folder='templates')

BBC_FEED = {'bbc':"http://feeds.bbci.co.uk/news/rss.xml",
            'cnn':"http://rss.cnn.com/rss/edition.rss",
            'fox':"http://feeds.foxnews.com/foxnews/latest",
            'iol':"http://www.iol.co.za/cmlink/1.640"}

@app.route("/")
@app.route("/<publication>")
def get_news(publication="bbc"):
    feed = feedparser.parse(BBC_FEED[publication])
    return render_template("home.html",articles=feed['entries'])

if __name__ == '__main__':
    app.run(port=5000, debug=True)

