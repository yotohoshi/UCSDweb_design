

/*$(document).ready(function() {
    $('#sidebarText').load('templates/sidebar.html');
    $('#Topright').load('templates/index_top_right.html');
    $('#keywordsearch').load('templates/simple_keyword_search.html');
    $('#personallinks').load('templates/personal_links.html');
    $('#right-upper').load('templates/profile_right_upper.html');
    $('#personal').load('templates/profile_right_lower_about.html');
    $('#event').load('templates/profile_right_lower_events.html');
      //alert("YES");
  });*/

/*$('.leftmenutrigger').on('click', function(e) {
      $('.side-nav').toggleClass("open");
      e.preventDefault();
    });*/

$(document).ready(function() {
    $('#sidebarText').load('/templates/sidebar.html');
    $('#Topright').load('/templates/index_top_right.html');
    $('#keywordsearch').load('/templates/simple_keyword_search.html');
    $('#personallinks').load('/templates/personal_links.html');
    $('#right-upper').load('/templates/profile_right_upper.html');
    $('#calendar').load('/templates/calendar.html');
    $('#add_referral').load('/templates/add_referral.html');
    $('#referral_list').load('/referral_list');
    //$('#personal').load('/templates/profile_right_lower.html');
    //$('#event').load('/templates/profile_right_lower_events.html');
    $('#logout-successful-div').load('/templates/logout_successful.html');
    $('.leftmenutrigger').on('click', function(e) {
      $('.side-nav').toggleClass("open");
      e.preventDefault();
    });
  });