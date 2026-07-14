// =====================================================
// CAPAS.JS
// GeoPalmas Colombia
// =====================================================

// ------------------------------
// VARIABLES
// ------------------------------

let capaPriorizacion;
let capaRiesgo;

// ------------------------------
// COLORES
// ------------------------------

function colorRiesgo(valor) {

    switch (String(valor).trim().toLowerCase()) {

        case "muy alto":
            return "#8B0000";

        case "alto":
            return "#F21F1F";

        case "medio":
            return "#FF8C1A";

        case "bajo":
            return "#F5F36A";

        case "muy bajo":
        default:
            return "#FFF9D7";

    }

}

// ------------------------------
// ESTILO
// ------------------------------

function estilo(feature) {

    return {

        color: "#555",
        weight: 1,
        fillColor: colorRiesgo(feature.properties.riesgo),
        fillOpacity: 0.75

    };

}

// ------------------------------
// HOVER
// ------------------------------

function resaltar(e) {

    const layer = e.target;

    layer.setStyle({

        weight: 3,
        color: "#000",
        fillOpacity: 0.9

    });

    layer.bringToFront();

}

function quitarResaltado(e) {

    capaPriorizacion.resetStyle(e.target);

    if (capaRiesgo) {

        capaRiesgo.resetStyle(e.target);

    }

}

// ------------------------------
// POPUP
// ------------------------------

function popup(feature, layer) {

    const p = feature.properties;

    layer.bindPopup(`

        <h3>${p.LEVEL_3}</h3>

        <b>🌴 Especies de palmas:</b> ${p.riqueza_palmas}<br>

        <b>🌳 Bosque:</b> ${Number(p.bosque_pct).toFixed(1)} %<br>

        <b>🌾 Agricultura:</b> ${Number(p.agro_pct).toFixed(1)} %<br>

        <b>🚨 Alertas 2025:</b> ${p.alertas_2025 ?? 0}<br>

        <b>🤖 Predicción 2026:</b> ${Number(p.pred_alertas_2026).toFixed(2)}<br>

        <b>⚠ Riesgo:</b> ${p.riesgo}

    `);

    layer.on({

        mouseover: resaltar,

        mouseout: quitarResaltado

    });

}

// ------------------------------
// LEYENDA
// ------------------------------

//======================================================
// LEYENDA MODELO DE PRIORIZACIÓN
//======================================================

const leyendaPriorizacion = L.control({
    position: "bottomright"
});

leyendaPriorizacion.onAdd = function () {

    const div = L.DomUtil.create("div");

    div.style.background = "white";
    div.style.padding = "10px";
    div.style.borderRadius = "8px";
    div.style.boxShadow = "0 0 8px rgba(0,0,0,.3)";
    div.style.lineHeight = "22px";

    div.innerHTML = `
        <b>🎯 Modelo de Priorización</b><br><br>

        <i style="background:#8B0000;width:18px;height:18px;display:inline-block;"></i> Muy alto<br>

        <i style="background:#F21F1F;width:18px;height:18px;display:inline-block;"></i> Alto<br>

        <i style="background:#FF8C1A;width:18px;height:18px;display:inline-block;"></i> Medio<br>

        <i style="background:#F5F36A;width:18px;height:18px;display:inline-block;"></i> Bajo<br>

        <i style="background:#FFF9D7;width:18px;height:18px;border:1px solid gray;display:inline-block;"></i> Muy bajo
    `;

    return div;

};


//======================================================
// LEYENDA RIESGO
//======================================================

const leyendaRiesgo = L.control({
    position: "bottomright"
});

leyendaRiesgo.onAdd = function () {

    const div = L.DomUtil.create("div");

    div.style.background = "white";
    div.style.padding = "10px";
    div.style.borderRadius = "8px";
    div.style.boxShadow = "0 0 8px rgba(0,0,0,.3)";
    div.style.lineHeight = "22px";

    div.innerHTML = `
        <b>🚨 Riesgo de Deforestación</b><br><br>

        <i style="background:#8B0000;width:18px;height:18px;display:inline-block;"></i> Muy alto<br>

        <i style="background:#F21F1F;width:18px;height:18px;display:inline-block;"></i> Alto<br>

        <i style="background:#FF8C1A;width:18px;height:18px;display:inline-block;"></i> Medio<br>

        <i style="background:#F5F36A;width:18px;height:18px;display:inline-block;"></i> Bajo<br>

        <i style="background:#FFF9D7;width:18px;height:18px;border:1px solid gray;display:inline-block;"></i> Muy bajo
    `;

    return div;

};

// ------------------------------
// CONTROL DE CAPAS
// ------------------------------

const overlays = {

    "🌴 Registros": markers

};

const controlCapas = L.control.layers(

    mapasBase,

    overlays,

    {

        collapsed: false

    }

).addTo(map);

// =====================================================
// CAPA 1
// MODELO DE PRIORIZACIÓN
// =====================================================

fetch("geo/Municipios_con_palmas_con_riesgo_alertas_2026.geojson")

.then(r => r.json())

.then(data => {

    capaPriorizacion = L.geoJSON(data, {

        style: estilo,

        onEachFeature: popup

    });

    controlCapas.addOverlay(

        capaPriorizacion,

        "Modelo de Priorización"

    );

});

// =====================================================
// CAPA 2
// RIESGO DE DEFORESTACIÓN
// =====================================================

fetch("geo/Municipios_con_riesgo_alertas_2026.geojson")

.then(r => r.json())

.then(data => {

    capaRiesgo = L.geoJSON(data, {

        style: estilo,

        onEachFeature: popup

    });

    controlCapas.addOverlay(

        capaRiesgo,

        "Riesgo de Deforestación"

    );

});
//======================================================
// MOSTRAR LEYENDAS
//======================================================

map.on("overlayadd", function (e) {

    if (e.name === "Modelo de Priorización") {

        leyendaPriorizacion.addTo(map);

    }

    if (e.name === "Riesgo de Deforestación") {

        leyendaRiesgo.addTo(map);

    }

});

map.on("overlayremove", function (e) {

    if (e.name === "Modelo de Priorización") {

        map.removeControl(leyendaPriorizacion);

    }

    if (e.name === "Riesgo de Deforestación") {

        map.removeControl(leyendaRiesgo);

    }

});