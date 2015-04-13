## Political boundary layer
To create a visually compelling layer with political boundaries, it is necessary to hide the maritime boundaries. Since the Philippines is basically a big group of islands, it is relatively easy to generate such a layer using QGIS.

In this example we generate this layer for the municipalities and a separate layer with the centroids for label placement. The same process applies to other levels as well, such as barangays and provinces.

### 1. Generate layer with outside borders
Input shapefile: _Municipality.shp

1. Save as tmp_country.shp and open it in QGIS
2. Merge all features
  - Select all
  - Edit -> Merge selected features
3. Store it as a line shapefile
  - Vector -> Geometry Tools -> Polygon to line
  - Save it as country-boundary.shp

### 2. Generate final boundaries
Input shapefile: _Municipality.shp  

1. Open _Municipality.shp
2. Generate a line shapefile
  - Vector -> Geometry Tools -> Polygon to line
  - Save it as tmp_mun-boundary.shp
2. Cut the maritime boundaries (lengthy process)
  - Vector -> Geoprocessing tools -> Difference
  - Input: tmp_mun-boundary.shp, Difference: country-boundary.shp
  - Output: mun-boundaries-no-maritime.shp

Final file: **mun-boundaries-no-maritime.shp**

### 3. Generate municipal labels
Input shapefile: _Municipality.shp  

1. Open _Municipality.shp
2. Generate a point layer
  - Vector -> Geometry Tools -> Polygon centroids
  - Output: mun-labels.shp

Final file: **mun-labels.shp**