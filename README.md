## Know the Boundary

## Description

The Project lets user put the boundary coordinates and allows to segregate the coordinates into those boundaries.

It is the initial part of the project which is aimed to automate the segregating of coordinates according to the choice of boundaries set by the user. 
  
Later on, it would include the ML Model to extract the boundary coordinates on its own with the help of image analysis.

## Usage

Download necessary python Libraries,
- Library ```pandas```, this is used to read excel or csv files in which coornates are present.
  ```bash
  pip install pandas
  ```
  
- ```shapely```,
  ```bash
  pip install shapely
  ```
- Use
  ```bash
  pip install package_name --user
  ```
  This makes pip install packages in your home directory, which doesn't require any special privileges.
  ## Code

1. Import ``` pandas ``` Library 
   ```bash
   import pandas
   ```
   OR
   ```bash
   import pandas as pd
   ```
2. Import ```shapely``` library, particularly the ```Point``` and ```Polygon``` which are used to mark points and make a polygon out of them.
   ```bash
   from shapely.geometry import Point, Polygon
3. In ```boundary_file = r'C:\Users\boundary.csv'``` use the path of your ```.csv``` or ```.xlsx``` file of Boundary coordinates.
4. Edit the ```usecols``` variable values according to the name of the column which has the Latitude and Longitude.
5. Also edit the ```boundary_coordinates = list(zip(df['LAT'], df['LONG']))``` statement with the same names.
