from flask import Flask, render_template, redirect
import pymongo
import scraper

app = Flask(__name__)
mongo = pymongo.MongoClient("mongodb://localhost:27017/")
db = mongo.mars_db

@app.route("/")
def index():
    summary = db.summaries.find_one()
    return render_template("index.html", data=summary)


@app.route("/scrape")
def scrape():
    new_summary = scraper.scrape_all()
    db.summaries.delete_many({})
    db.summaries.insert_one(new_summary)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
