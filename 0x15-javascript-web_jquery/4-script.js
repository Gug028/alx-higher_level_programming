#!/usr/bin/node

$(document).ready(function () {
  $('#toggle_header').click(function () {
    if ($('header').hasClass('green')) {
      $('header').removeClass('green');
	$('header').addClass('red');
    } else {
      $('header').removedClass('red');
      $('header').addClass('green');
    }
  });
});
