// ===================================================
// CARGAR FICHAS
// ===================================================

let fichas = {};

// ===================================================
// NORMALIZAR NOMBRE
// ===================================================

function normalizarNombre(nombre){

    if(!nombre) return "";

    return nombre
        .trim()
        .toLowerCase();

}

// ===================================================
// LEER CSV DE FICHAS
// ===================================================

Papa.parse("data/Fichas_especies_actualizado.csv",{

    download:true,

    header:true,

    skipEmptyLines:true,

    encoding:"UTF-8",

    complete:function(resultado){

        resultado.data.forEach(function(fila){

            fichas[normalizarNombre(fila.NOMBRE_CIENTIFICO)] = fila;

        });

        console.log("Fichas cargadas:",Object.keys(fichas).length);

    }

});

// ===================================================
// MOSTRAR FICHA
// ===================================================

function mostrarFicha(nombre){

    const especie = fichas[normalizarNombre(nombre)];

    if(!especie){

        document.querySelector(".panel").innerHTML = `

        <h2>Información</h2>

        <p><b>${nombre}</b></p>

        <p>No existe una ficha para esta especie.</p>

        `;

        return;

    }

    // Imagen

    const rutaImagen =
        "images/" +
        especie.NOMBRE_CIENTIFICO.replace(/ /g,"_") +
        ".jpg";

    document.querySelector(".panel").innerHTML = `

        <h2>${especie.NOMBRE_CIENTIFICO}</h2>

        <img
            src="${rutaImagen}"
            style="
                width:100%;
                border-radius:12px;
                margin:15px 0;
            "
            onerror="this.src='images/sin_imagen.jpg'"
        >

        <p><strong>Nombre común</strong><br>
        ${especie.NOMBRE_COMUN}</p>

        <br>

        <p><strong>Familia</strong><br>
        ${especie.FAMILIA}</p>

        <br>

        <p><strong>Estado de amenaza</strong><br>
        ${especie.ESTADO_AMENAZA}</p>

        <br>

        <p><strong>Número de registros</strong><br>
        ${especie.REGISTROS}</p>

        <br>

        <p><strong>Uso reportado</strong><br>
        ${especie.USO_REPORTADO}</p>

        <br>

        <p><strong>Fuente</strong><br>
        ${especie.FUENTE_USO}</p>

        <br>

        <p><strong>Atribución</strong><br>
        ${especie.ATRIBUCION}</p>

        <br>

        <a href="${especie.URL_OBSERVACION}" target="_blank">

            🔗 Ver observación

        </a>

    `;

}