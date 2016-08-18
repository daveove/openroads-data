'''
A translation function for ogr2osm for the OpenRoads project:

Admin area
name:     San Vicente
type:     municipality
id:       13591213000
data:     Basic road network

Data
files:    FV_010_Geoprocessed_fin.shp
notes:    Provided by OpenRoads team on August 10

'''

def filterTags(attrs):
  if not attrs: return

  tags = {}

  # Map the road type to the OSM highway classification
  if attrs['or_respons'] and attrs['or_respons'] == "barangay":
    tags.update({'or_responsibility':'barangay', 'highway': attrs['Type']})
  elif attrs['or_respons'] and attrs['or_respons'] == "municipal":
    tags.update({'or_responsibility':'municipal', 'highway': attrs['Type']})
  elif attrs['or_respons'] and attrs['or_respons'] == "municipal;barangay":
    tags.update({'or_responsibility': attrs['or_respons'], 'highway': attrs['Type']})
  elif attrs['or_respons'] and attrs['or_respons'] == "municipal;provincial":
    tags.update({'or_responsibility': attrs['or_respons'], 'highway': attrs['Type']})
  elif attrs['or_respons'] and attrs['or_respons'] == "national":
    tags.update({'or_responsibility':'national', 'highway': attrs['Type']})
  elif attrs['or_respons'] and attrs['or_respons'] == "provincial":
    tags.update({'or_responsibility':'provincial', 'highway': attrs['Type']})
  elif attrs['or_respons'] and attrs['or_respons'] == "private":
    tags.update({'or_responsibility':'private', 'highway': attrs['Type']})
  else:
    tags.update({'highway':'road'})

  # Add surface type
  if attrs['Surface_Ty']:
    tags.update({'surface': attrs['Surface_Ty'].lower()})

  # Add condition
  if attrs['Surface_Co']:
    tags.update({'or_condition': attrs['Surface_Co'].lower()})

  # Add width
  if attrs['Width']:
    tags.update({'or_width': attrs['Width']})

  # Add the source
  if attrs['Source']:
    tags.update({'source': attrs['Source']})

  return tags