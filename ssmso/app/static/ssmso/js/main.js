// MUESTRA CONTENIDO
const add =  document.getElementById("radio2");
if (add) {
    add.addEventListener("click", () => {
        document.getElementById("jean").classList.remove("filtro")
        if (document.getElementById("botonValido") || document.getElementById("botonInvalido")) {
            if (document.getElementById("botonValido")) {
                document.getElementById("botonValido").classList.remove("filtro")
            }
            
            if (document.getElementById("botonInvalido")) {
                document.getElementById("botonInvalido").classList.add("filtro")
            }
        }
    
        if (document.getElementById("alertMessage")) {
            document.getElementById("alertMessage").classList.add("filtro")
        }
    });
}

// OCULTA CONTENIDO
const remove =  document.getElementById("radio1");
if (remove) {
    remove.addEventListener("click", () => {
        document.getElementById("jean").classList.add("filtro")
        if (document.getElementById("botonValido") || document.getElementById("botonInvalido")) {
            if (document.getElementById("botonValido")) {
                document.getElementById("botonValido").classList.add("filtro")
            }
    
            if (document.getElementById("botonInvalido")) {
                document.getElementById("botonInvalido").classList.remove("filtro")
            }
        }
        
        if (document.getElementById("alertMessage")) {
            document.getElementById("alertMessage").classList.remove("filtro")
        }
    });
}

// MUESTRA CONTENIDO 2
const add2 =  document.getElementById("radio3");
if (add2) {
    add2.addEventListener("click", () => {
        document.getElementById("jean2").classList.remove("filtro")
    });
}

// OCULTA CONTENIDO 2
const remove2 =  document.getElementById("radio4");
if (remove2) {
    remove2.addEventListener("click", () => {
        document.getElementById("jean2").classList.add("filtro")
        const jean = document.getElementById("inputJean2")
        jean.value = "";
    });
}

// MUESTRA CONTENIDO 3
const add3 =  document.getElementById("radio5");
if (add3) {
    add3.addEventListener("click", () => {
        document.getElementById("jean3").classList.remove("filtro")
    });
}

// OCULTA CONTENIDO 3
const remove3 =  document.getElementById("radio6");
if (remove3) {
    remove3.addEventListener("click", () => {
        const jean = document.getElementById("inputJean3")
        jean.value = "";
        document.getElementById("jean3").classList.add("filtro")
    });
}