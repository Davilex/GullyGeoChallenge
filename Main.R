# Title: Accuracy of gully cross sections in a high resolution DEM.
# Team: Gully Bully (David Scholte-Albers)
# Date: 29-01-2015 

############### Initialization ###############

rm(list = ls())
ls()

# Check Working Directory
getwd()
# setwd("D:/GullyGeoChallenge")

# Set username
username = "Gully Bully"

# Load packages
require(ggplot2)
require(gridExtra)

# import functions
source("Scripting/R/Load_Field_and_DEM_CSV_Data.R")
source("Scripting/R/Make_Gully_Plots.R")
source("Scripting/R/Combine_Plots.R")
source("Scripting/R/Conclusion.R")

############### Data processing ###############

# Load Gully Data, change GPS_points for different data
# Valid combinations are: (1, 3); (13, 16); (26, 28); (39, 41); (48, 50); 
# (73, 75); (78, 79); (115, 117); (146, 147); (148, 149)
GPS_points <- c(26,28)
DEM_table <- load_dem_data(GPS_points[1], GPS_points[2])
Field_table <- load_field_data(GPS_points[1], GPS_points[2])

# Add Depth Field to Gully_DEM
DEM_table$Depth <- DEM_table$RASTERVALU[1] - DEM_table$RASTERVALU

############### Data Visualisation ###############

# Plot DEM and Field data next to each other 
plot_DEM <- make_dem_plot(DEM_table)
plot_field <- make_field_plot(Field_table)
grid.arrange(plot_DEM, plot_field, ncol=2)

# Plot DEM and Field profile in same plot
make_plot(DEM_table, Field_table)

# Determine Difference
options(warn=-1)
difference_per_5_cm <- abs(abs(Field_table$Depth.until.soil.surface) - abs(DEM_table$Depth))
options(warn=0)

# Plot difference in same plot
if (length(Field_table$Length) >= length(DEM_table$DISTANCE)) {
  lines(Field_table$Length, difference_per_5_cm, lwd=6, col="Black")
  } else {
    lines(lines(DEM_table$DISTANCE, difference_per_5_cm, lwd=3, col="Black"))
  }
legend("bottomright", c("Field","DEM", "Difference"), lty=c(1,1,1), lwd=c(4, 4, 4),col=c("blue","red", "Black"))

############### Statistics ###############

# Functions for the mean, max and standard deviation of the difference
mean_difference <- round(mean(difference_per_5_cm), digits=2)
max_difference <- round(max(difference_per_5_cm), digits=2)
sd_difference <- round(sd(difference_per_5_cm), digits=2)

############### Conclusion ###############

# Print out the conclusion
print(conclusion())

############### End of Script ###############
