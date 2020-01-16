# 1. Import Flask
from flask import Flask, jsonify

#import dependencies
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func,inspect

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Create our session (link) from Python to the DB
session = Session(engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# 2. Create an app
app = Flask(__name__)


# 3. Define static routes
@app.route("/")
def index():
    return (
        f"<h1>This is the home page!</h1> <br/>"
        f"<h2>Feel free to explore the following links: </h2><br/>"
        f"""<ol>
                <li>/api/v1.0/precipitation<br/>
                    <ul>
                        <li>Return a JSON of date and precipitation value.</li>
                    </ul>
                </li><br/>
                <li>/api/v1.0/stations<br/>
                    <ul>
                        <li>Return a JSON  list of stations from the dataset.</li>
                    </ul>
                </li><br/>
                <li>/api/v1.0/tobs<br/>
                    <ul>
                        <li>Return a JSON list of Temperature Observations (tobs) for the previous year.</li>
                    </ul>
                </li><br/>
                <li>/api/v1.0/(start_date)<br/>
                    <ul>
                        <li>Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start range.</li>
                        <li>Please enter start_date in yyyy-mm-dd format</li>                    
                    </ul>
                </li><br/>
                <li>/api/v1.0/(start_date)/(end_date)<br/>
                    <ul>
                        <li>Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start-end range.</li>
                        <li>Please enter start_date and end_date in yyyy-mm-dd format</li>    
                    </ul>
                </li><br/>
            </ol>"""
    )
    


@app.route("/api/v1.0/precipitation")
def precipitation():
    pcpr = session.query(Measurement.date, Measurement.prcp).all()
    pcpr_dict = dict(pcpr)
    return jsonify(pcpr_dict)

@app.route("/api/v1.0/stations")
def stations():
    stations = session.query(Measurement.station).\
    group_by(Measurement.station).all()
    stations_list = list(stations)
    return jsonify(stations_list)

@app.route("/api/v1.0/tobs")
def tobs():
    one_year_ago = dt.date(2017,8,23) - dt.timedelta(days=365)
    last_year_data = session.query(Measurement.tobs).\
    filter(func.datetime(Measurement.date) >= one_year_ago ).\
    filter(Measurement.tobs != 'None').\
    order_by(func.datetime(Measurement.date)).all()

    last_year_data_list = list(last_year_data)
    return jsonify(last_year_data_list)

@app.route("/api/v1.0/<start_date>")
def start_date(start_date):


    last_year_data_list = list(last_year_data)
    return jsonify(last_year_data_list)    

@app.route("/contact")
def contact():
    email = "peleke@example.com"

    return f"Questions? Comments? Complaints? Shoot an email to {email}."


# 4. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
