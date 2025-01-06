# SQLAlchemy-Challenge

## Instructions

You've decided to treat yourself to a long holiday in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.

## Part 1: Analyze and Explore the Climate Data

In this section, you’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. Specifically, you’ll use SQLAlchemy ORM queries, Pandas, and Matplotlib. To do so, complete the following steps:

* Use the SQLAlchemy create_engine() function to connect to the SQLite database.
* Use the SQLAlchemy automap_base() function to reflect the tables into classes, and then save references to the classes named station and measurement.
* Link Python to the database by creating a SQLAlchemy session. IMPORTANT: Close session at end of notebook.
* Perform a precipitation analysis and a station analysis by completing the steps in the following two subsections.

_Import dependencies_
    ![Screenshot 2025-01-06 at 14 42 28](https://github.com/user-attachments/assets/9318dcd5-c7e2-4471-9ca0-a0486adfdcf7)

_Reflect tables into SQLAlchemy ORM_
    ![Screenshot 2025-01-06 at 14 42 40](https://github.com/user-attachments/assets/04af665b-3ef7-4ba0-9c18-d2d67ae69719)

_While not requested, before starting analyses I inspected contents of tables (column names and types)_
    ![Screenshot 2025-01-06 at 14 42 56](https://github.com/user-attachments/assets/e73d44ba-dce2-4ba5-b076-1c253a451adc)

### Precipitation Analysis

1. Find the most recent date in the dataset.
2. Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.
3. Select only the "date" and "prcp" values.
4. Load the query results into a Pandas DataFrame. Explicitly set the column names.
5. Sort the DataFrame values by "date".
6. Plot the results by using the DataFrame plot method, as the following image shows:
    ![Screenshot 2025-01-05 at 23 28 53](https://github.com/user-attachments/assets/31e4803b-e3e2-453f-8f36-5ec5d36e0cd7)
7. Use Pandas to print summary statistics for the precipitation data.

_Analyses_
    ![Screenshot 2025-01-06 at 14 39 54](https://github.com/user-attachments/assets/ed0b9f90-b911-4ada-9e8e-21e15c1c1a9b)
    ![Screenshot 2025-01-06 at 14 40 07](https://github.com/user-attachments/assets/42a08b37-bdfd-4ae8-8528-54936c530c12)


### Station Analysis

1. Design a query to calculate the total number of stations in the dataset.
2. Design a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the following steps:
    * List the stations and observation counts in descending order (use func.count)
    * Answer the following question: which station id has the greatest number of observations?
3. Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query (use functions such as func.min, func.max, and func.avg in query).
4. Design a query to get the previous 12 months of temperature observation (TOBS) data. To do so, complete the following steps:
    * Filter by the station that has the greatest number of observations.
    * Query the previous 12 months of TOBS data for that station.
    * Plot the results as a histogram with bins=12, as the following image shows:
  ![Screenshot 2025-01-05 at 23 32 03](https://github.com/user-attachments/assets/ef6533ad-0b1c-4d2e-a447-cd84f667b745)
5. Close your session.

_Analyses_
    ![Screenshot 2025-01-06 at 14 49 11](https://github.com/user-attachments/assets/af2623c5-8fc5-4858-aa5a-e957c280d8ef)
    ![Screenshot 2025-01-06 at 14 49 25](https://github.com/user-attachments/assets/55275fdc-ddd8-454e-bba0-a11e5c79e5a9)


## Part 2: Design Your Climate App

Now that you’ve completed your initial analysis, you’ll design a Flask API based on the queries that you just developed. To do so, use Flask to create your routes as follows:

1. /
    * Start at the homepage.
    * List all the available routes.
2. /api/v1.0/precipitation
    * Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
    * Return the JSON representation of your dictionary.
3. /api/v1.0/stations
    * Return a JSON list of stations from the dataset.
4. /api/v1.0/tobs
    * Query the dates and temperature observations of the most-active station for the previous year of data.
    * Return a JSON list of temperature observations for the previous year.
5. /api/v1.0/<start> and /api/v1.0/<start>/<end>
    * Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
    * For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
    * For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.

Hints:
* Join the station and measurement tables for some of the queries.
* Use the Flask jsonify function to convert your API data to a valid JSON response object.

## Resources
* https://docs.python.org/3/library/datetime.html
