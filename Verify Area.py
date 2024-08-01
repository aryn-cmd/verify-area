import pandas as pd
from shapely.geometry import Point, Polygon

# Define the path to your CSV or Excel file
boundary_file = r'C:\Users\boundary.csv'  # Change the extension to .xlsx if it's an Excel file

# Read the file into a DataFrame
if boundary_file.endswith('.csv'):
    df = pd.read_csv(boundary_file, usecols=['LAT', 'LONG'])
elif boundary_file.endswith('.xlsx'):
    df = pd.read_excel(boundary_file, usecols=['LAT', 'LONG'])

# Extract the boundary coordinates as a list of tuples
boundary_coordinates = list(zip(df['LAT'], df['LONG']))

# Create a polygon from the boundary coordinates
boundary_polygon = Polygon(boundary_coordinates)

def is_within_boundary(latitude, longitude):
    point = Point(latitude, longitude)
    return boundary_polygon.contains(point)



latitude = float(input("Enter the latitude: "))
longitude = float(input("Enter the longitude: "))


if is_within_boundary(latitude, longitude):
    print("The coordinate is within the boundary.")
else:
    print("The coordinate is outside the boundary.")
