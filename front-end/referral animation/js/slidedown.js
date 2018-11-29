jQuery(function($){
    $("#oneII").toggle()
		 $( '#oneI' ).click(function () {

  if ( $( "#oneII" ).is( ":hidden" ) ) {
    $( "#oneII" ).slideDown( "slow" );
  } else {
    $( "#oneII" ).hide();
  }
});


    $("#twoII").toggle()
		 $( '#twoI' ).click(function () {

  if ( $( "#twoII" ).is( ":hidden" ) ) {
    $( "#twoII" ).slideDown( "slow" );
  } else {
    $( "#twoII" ).hide();
  }
});

    $("#threeII").toggle()
		 $( '#threeI' ).click(function () {

  if ( $( "#threeII" ).is( ":hidden" ) ) {
    $( "#threeII" ).slideDown( "slow" );
  } else {
    $( "#threeII" ).hide();
  }
});

    $("#fourII").toggle()
		 $( '#fourI' ).click(function () {

  if ( $( "#fourII" ).is( ":hidden" ) ) {
    $( "#fourII" ).slideDown( "slow" );
  } else {
    $( "#fourII" ).hide();
  }
});

    $("#fiveII").toggle()
		 $( '#fiveI' ).click(function () {

  if ( $( "#fiveII" ).is( ":hidden" ) ) {
    $( "#fiveII" ).slideDown( "slow" );
  } else {
    $( "#fiveII" ).hide();
  }
});

    $("#sixII").toggle()
		 $( '#sixI' ).click(function () {

  if ( $( "#sixII" ).is( ":hidden" ) ) {
    $( "#sixII" ).slideDown( "slow" );
  } else {
    $( "#sixII" ).hide();
  }
});


    $("#sevenII").toggle()
		 $( '#sevenI' ).click(function () {

  if ( $( "#sevenII" ).is( ":hidden" ) ) {
    $( "#sevenII" ).slideDown( "slow" );
  } else {
    $( "#sevenII" ).hide();
  }
});


    $('.firstClass').click(function(e) {
  var target = $(e.target);
  if(!target.is('#oneI')) {
          if ($('#oneII').is(':visible')) {
              $('#oneII').hide();
          }
      }
  if(!target.is('#twoI')) {
    if ( $('#twoII').is(':visible') ) {
      $('#twoII').hide();
    }
  }
  if(!target.is('#threeI')) {
    if ( $('#threeII').is(':visible') ) {
      $('#threeII').hide();
    }
  }
  if(!target.is('#fourI')) {
    if ( $('#fourII').is(':visible') ) {
      $('#fourII').hide();
    }
  }
  if(!target.is('#fiveI')) {
    if ( $('#fiveII').is(':visible') ) {
      $('#fiveII').hide();
    }
  }
  if(!target.is('#sixI')) {
    if ( $('#sixII').is(':visible') ) {
      $('#sixII').hide();
    }
  }
  if(!target.is('#sevenI')) {
    if ( $('#sevenII').is(':visible') ) {
      $('#sevenII').hide();
    }
  }
});

});