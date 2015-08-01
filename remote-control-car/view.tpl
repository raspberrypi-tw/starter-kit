<html>
<head>
<script type="text/javascript" src="jquery.min.js"></script>
<script language="Javascript">

$(document).ready(function(){
  $(document).keypress(function(e){
    $.post( "/ajax", {arrow:e.which}, function( data ) {
      //console.log(e);
    });
  });

  $(document).keyup(function(e){
    $.post( "/ajax", {arrow:e.which}, function( data ) {
      //console.log(e);
    });
  });

  $("#f")
    .mousedown(function(){
      $.post( "/ajax", {arrow:119}, function( data ) {});
    })
    .mouseup(function(){
      $.post( "/ajax", {arrow:87}, function( data ) {});
    });

  $("#b")
    .mousedown(function(){
      $.post( "/ajax", {arrow:120}, function( data ) {});
    })
    .mouseup(function(){
      $.post( "/ajax", {arrow:88}, function( data ) {});
    });

  $("#l")
    .mousedown(function(){
      $.post( "/ajax", {arrow:97}, function( data ) {});
    })
    .mouseup(function(){
      $.post( "/ajax", {arrow:65}, function( data ) {});
    });

  $("#r")
    .mousedown(function(){
      $.post( "/ajax", {arrow:100}, function( data ) {});
    })
    .mouseup(function(){
      $.post( "/ajax", {arrow:68}, function( data ) {});
    });
});

</script>
</head>
<body>
<form>
    <div id="f">前進</div>
    <div id="b">後退</div>
    <div id="l">左轉</div>
    <div id="r">右轉</div>
</form>
</body>
</html>

