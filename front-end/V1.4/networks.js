$(document).ready(
  function() {
    $('#sidebarText').load("sidebar.html");
    $('#Topright').load("index_top_right.html");    //  alert("YES");
    $('.leftmenutrigger').on('click', function(e) {
      $('.side-nav').toggleClass("open");
      e.preventDefault();
    });
    $('#networksBar').load("network_sidebar.html");
    $('#networksTree').load("network.html");
    
    
    
    
    
    function toggleIcon(e) {
  $(e.target)
    .prev('.panel-heading')
    .find(".more-less")
    .toggleClass('glyphicon-plus glyphicon-minus');
}

$( function() {
  $( "#networksTree" ).draggable();
} );
    
    
    
    
      var angleStart = -360;

  // jquery rotate animation
  function rotate(li,d) {
      $({d:angleStart}).animate({d:d}, {
          step: function(now) {
              $(li)
                 .css({ transform: 'rotate('+now+'deg)' })
                 .find('label')
                    .css({ transform: 'rotate('+(-now)+'deg)' });
          }, duration: 0
      });
  }



  $('.selector button').click(function(e) {
      toggleOptions($(this).parent());
  });

  setTimeout(function() { toggleOptions('.selector'); }, 100);
    
    
    
  });


// $('.panel-group').on('hidden.bs.collapse', toggleIcon);
// $('.panel-group').on('shown.bs.collapse', toggleIcon);
