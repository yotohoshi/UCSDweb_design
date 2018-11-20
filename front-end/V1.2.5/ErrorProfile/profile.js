$(document).ready(
  function() {
    $('#sidebarText').load("sidebar.html");
    $('#Topright').load("index_top_right.html");
    $('#keywordsearch').load("simple_keyword_search.html");
    $('#personallinks').load("personal_links.html");
    $('#right-upper').load("profile_right_upper.html");
    $('#personal').load("profile_right_lower_about.html");
    $('#event').load("profile_right_lower_events.html");
    //  alert("YES");
    $('.leftmenutrigger').on('click', function(e) {
      $('.side-nav').toggleClass("open");
      e.preventDefault();
    });
  });
