'''
A translation function for ogr2osm for the OpenRoads project:

'''

def filterTags(attrs):
  if not attrs: return

  tags = {}

  # Add the MPA name
  if attrs['MPA_Name']:
    tags.update({'name':attrs['MPA_Name'].strip(' ').title()})

  # Add the mandatory MPA identifiers
  tags.update({'boundary':'protected_area'})
  tags.update({'protect_type':'marine_area'})

  # Add the source
  if attrs['source']:
    tags.update({'source':attrs['source']})

  return tags