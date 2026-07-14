// =============================================
// CARGAR FILTRO DE ESPECIES
// =============================================

function cargarFiltroEspecies() {

    console.log("Entró a cargarFiltroEspecies");

    const select = document.getElementById("filtroEspecie");

    // Limpiar opciones
    select.innerHTML = "";

    // Opción inicial
    const opcion = document.createElement("option");
    opcion.value = "";
    opcion.textContent = "Todas las especies";
    select.appendChild(opcion);

    // Obtener especies únicas
    const especies = [...new Set(
        datosPalmas.map(row => row.species)
    )];

    // Ordenar alfabéticamente
    especies.sort();

    // Agregar especies al selector
    especies.forEach(function (especie) {

        const option = document.createElement("option");

        option.value = especie;
        option.textContent = especie;

        select.appendChild(option);

    });

}

// =============================================
// CARGAR FILTRO DE DEPARTAMENTOS
// =============================================

function cargarFiltroDepartamentos() {

    const select = document.getElementById("filtroDepartamento");

    select.innerHTML = "";

    const opcion = document.createElement("option");

    opcion.value = "";

    opcion.textContent = "Todos";

    select.appendChild(opcion);

    // Obtener departamentos únicos
const departamentos = [];

datosPalmas.forEach(function(row){

    if(!row.stateProvince) return;

    let departamento = row.stateProvince
        .trim()
        .toUpperCase()
        .normalize("NFD")
        .replace(/[\u0300-\u036f]/g,"");

    // Correcciones
    departamento = departamento
        .replace("META DEPT.","META");

    // CHOCO/ALTO PUTUMAYO -> CHOCO
    if(
        departamento.includes("PUTUMAYO") &&
        departamento.includes("CHO")
    ){
        departamento = "CHOCO";
    }

    // Excluir San Andrés
    if(
        departamento === "SAN ANDRES & PROVIDENCIA" ||
        departamento === "ARCHIPIELAGO DE SAN ANDRES, PROVIDENCIA Y SANTA CATALINA"
    ){
        return;
    }

    departamentos.push(departamento);

});

const listaDepartamentos = [...new Set(departamentos)];

listaDepartamentos.sort();

    // Ordenar
    departamentos.sort();

    listaDepartamentos.forEach(function(departamento){

        if(departamento){

            const option = document.createElement("option");

            option.value = departamento;

            option.textContent = departamento;

            select.appendChild(option);

        }

    });

}

// =============================================
// APLICAR FILTROS
// =============================================

function aplicarFiltros() {

    const especie = document.getElementById("filtroEspecie").value;
    const departamento = document.getElementById("filtroDepartamento").value;
    const estado = document.getElementById("filtroCobertura").value;
    const anio = document.getElementById("filtroAnio").value;

    const datosFiltrados = datosPalmas.filter(function(row){

        // --------------------
        // Especie
        // --------------------

        if (
            especie !== "" &&
            row.species !== especie
        ) {
            return false;
        }

        // --------------------
        // Departamento
        // --------------------

        if (departamento !== "") {

            let dep = "";

            if (row.stateProvince) {

                dep = row.stateProvince
                    .trim()
                    .toUpperCase()
                    .normalize("NFD")
                    .replace(/[\u0300-\u036f]/g, "");

                dep = dep.replace("META DEPT.", "META");

                if (
                    dep.includes("PUTUMAYO") &&
                    dep.includes("CHO")
                ) {
                    dep = "CHOCO";
                }

                if (
                    dep === "SAN ANDRES & PROVIDENCIA" ||
                    dep === "ARCHIPIELAGO DE SAN ANDRES, PROVIDENCIA Y SANTA CATALINA"
                ) {
                    return false;
                }

            }

            if (dep !== departamento) {
                return false;
            }

        }

        // --------------------
        // Estado de amenaza
        // --------------------

        if (
            estado !== "" &&
            row["ESTADO DE AMENAZA"] !== estado
        ) {
            return false;
        }

        // --------------------
        // Año
        // --------------------

        if (
            anio !== "" &&
            String(row.year) !== anio
        ) {
            return false;
        }

        return true;

    });

    actualizarMapa(datosFiltrados);

}

// =============================================
// EVENTOS DE LOS FILTROS
// =============================================

document.getElementById("filtroEspecie")
    .addEventListener("change", aplicarFiltros);

document.getElementById("filtroDepartamento")
    .addEventListener("change", aplicarFiltros);

document.getElementById("filtroCobertura")
    .addEventListener("change", aplicarFiltros);

document.getElementById("filtroAnio")
    .addEventListener("change", aplicarFiltros);
// =============================================
// CARGAR FILTRO DE ESTADO DE AMENAZA
// =============================================

function cargarFiltroEstado() {

    const select = document.getElementById("filtroCobertura");

    select.innerHTML = "";

    const opcion = document.createElement("option");
    opcion.value = "";
    opcion.textContent = "Todos";

    select.appendChild(opcion);

    const estados = [...new Set(

        datosPalmas
            .map(row => row["ESTADO DE AMENAZA"])
            .filter(e => e && e !== "")

    )];

    estados.sort();

    estados.forEach(function(estado){

        const option = document.createElement("option");

        option.value = estado;
        option.textContent = estado;

        select.appendChild(option);

    });

}

// =============================================
// CARGAR FILTRO DE AÑOS
// =============================================

function cargarFiltroAnio(){

    const select = document.getElementById("filtroAnio");

    select.innerHTML = "";

    const opcion = document.createElement("option");

    opcion.value = "";
    opcion.textContent = "Todos";

    select.appendChild(opcion);

    const anios = [...new Set(

        datosPalmas
            .map(row => row.year)
            .filter(a => a)

    )];

    anios.sort((a,b)=>a-b);

    anios.forEach(function(anio){

        const option = document.createElement("option");

        option.value = anio;
        option.textContent = anio;

        select.appendChild(option);

    });

}