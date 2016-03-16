'''
A translation function for ogr2osm for the OpenRoads project:

Admin area
name:     Bohol (part)
type:     Province
id:       7150000000
data:     Basic road network

Data
files:    crid-data-bohol.shp
source:   OpenRoads
notes:    Provided by WB, Ali Baqi



The following fields are dropped from the source shapefile:

Field           Definition            Reason
MUN_NAME        Name municipality     Automatically generated
BRGY_NAME       Name barangay         Automatically generated
RD_LENGTH       Length of road        Measured length of the road. Automatically generated


The following fields are used:    

Field           Used for              Reason
ROAD_NAME       name=ROAD_NAME        Name of the road
RD_CLASS        or_responsibility=*          Main classification of road
                highway=*
RD_TYPE         surface=RD_TYPE       Surface of the road
RD_COND         or_condition          Condition of the road
'''

def filterTags(attrs):
  if not attrs: return

  tags = {}

  # Add the road name
  if attrs['ROAD_NAME']:
    tags.update({'name':attrs['ROAD_NAME'].strip(' ').title()})

  # Map the road type to the OSM highway classification
  if attrs['RD_CLASS'] and attrs['RD_CLASS'].lower() == "national":
    tags.update({'or_responsibility':'national', 'highway':'primary'})
  elif attrs['RD_CLASS'] and attrs['RD_CLASS'].lower() == "provincial":
    tags.update({'or_responsibility':'provincial', 'highway':'secondary'})
  elif attrs['RD_CLASS'] and attrs['RD_CLASS'].lower() == "municipal":
    tags.update({'or_responsibility':'municipal', 'highway':'tertiary'})
  elif attrs['RD_CLASS'] and attrs['RD_CLASS'].lower() == "barangay":
    tags.update({'or_responsibility':'barangay', 'highway':'unclassified'})
  elif attrs['RD_CLASS'] and attrs['RD_CLASS'].lower() == "private":
    tags.update({'or_responsibility':'private', 'highway':'service'})
  else:
    tags.update({'highway':'road'})

  # Add the road type (surface)
  if attrs['RD_TYPE']:
    tags.update({'surface':attrs['RD_TYPE'].lower()})

  # Map the road condition
  # Catch bad spelling of excelent
  if attrs['RD_COND'] and attrs['RD_COND'].lower() == "excelent":
    tags.update({'or_condition':'excellent'})
  else:
    tags.update({'or_condition':attrs['RD_COND'].lower()})

  # Add the source
  tags.update({'source':'OpenRoads'})

  return tags