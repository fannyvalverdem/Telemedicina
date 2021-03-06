$('#data_table').DataTable({
    "destroy": true,
    rowCallback: function( row, data, index ) {
        var especialidad=String($('#id_usuario_doc').html())
        if (data['especialidad']['nombre'] == especialidad) {
            $(row).hide();
        }
    },
    
    "ajax": 
        {
        "method": "GET",
        "url": "/api/doctor/",
        "dataSrc": "",
        "error": function(xhr, status, error) {
            console.log("readyState: " + xhr.readyState);
            console.log("responseText: "+ xhr.responseText);
            console.log("status: " + xhr.status);
            console.log("text status: " + status);
            console.log("error: " + error);
        },
    
    },
    
    "columns": [
        { data: "imagen"},
        { data: "user_id.persona_id.nombre"},
        { data: "user_id.persona_id.apellido"},
        { data: "especialidad.nombre"},
        { data: "especialidad"}
    ],
    columnDefs: [
        { width: 100, targets: 0, render: function(data) {
            var image = '';
            if (data == null){
                image = `<img src="https://via.placeholder.com/300x300" width="100%">`;
            } else {
                image = '<img src="' + data + '" width="100%">';
            }
            return image;
        }},
        { width: 150, targets: 1},
        { width: 150, targets: 2},
        { width: 150, targets: 3},
        { width: 150, className: "text-center", targets: 4, render: function(data){
            return `<a href="/confirmacion_cita/" class="btn btn-primary" role="button"></a>
                 `
        }},
    ],
});

$('#data_table_paquete').DataTable({
    "destroy": true,
    "ajax": 
        {
        "method": "GET",
        "url": "/api/paquete/",
        "dataSrc": "",
        "error": function(xhr, status, error) {
            console.log("readyState: " + xhr.readyState);
            console.log("responseText: "+ xhr.responseText);
            console.log("status: " + xhr.status);
            console.log("text status: " + status);
            console.log("error: " + error);
        },
    
    },
    
    "columns": [
        { data: "nombre"},
        { data: "descripcion"},
        { data: "especialidad.nombre"},
        { data: "duracion"},
        { data: "citas"},
        { data: "precio"}
    ],
    columnDefs: [
        { width: 100, targets: 0},
        { width: 150, targets: 1},
        { width: 150, targets: 2},
        { width: 150, targets: 3},
        { width: 150, targets: 4},
        { width: 150, targets: 5},
    ],
});

$('#data_table_tarifa').DataTable({
    "destroy": true,
    "ajax": 
        {
        "method": "GET",
        "url": "/api/tarifas/",
        "dataSrc": "",
        "error": function(xhr, status, error) {
            console.log("readyState: " + xhr.readyState);
            console.log("responseText: "+ xhr.responseText);
            console.log("status: " + xhr.status);
            console.log("text status: " + status);
            console.log("error: " + error);
        },
    
    },
    
    "columns": [
        { data: "nombre"},
        { data: "descripcion"},
        { data: "precio"}
    ],
    columnDefs: [
        { width: 100, targets: 0},
        { width: 100, targets: 1},
        { width: 100, targets: 2},
    ],
});


$('#data_table_citas').DataTable({
    "destroy": true,
    rowCallback: function( row, data, index ) {
        var id_doc=String($('#id_usuario_doc').html())
        if (data['estado'] == "agendada" || data['doctor_id']['user_id']['email']!=id_doc) {
            $(row).hide();
        }
    },
    "ajax": 
        {
        "method": "GET",
        "url": "/api/consulta/",
        "dataSrc": "",
        "error": function(xhr, status, error) {
            console.log("readyState: " + xhr.readyState);
            console.log("responseText: "+ xhr.responseText);
            console.log("status: " + xhr.status);
            console.log("text status: " + status);
            console.log("error: " + error);
        },
    
    },

        "columns": [
            { data: "paciente_id.user_id.persona_id.nombre"},
            { data: "paciente_id.user_id.persona_id.apellido"},
            { data: "detalle.fecha_reser"},
            { data: "detalle.fecha_prog"},
            { data: "detalle.precio"}
        ],
        columnDefs: [
            { width: 100, targets: 0},
            { width: 150, targets: 1},
            { width: 150, targets: 2},
            { width: 150, targets: 3},
            { width: 150, targets: 4},
        ],
    
});

$('#data_table_rmedico').DataTable({
    "destroy": true,
    "ajax": 
        {
        "method": "GET",
        "url": "/api/match_especialidades/",
        "dataSrc": "",
        "error": function(xhr, status, error) {
            console.log("readyState: " + xhr.readyState);
            console.log("responseText: "+ xhr.responseText);
            console.log("status: " + xhr.status);
            console.log("text status: " + status);
            console.log("error: " + error);
        },
    
    },
    
    "columns": [
        { data: "doctor.identificador_medico"},
        { data: "doctor.user_id.persona_id.nombre"},
        { data: "doctor.user_id.persona_id.apellido"},
        { data: "especialidad.nombre"},
        { data: "doctor.citas_realizadas"},
        { data: "doctor.calificacion_total"}
    ],
    columnDefs: [
        { width: 100, targets: 0},
        { width: 100, targets: 1},
        { width: 100, targets: 2},
        { width: 100, targets: 3},
        { width: 100, targets: 4},
        { width: 100, targets: 5},
    ],
});


$('#data_table_vinculadas').DataTable({
    "destroy": true,
    // rowCallback: function( row, data, index ) {
    //     var usuario={{ usuario.username }};
    //     if (data['paciente']['user_id']['username'] == usuario) {
    //         $(row).hide();
    //     }
    // },
    "ajax": 
        {
        "method": "GET",
        "url": "/api/grupofamiliar/",
        "dataSrc": "",
        "error": function(xhr, status, error) {
            console.log("readyState: " + xhr.readyState);
            console.log("responseText: "+ xhr.responseText);
            console.log("status: " + xhr.status);
            console.log("text status: " + status);
            console.log("error: " + error);
        },
    
    },
    
    "columns": [
        { data: "paciente.user_id.persona_id.nombre"},
        { data: "paciente.user_id.persona_id.apellido"},
        { data: "paciente.user_id.username"},
    ],
    columnDefs: [
        { width: 100, targets: 0},
        { width: 100, targets: 1},
        { width: 100, targets: 2},
        { width: 150, className: "text-center", targets: 5, render: function(data){
            return `<a href="/cambiar_cuenta/" class="btn btn-primary" role="button"><i class="fas fa-eye"></i></a>
                 `
        }},
    ],
});

$('#data_table_resumen').DataTable({
    "destroy": true,
    // rowCallback: function( row, data, index ) {
    //     var usuario={{ usuario.username }};
    //     if (data['paciente']['user_id']['username'] == usuario) {
    //         $(row).hide();
    //     }
    // },
    "ajax": 
        {
        "method": "GET",
        "url": "/api/grupofamiliar/",
        "dataSrc": "",
        "error": function(xhr, status, error) {
            console.log("readyState: " + xhr.readyState);
            console.log("responseText: "+ xhr.responseText);
            console.log("status: " + xhr.status);
            console.log("text status: " + status);
            console.log("error: " + error);
        },
    
    },
    
    "columns": [
        { data: "paciente.user_id.persona_id.nombre"},
        { data: "paciente.user_id.persona_id.apellido"},
        { data: "paciente.user_id.username"},
    ],
    columnDefs: [
        { width: 100, targets: 0},
        { width: 100, targets: 1},
        { width: 100, targets: 2},
        
    ],
});



$('#data_table_rpaciente').DataTable({
    "destroy": true,
    "ajax": 
        {
        "method": "GET",
        "url": "/api/pagos_paciente/",
        "dataSrc": "",
        "error": function(xhr, status, error) {
            console.log("readyState: " + xhr.readyState);
            console.log("responseText: "+ xhr.responseText);
            console.log("status: " + xhr.status);
            console.log("text status: " + status);
            console.log("error: " + error);
        },
    
    },
    
    "columns": [
        { data: "paciente.user_id.persona_id.nombre"},
        { data: "paciente.user_id.persona_id.apellido"},
        { data: "paciente.citas_realizadas"},
        { data: "pago_total"}
    ],
    columnDefs: [
        { width: 100, targets: 0},
        { width: 100, targets: 1},
        { width: 100, targets: 2},
        { width: 100, targets: 3},
    ],
});


$('#data_table_respecialidad').DataTable({
    "destroy": true,
    "ajax": 
        {
        "method": "GET",
        "url": "/api/detalles_especialidad/",
        "dataSrc": "",
        "error": function(xhr, status, error) {
            console.log("readyState: " + xhr.readyState);
            console.log("responseText: "+ xhr.responseText);
            console.log("status: " + xhr.status);
            console.log("text status: " + status);
            console.log("error: " + error);
        },
    
    },
    
    "columns": [
        { data: "especialidad.nombre"},
        { data: "citas_realizadas"},
        { data: "pagos_total"},
        { data: "total_doctor"}
    ],
    columnDefs: [
        { width: 100, targets: 0},
        { width: 100, targets: 1},
        { width: 100, targets: 2},
        { width: 100, targets: 3},
    ],
});

$('#data_table_rpaquetes').DataTable({
    "destroy": true,
    "ajax": 
        {
        "method": "GET",
        "url": "/api/detalles_paquetes/",
        "dataSrc": "",
        "error": function(xhr, status, error) {
            console.log("readyState: " + xhr.readyState);
            console.log("responseText: "+ xhr.responseText);
            console.log("status: " + xhr.status);
            console.log("text status: " + status);
            console.log("error: " + error);
        },
    
    },
    
    "columns": [
        { data: "paquetes.nombre"},
        { data: "paquetes.descripcion"},
        { data: "paquetes.precio"},
        { data: "paquetes.especialidad.nombre"},
        { data: "total_pacientes"},
        { data: "pagos_total"}
    ],
    columnDefs: [
        { width: 100, targets: 0},
        { width: 100, targets: 1},
        { width: 100, targets: 2},
        { width: 100, targets: 3},
        { width: 100, targets: 4},
        { width: 100, targets: 5},
    ],
});

$('#data_table_publicidad').DataTable({
    "destroy": true,
    "ajax": 
        {
        "method": "GET",
        "url": "/api/publicidad/",
        "dataSrc": "",
        "error": function(xhr, status, error) {
            console.log("readyState: " + xhr.readyState);
            console.log("responseText: "+ xhr.responseText);
            console.log("status: " + xhr.status);
            console.log("text status: " + status);
            console.log("error: " + error);
        },
    
    },
    
    "columns": [
        { data: "nombre"},
        { data: "imagen"},
        { data: "fecha"},
        { data: "dueno"},
        { data: "precio"},
        { data: "telefono"},
        { data: "ciudad"},
        { data: "direccion"}
    ],
    columnDefs: [
        { width: 100, targets: 0},
        { width: 100, targets: 1},
        { width: 100, targets: 2},
        { width: 100, targets: 3},
        { width: 100, targets: 4},
        { width: 100, targets: 5},
        { width: 100, targets: 6},
        { width: 100, targets: 7},
    ],
});


$('#data_table_info_medica').DataTable({
    "destroy": true,
    "ajax": 
        {
        "method": "GET",
        "url": "/api/info_medica/",
        "dataSrc": "",
        "error": function(xhr, status, error) {
            console.log("readyState: " + xhr.readyState);
            console.log("responseText: "+ xhr.responseText);
            console.log("status: " + xhr.status);
            console.log("text status: " + status);
            console.log("error: " + error);
        },
    
    },
    
    "columns": [
        { data: "id"},
        { data: "peso"},
        { data: "talla"},
        { data: "sys"},
        { data: "dia"},
        { data: "pulse"},
        { data: "glucosa"},
        { data: "colesterol"}
    ],
    columnDefs: [
        { width: 100, targets: 0},
        { width: 100, targets: 1},
        { width: 100, targets: 2},
        { width: 100, targets: 3},
        { width: 100, targets: 4},
        { width: 100, targets: 5},
        { width: 100, targets: 6},
        { width: 100, targets: 7},
    ],
});


$('#data_table_noticias').DataTable({
    "destroy": true,
    "ajax": 
        {
        "method": "GET",
        "url": "/api/noticias/",
        "dataSrc": "",
        "error": function(xhr, status, error) {
            console.log("readyState: " + xhr.readyState);
            console.log("responseText: "+ xhr.responseText);
            console.log("status: " + xhr.status);
            console.log("text status: " + status);
            console.log("error: " + error);
        },
    
    },
    
    "columns": [
        { data: "id"},
        { data: "imagen"},
        { data: "titulo"},
        { data: "fuente"},
    ],
    columnDefs: [
        { width: 100, targets: 0},
        { width: 100, targets: 1},
        { width: 100, targets: 2},
        { width: 100, targets: 3},
    ],
});


$('#data_table_consejos').DataTable({
    "destroy": true,
    "ajax": 
        {
        "method": "GET",
        "url": "/api/consejos/",
        "dataSrc": "",
        "error": function(xhr, status, error) {
            console.log("readyState: " + xhr.readyState);
            console.log("responseText: "+ xhr.responseText);
            console.log("status: " + xhr.status);
            console.log("text status: " + status);
            console.log("error: " + error);
        },
    
    },
    
    "columns": [
        { data: "id"},
        { data: "imagen"},
        { data: "titulo"},
        { data: "fuente"},
    ],
    columnDefs: [
        { width: 100, targets: 0},
        { width: 100, targets: 1},
        { width: 100, targets: 2},
        { width: 100, targets: 3},
    ],
});

$('#data_table_ver_medico_fav').DataTable({
    "destroy": true,
    "ajax": 
        {
        "method": "GET",
        "url": "/api/medico_favorito/",
        "dataSrc": "",
        "error": function(xhr, status, error) {
            console.log("readyState: " + xhr.readyState);
            console.log("responseText: "+ xhr.responseText);
            console.log("status: " + xhr.status);
            console.log("text status: " + status);
            console.log("error: " + error);
        },
    
    },
    
    "columns": [
        { data: "imagen"},
        { data: "medico.doctor.user_id.persona_id.nombre"},
        { data: "medico.doctor.user_id.persona_id.apellido"},
        { data: "medico.especialidad.nombre"},
    ],
    columnDefs: [
        { width: 100, targets: 0, render: function(data) {
            var image = '';
            if (data == null){
                image = `<img src="http://127.0.0.1:8000/static/imagenes/doctor.png" width="100%">`;
            } else {
                image = '<img src="' + data + '" width="100%">';
            }
            return image;
        }},
        { width: 100, targets: 1},
        { width: 100, targets: 2},
        { width: 100, targets: 3},
    ],
});
li=[];
$('#data_table_ingresar_medico_fav').DataTable({
    rowCallback: function( row, data ) {
        if (li.length==0){
            li.push(data['doctor_id']['identificador_medico']);
        }
        else{
            for (var i=0; i<li.length;i++){
                if (li[i]==data['doctor_id']['identificador_medico']){
                    $(row).hide();
                }
                else{
                    li.push(data['doctor_id']['identificador_medico'])
                }
            }
        }
    },
    "destroy": true,
    "ajax": 
        {
        "method": "GET",
        "url": "/api/consulta/",
        "dataSrc": "",
        "error": function(xhr, status, error) {
            console.log("readyState: " + xhr.readyState);
            console.log("responseText: "+ xhr.responseText);
            console.log("status: " + xhr.status);
            console.log("text status: " + status);
            console.log("error: " + error);
        },
    
    },
    
    "columns": [
        { data: "imagen"},
        { data: "doctor_id.user_id.persona_id.nombre"},
        { data: "doctor_id.user_id.persona_id.apellido"},
        { data: "detalle.calificacion"},
        { data: "doctor_id.id"},
    ],
    columnDefs: [
        { width: 100, targets: 0, render: function(data) {
            var image = '';
            if (data == null){
                image = `<img src="http://127.0.0.1:8000/static/imagenes/doctor.png" width="100%">`;
            } else {
                image = '<img src="' + data + '" width="100%">';
            }
            return image;
        }},
        { width: 100, targets: 1},
        { width: 100, targets: 2},
        { width: 100, targets: 3},
        { width: 150, className: "text-center", targets: 4, render: function(data){
            
            return '<a href="/ingresar_fav/?id=' + data + '" class="btn btn-primary" role="button"></a>'
        }},
    ],
});

$('#data_table_cobrar').DataTable({
    "destroy": true,
    rowCallback: function( row, data, index ) {
        var id_doc=String($('#id_usuario_doc').html())
        if (data['estado'] == "pagado" || data['doctor']['user_id']['email']!=id_doc) {
            $(row).hide();
        }
    },
    "ajax": 
        {
        "method": "GET",
        "url": "/api/pagos_medico/",
        "dataSrc": "",
        "error": function(xhr, status, error) {
            console.log("readyState: " + xhr.readyState);
            console.log("responseText: "+ xhr.responseText);
            console.log("status: " + xhr.status);
            console.log("text status: " + status);
            console.log("error: " + error);
        },
    
    },

        "columns": [
            { data: "fecha"},
            { data: "hora"},
            { data: "precio"}
        ],
        columnDefs: [
            { width: 100, targets: 0},
            { width: 150, targets: 1},
            { width: 150, targets: 2},
        ],
    
});


$('#data_table_pagos_medico').DataTable({
    "destroy": true,
    rowCallback: function( row, data, index ) {
        var id_doc=String($('#id_usuario_doc').html())
        if (data['estado'] == "pendiente" || data['doctor']['user_id']['email']!=id_doc) {
            $(row).hide();
        }
    },
    "ajax": 
        {
        "method": "GET",
        "url": "/api/pagos_medico/",
        "dataSrc": "",
        "error": function(xhr, status, error) {
            console.log("readyState: " + xhr.readyState);
            console.log("responseText: "+ xhr.responseText);
            console.log("status: " + xhr.status);
            console.log("text status: " + status);
            console.log("error: " + error);
        },
    
    },

        "columns": [
            { data: "fecha"},
            { data: "hora"},
            { data: "precio"}
        ],
        columnDefs: [
            { width: 100, targets: 0},
            { width: 150, targets: 1},
            { width: 150, targets: 2},
        ],
    
});

$('#data_table_pagado').DataTable({
    "destroy": true,
    rowCallback: function( row, data, index ) {
        var id_doc=String($('#id_usuario_doc').html())
        if (data['estado'] == "pendiente") {
            $(row).hide();
        }
    },
    "ajax": 
        {
        "method": "GET",
        "url": "/api/pagos_medico/",
        "dataSrc": "",
        "error": function(xhr, status, error) {
            console.log("readyState: " + xhr.readyState);
            console.log("responseText: "+ xhr.responseText);
            console.log("status: " + xhr.status);
            console.log("text status: " + status);
            console.log("error: " + error);
        },
    
    },

        "columns": [
            { data: "doctor.user_id.persona_id.nombre"},
            { data: "doctor.user_id.persona_id.apellido"},
            { data: "fecha"},
            { data: "hora"},
            { data: "precio"},
        ],
        columnDefs: [
            { width: 100, targets: 0},
            { width: 100, targets: 1},
            { width: 100, targets: 2},
            { width: 100, targets: 3},
            { width: 100, targets: 4},
        ],
    
});

$('#data_table_pendiente').DataTable({
    "destroy": true,
    rowCallback: function( row, data, index ) {
        var id_doc=String($('#id_usuario_doc').html())
        if (data['estado'] == "pagado") {
            $(row).hide();
        }
    },
    "ajax": 
        {
        "method": "GET",
        "url": "/api/pagos_medico/",
        "dataSrc": "",
        "error": function(xhr, status, error) {
            console.log("readyState: " + xhr.readyState);
            console.log("responseText: "+ xhr.responseText);
            console.log("status: " + xhr.status);
            console.log("text status: " + status);
            console.log("error: " + error);
        },
    
    },

        "columns": [
            { data: "doctor.user_id.persona_id.nombre"},
            { data: "doctor.user_id.persona_id.apellido"},
            { data: "fecha"},
            { data: "hora"},
            { data: "precio"},
            { data: "id"},
        ],
        columnDefs: [
            { width: 100, targets: 0},
            { width: 100, targets: 1},
            { width: 100, targets: 2},
            { width: 100, targets: 3},
            { width: 100, targets: 4},
            { width: 150, className: "text-center", targets: 5, render: function(data){
            
            return '<a href="/realizar_pago/?id=' + data + '" class="btn btn-primary" role="button"></a>'
        }},
        ],
    
});


$('#data_table_espe').DataTable({
    "destroy": true,
    "ajax": 
        {
        "method": "GET",
        "url": "/api/especialidad/",
        "dataSrc": "",
        "error": function(xhr, status, error) {
            console.log("readyState: " + xhr.readyState);
            console.log("responseText: "+ xhr.responseText);
            console.log("status: " + xhr.status);
            console.log("text status: " + status);
            console.log("error: " + error);
        },
    
    },
    
    "columns": [
        { data: "nombre"}
    ],
    columnDefs: [
        { width: 100, targets: 0},
    ],
});

$('#data_table_med').DataTable({
    "destroy": true,
    "ajax": 
        {
        "method": "GET",
        "url": "/api/doctor/",
        "dataSrc": "",
        "error": function(xhr, status, error) {
            console.log("readyState: " + xhr.readyState);
            console.log("responseText: "+ xhr.responseText);
            console.log("status: " + xhr.status);
            console.log("text status: " + status);
            console.log("error: " + error);
        },
    
    },
    
    "columns": [
        { data: "user_id.persona_id.nombre"},
        { data: "user_id.persona_id.apellido"},
        { data: "identificador_medico"},
        { data: "user_id.email"},
        { data: "tarifa.nombre"},
    ],
    columnDefs: [
        { width: 100, targets: 0},
        { width: 100, targets: 1},
        { width: 100, targets: 2},
        { width: 100, targets: 3},
        { width: 100, targets: 4},
    ],
});