'''
A translation function for ogr2osm for the OpenRoads project:

Admin area
name:     Malvar
type:     municipality
id:       041017000
data:     Basic road network

Data
files:    MALVAR_ROAD_FINAL2.shp
source:   Municipality of Malvar
date:     27/03/2015
notes:    Provided by Baby Balbuena, through Celina Agaton



The following fields are dropped from the source shapefile:

Field           Definition            Reason
Id              Id                    Automatically generated
LENGTH          Length road           Automatically generated


The following fields are used:    

Field           Used for              Reason
NAME            name=NAME             Name of the road
FOLDER          or_responsibility=*   Main classification of road (Malvar 2)
                highway=*
'''

def filterTags(attrs):
  if not attrs: return

  tags = {}

  # Add the road name
  if attrs['NAME']:
    tags.update({'name':attrs['NAME'].strip(' ').title()})

  # Map the road type to the OSM highway classification
  if attrs['FOLDER'] and attrs['FOLDER'] == "National Road":
    tags.update({'or_responsibility':'national', 'highway':'motorway'})
  else:
    tags.update({'highway':'road'})

  # Add the source
  tags.update({'source':'Municipality of Malvar'})

  return tags