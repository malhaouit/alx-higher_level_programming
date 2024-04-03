$(document).ready(function () {
  $('#btn_translate').click(function () {
    const lang = $('#language_code').val();
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + lang,
      type: 'GET',
      success: function (response) {
        $('#hello').text(response.hello);
      }
    });
  });
});
