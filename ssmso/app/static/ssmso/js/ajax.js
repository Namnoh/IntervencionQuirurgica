// function validaForm(){
//     if($("#primero").val()== ""){
//         alert("El campo ... no puede estar vacío.");
//         $("#primero").focus();
//         return false;
//     }
//     if($("#segundo").val()== ""){
//         alert("El campo ... no puede estar vacío.");
//         $("#segundo").focus();
//         return false;
//     }
//     if($("#tercero").val() == ""){
//         alert("El campo Dirección no puede estar vacío.");
//         $("#tercero").focus();
//         return false;
//     }
//     return true;
// }
// $(document).ready( function() {   
//     $("#botonenviar").click( function() {    
//         if(validaForm()){                               
//             $.post("...",$("#formdata").serialize(),function(res){
//                 $("#formulario").fadeOut("slow");   
//                 if(res == 1){
//                     $("#exito").delay(500).fadeIn("slow");      
//                 } else {
//                     $("#fracaso").delay(500).fadeIn("slow");   
//                 }
//             });
//         }
//     });    
// });