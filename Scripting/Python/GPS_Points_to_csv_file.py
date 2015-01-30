# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# GPS_Points_to_csv_file.py
# Created on: 2015-01-29 21:05:12.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: GPS_Points_to_csv_file <Expression> <Tej_1_3_csv> 
# Description: 
# ---------------------------------------------------------------------------



########### Make sure to download the DEM of the Tejeria region (northern Spain).
########### The file can be downloaded from the following link:
########### https://sendit.wur.nl/Download.aspx?id=d6917691-0e09-4d22-ba08-1eeacba84d08
########### "Place the DEM in the following directory: "D:\\GS_Final\\data"



# Import arcpy module
import arcpy

# Check out any necessary licenses
arcpy.CheckOutExtension("spatial")

# Load required toolboxes
arcpy.ImportToolbox("D:/GS_Final/Scripting/Python/CreatePointsFromLinesTool/CreatePointsFromLines.pyt")

# Set Geoprocessing environments
arcpy.env.newPrecision = "DOUBLE"
arcpy.env.autoCommit = "1000"
arcpy.env.XYResolution = "0.001 Meters"
arcpy.env.XYDomain = ""
arcpy.env.scratchWorkspace = "D:\\GS_Final\\data\\Step.gdb"
arcpy.env.cartographicPartitions = ""
arcpy.env.terrainMemoryUsage = "true"
arcpy.env.MTolerance = ""
arcpy.env.compression = "LZ77"
arcpy.env.coincidentPoints = "MEAN"
arcpy.env.randomGenerator = "0 ACM599"
arcpy.env.outputCoordinateSystem = ""
arcpy.env.rasterStatistics = "STATISTICS 1 1"
arcpy.env.ZDomain = ""
arcpy.env.transferDomains = "false"
arcpy.env.resamplingMethod = "NEAREST"
arcpy.env.snapRaster = ""
arcpy.env.projectCompare = "NONE"
arcpy.env.cartographicCoordinateSystem = ""
arcpy.env.configKeyword = ""
arcpy.env.outputZFlag = "Disabled"
arcpy.env.qualifiedFieldNames = "true"
arcpy.env.tileSize = "128 128"
arcpy.env.parallelProcessingFactor = ""
arcpy.env.pyramid = "PYRAMIDS -1 NEAREST DEFAULT 75 NO_SKIP"
arcpy.env.referenceScale = ""
arcpy.env.extent = "DEFAULT"
arcpy.env.XYTolerance = "0.001 Meters"
arcpy.env.tinSaveVersion = "CURRENT"
arcpy.env.nodata = "NONE"
arcpy.env.MDomain = ""
arcpy.env.spatialGrid1 = "0"
arcpy.env.cellSize = "MAXOF"
arcpy.env.outputZValue = ""
arcpy.env.outputMFlag = "Same As Input"
arcpy.env.geographicTransformations = ""
arcpy.env.spatialGrid2 = "0"
arcpy.env.ZResolution = ""
arcpy.env.mask = ""
arcpy.env.spatialGrid3 = "0"
arcpy.env.maintainSpatialIndex = "false"
arcpy.env.workspace = "D:\\GS_Final\\data\\Step.gdb"
arcpy.env.MResolution = ""
arcpy.env.derivedPrecision = "DOUBLE"
arcpy.env.ZTolerance = ""

# Local variables:
Selected_Points = Expression
Line_From_Points = Selected_Points
Points_Along_Line = Line_From_Points
Values_Extracted_To_Points = Points_Along_Line
Values_Extracted_To_Points__2_ = Values_Extracted_To_Points
Values_Extracted_To_Points__3_ = Values_Extracted_To_Points__2_
Interval__units_are_in_units_of_input_ = "0.05"
Sort_Field = "y"
Value_Field = "RASTERVALU;Distance"
Delimiter = "COMMA"
Add_Field_Names_to_Output = "true"
Field_Name = "Distance"
Field_Name__2_ = "Distance"
Expression__2_ = "([OBJECTID] -1) * 0.05"
Field_Type = "FLOAT"
tejeria_dsm_medium_tif = "D:\\GS_Final\\data\\tejeria_dsm_medium.tif"
GPS_Points_Tejeria_shp = "D:\\GS_Final\\data\\GPS_Points_Tejeria.shp"

# Process: Select
# Set GPS points in the expression below or choose them when running the model in ArcGIS.
# Replace one of the following combinations for the 001 and 003 in the expression.
# Valid combinations are: (001, 003); (013, 016); (026, 028); (039, 041); (048, 050);
# (073, 075); (078, 079); (0115, 0117); (0146, 0147); (0148, 0149)
Expression = arcpy.GetParameterAsText(0)
if Expression == '#' or not Expression:
    Expression = "\"id\" = 'TEJGUL001' OR \"id\" = 'TEJGUL003'" 
arcpy.Select_analysis(GPS_Points_Tejeria_shp, Selected_Points, Expression)

# Process: Points To Line
arcpy.PointsToLine_management(Selected_Points, Line_From_Points, "", Sort_Field, "NO_CLOSE")

# Process: Create Points Along Lines
arcpy.CreatePointsAlongLines_alonglines(Line_From_Points, Points_Along_Line, Interval__units_are_in_units_of_input_, "VALUE", "NO_END_POINTS")

# Process: Extract Values to Points
arcpy.gp.ExtractValuesToPoints_sa(Points_Along_Line, tejeria_dsm_medium_tif, Values_Extracted_To_Points, "NONE", "VALUE_ONLY")

# Process: Add Field
arcpy.AddField_management(Values_Extracted_To_Points, Field_Name, Field_Type, "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field
arcpy.CalculateField_management(Values_Extracted_To_Points__2_, Field_Name__2_, Expression__2_, "VB", "")

# Process: Export Feature Attribute to ASCII
Tej_1_3_csv = arcpy.GetParameterAsText(1)
if Tej_1_3_csv == '#' or not Tej_1_3_csv:
    Tej_1_3_csv = "D:\\GS_Final\\data\\Results.gdb\\Tej_1_3.csv"
arcpy.ExportXYv_stats(Values_Extracted_To_Points__3_, Value_Field, Delimiter, Tej_1_3_csv, Add_Field_Names_to_Output)
