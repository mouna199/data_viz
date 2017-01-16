                                                 
# Project : World Map of earthquakes 

### Summary 

This visualization is a wold map of earthquakes that took place between mid-December 2016 and January 2017, the data used is provided from http://earthquake.usgs.gov/ and contains many variables, the one we used here are the time, the intensity of the earthquake and of course the coordinates of the location. 

### Design

The choice of a map came from the data we have, having coordinates makes it interesting to discover the distribution of earthquakes and their intensity.
We first need to clean data and create a new one with the variables we are interested in, convert the time variable then sort them by time ascendantly. 
The visualization shows that lately, all the intense and frequent earthquakes were at south Asia. The size of each point indicates the intensity of the earthquake.

### Feedback 

### How to run the visualization 
We will need to run local server to render the visualization. it can be done using Python. We first navigate to the directory that contains all of the files and then type python -m SimpleHTTPServer in the command line. When we localhost:8000 into the address bar of the browser, we should be able to see the files displayed in the web page.


### Resources
Data source http://earthquake.usgs.gov <br />
Documentation of D3 https://d3js.org/ <br />
Tutorial of D3 https://maptimeboston.github.io/d3-maptime/#  <br />
http://stackoverflow.com 
