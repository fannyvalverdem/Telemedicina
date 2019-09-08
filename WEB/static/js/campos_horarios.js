var conditional_fields = $("div.horario");
conditional_fields.hide();

$(".lunes").change(function() {
    if ($(this).prop('checked') === 'checked') {
        conditional_fields.show();
    } else {
        conditional_fields.hide();
    }
});