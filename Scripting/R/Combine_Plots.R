# This function will combine the crosssection profile of the DEM and the field measurements
# in the same plot.
make_plot <- function(Gully_DEM, Gully_field) {

  Depth_Field <- Gully_field$Depth.until.soil.surface
  Distance_Field <- Gully_field$Length
  Depth_DEM <- Gully_DEM$Depth
  Distance_DEM <- Gully_DEM$DISTANCE
  plot(Distance_Field, Depth_Field, type="l", main="Gully Cross Section", xlab="Distance (m)", 
     ylab="Depth (m)", ylim=c(max(Depth_Field), min(Depth_DEM)), lwd=4, col="Blue")
  points(Distance_Field, Depth_Field, lwd=6, col="Darkblue", ylim=c(max(Depth_Field), min(Depth_DEM)))
  #Add DEM profile to same graph
  lines(Distance_DEM, Depth_DEM, lwd=4, col="Red", ylim=rev(range(Depth_DEM)))
  points(Distance_DEM, Depth_DEM, lwd=6, col="darkred", ylim=rev(range(Depth_DEM)))
  legend("bottomright", c("Field","DEM"), lty=c(1,1), lwd=c(3, 3),col=c("blue","red"))
}