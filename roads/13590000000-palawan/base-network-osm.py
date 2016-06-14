'''
A translation function for ogr2osm for the OpenRoads project:

Admin area
name:     Palawan
type:     province
id:       13590000000
data:     Basic road network

Data
files:    Palawan_OSM_Local_WGS84.shp
date:     Extracted from OSM in May 2016
notes:    Provided by OpenRoads team

The following fields are used:    

Field           Used for              Reason
highway         or_responsibility=*          Main classification of road
                highway=*
'''

def filterTags(attrs):
  if not attrs: return

  tags = {}

  # Map the road type to the OSM highway classification
  if attrs['highway'] and attrs['highway'] == "primary":
    tags.update({'or_responsibility':'provincial', 'highway':'primary'})
  elif attrs['highway'] and attrs['highway'] == "secondary":
    tags.update({'or_responsibility':'provincial', 'highway':'secondary'})
  elif attrs['highway'] and attrs['highway'] == "tertiary":
    tags.update({'or_responsibility':'municipal', 'highway':'tertiary'})
  elif attrs['highway'] and attrs['highway'] == "unclassified":
    tags.update({'or_responsibility':'barangay', 'highway':'unclassified'})
  elif attrs['highway'] and attrs['highway'] == "service":
    tags.update({'or_responsibility':'private', 'highway':'service'})
  else:
    tags.update({'highway':'road'})

  if attrs['name']:
    tags.update({'name': attrs['name']})

  # Add the source
  tags.update({'source':'OSM'})

  return tags