'''
A translation function for ogr2osm for the OpenRoads project:

Admin area
name:     Palawan
type:     province
id:       13590000000
data:     Basic road network

Data
files:    Palawan_REID_Local_WGS84.shp
date:     
notes:    Provided by OpenRoads team

The following fields are used:    

Field           Used for              Reason
highway         or_responsibility=*   Main classification of road
                highway=*
'''

def filterTags(attrs):
  if not attrs: return

  tags = {}

  # Map the road type to the OSM highway classification and or_responsibility
  if attrs['ROADCLASS'] and attrs['ROADCLASS'] == "Provincial Road":
    tags.update({'or_responsibility':'provincial', 'highway':'secondary'})
  elif attrs['ROADCLASS'] and attrs['ROADCLASS'] == "City Road":
    tags.update({'or_responsibility':'municipal', 'highway':'tertiary'})
  elif attrs['ROADCLASS'] and attrs['ROADCLASS'] == "Municipal Road":
    tags.update({'or_responsibility':'municipal', 'highway':'tertiary'})
  elif attrs['ROADCLASS'] and attrs['ROADCLASS'] == "Barangay Road":
    tags.update({'or_responsibility':'barangay', 'highway':'unclassified'})
  elif attrs['ROADCLASS'] and attrs['ROADCLASS'] == "Private Road":
    tags.update({'or_responsibility':'private', 'highway':'service'})
  else:
    tags.update({'highway':'road'})

  # Add the source
  tags.update({'source':'Palawan Provincial Government, in association with REID Foundation and World bank.'})

  return tags