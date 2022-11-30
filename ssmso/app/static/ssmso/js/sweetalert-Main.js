function exito(){
    Swal.fire(
        'Registro Exitoso',
        'Se ha creado el registro quirúrgico exitosamente',
        'success'
    )
}

function eliminarReg(){
    Swal.fire({
        title: '¿Está seguro?',
        text: "¡Este cambio es irreversible!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, eliminar.'
      }).then((result) => {
        if (result.isConfirmed) {

          window.location.href = "/delReg/"+id+"/"
        }
      })
}