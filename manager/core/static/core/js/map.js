/* Cache de Rotas */
var routes = {}


/* Cache de alertas */
var alerts = {}


/* Componentes */
const listRoutes = document.getElementById('list-routes')
const listToasts = document.getElementById('list-toasts')
const listEvents = document.getElementById('list-events')


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
        const { code } = routes[route]
        return [
            "FORA DE ROTA", 
            `O ônibus ${bus} da rota ${code} está ${distance} metros fora da rota`
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
}

function addRoutesToSidebar(data) {
    const allRoutesOption = `<option value="0">Todas</option>`
    listRoutes.innerHTML = allRoutesOption + data.features.map(({ properties: props }) => `
        <option value="${props.id}">${props.code} - ${props.name}</option>
    `).join('')
}

function onEachRoute(feature, layer) {
    if (feature.properties) {
        const { code, name } = feature.properties
        layer.bindPopup(`${code} - ${name}`)
    }
}

const loadRoutes = data => {
    addRoutesToSidebar(data)
    addRoutesToMap(data)
    addRoutesToCache(data)
}

const showToastAlert = (label, description) => {
    const newToast = document.createElement('div')
    newToast.classList.add('toast', 'align-items-center', 'text-white', 'bg-danger', 'border-0')
    newToast.innerHTML = `
        <div class="d-flex">
            <div class="toast-body">
                <strong>${label}</strong>
                <br>${description}
            </div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
    `
    listToasts.appendChild(newToast)

    let newToastObj = new bootstrap.Toast(newToast)
    newToastObj.show()
}

const addEventToSidebar = (label, description) => {
    const newAlert = document.createElement('a')
    newAlert.classList.add('list-group-item', 'list-group-item-action')
    newAlert.setAttribute('href', '#')
    newAlert.innerHTML = `
        <div class="d-flex w-100 justify-content-between">
            <p class="mb-1"><strong>${label}</strong></p>
            <small>Há alguns segundos</small>
        </div>
        <small class="text-muted">${description}</small>
    `
    listEvents.appendChild(newAlert)
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
    const { type, extra } = data

    const [label, description] = ALERT_TYPE_MAP[type](extra)

    const busId = extra['bus']

    if (!alerts[busId]) {
        showToastAlert(label, description)
        addEventToSidebar(label, description)
        alerts[busId] = true
    }
}

sse.addEventListener('position', handlePositionEvent)

sse.addEventListener('alert', handleAlertEvent);


/* Limpa o cache de alertas a cada 60 segundos */
(function handleCache() {
    for (const busId in alerts) {
        alerts[busId] = false
    }
    setTimeout(handleCache, 60 * 1000)
})()
