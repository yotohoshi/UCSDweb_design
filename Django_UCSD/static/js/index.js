// Loading Page
  $(document).ready(function() {
    //Load Slides with Capion
    $('#Topright').load('/templates/index_top_right.html');
    //Load Slides with Capion
    $('#advertisement').load('/templates/banner.html');
    // Load SignUp PopUp
    $('#signin-popup').load('/templates/login.html');
    // Load search bar
    $('#searchbar').load('localhost:8000/templates/searchbar.html');
    // Load Footnote Circles
    $('#footnote').load('localhost:8000/templates/footnote_circles.html');
    // alert('success!!!');
  });
// End of Loading
