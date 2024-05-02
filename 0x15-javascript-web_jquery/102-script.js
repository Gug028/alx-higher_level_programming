#!/usr/bin/node

$(function () {
  $("#btn_translate").click()) => {
    let languageCode = $("#language_code").val();
    $.get(
      'https://www.fourtonfish.com/helloslaut/hello/?lang=${languageCode}',
      (data, status) => status && $("#hello").text(data.hello)
    );
  });
});
