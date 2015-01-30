# This function will print out a conclusion about the gully data used as input.
conclusion <- function() {
  concl <- paste("Welcome ", username, "! Thank you for using this lovely tool to determine the difference in depth",
                  " between a real gully and the same gully in a DEM. The GPS points you chose are ", GPS_points[1], " and ",
                  GPS_points[2], ". The accuracy of the DEM is a bit disappointing, because there is a mean difference of ", 
                  mean_difference, "m and a standard deviation of ", sd_difference, "m. The largest difference between DEM ", 
                  "and measurement is " , max_difference, "m. Thank you for using this tool, we hope to see you again.", sep="")
  return(concl)
  }
