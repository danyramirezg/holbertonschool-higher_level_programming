// Toggles the class of the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#toggle_heade
$('DIV#toggle_header').click(function () {
  if ($('HEADER').hasClass('green')) {
    $('HEADER').removeClass('green');
    $('HEADER').addClass('red');
  } else if ($('HEADER').hasClass('red')) {
    $('HEADER').removeClass('red');
    $('HEADER').addClass('green');
  }
});
