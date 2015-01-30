# GullyGeoChallenge
Final exercise of the Geoscripting course of Wageningen University 2015

For this project Gully crossections extracted from a Digital Elevation Model (DEM) will be compared with ground truth data. For every 5 centimeters in length, the depth of a gully has been measured, and will be compared to the elevation of the DEM at the same location.

The python script "GPS_Points_to_csv_file.py" (located in the Scripting/Python folder) should be run first to extract elevation data from the DEM. The DEM is a large file and should be downloaded according to the python script.

The extracted DEM values will be exported in a .csv value and will be loaded into R, for further analysis of the gullies.
