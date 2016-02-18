# Marine Protected Areas
This folder contains shapefile with Marine Protected Areas. It also contains conversion scripts to process the shapefile and prepare it for upload through the openroads-api.

To convert the Shapefile to OSM XML that can be uploaded:

`python bin/ogr2osm/ogr2osm.py -t mpa/4120000000-batangas/mpa.py mpa/4120000000-batangas/source/Batangas.shp --create-changeset`
