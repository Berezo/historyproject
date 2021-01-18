var osm = new ol.layer.Tile({
    source: new ol.source.OSM(),
    title: 'OpenStreetMap',
    baseLayer: true
});

var orto = new ol.layer.Image({
    source: new ol.source.ImageWMS({
        url: 'http://mapy.geoportal.gov.pl/wss/service/img/guest/ORTO/MapServer/WMSServer',
        params: {
            LAYERS: 'Raster'
        }
    }),
    title: 'Ortofotomapa',
    baseLayer: true,
    visible: false
});

var map = new ol.Map({
    target: 'map',
    layers: [osm, orto],
    view: new ol.View({
        center: ol.proj.fromLonLat([22.8, 51.35]),
        zoom: 8
    })
});