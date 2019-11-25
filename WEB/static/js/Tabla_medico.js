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
        { data: "precio"},
        { data: "especialidad"}
    ],
    columnDefs: [
        { width: 100, targets: 0},
        { width: 150, targets: 1},
        { width: 150, targets: 2},
        { width: 150, targets: 3},
        { width: 150, targets: 4},
        { width: 150, className: "text-center", targets: 5, render: function(data){
            return `<a href="/confirmacion_emergencia/" class="btn btn-primary" role="button"><i class="fas fa-eye"></i></a>
                 `
        }},
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
        if (data['consulta_id']['estado'] == "agendada" || data['consulta_id']['doctor_id']['user_id']['username']!=id_doc) {
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
            { data: "consulta_id.paciente_id.user_id.persona_id.nombre"},
            { data: "consulta_id.paciente_id.user_id.persona_id.apellido"},
            { data: "fecha_reser"},
            { data: "fecha_prog"},
            { data: "precio"}
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