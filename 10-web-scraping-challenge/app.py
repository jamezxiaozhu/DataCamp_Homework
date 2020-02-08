from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from scrape_mars import scrape

app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_info")


@app.route("/")
def index():
    # write a statement that finds all the items in the db and sets it to a variable
    mars_facts = mongo.db.collection.find_one()
    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", mars_data = mars_facts)

@app.route("/scrape")
def scrape_app():
    # scrape_output = {}
    results = scrape()
    mongo.db.collection.update({}, results, upsert=True)
    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
