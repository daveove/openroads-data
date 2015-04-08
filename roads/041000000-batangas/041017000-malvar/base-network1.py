'''
A translation function for ogr2osm for the OpenRoads project:

Admin area
name:     Malvar
type:     municipality
id:       041017000
data:     Basic road network

Data
files:    MALVAR_ROAD_FINAL1.shp
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
DESCR           or_class=*            Main classification of road (Malvar 1)
                highway=*
'''

def filterTags(attrs):
  if not attrs: return

  tags = {}

  # Add the road name
  if attrs['NAME']:
    tags.update({'name':attrs['NAME'].strip(' ').title()})

  # Map the road type to the OSM highway classification
  # Malvar 1 uses 'DESCR' to indicate road type, Malvar 2 uses 'FOLDER'
  if attrs['DESCR'] and attrs['DESCR'] == "PNR":
    tags.update({'or_class':'national', 'highway':'primary'})
  elif attrs['DESCR'] and attrs['DESCR'] == "Provincial Road":
    tags.update({'or_class':'provincial', 'highway':'secondary'})
  elif attrs['DESCR'] and attrs['DESCR'] == "Municipal Road":
    tags.update({'or_class':'municipal', 'highway':'tertiary'})
  elif attrs['DESCR'] and attrs['DESCR'] == "Barangay Road":
    tags.update({'or_class':'barangay', 'highway':'unclassified'})
  elif attrs['DESCR'] and attrs['DESCR'] == "Private Road":
    tags.update({'or_class':'private', 'highway':'service'})
  else:
    tags.update({'highway':'road'})

  # Add the source
  tags.update({'source':'Municipality of Malvar'})

  return tags