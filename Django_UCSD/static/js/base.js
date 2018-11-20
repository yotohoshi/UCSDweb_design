
$(document).ready(function(){
    $('#sidebarText').load('/templates/sidebar.html');

    $('.leftmenutrigger').on('click', function(e) {
      $('.side-nav').toggleClass("open");
      e.preventDefault();
    });
});