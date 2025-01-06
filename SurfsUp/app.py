# Import dependencies
from flask import Flask, jsonify

import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

# Database setup / create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create session (link) from Python to the database
session = Session(engine)

# Flask setup
app = Flask(__name__)

# Flask routes
@app.route("/")
def home():
    return(
        f"<center><h2>Welcome to the Hawaii Climate Analysis Local API!</h2></center>"
        f"<center><h3>Select from one of the available routes:</h3></center>"
        f"<center>/api/v1.0/precipitation</center>"
        f"<center>/api/v1.0/stations</center>"
        f"<center>/api/v1.0/tobs</center>"
        f"<center>/api/v1.0/start/end</center>"
        )

# return prior year's precipitation observations as json
@app.route("/api/v1.0/precipitation")
def precip():

    # calculate data one year from last date in data set 
    priorYear = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # perform query to retrieve the date and precipitation values
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= priorYear).all()

    # close session
    session.close()
    
    # create dictionary with data as key and precipitation (prcp) as value (format as tuple)
    precip = {date: prcp for date, prcp in results}

    # convert to json
    return jsonify(precip)

# show station list as json
@app.route("/api/v1.0/stations")
def stations():

    # perform query to retrieve station names; close session; format results as list; convert to json and display
    results = session.query(Station.station).all()
    session.close()
    stationList = list(np.ravel(results)) # array
    return jsonify(stationList)

# show dates/temps of most active station over priorYear
@app.route("/api/v1.0/tobs")
def temps():
    priorYear = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == "USC00519281").filter(Measurement.date >= priorYear).all()
    session.close()
    tempsList = {date: tobs for date, tobs in results} # tuple
    return jsonify(tempsList)
    
# show min, max, avg temps for given start or start-end dates
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def dateStats(start=None, end=None):

    # select statement
    selection = [func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs),]

    if not end:
        startDate = dt.datetime.strptime(start, "%m%d%Y")
        results = session.query(*selection).filter(Measurement.date >= startDate).all()
        session.close()
        tempList = list(np.ravel(results))
        return jsonify(tempList)
    
    else:
        startDate = dt.datetime.strptime(start, "%m%d%Y")
        endDate = dt.datetime.strptime(end, "%m%d%Y")
        results = session.query(*selection).\
                filter(Measurement.date >= startDate).\
                filter(Measurement.date <= endDate).all()
        session.close()
        tempList = list(np.ravel(results))
        return jsonify(tempList)


# App launcher
if __name__ == '__main__':
    app.run(debug=True)