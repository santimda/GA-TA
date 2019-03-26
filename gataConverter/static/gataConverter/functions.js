$('#customFile').change(function() {
  var file = $('#customFile')[0].files[0].name;
  $('#fileLabel').text(file);
});

/*$.fileDownload('/download', {
    successCallback: function (url) {

        alert('You just got a file download dialog or ribbon for this URL :' + url);
    },
    failCallback: function (html, url) {

        alert('Your file download just failed for this URL:' + url + '\r\n' +
                'Here was the resulting error HTML: \r\n' + html
                );
    }
});*/