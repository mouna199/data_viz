                                                 
# Project : World Map of earthquakes 

The link to the visualization 
http://htmlpreview.github.io/?https://github.com/mouna199/data_viz/blob/master/index_final.html

### Summary 

This visualization is a wold map of earthquakes that took place between mid-December 2016 mid-January 2017, the data used is provided from http://earthquake.usgs.gov/ and contains many variables, the one we used here are the time, the intensity of the earthquake and of course the coordinates of the location. 

### Design

The choice of a map came from the data we have, the coordinates allow us to discover the distribution of earthquakes and their intensity gloably.
we choose the red color and circle to show earthquake to attract attention on the points, since earthquakes move with time and location, the legend came naturally after the choice of circles, the goal was to play on the size to show the intensity. 
The colors of the map and the background are relaxing for the eyes, so we focus more on the dates and the red circles. 
We first had to clean data and create a new one called 'examples.csv' with the variables we are interested in, convert the time variable then sort them by time ascendantly.
After receiving feedbacks, we changed the style of the text, the speed of animation from slow to faster and the colors of background along with the opacity of each point, we also added pulse so the intensity looks much convincing.
The visualization shows that lately, all the intense and frequent earthquakes were at south Asia. The size of each point indicates the intensity of the earthquake.

### Feedback 
The first feedback is that the visualization was slow and didn't show the intensity of each earthquake, also the title is supposed to be in the header not the foot of the page. 
The second feedback was about the opacity of the points, and the size of the title, which i edited. 
The third feedback suggested adding legend to explain the radius of each point stroke, and deleting the year since it is already in the title, the visualization was clear and could easly spot the intensity and frequency of earthquakes in south asia.


### How to run the visualization 
We will need to run local server to render the visualization. it can be done using Python. We first navigate to the directory that contains all of the files and then type python -m SimpleHTTPServer in the command line. When we localhost:8000 into the address bar of the browser, we should be able to see the files displayed in the web page.


### Resources
Data source http://earthquake.usgs.gov <br />
Documentation of D3 https://d3js.org/ <br />
Tutorial of D3 https://maptimeboston.github.io/d3-maptime/#  <br />
http://stackoverflow.com 
