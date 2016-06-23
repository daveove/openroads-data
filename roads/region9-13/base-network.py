'''
A translation function for ogr2osm for the OpenRoads project, used
to prepare road network data for:

Admin areas
- 9000000000, Region IX (Zamboanga Peninsula)
- 10000000000, Region X (Northern Mindanao)
- 11000000000, Region XI (Davao Region)
- 12000000000, Region XII (Soccsksargen)
- 13000000000, Region XII (Caraga)
- 17000000000, Autonomous region in Muslim Mindanao (ARMM)

Data
Provided by OpenRoads team and collected from three sources:

Type: National
Source: RBIA-DPWH
Extent: Mindanao

Type: Local
Source: Woodfield (manual tracing)
Extent: 6 pilot municipalities in Zamboanga Region

Type: Local
Source: OSM
Extent: Mindanao (-6 municipalities)

Type: Local
Source: WB (manual tracing)
Extent: additional for Lantapan municipality

'''

def filterTags(attrs):
  if not attrs: return

  tags = {}

  # Map the roads extracted from OSM
  if attrs['Source'] and attrs['Source'] == 'RBIA':
    # All roads in this dataset are national highways
    tags.update({'or_responsibility':'national', 'highway':'primary'})
  
    # Add the source
    tags.update({'source':'Road and Bridge Information Application - Department of Public Works and Highways (RBIA-DPWH)'})

  # Map the roads extracted from OSM
  elif attrs['Source'] and attrs['Source'] == 'OSM':

    # Map the highway classification
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
    
    # Add the source
    tags.update({'source':'OSM'})
  
  # Map the roads traced by Woodfield
  elif attrs['Source'] and attrs['Source'] == 'Woodfields Discovery':
    # Add the source
    tags.update({'source':'Woodfields'})
    
  # If everything else fails, attribute it to WB
  else:
    # Add the source
    tags.update({'source':'World Bank'})


  # Add the name of the road
  if attrs['name']:
    tags.update({'name': attrs['name']})
  elif attrs['SITE_NAME']:
    tags.update({'name': attrs['SITE_NAME']})


  return tags