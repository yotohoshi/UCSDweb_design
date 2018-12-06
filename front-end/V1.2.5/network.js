$(document).ready(function() {
  $('#new-friend-content').load('newfriend_search_result.html');


  $('#sidebarText').load("sidebar.html");
  $('#Topright').load("index_top_right.html");
  $('#keywordsearch').load("simple_keyword_search.html");

  //  alert("YES");
  $('.scroll').css('height', $(window).height() * 0.6);
  $('.tab-content').css('height', $(window).height() * 0.9);
  $('#paddingrow').css('height', $(window).height() * 0.1);
  $('.card').addClass('shadow');
  $('#racommanding').css('height', $(window).height() * 0.15);

  $('.leftmenutrigger').on('click', function(e) {
    $('.side-nav').toggleClass("open");
    e.preventDefault();
  });

  function toggleIcon(e) {
    $(e.target)
      .prev('.panel-heading')
      .find(".more-less")
      .toggleClass('glyphicon-plus glyphicon-minus');
  }

  $('.panel-group').on('hidden.bs.collapse', toggleIcon);
  $('.panel-group').on('shown.bs.collapse', toggleIcon);


  // Stuff to do as soon as the DOM is ready
  $('#friend-referrals').hide();

  $('#referralbtn').on('click', function() {
    $('#keywordsearch').hide();
    $('#newfriend_search_result').hide();
    $('#racommanding').hide();
    // $('#myTab').hide();
    // $('#myTabContent').hide();
    // $('#friend-referrals').show();
    $('body').css('background-color', '#303136');
    $('#myTabContent').css('background-color', '#333');
    $('#myTabContent').css('border', 0);
    $('#myTab').css('border', 0);
    $(this).css('background-color', '#333');
    $('#referral_num_box').css('background-color', '#333');
    $('.nav-tabs').css('background-color', '#333');
    $('.tab-content').css('background-color', '#333');
    $('.tab-content').css('color', '#fff');
    $('#referr_border').css('border', 0);
    $('#referr_border').css('background-color', '#333');
    $('#friend-tab').css('background-color', '#333');
    $('#request-tab').css('background-color', '#333');
    $('#friend-tab').css('color', '#fff');
    $('#request-tab').css('color', '#fff');
    $('#friend-tab').css('border', 'color gray');
    $('#request-tab').css('border', 'color gray');
    $(this).css('color', '#fff');

    $('#myTabContent').css('opacity', .7);
    $(this).css('opacity', .7);
    $('#referral_num_box').css('opacity', .7);
    $('.nav-tabs').css('opacity', .5);
    $('.tab-content').css('opacity', .7);
    $('#friend-tab').css('opacity', .7);
    $('#request-tab').css('opacity', .7);
    $('#referr_border').css('opacity', .7);

    alert('HELLO');

  });




  $("#referralbtn").onClick(function() {
    var color = clicked ? 'red' : 'black';
    $(this).css('background-color', color);
    clicked = !clicked;
  });



  // $('#referralbtn').on('click', function{
  //   $('body').css('background-color', #000);
  // });

});
