$(document).ready(function() {
    jQuery.validator.addMethod("customNombre", function(value, element) { 
    return this.optional( element ) || /^([a-zA-Zñ," "])+$/.test( value ); 
    }, "Porfavor, solo letras");    
    jQuery.validator.addMethod("customNumeros", function(value, element) { 
    return this.optional( element ) || /^([0-9])+$/.test( value ), required; 
    }, "Porfavor, solo numeros");   
    jQuery.validator.addMethod("customEmail", function(value, element) { 
    return this.optional( element ) || /^([a-zA-Z0-9_ñ\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/.test( value ); 
    }, "Porfavor, ingresa un correo valido. Ejemplo: correo@mail.com"); 
    jQuery.validator.addMethod("noEspacio",function(value, element) { 
    return value == '' || value.trim().length != 0;  
    }, "No espacios");
    
    
    var $formIntervencion = $('#formInter');
    if($formIntervencion.length){   
        $formIntervencion.validate({
            rules:{
                interAnestesia: {
                    required: true,
                    maxlength: 15,
                    minlength:3,
                },
                interApoyo: {
                    maxlength: 15,
                    minlength:3,
                },
                interCantApoyo: {
                    Number: true
                },
                interObs:{       
                    maxlength: 100,
                    minlength:2,
                },
                interInsumos:{
                    required: true,
                    maxlength: 3,
                    minlength:1,
                },
            },
            messages:{
                interAnestesia:{
                    required: "" ,
                    maxlength:"No puede tener más de 30 caracteres",
                    minlength:"No puede tener menos de 3 caracteres"
                },
                interApoyo:{    
                    maxlength:"No puede tener más de 30 caracteres",
                    minlength:"No puede tener menos de 3 caracteres"
                },
                interObs:{
                    maxlength:"No puede tener más de 100 caracteres",
                    minlength:"No puede tener menos de 2 caracteres"
                },
                interInsumos:{
                    required: "",
                    maxlength:"No puede tener más de 3 caracteres",
                    minlength:"No puede tener menos de 1 caracteres"
                },
            }
        });
    }
}); //function


