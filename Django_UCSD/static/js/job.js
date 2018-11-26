$(document).ready(
  function() {
    $('#sidebarText').load("/templates/sidebar.html");
    $('#Topright').load("/templates/index_top_right.html");
    $('#keywordsearch').load("/templates/simple_keyword_search.html");
    //$('#contents').load("/templates/jobs_content.html");
    $('#signin-popup').load("/templates/login.html");
    //$('#adfilter').load("/templates/afilter.html");
    //  alert("YES");
    $('.leftmenutrigger').on('click', function(e) {
      $('.side-nav').toggleClass("open");
      e.preventDefault();
    });
  });

/*function toggleIcon(e) {
  $(e.target)
    .prev('.panel-heading')
    .find(".more-less")
    .toggleClass('glyphicon-plus glyphicon-minus');
}
$('.panel-group').on('hidden.bs.collapse', toggleIcon);
$('.panel-group').on('shown.bs.collapse', toggleIcon);

// Toggle start icon to like and dislike
$(document).ready(function() {
    for (i=0; i<)
  $('#icon1').on('click', function() {
    //alert("lll");
    $(this).find('#1').toggleClass("fa-star fa-star-o");
  });
  $('#icon2').on('click', function() {
    //alert("lll");
    $(this).find('#2').toggleClass("fa-star fa-star-o");
  });
  $('#icon3').on('click', function() {
    //alert("lll");
    $(this).find('#3').toggleClass("fa-star fa-star-o");
  });
});
*/