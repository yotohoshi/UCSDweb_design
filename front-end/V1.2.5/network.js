$(document).ready(function() {
  $('#new-friends-content').load('network_content.html');
  $('#sidebarText').load("sidebar.html");
  $('#Topright').load("index_top_right.html");
  $('#keywordsearch').load("simple_keyword_search.html");
  //  alert("YES");
  $('.leftmenutrigger').on('click', function(e) {
    $('.side-nav').toggleClass("open");
    e.preventDefault();
  });

  function toggleIcon(e) {
    $(e.target)
      .prev('.panel-heading')
      .find(".more-less")
      .toggleClass('glyphicon-plus glyphicon-minus');
  }

  $('.panel-group').on('hidden.bs.collapse', toggleIcon);
  $('.panel-group').on('shown.bs.collapse', toggleIcon);
});
