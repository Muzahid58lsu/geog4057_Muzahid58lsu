import json
import arcpy
import os

def jsonToFC(input_file, output_file):
    # Load JSON data
    with open(input_file, 'r') as file:
        tax_json = json.load(file)

    # Convert geometry from WKT
    for row in tax_json['data']:
        row[8] = arcpy.FromWKT(row[8])

    # Extract workspace and feature class name
    workspace, fcname = os.path.split(output_file)

    # Delete existing feature class if it exists
    if arcpy.Exists(output_file):
        arcpy.management.Delete(output_file)

    # Create feature class
    arcpy.management.CreateFeatureclass(
        out_path=workspace,
        out_name=fcname,
        geometry_type='POLYGON',
        spatial_reference=4236
    )

    # Prepare fields
    fields = tax_json['meta']['view']['columns']
    field_type = ['TEXT','TEXT','LONG','LONG','TEXT','LONG','TEXT','TEXT','TEXT','TEXT','TEXT','TEXT','TEXT']
    field_names = []
    for ind, field in enumerate(fields):
        name = field['name']
        if name == 'the_geom':
            continue
        if name.lower() == 'id':
            name = f'id_{ind}'
        max_len = min(10, len(name))
        name = name[:max_len]
        field_names.append(name)
    field_names = [f.replace(" ", "_").replace(".", "_") for f in field_names]

    # Add fields to the feature class
    for ind, field_name in enumerate(field_names):
        arcpy.management.AddField(output_file, field_name=field_name, field_type=field_type[ind])
    field_names.append('SHAPE@')

    # Insert rows
    with arcpy.da.InsertCursor(output_file, field_names=field_names) as cursor:
        for row in tax_json['data']:
            new_row = []
            for ind, value in enumerate(row):
                if ind == 8:
                    continue
                if value is None:
                    value = ""
                new_row.append(value)
            new_row.append(row[8])
            cursor.insertRow(new_row)

def main():
    input_file = r'C:\Users\muzah\OneDrive - Louisiana State University\Documents\Programming\geog4057_Muzahid58lsu\In_class_Project_02\no_tax.json'
    output_file = r'C:\Users\muzah\OneDrive - Louisiana State University\Documents\Programming\geog4057_Muzahid58lsu\In_class_Project_02\notax_fc.shp'
    jsonToFC(input_file, output_file)

if __name__ == "__main__":
    main()
