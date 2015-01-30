# These function load the gully data (DEM data and field measurement data) that is stored as .csv file.
# The files are described by 2 GPS points between which a crosssection profile has been measured.

load_dem_data <- function (GPSpoint1, GPSpoint2) {
  file_loc <- paste("data/Results.gdb/Tej_", GPSpoint1, "_", GPSpoint2, ".csv", sep="")
  Gully_DEM<- read.csv(file_loc)
}

load_field_data <- function (GPSpoint1, GPSpoint2) {
  file_loc <- paste("data/Results.gdb/Tej_", GPSpoint1, "_", GPSpoint2, "_field_meas.csv", sep="") 
  Gully_DEM<- read.csv(file_loc, sep=";")
}