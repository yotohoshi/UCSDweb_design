$(document).ready(
  function() {
    $('#sidebarText').load("sidebar.html");
    $('#Topright').load("index_top_right.html");
    $('#keywordsearch').load("simple_keyword_search.html");
    $('#contents').load("event_content.html");

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
