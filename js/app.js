// ==========================================
// CREAR MAPA
// ==========================================
let datosPalmas = [];

const map = L.map("map").setView([4.6, -74.1], 6);

// ==========================================
// MAPAS BASE
// ==========================================

// OpenStreetMap
const osm = L.tileLayer(
    "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
    {
        attribution: "&copy; OpenStreetMap contributors"
    }
);

// ESRI World Imagery
const esri = L.tileLayer(
    "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    {
        attribution: "Tiles © Esri"
    }
);

// Agregar OpenStreetMap por defecto
osm.addTo(map);

// Control de capas
const mapasBase = {
    "OpenStreetMap": osm,
    "Imagen Satelital (Esri)": esri
};


// ==========================================
// CLUSTERS
// ==========================================

const markers = L.markerClusterGroup();

map.addLayer(markers);

function actualizarMapa(datos){

    markers.clearLayers();

    const ubicacionesUnicas = new Map();

    datos.forEach(function(row){

        const lat = row.decimalLatitude;
        const lon = row.decimalLongitude;

        if(lat && lon){

            const clave = `${row.species}_${lat}_${lon}`;

            if(!ubicacionesUnicas.has(clave)){
                ubicacionesUnicas.set(clave,row);
            }

        }

    });

    ubicacionesUnicas.forEach(function(row){

        const marker = L.marker([
            row.decimalLatitude,
            row.decimalLongitude
        ]);

        marker.bindPopup(`
            <b><i>${row.scientificName}</i></b>
        `);

        marker.on("click",function(){

            mostrarFicha(row.species);

        });

        markers.addLayer(marker);

    });

}
// ==========================================
// LEER CSV
// ==========================================

Papa.parse("data/ocurrencias_palmas_enriquecido.csv", {

    download: true,
    header: true,
    dynamicTyping: true,
    skipEmptyLines: true,

    complete: function(results){

        datosPalmas = results.data;

        console.log("CSV cargado");

        // ==========================================
        // UBICACIONES ÚNICAS (ESPECIE + COORDENADAS)
        // ==========================================

        const ubicacionesUnicas = new Map();

        // ==========================
        // ESTADÍSTICAS
        // ==========================

        const especies = new Set();
        const departamentos = new Set();
        const amenazadas = new Set();

        results.data.forEach(function(row){

            // --------------------------
            // Estadísticas
            // --------------------------

            if(row.species)
                especies.add(row.species);

         if (row.stateProvince) {

    let departamento = row.stateProvince
        .trim()
        .toUpperCase()
        .normalize("NFD")
        .replace(/[\u0300-\u036f]/g, "");

    // Correcciones conocidas
    departamento = departamento
        .replace("META DEPT.", "META");

    // Si contiene PUTUMAYO y CHO, dejarlo como CHOCO
    if (
        departamento.includes("PUTUMAYO") &&
        departamento.includes("CHO")
    ) {
        departamento = "CHOCO";
    }

    // Excluir San Andrés y Providencia
    if (
        departamento === "SAN ANDRES & PROVIDENCIA" ||
        departamento === "ARCHIPIELAGO DE SAN ANDRES, PROVIDENCIA Y SANTA CATALINA"
    ) {
        return;
    }

    departamentos.add(departamento);

}
            if(
                row["ESTADO DE AMENAZA"] === "EN" ||
                row["ESTADO DE AMENAZA"] === "VU" ||
                row["ESTADO DE AMENAZA"] === "CR"
            ){
                amenazadas.add(row.species);
            }

            // --------------------------
            // GUARDAR UBICACIONES ÚNICAS
            // --------------------------

            const lat = row.decimalLatitude;
            const lon = row.decimalLongitude;

            if(lat && lon){

                const clave = `${row.species}_${lat}_${lon}`;

                if(!ubicacionesUnicas.has(clave)){
                    ubicacionesUnicas.set(clave, row);
                }

            }

        });

        // ==========================================
        // CREAR MARCADORES ÚNICOS
        // ==========================================

        /* ubicacionesUnicas.forEach(function(row){

            const marker = L.marker([
                row.decimalLatitude,
                row.decimalLongitude
            ]);

            marker.bindPopup(`
                <b><i>${row.scientificName}</i></b>
            `);

            marker.on("click", function(){

                mostrarFicha(row.species);

            });

            markers.addLayer(marker);

        });

        map.addLayer(markers);*/
        actualizarMapa(datosPalmas);

        // ===================================
        // LLENAR TARJETAS
        // ===================================

        document.getElementById("totalRegistros").innerHTML =
    ubicacionesUnicas.size.toLocaleString("es-CO");

        document.getElementById("totalEspecies").innerHTML =
            especies.size;

        document.getElementById("totalDepartamentos").innerHTML =
            departamentos.size;

        const criticas = new Set();

results.data.forEach(function(row){
    if(row["ESTADO DE AMENAZA"] === "CR"){
        criticas.add(row.species);
    }
});

document.getElementById("totalCriticas").innerHTML =
    criticas.size;

        cargarFiltroEspecies();
cargarFiltroDepartamentos();
cargarFiltroEstado();
cargarFiltroAnio();

        console.log("Registros:", results.data.length);
        console.log("Especies:", especies.size);
        console.log("Departamentos:", departamentos.size);
        console.log("Amenazadas:", amenazadas.size);
        console.log("Ubicaciones únicas:", ubicacionesUnicas.size);

        console.log([...departamentos].sort());

    }

});