# These functions will extract the columns of interest from the data frames and if called will
# plot the data.

make_dem_plot <- function(Gully_DEM) {
  Depth_DEM <- Gully_DEM$Depth
  Distance_DEM <- Gully_DEM$DISTANCE
  ggplot(data=Gully_DEM, aes(x=DISTANCE, y=Depth, group=1)) + geom_line(colour="red", size=2) +
    geom_point(colour= "black", size=4) + 
    xlim(0, max(Distance_DEM)) +
    ylim(max(Depth_DEM), -0.1) +
    xlab("Distance (m)") + ylab("Depth (m)") + ggtitle("Gully Cross Section DEM")
}

make_field_plot <- function(Gully_field) {
  Depth_Field <- Gully_field$Depth.until.soil.surface
  Distance_Field <- Gully_field$Length
  ggplot(data=Gully_field, aes(x=Length, y=Depth.until.soil.surface, group=1)) + geom_line(colour="Red", size=2) +
    geom_point(colour= "black", size=4) + 
    xlim(0, max(Distance_Field)) +
    ylim(max(Depth_Field), -0.1) +
    xlab("Distance (m)") + ylab("Depth (m)") + ggtitle("Gully Cross Section Field")
}