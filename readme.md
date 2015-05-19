# OpenRoads Data
This repository is part of the [OpenRoads](https://github.com/developmentseed/openroads) project. It contains scripts to process the raw source data into something that can be used by the project.

## Road network data
Road data is imported into OpenRoads in OSM XML format. To transform the source data into this format, this project uses [OGR2OSM](https://github.com/pnorman/ogr2osm). This python library uses translation files to map attributes to OSM tags.  
For the purpose of OpenRoads, we use a slightly adapted version that allows to specify a `uid` and `user` on each way, node and relation.

This repository contains mostly the org2osm translation files, organized by administrative area. These can be used as follows:

``` bash
python bin/ogr2osm/ogr2osm.py roads/041017000-malvar/source/MALVAR_ROAD_FINAL1.shp -t roads/041017000-malvar/network.py --add-user="openroads"
```

This command applies the translation file (`network.py`) to the Malvar shapefile provided by the municipality.

Other notes:

- unless stated otherwise, the data will be attributed to the OSM user `openroads`
- the data should be imported using negative id's. OGR2OSM takes care of this by default.

### Basic road network
[add info about main attributes]

### Project roads
OpenRoads contains data about the basic Philippine road network, but also data about project roads such as FMR and TRIP. These are imported as ways into the OR database and then manually converted to relations.

## Administrative areas
[notes about what info is stored about the admin areas]
final format = geojson
