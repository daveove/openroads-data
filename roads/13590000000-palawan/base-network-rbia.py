'''
A translation function for ogr2osm for the OpenRoads project:

Admin area
name:     Palawan
type:     province
id:       13590000000
data:     Basic road network

Data
files:    Palawan_RBIA_National_WGS84.shp
date:     Cleaned up RBIA road layer from DPWH
notes:    Provided by OpenRoads team

The following fields are used:    

Field           Used for              Reason
highway         or_responsibility=*          Main classification of road
                highway=*
'''

def filterTags(attrs):
  if not attrs: return

  tags = {}

  if attrs['SITE_NAME']:
    tags.update({'name': attrs['SITE_NAME']})

  # All roads in this dataset are national highways
  tags.update({'or_responsibility':'national', 'highway':'primary'})
  
  # Add the source
  tags.update({'source':'Road and Bridge Information Application - Department of Public Works and Highways (RBIA-DPWH)'})

  return tags