// Loading Page
$(document).ready(function () {
    //Load Slides with Capion
    $('#Topright').load('index_top_right.html');
    //Load Slides with Capion
    <!--$('#advertisement').load('banner.html');-->
    // Load SignUp PopUp
    $('#signup-popup').load('signup.html');
    // Load search bar
    <!--$('#searchbar').load('searchbar.html');-->
    // Load Footnote Circles
    $('#footnote').load('footnote_circles.html');
    // alert('success!!!');

    var x = document.getElementById("sign");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }


});
// End of Loading
