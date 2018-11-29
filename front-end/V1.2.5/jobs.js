$(document).ready(
  function() {
    $('#sidebarText').load("sidebar.html");
    $('#Topright').load("index_top_right.html");
    $('#keywordsearch').load("simple_keyword_search.html");
    $('#contents').load("jobs_content.html");
    $('#adfilter').load("adfilter.html");
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

// Toggle start icon to like and dislike
$(document).ready(function() {
  $('#icon1').on('click', function() {
    //alert("lll");
    $(this).find('#ii').toggleClass("fa-star fa-star-o");
  });
  $('#icon2').on('click', function() {
    //alert("lll");
    $(this).find('#iii').toggleClass("fa-star fa-star-o");
  });
  $('#icon3').on('click', function() {
    //alert("lll");
    $(this).find('#iiii').toggleClass("fa-star fa-star-o");
  });
});
