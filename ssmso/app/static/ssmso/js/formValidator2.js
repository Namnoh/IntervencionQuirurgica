$(document).ready(function() {
  jQuery.validator.addMethod("customNombre", function(value, element) 
  {
  return this.optional(element) || /^[a-z-Z0-9ñ," "]+$/i.test(value);
  }, "Porfavor, solo letras");

  var $formTraslado = $('#formdata');
  if($formTraslado.length){
    $formTraslado.validate({
      rules:{
        trasEquipo:{
          required: true,
          maxlength: 30,
          minlength:1,
          customNombre: true
          },
        trasSala:{
          required: true,
          maxlength: 30,
          minlength:3,
          customNombre: true
        },
        trasObs:{
          maxlength: 200,
          minlength:1,
          customNombre: true
        }, 
      },
      messages:{
        trasEquipo:{
          required:"",
          maxlength:"No puede tener más de 30 caracteres",
          minlength:"No puede tener menos de 1 caracteres"
        },
        trasSala:{
          required:"",
          maxlength:"No puede tener más de 30 caracteres",
          minlength:"No puede tener menos de 3 caracteres"
        },
        trasObs:{
          maxlength:"No puede tener más de 50 caracteres",
          minlength:"No puede tener menos de 1 caracteres"
        },
      }
    });
  }
});



