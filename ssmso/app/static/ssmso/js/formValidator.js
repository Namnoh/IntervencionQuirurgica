//  FORMS REGISTRO DE RECEPCIÓN
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



  // inicio del primer formulario Recepcion

  var $formRegistro = $('#formReg');
  if($formRegistro.length){
    $formRegistro.validate({
      rules:{
        paNombres:{
          required: true,
          maxlength: 30,
          minlength:3,
          customNombre: true
        },
        paApellidos: {
          required: true,
          maxlength: 30,
          minlength:3,
          customNombre: true
        },
        paRut: {
          required: true,
          maxlength: 10,
          minlength:9
        
        },
        paCorreoEmerg: {
          required: true,
          customEmail: true,
          noEspacio: true
        },

      },
      messages: {
        paNombres:{
          required: "" ,
          maxlength:"No puede tener más de 30 caracteres",
          minlength:"No puede tener menos de 3 caracteres"
        },
        paApellidos:{
          required: "" ,
          maxlength:"No puede tener más de 30 caracteres",
          minlength:"No puede tener menos de 3 caracteres"
        },
        paRut:{
          required:"",
          maxlength:"El rut no puede contener más de 10 caracteres",
          minlength:"El rut no puede contener menos de 9 caracteres"
        },
        paCorreoEmerg:{
          required:""
        },

      }
    });
  }
  // fin del primer formulario Recepcion
}); // FUNCTION

