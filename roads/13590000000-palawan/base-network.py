'''
A translation function for ogr2osm for the OpenRoads project:

Admin area
name:     Palawan
type:     province
id:       13590000000
data:     Basic road network

Data
files:    Palawan_Roads.shp
date:     27/03/2015
notes:    Provided by Karlo Pornadoro
          1. Data is only classified for now per road type.
          2. Data is gathered by combination of gpx and kml files, but then merged it to a single
          shapefile.

The following fields are used:    

Field           Used for              Reason
OR_RDCLASS      or_rdclass=*          Main classification of road
                highway=*
'''

def filterTags(attrs):
  if not attrs: return

  tags = {}

  # Map the road type to the OSM highway classification
  # Malvar 1 uses 'DESCR' to indicate road type, Malvar 2 uses 'FOLDER'
  if attrs['OR_RDCLASS'] and attrs['OR_RDCLASS'] == "National Highway":
    tags.update({'or_rdclass':'national', 'highway':'primary'})
  elif attrs['OR_RDCLASS'] and attrs['OR_RDCLASS'] == "Provincial Road":
    tags.update({'or_rdclass':'provincial', 'highway':'secondary'})
  elif attrs['OR_RDCLASS'] and attrs['OR_RDCLASS'] == "City Road":
    tags.update({'or_rdclass':'municipal', 'highway':'tertiary'})
  elif attrs['OR_RDCLASS'] and attrs['OR_RDCLASS'] == "Municipal Road":
    tags.update({'or_rdclass':'municipal', 'highway':'tertiary'})
  elif attrs['OR_RDCLASS'] and attrs['OR_RDCLASS'] == "Barangay Road":
    tags.update({'or_rdclass':'barangay', 'highway':'unclassified'})
  elif attrs['OR_RDCLASS'] and attrs['OR_RDCLASS'] == "Private Road":
    tags.update({'or_rdclass':'private', 'highway':'service'})
  else:
    tags.update({'highway':'road'})

  # Add the source
  tags.update({'source':'Palawan Provincial Government, in association with REID Foundation and World bank.'})

  return tags