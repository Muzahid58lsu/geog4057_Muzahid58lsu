# import arcpy
# arcpy.analysis.Buffer(
#     in_features="no_retail.shp",
#     out_feature_class="./retail_buffer.shp",
#     buffer_distance_or_field="500 Meters",
#     line_side="FULL",
#     line_end_type="ROUND",
#     dissolve_option="NONE",
#     dissolve_field=None,
#     method="PLANAR"
# )
import arcpy
import os

# Define the input and output file paths
input_file = r"C:\Users\muzah\OneDrive - Louisiana State University\Documents\Programming\geog4057_Muzahid58lsu\Assignment 2\no_retail.shp"
output_file = r"C:\Users\muzah\OneDrive - Louisiana State University\Documents\Programming\geog4057_Muzahid58lsu\Assignment 2\no_retail_buffer.shp"

# Debugging: Verify file paths
print("Current Directory:", os.getcwd())
print("Input File Exists:", os.path.exists(input_file))

# Check if input file exists
if not os.path.exists(input_file):
    raise FileNotFoundError(f"Input shapefile '{input_file}' not found!")

# Run the buffer analysis
arcpy.analysis.Buffer(
    in_features=input_file,
    out_feature_class=output_file,
    buffer_distance_or_field="500 Meters",
    line_side="FULL",
    line_end_type="ROUND",
    dissolve_option="NONE",
    dissolve_field=None,
    method="PLANAR"
)

print("Buffer analysis completed successfully.")
