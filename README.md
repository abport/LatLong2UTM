# Batch converte latitude and longitude coordinates to UTM (Universal Transverse Mercator)

Batch converting latitude and longitude coordinates to UTM (Universal Transverse Mercator) can be a useful task when working with geographic data. For example, you may have a large dataset with coordinates in latitude/longitude format, but need to perform analysis or visualization using UTM coordinates. In this post, we will discuss how to create a Python script that can batch convert a list of coordinates from a CSV file to UTM and save the output to a new CSV file.

To perform the coordinate conversion, we will use the `pyproj` library, which provides functionality for performing projections and coordinate transformations. Specifically, we will use the `pyproj.transform` function to convert the coordinates from latitude/longitude (EPSG:4326) to UTM (EPSG:32611).

Here is the complete script that can batch convert latitude and longitude coordinates from a CSV file to UTM and save the output in a new CSV file:
```python
import csv
import pyproj
import utm

def lat_long_to_utm(lat, lon):
    # Determine the UTM zone number based on the latitude and longitude
    utm_zone = utm.from_latlon(lat, lon)[2]
    # Define the UTM projection
    utm_projection = pyproj.Proj(proj='utm', zone=utm_zone, ellps='WGS84')
    # Convert the lat/long to UTM coordinates
    utm_x, utm_y = pyproj.transform(pyproj.Proj(init='epsg:4326'), utm_projection, lon, lat)
    # Return the UTM coordinates as a tuple
    return utm_x, utm_y

# Read the input CSV file
with open('input.csv', 'r') as input_file:
    reader = csv.reader(input_file)
    # Read the header row
    header = next(reader)
    # Read the rest of the rows
    rows = [row for row in reader]

# Convert the coordinates and save the output
with open('output.csv', 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    # Write the header row
    writer.writerow(header + ['UTM X', 'UTM Y'])
    # Loop through the input rows
    for row in rows:
        # Convert the coordinates
        lat, lon = float(row[0]), float(row[1])
        utm_x, utm_y = lat_long_to_utm(lat, lon)
        # Write the converted coordinates and original values to the output file
        writer.writerow(row + [utm_x, utm_y])
```

To use this script, you will need to have a CSV file named `input.csv` in the same directory as the script. The CSV file should contain a header row and rows containing latitude and longitude values. 
```
Latitude,Longitude
37.774929,-122.419416
40.7128,-74.0060
34.052235,-118.243683
35.689487,139.691706
```

The script will read the input file, determine the UTM zone for each coordinate, convert the coordinates to UTM, and write the output to a new CSV file named `output.csv`.

Using this script, you can quickly and easily batch convert a large number of coordinates from latitude/longitude to UTM, allowing you to perform analysis or visualization using the UTM coordinate system.



