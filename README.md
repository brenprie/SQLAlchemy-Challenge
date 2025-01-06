# SQLAlchemy-Challenge

## Instructions

You've decided to treat yourself to a long holiday in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.

## Part 1: Analyze and Explore Climate Data

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


## Part 2: Design Climate App

Design a Flask API based on the queries that you just developed. To do so, use Flask to create the routes as specified below.

_Preliminaries_
![Screenshot 2025-01-06 at 15 02 02](https://github.com/user-attachments/assets/a4de440e-5966-4845-869a-849aef8f325c)

1. /
* List all the available routes.
* _Code_
  ![Screenshot 2025-01-06 at 15 02 19](https://github.com/user-attachments/assets/d8a4aadc-6822-4631-8f36-a997cdcc4797)
* _Output_
  ![Screenshot 2025-01-06 at 14 56 05](https://github.com/user-attachments/assets/2e657ad2-e118-409c-b68c-afc0f749290e)

2. /api/v1.0/precipitation
* Convert query results from precipitation analysis (i.e. the last 12 months of data) to dictionary using date as the key and prcp as the value; return JSON representation of dictionary.
* _Code_
  ![Screenshot 2025-01-06 at 15 02 40](https://github.com/user-attachments/assets/bedcd51f-f3a4-4fa8-8032-2aad06c4de7f)
* _Output_
  ![Screenshot 2025-01-06 at 14 56 24](https://github.com/user-attachments/assets/9c9221aa-37d2-4687-b3c1-05a405b8a678)

3. /api/v1.0/stations
* Return JSON list of stations from data set.
* _Code_
   ![Screenshot 2025-01-06 at 15 02 51](https://github.com/user-attachments/assets/b305bb15-e683-40c7-9592-9d5985c9a3b1)
* _Output_
   ![Screenshot 2025-01-06 at 14 56 43](https://github.com/user-attachments/assets/52115568-d6af-47fb-8df7-93ac053bda59)

4. /api/v1.0/tobs
* Query dates and temperature observations of the most-active station for the previous year of data; return JSON list of temperature observations for previous year.
* _Code_
   ![Screenshot 2025-01-06 at 15 03 06](https://github.com/user-attachments/assets/01403aee-c3c0-4fcb-89af-246e5623ace0)
* _Output_    
   ![Screenshot 2025-01-06 at 14 57 09](https://github.com/user-attachments/assets/791a4fe2-8e9f-444c-b7ce-8f2ac502b783)

5. /api/v1.0/<start> and /api/v1.0/start/end
* Return JSON list of minimum temperature, average temperature, and maximum temperature for specified start date or start date/end date range; calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date or for dates from start date to end date, inclusive.
* _Code_
   ![Screenshot 2025-01-06 at 15 00 24](https://github.com/user-attachments/assets/e8ee463f-6654-44af-a4a2-c416d98d163c)
* _Output, using random date and date range from data set_
   ![Screenshot 2025-01-06 at 14 57 46](https://github.com/user-attachments/assets/5f0a8489-4d45-4ec8-a201-c306341dce63)
   ![Screenshot 2025-01-06 at 14 58 14](https://github.com/user-attachments/assets/51f66f77-2ebe-4033-84f8-91c25db8cc39)

_App launcher_
    ![Screenshot 2025-01-06 at 15 03 32](https://github.com/user-attachments/assets/9acf1e04-656d-4b6d-8bf4-a3993e8d5c1a)


## Resources
* Python Libary, datetime -- https://docs.python.org/3/library/datetime.html

## Acknowledgements - Data Source

Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, https://journals.ametsoc.org/view/journals/atot/29/7/jtech-d-11-00103_1.xml
