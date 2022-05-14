/* Cache de Rotas */
var routes = {}


/* Funções de inicialização */
fetch('/api/routes')
    .then(response => response.json())
    .then(data => loadRoutes(data))

var map = L.map('map', {
    maxBounds: [[-7.040130, -34.965619], [-7.253412, -34.787168]],
    minZoom: 12,
    maxZoom: 18
}).setView([-7.145422, -34.859948], 12)

var setBaseMap = L.tileLayer(mapTileLayer, {
    attribution: mapAttribution
}).addTo(map)


/* Constantes */
const ALERT_TYPE_MAP = {
    "OFF_ROUTE": ({ bus, route, distance }) => {
        const { code, name } = routes[route]
        return [
            "Fora de rota", 
            `O ônibus ${bus} da rota ${code} (${name}) está ${distance} metros fora da rota`
        ]
    }
}


/* Funções para carga das rotas */
function addRoutesToMap(data) {
    layer = L.geoJSON(data, {onEachFeature: onEachRoute}).addTo(map);
}

function addRoutesToCache(data) {
    data.features.forEach(feat => {
        routes[feat.properties.pk] = feat.properties
    })
    console.log(routes)
}

function onEachRoute(feature, layer) {
    if (feature.properties) {
        const { code, name } = feature.properties
        layer.bindPopup(`${code} - ${name}`)
    }
}

const loadRoutes = data => {
    addRoutesToMap(data)
    addRoutesToCache(data)
}


/* Ícone dos ônibus */
var busIcon = L.icon({
    iconSize: [25, 33],
    iconAnchor: [16, 33],
    popupAnchor: [-3, -34],
    iconUrl: iconUrl
})


/* Server-sent events */
const sse = new EventSource('http://localhost:3000/events')

var markers = {}

const handlePositionEvent = event => {
    const data = JSON.parse(event.data)
    const { lat, lng, vehicle_id: busId, route_id: routeId, correlation_key: corrKey } = data

    if (!markers[busId]) {
        markers[busId] = L.marker([lat, lng], {icon: busIcon})
            .addTo(map)
            .bindPopup(`Veículo ${busId}`)
    } else {
        markers[busId].setLatLng([lat, lng])
    }
}

const handleAlertEvent = event => {
    const data = JSON.parse(event.data)
    const { type, extra, correlation_key: corrKey } = data

    const [label, description] = ALERT_TYPE_MAP[type](extra)

    console.log(label, description, corrKey)
}

sse.addEventListener('position', handlePositionEvent)

sse.addEventListener('alert', handleAlertEvent)
