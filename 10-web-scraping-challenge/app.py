from flask import Flask, render_template
import pymongo

app = Flask(__name__)

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.mars_info
collection = db.scrape_info


@app.route("/")
def index():
    # write a statement that finds all the items in the db and sets it to a variable
    inventory = list(db.collection.find())
    print(inventory)

    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", inventory=inventory)

@app.route("/scrape")
def scrape():
    from scrape_mars import scrape
    scrape()
    final_scrape_output
    
if __name__ == "__main__":
    app.run(debug=True)
