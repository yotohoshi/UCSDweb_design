$(document).ready(
  function() {
    $('#sidebarText').load("/templates/sidebar.html");
    $('#Topright').load("/templates/index_top_right.html");
    $('#keywordsearch').load("/templates/simple_keyword_search.html");
    //$('#signin-popup').load("/templates/login.html");
    //$('#contents').load("/templates/event_content.html");

    //  alert("YES");
    $('.leftmenutrigger').on('click', function(e) {
      $('.side-nav').toggleClass("open");
      e.preventDefault();
    });
  });

function toggleIcon(e) {
  $(e.target)
    .prev('.panel-heading')
    .find(".more-less")
    .toggleClass('glyphicon-plus glyphicon-minus');
}
$('.panel-group').on('hidden.bs.collapse', toggleIcon);
$('.panel-group').on('shown.bs.collapse', toggleIcon);


$('#icon1').on('click', function() {
  $(this).toggleClass('fa-star');
});