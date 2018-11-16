
$( document ).ready(function() {
     $('.leftmenutrigger').on('click', function(e) {
     $('.side-nav').toggleClass("open");
     e.preventDefault();
    });
});

// With JQuery
//$("#ex2").slider({});

// Without JQuery
var slider = new Slider('#ex2', {});
