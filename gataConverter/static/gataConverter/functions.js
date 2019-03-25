$('#customFile').change(function() {
  var file = $('#customFile')[0].files[0].name;
  $('#fileLabel').text(file);
});
