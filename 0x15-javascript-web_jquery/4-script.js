const $ = window.$;
$(document).ready(function () {
  const button = $('#toggle_header');
  const header = $('header');

  button.click(function () {
    if (header.attr('class') === 'green') {
      header.addClass('red');
      header.removeClass('green');
    } else {
      header.removeClass('red');
      header.addClass('green');
    }
  });
});
