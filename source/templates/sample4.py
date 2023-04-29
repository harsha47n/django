"""
comments here
"""

import arcpy

arcpy.env.workspace = r"E:\Project works\Arcgis\Ex7_data\usa"
arcpy.env.overwriteOutput = True

input_list = arcpy.ListFeatureClasses("", "point", "")  # change so that all are iterated

for shp in input_list:

    print(shp)  # write this, as well as string text for line 2 that doesn't change

    for i in range(5, 56, 50):  # change so that all buffer distances are used, and write this
        arcpy.Buffer_analysis(in_features=shp, out_feature_class="test_single_buff_" + str(i) + "km.shp",
                              buffer_distance_or_field=str(i) + " Kilometers", dissolve_option="NONE")

        arcpy.Dissolve_management(in_features="test_single_buff_" + str(i) + "km.shp",
                                  out_feature_class="test_single_buff_" + str(i) + "km_d.shp", multi_part="SINGLE_PART")

        print(arcpy.GetCount_management("test_single_buff_" + str(i) + "km_d.shp"))  # write this
