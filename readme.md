# OpenRoads Data
This repository is part of the [OpenRoads](https://github.com/developmentseed/openroads) project. It contains scripts to process the raw source data into something that can be used by the project. It also contains the schema for the database that powers the [OpenRoads API](https://github.com/opengovt/openroads-api)

## Road network data
Road data is imported into OpenRoads in OSM XML format. To transform the source data into this format, this project uses [OGR2OSM](https://github.com/pnorman/ogr2osm). This python library uses translation files to map attributes to OSM tags.  
For the purpose of OpenRoads, we use a slightly adapted version that allows to specify a `uid` and `user` on each way, node and relation.

This repository contains mostly the org2osm translation files, organized by administrative area. These can be used as follows:

``` bash
python bin/ogr2osm/ogr2osm.py roads/041017000-malvar/source/MALVAR_ROAD_FINAL1.shp -t roads/041017000-malvar/network.py --add-user="openroads" --create-changeset
```

This command applies the translation file (`network.py`) to the Malvar shapefile provided by the municipality.

Other notes:

- unless stated otherwise, the data will be attributed to the OSM user `openroads`
- the data should be imported using negative id's. OGR2OSM takes care of this by default.

### Basic road network

- name
- or_responsibility
- or_condition
- surface

### Project roads
OpenRoads contains data about the basic Philippine road network, but also data about project roads such as FMR and TRIP. These are imported as ways into the OR database and then manually converted to relations.

## Administrative areas
The administrative areas are stored in its own repository: [OpenRoads Boundaries](https://github.com/opengovt/openroads-boundaries).

## Generating the baselayer
Until the automatic generation of the baselayer is implemented, we are manually rendering it using Mapbox Studio.

The basic styles are defined in the 'OR - Roads baselayer' project (`openroads.cc286209`). New road data that's delivered has to be uploaded as a data source and then added as a layer to the style.

1. Upload the data as a data source to Mapbox.  
Make sure the layer is called 'roads' and the road network itself is classified with the `or_responsibility` attribute, with one of the following values: national, provincial, municipal, barangay, private.  
Upload the data source to Mapbox.
2. Add the new data source as an extra layer to the style.  
Open the style and go to Layers -> Change source. Append the Mapbox ID.
3. Upload the style back to Mapbox

## Openroads Database
This repo also contains the Openroads Database Schema. [Documentation](db/README.md#openroads-db)
