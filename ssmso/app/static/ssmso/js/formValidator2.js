$(document).ready(function(){

    jQuery.validator.addMethod("customNombre", function(value, element) { 
    return this.optional( element ) || /^([a-zA-Z])+$/.test( value ); 
    }, "Porfavor, solo letras");
  
    jQuery.validator.addMethod("custonNumeros", function(value, element) { 
      return this.optional( element ) || /^([0-9])+$/.test( value ); 
      }, "Porfavor, solo numeros");
   
    jQuery.validator.addMethod("customEmail", function(value, element) { 
    return this.optional( element ) || /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/.test( value ); 
    }, "Porfavor, ingresa un correo valido. Ejemplo: correo@mail.com");
    
    jQuery.validator.addMethod("noEspacio",function(value, element) { 
       return value == '' || value.trim().length != 0;  
     }, "No espacios");
  
     // inicio segundo formulario Intervencion
    var $formIntervencion = $('#formInter');
    if($formIntervencion.length){
        $formIntervencion.validate({
            rules:{
                interNombre: {
                  required: true,
                  maxlength: 30,
                  minlength:3,
                  customNombre: true
                },
                interAnestesia: {
                  required: true,
                  maxlength: 15,
                  minlength:3,
                  customNombre: true
                },
                interApoyo: {
                  required: true,
                  maxlength: 15,
                  minlength:3,
                  customNombre: true
                },
                interCantApoyo: {
                  required: true,
                  maxlength: 3,
                  minlength:1,
                  customNumeros: true
                },
                interObs:{
                  required: true,
                  maxlength: 100,
                  minlength:2,
                },
                interInsumos:{
                  required: true,
                  maxlength: 3,
                  minlength:1,
                  customNumeros: true
                }
            },
            mesagge:{
                interNombre:{
                  required: "" ,
                  maxlength:"No puede tener más de 30 caracteres",
                  minlength:"No puede tener menos de 3 caracteres"
                },
                interAnestesia:{
                  required: "" ,
                  maxlength:"No puede tener más de 30 caracteres",
                  minlength:"No puede tener menos de 3 caracteres"
                },
                interApoyo:{
                  required: "" ,
                  maxlength:"No puede tener más de 30 caracteres",
                  minlength:"No puede tener menos de 3 caracteres"
                },
                interCantApoyo:{
                  required: "" ,
                  maxlength:"No puede tener más de 3 caracteres",
                  minlength:"No puede tener menos de 1 caracteres"
                },
                interObs:{
                  required: "" ,
                  maxlength:"No puede tener más de 100 caracteres",
                  minlength:"No puede tener menos de 2 caracteres"
                },
                interInsumos:{
                  required: "",
                  maxlength:"No puede tener más de 3 caracteres",
                  minlength:"No puede tener menos de 1 caracteres"
                }
            }   
        });
    }// fin del segundo formulario Intervencion
});