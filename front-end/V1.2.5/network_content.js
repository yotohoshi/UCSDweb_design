var angleStart = -360;

// jquery rotate animation
function rotate(li, d) {
  $({
    d: angleStart
  }).animate({
    d: d
  }, {
    step: function(now) {
      $(li)
        .css({
          transform: 'rotate(' + now + 'deg)'
        })
        .find('label')
        .css({
          transform: 'rotate(' + (-now) + 'deg)'
        });
    },
    duration: 0
  });
}

// show / hide the options
function toggleOptions(s) {
  $(s).toggleClass('open');
  var li = $(s).find('li');
  var deg = $(s).hasClass('half') ? 0 : 360 / li.length;
  for (var i = 0; i < li.length; i++) {
    if (window.CP.shouldStopExecution(1)) {
      break;
    }
    var d = $(s).hasClass('half') ? 0 : i * deg;
    $(s).hasClass('open') ? rotate(li[i], d) : rotate(li[i], angleStart);
  }
  window.CP.exitedLoop(1);

}

// $('.selector button').click(function(e) {
//   toggleOptions($(this).parent());
// });

setTimeout(function() {
  toggleOptions('.selector');
}, 100);
//# sourceURL=pen.js


$(function() {
  $("#networksTree").draggable();
});

// dragElement(document.getElementById("networksTree"));

//Make the DIV element draggagle:
// $(document).ready(function(){
//   console.log("load");
//   var element = document.getElementById("#treeButton");
//   var mouse = 0;
//   var move = 0;
//   element.addEventListener('mousedown', function(){
//     mouse = 1;
//   });
//   element.addEventListener('mousemove', function(){
//     move = 1;
//   });
//   element.addEventListener('mouseup', function(){
//     if (mouse == 1 && move == 1) // drag
//     {
// dragElement(document.getElementById("networksTree"));
// console.log("1");
//     }
//     else if (mouse == 1 && move == 0) // click
//     {
//       $('.selector button').click(function(e) {
//         toggleOptions($(this).parent());
//       });
//       console.log("2");
//     }
//     mouse = 0;
//     move = 0;
//   });
// });




//dragElement(document.getElementById("networksTree"));

function dragElement(elmnt) {
  var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
  if (document.getElementById(elmnt.id)) {
    /* if present, the header is where you move the DIV from:*/
    document.getElementById(elmnt.id).onmousedown = dragMouseDown;
  } else {
    /* otherwise, move the DIV from anywhere inside the DIV:*/
    elmnt.onmousedown = dragMouseDown;
  }

  function dragMouseDown(e) {
    e = e || window.event;
    e.preventDefault();
    // get the mouse cursor position at startup:
    pos3 = e.clientX;
    pos4 = e.clientY;
    document.onmouseup = closeDragElement;
    // call a function whenever the cursor moves:
    document.onmousemove = elementDrag;
  }

  function elementDrag(e) {
    e = e || window.event;
    e.preventDefault();
    // calculate the new cursor position:
    pos1 = pos3 - e.clientX;
    pos2 = pos4 - e.clientY;
    pos3 = e.clientX;
    pos4 = e.clientY;
    // set the element's new position:
    elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
    elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
  }

  function closeDragElement() {
    /* stop moving when mouse button is released:*/
    document.onmouseup = null;
    document.onmousemove = null;
  }
}
