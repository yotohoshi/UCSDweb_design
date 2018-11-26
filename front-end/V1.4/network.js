// Loading Page
$(document).ready(function() {
  function start() {
    var submit = document.getElementById('submit');
    submit.addEventListener('click', toggle);
  };

  function toggle() {
    var color = document.getElementById('submit');
    color.classList.toggle('black');
  };


  start();
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

  // show / hide the options
  function toggleOptions(s) {
      $(s).toggleClass('open');
      var li = $(s).find('li');
      var deg = $(s).hasClass('half') ? 0 : 360/li.length;
      for(var i=0; i<li.length; i++) {if (window.CP.shouldStopExecution(1)){break;}
          var d = $(s).hasClass('half') ? 0 : i*deg;
          $(s).hasClass('open') ? rotate(li[i],d) : rotate(li[i],angleStart);
      }
  window.CP.exitedLoop(1);

  }

  $('.selector button').click(function(e) {
      toggleOptions($(this).parent());
  });

  setTimeout(function() { toggleOptions('.selector'); }, 100);
  //# sourceURL=pen.js


});

$( function() {
  $( "#draggable" ).draggable();
} );
