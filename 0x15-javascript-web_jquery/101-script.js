// Adds, removes, and clears LI elements from a list using JQuery API

$(document).ready(function () {
  $('#add_item').click(function () {
    let element = '<li>Item</li>';
    $('ul.my_list').append(element);
  });

  $('#remove_item').click(function () {
    $('ul.my_list li:last-child').remove();
  });

  $('#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});
