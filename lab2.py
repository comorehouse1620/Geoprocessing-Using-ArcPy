Arcpy.clip_analysis("parks", "zip", "C:\Users\CMorehouse\Desktop\compprog\Results\parks_Clip.shp"

arcpy.Clip_analysis("parks", "zip", "C:/Users/CMorehouse/Desktop/compprog/Results/parks_Clip.shp")
arcpy.Clip_analysis("parks", "zip", "C:\Users\CMorehouse\Desktop\compprog\Results\parks_Clip.shp")
arcpy.Clip_analysis("parks", "zip", "C:\\Users\\CMorehouse\\Desktop\\compprog\\Results\parks_Clip.shp")
arcpy.Clip_analysis("parks", "zip", "C:\\Users\\CMorehouse\\Desktop\\compprog\\Results\\parks_Clip.shp")
arcpy.Clip_analysis("parks", "zip", "C:\\Users\\CMorehouse\\Desktop\\compprog\\Results\\parks_Clip.shp")
arcpy.Clip_analysis("parks", "zip", "C:\\Users\\CMorehouse\\Desktop\\compprog\\Results\\p_Clip.shp")
arcpy.Clip_analysis("parks", "zip", "C:\\Users\\CMorehouse\\Desktop\\compprog\\p_Clip.shp")
from arcpy import env
env.workspace = "C:\\Users\\CMorehouse\\Desktop\\compprog"
arcpy.Buffer_analysis("facilities.shp", "compprog/facilities_buffer.shp", "500 METERS")
arcpy.Buffer_analysis("facilities", "compprog/facilities_buffer.shp", "500 METERS")
arcpy.Buffer_analysis("facilities.shp", "compprog/facilities_buffer.shp", "500 METERS")
arcpy.Buffer_analysis("facilities.shp", "compprog/facilities_buffer.shp", "500 METERS")
from arcpy import env
env.workspace = "C:\\Users\\CMorehouse\\Desktop\\compprog\\Lab2\\Data Lab_2_Geoprocessing_Python"
arcpy.Buffer_analysis("facilities.shp", "Results/facilities_buffer.shp", "500 METERS")
arcpy.Buffer_analysis("facilities.shp", "Lab2\\facilities_buffer.shp", "500 METERS")
arcpy.Buffer_analysis("facilities.shp", "Lab2\\f_b.shp", "500 METERS")
arcpy.Buffer_analysis("facilities", "Lab2\\f_b.shp", "500 METERS")
arcpy.Buffer_analysis("facilities", "f_b.shp", "500 METERS")
arcpy.Buffer_analysis("facilities", "facilities_buffer.shp", "500 METERS", "", "", "ALL")
in_features = "bike_routes.shp"
clip_features = "zip.shp"
out_features = "bike_Clip.shp"
xy_tolerance = ""
arcpy.Clip_analysis(in_features, clip_features, out_features, xy_tolerance)

