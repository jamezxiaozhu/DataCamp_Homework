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

# 1. Import Flask
from flask import Flask, jsonify

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
                        <li>Please enter start_date in YYYY-MM-DD format.</li>                    
                    </ul>
                </li><br/>
                <li>/api/v1.0/(start_date)/(end_date)<br/>
                    <ul>
                        <li>Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start-end range.</li>
                        <li>Please enter start_date and end_date in YYYY-MM-DD format.</li>    
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
    try:
        dt.datetime.strptime(start_date, '%Y-%m-%d')
        if start_date > '2017-08-23' or start_date <'2010-01-01':
            return f'{start_date} is out of range of the current data base. Please choose a date from "2010-01-01" to "2018-08-23".'
        start_date_only = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).all()
        start_date_only_list = list(start_date_only)
        return jsonify(start_date_only_list)
    except ValueError:
        return jsonify({"error":"Incorrect data format, should be YYYY-MM-DD"}), 404
    

@app.route("/api/v1.0/<start_date>/<end_date>")
def start_end_date(start_date,end_date):
    try:
        dt.datetime.strptime(start_date, '%Y-%m-%d')
        dt.datetime.strptime(end_date, '%Y-%m-%d')
        if start_date > '2017-08-23' or start_date <'2010-01-01':
            return f'{start_date} is out of range of the current data base. Please choose a date from "2010-01-01" to "2018-08-23".'
        elif end_date > '2017-08-23' or end_date <'2010-01-01':
            return f'{end_date} is out of range of the current data base. Please choose a date from "2010-01-01" to "2018-08-23".'
        start_end = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
            filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
        start_end_list = list(start_end)
        return jsonify(start_end_list)
    except ValueError:
        return jsonify({"error":"Incorrect data format, should be YYYY-MM-DD"}), 404
      

# 4. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
