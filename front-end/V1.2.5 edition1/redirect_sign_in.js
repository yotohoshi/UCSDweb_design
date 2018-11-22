
$(document).ready(
    function() {
        $('#signup_wrong_page').load('signup.html');


        //  alert("YES");
        $('.leftmenutrigger').on('click', function(e) {
            $('.side-nav').toggleClass("open");
            e.preventDefault();
        });
    });