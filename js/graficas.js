console.log("Graficas.js cargado correctamente");
// =============================================
// GRÁFICA 1 - REGISTROS POR AÑO
// =============================================

Papa.parse("data/registros_por_anio.csv", {

    download: true,

    header: true,

    dynamicTyping: true,

    skipEmptyLines: true,

    complete: function(results){

        const anios = [];
        const registros = [];

        results.data.forEach(function(row){

            anios.push(row.year);

            registros.push(row.count);

        });

        const ctx = document
            .getElementById("graficaAnio")
            .getContext("2d");

        new Chart(ctx,{

            type:"line",

            data:{

                labels:anios,

                datasets:[{

                    label:"Registros",

                    data:registros,

                    borderColor:"#2E7D32",

                    backgroundColor:"rgba(46,125,50,0.15)",

                    borderWidth:3,

                    fill:true,

                    tension:0.35,

                    pointRadius:4,

                    pointBackgroundColor:"#1B5E20"

                }]

            },

            options:{

    responsive:true,

    maintainAspectRatio:false,

    animation:{
        duration:1500
    },

    plugins:{

        legend:{
            display:false
        },

        tooltip:{

            backgroundColor:"#1B4332",

            titleColor:"#FFFFFF",

            bodyColor:"#FFFFFF",

            cornerRadius:8,

            padding:12,

            displayColors:false

        }

    },

    scales:{

        x:{

            ticks:{
                color:"#4A4A4A"
            },

            grid:{
                display:false
            }

        },

        y:{

            beginAtZero:true,

            ticks:{
                color:"#4A4A4A"
            },

            grid:{
                color:"rgba(0,0,0,.05)"
            }

        }

    }

}

        });

    }

});

// =============================================
// GRÁFICA 2 - TOP DEPARTAMENTOS
// =============================================

Papa.parse("data/departamentos.csv", {

    download: true,

    header: true,

    dynamicTyping: true,

    skipEmptyLines: true,

    complete: function(results){

        const departamentos = {};

        results.data.forEach(function(row){

            let dep = row.stateProvince;

            if(!dep) return;

            dep = dep
                .trim()
                .toUpperCase()
                .normalize("NFD")
                .replace(/[\u0300-\u036f]/g,"");

            // Correcciones
            dep = dep.replace("META DEPT.","META");

            if(
                dep.includes("PUTUMAYO") &&
                dep.includes("CHO")
            ){
                dep = "CHOCO";
            }

            // Excluir San Andrés
            if(
                dep === "SAN ANDRES & PROVIDENCIA" ||
                dep === "ARCHIPIELAGO DE SAN ANDRES, PROVIDENCIA Y SANTA CATALINA"
            ){
                return;
            }

            if(!departamentos[dep]){
                departamentos[dep] = 0;
            }

            departamentos[dep] += Number(row.count);

        });

        // Convertir a arreglo
        const lista = Object.entries(departamentos);

        // Ordenar
        lista.sort(function(a,b){

            return b[1]-a[1];

        });

        // Top 10
        const top = lista.slice(0,10);

        const nombres = top.map(x=>x[0]);

        const valores = top.map(x=>x[1]);

        const ctx = document
            .getElementById("graficaDepartamentos")
            .getContext("2d");

        new Chart(ctx,{

            type:"bar",

            data:{

                labels:nombres,

                datasets:[{

                    data:valores,

                    backgroundColor:"#2E7D32",

hoverBackgroundColor:"#1B5E20",

                    borderRadius:8

                }]

            },

            options:{

    indexAxis:"y",

    responsive:true,

    maintainAspectRatio:false,

    animation:{
        duration:1500
    },

    plugins:{

        legend:{
            display:false
        },

        tooltip:{

            backgroundColor:"#1B4332",

            titleColor:"#FFFFFF",

            bodyColor:"#FFFFFF",

            cornerRadius:8,

            padding:12,

            displayColors:false,

            callbacks:{

                label:function(context){

                    return context.raw.toLocaleString("es-CO") + " registros";

                }

            }

        }

    },

    scales:{

        x:{

            beginAtZero:true,

            ticks:{
                color:"#4A4A4A"
            },

            grid:{
                color:"rgba(0,0,0,.05)"
            }

        },

        y:{

            ticks:{

                color:"#2D2D2D",

                font:{
                    size:12,
                    weight:"bold"
                }

            },

            grid:{
                display:false
            }

        }

    }

}
        });

    }

});
// =============================================
// GRÁFICA 3 - TOP ESPECIES
// =============================================

Papa.parse("data/top10_especies.csv", {

    download: true,

    header: true,

    dynamicTyping: true,

    skipEmptyLines: true,

    complete: function(results){

        const especies = [];
        const registros = [];

        results.data.forEach(function(row){

            especies.push(row.species);

            registros.push(row.count);

        });

        const ctx = document
            .getElementById("graficaEspecies")
            .getContext("2d");

        new Chart(ctx,{

            type:"bar",

            data:{

                labels:especies,

                datasets:[{

    data:registros,

    backgroundColor:"#4E8F3A",

    hoverBackgroundColor:"#2E7D32",

    borderRadius:10,

    borderSkipped:false,

    barPercentage:0.70,

    categoryPercentage:0.75

}]

            },

           options:{

    indexAxis:"y",

    responsive:true,

    maintainAspectRatio:false,

    animation:{
        duration:1500
    },

    plugins:{

        legend:{
            display:false
        },

        tooltip:{

            backgroundColor:"#1B4332",

            titleColor:"#FFFFFF",

            bodyColor:"#FFFFFF",

            cornerRadius:8,

            padding:12,

            displayColors:false,

            callbacks:{

                label:function(context){

                    return context.raw.toLocaleString("es-CO") + " registros";

                }

            }

        }

    },

    scales:{

        x:{

            beginAtZero:true,

            ticks:{
                color:"#4A4A4A"
            },

            grid:{
                color:"rgba(0,0,0,.05)"
            }

        },

        y:{

            ticks:{

                color:"#2D2D2D",

                font:{

                    size:11,

                    style:"italic"

                }

            },

            grid:{
                display:false
            }

        }

    }

}

        });

    }

});
// =============================================
// GRÁFICA 4 - ESTADO DE AMENAZA
// =============================================

Papa.parse("data/estado_amenaza.csv", {

    download: true,

    header: true,

    dynamicTyping: true,

    skipEmptyLines: true,

    complete: function(results){

        const estados = [];
        const cantidades = [];
        const colores = [];

        results.data.forEach(function(row){

            const codigo = row["ESTADO DE AMENAZA"];

switch(codigo){

    case "CR":
        estados.push("CR - En Peligro Crítico");
        break;

    case "EN":
        estados.push("EN - En Peligro");
        break;

    case "VU":
        estados.push("VU - Vulnerable");
        break;

    case "NT":
        estados.push("NT - Casi Amenazada");
        break;

    case "LC":
        estados.push("LC - Preocupación Menor");
        break;

    default:
        estados.push(codigo);

}

            cantidades.push(row.count);

            switch(row["ESTADO DE AMENAZA"]){

                case "CR":
                    colores.push("#C62828");
                    break;

                case "EN":
                    colores.push("#EF6C00");
                    break;

                case "VU":
                    colores.push("#F9A825");
                    break;

                case "NT":
                    colores.push("#7CB342");
                    break;

                case "LC":
                    colores.push("#2E7D32");
                    break;

                default:
                    colores.push("#90A4AE");

            }

        });

        const ctx = document
            .getElementById("graficaAmenaza")
            .getContext("2d");

        new Chart(ctx,{

            type:"doughnut",

            data:{

                labels:estados,

                datasets:[{

                    data:cantidades,

                    backgroundColor:colores,

                    borderWidth:2,

                    borderColor:"#FFFFFF"

                }]

            },

            options:{

    responsive:true,

    maintainAspectRatio:false,

    cutout:"68%",

    animation:{
        duration:1800
    },

    plugins:{

        legend:{

            position:"bottom",

            labels:{

                usePointStyle:true,

                pointStyle:"circle",

                padding:20,

                color:"#2D2D2D",

                font:{
                    size:12,
                    weight:"bold"
                }

            }

        },

        tooltip:{

            backgroundColor:"#1B4332",

            titleColor:"#FFFFFF",

            bodyColor:"#FFFFFF",

            cornerRadius:8,

            padding:12,

            callbacks:{

                label:function(context){

                    const total = context.dataset.data.reduce((a,b)=>a+b,0);

                    const valor = context.raw;

                    const porcentaje = ((valor/total)*100).toFixed(1);

                    return `${valor.toLocaleString("es-CO")} registros (${porcentaje}%)`;

                }

            }

        }

    }

}

        });

    }

});