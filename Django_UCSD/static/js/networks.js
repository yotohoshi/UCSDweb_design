$(document).ready(function() {
  // Load sections
  //$('#newfriend_search_result').load('/network/search_result');
  $('#sidebarText').load("/templates/sidebar.html");
  $('#Topright').load("/templates/index_top_right.html");
  $('#keywordsearch').load("/templates/simple_keyword_search1.html");
  $('#recommandation-results').load("/network/recommendations");
  //$('#friend_request_tabs').load("/templates/Network/friends_request_tab.html");
  $('#referral_people_content').load("/templates/Network/newfriend_search_result.html");
  $('#referral_list').load("/templates/Network/recommendation_results.html");
  $('#request').load("/network/request");
  $('#friend').load("/network/friends");
  $('#error_msg').load("/templates/error_popup.html");

  // Adjust window size
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
  // var checked = 0;
  var c = $('input[type=checkbox]').prop('checked');
  console.log(c);
  // at front page
  if (c == false) {
    $('#page2-section1').hide();
    $('#page2-section2').hide();
    $('#page1-section1').show();
    $('#page1-section2').show();
    $('#friend_front').show();
    $('#friend_back').hide();
    // alert('BACK');
    state_front();
  }
  // at back page
  else {
    // $('#friends_friends').show();
    $('#page2-section1').show();
    $('#page2-section2').show();
    $('#page1-section1').hide();
    $('#page1-section2').hide();
    $('#friend_front').hide();
    $('#friend_back').show();
    state_back();
    // alert('HELLO');
  }





  $('input[type=checkbox]').on('click', function(checked) {
    var c = $('input[type=checkbox]').prop('checked');
    console.log(c);
    if (c == false) {
      // checked = 0;
      $('#page2-section1').hide();
      $('#page2-section2').hide();
      $('#page1-section1').show();
      $('#page1-section2').show();
      $('#friend_front').show();
      $('#friend_back').hide();
      state_front();
      // alert('BACK');
    } else {
      // checked = 1;
      $('#page2-section1').show();
      $('#page2-section2').show();
      $('#page1-section1').hide();
      $('#page1-section2').hide();
      $('#friend_front').hide();
      $('#friend_back').show();
      state_back();
      // alert('HELLO');
    }


  });


function state_front(){
  $('body').css('background-color', '');
  $('#myTabContent').css('background-color', '');
  $('#myTabContent').css('border', );
  $('#myTab').css('border', );
  $(this).css('background-color', '');
  $('#referral_num_box').css('background-color', '');
  $('.nav-tabs').css('background-color', '');
  $('.tab-content').css('background-color', '');
  $('.tab-content').css('color', '');
  $('#referr_border').css('border', );
  $('#referr_border').css('background-color', '');
  $('#friend-tab').css('background-color', '');
  $('#request-tab').css('background-color', '');
  $('#friend-tab').css('color', '');
  $('#request-tab').css('color', '');
  $('#friend-tab').css('border', 'color ');
  $('#request-tab').css('border', 'color ');
  $(this).css('color', '');

  $('#myTabContent').css('opacity', 1);
  $(this).css('opacity', 1);
  $('#referral_num_box').css('opacity', 1);
  $('.nav-tabs').css('opacity', 1);
  $('.tab-content').css('opacity', 1);
  $('#friend-tab').css('opacity', 1);
  $('#request-tab').css('opacity', 1);
  $('#referr_border').css('opacity', 1);
  // $('#outpart').css('border-radius', '');
  $('#add-fri-button').css('background-color', '');
  $('#add-fri-button').css('color', '');
  $('#friend-content').css('color', '');
  $('#friend-content').css('background-color', '');
  $('button').css('background-color', '');
  $('button').css('color', '');
  $('#recommandation-whole-card').css('background-color', '');
  $('p').css('color', '');
  $('h4').css('color', '');
  $('.card-body.col-9.shadow').css('background-color', '#fff !important');
  $('.row.justify-content-center.description').css('color','');
  $('.col.col-10.card-body.shadow-lg').css('background-color', '#fff !important');
}

function state_back(){
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
  // $('#outpart').css('border-radius', '');
  // $('#add-fri-button').css('background-color', '#333');
  // $('#add-fri-button').css('color', '#fff');
  $('#friend-content').css('color', '#fff');
  $('#friend-content').css('background-color', '#333');
  $('button').css('background-color', '#333');
  $('button').css('color', '#fff');
  $('#recommandation-whole-card').css('background-color', '#333');
  $('p').css('color', '#fff');
  $('h4').css('color', '#fff');
  $('.card-body.col-9.shadow').css('background-color', '#333 !important');
  $('.row.justify-content-center.description').css('color','#fff');
  $('.col.col-10.card-body.shadow-lg').css('background-color', '#fff !important');

}


});
