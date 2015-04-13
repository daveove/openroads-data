@sans_lt:           "Open Sans Regular","Arial Unicode MS Regular";
@sans:              "Open Sans Semibold","Arial Unicode MS Regular";

@place_halo:        #000;
@place_text:        #fff;

@fill: #000;

// Political boundaries //
#mun-boundaries-no-maritime {
  [zoom>=7] {
    line-join: round;
    line-color: @fill;
    line-width: 0.5;
  }
  [zoom>=12] { line-width: 1; }
  [zoom>=15] { line-width: 1.5; }
}

#mun-labels[zoom>11][zoom<15] {
    text-name:[NAME_2];
    text-face-name: @sans_lt;
    text-placement: point;
    text-fill: @place_text;
    text-halo-fill: fadeout(@place_halo,60%);
    text-halo-radius: 2;
    text-halo-rasterizer: fast;
    text-min-distance: 1;
    text-size: 10;
    [zoom>10]{text-size: 12;}
    [zoom>11]{text-size: 14;}
    [zoom>12]{text-size: 16;}
    [zoom>13]{text-size: 18;}
}