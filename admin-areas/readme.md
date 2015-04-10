## Admin areas


### Custom IDs
The source shapefiles that were initially provided didn't contain any reference to an official geocoding standard like [PSGC](http://www.nscb.gov.ph/activestats/psgc/). Nor did the administrative areas have their own unique id.

For the OpenRoads project we constructed a custom ID of 10 or 11 characters.

| region | province | municipality | barangay |
| --- | --- | --- | --- |
| [00] | [00] | [0000] | [000] |

The region code consists of 1 or 2 digits.

In the original shapefiles, the provinces and municipalities contained some sort of ID. This was used as the basis to construct the OpenRoads ID. The region and barangay IDs were assigned in a more random fashion.

For example:

| id | type | name |
| --- | --- | --- |
| 2000000000 | 1 | Region II (Cagayan Valley) |
| 2110000000 | 2 | Batanes |
| 2110147000 | 3 | Basco |
| 2110147001 | 4 | Chanarian |
