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
