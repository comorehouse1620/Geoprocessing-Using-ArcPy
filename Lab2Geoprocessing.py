
'''
Author: Claire Morehouse
Script: This script runs two clips and a buffer. The inputs for the first clip are the shapefile parks and
the zip shapefile. The output is a clipped parks file of only the parks in that shapefile. This script also
sets a workspace to a particular folder. The buffer inputs are the facilities, and the output are buffers
500 metters around the point feature facilities. This script also creates dissolved buffers. Finally, this
script clips the bike route shapefile with the zip shapefile to create a shapefile of the bike routes only in the
shapefile.
'''

# Clip parks with zip
arcpy.Clip_analysis("parks", "zip", "C:\\Users\\CMorehouse\\Desktop\\compprog\\p_Clip.shp")
#create workspace in folder
from arcpy import env
env.workspace = "C:\\Users\\CMorehouse\\Desktop\\compprog\\Lab2\\Data Lab_2_Geoprocessing_Python"
#create buffer, only worked when folder wasn't specified
arcpy.Buffer_analysis("facilities", "f_b.shp", "500 METERS")
#create buffer will disolved edges 
arcpy.Buffer_analysis("facilities", "facilities_buffer.shp", "500 METERS", "", "", "ALL")
#clip features using different method, specify variables for inputs prior to running clip
in_features = "bike_routes.shp"
clip_features = "zip.shp"
out_features = "bike_Clip.shp"
xy_tolerance = ""
#run clip
arcpy.Clip_analysis(in_features, clip_features, out_features, xy_tolerance)

