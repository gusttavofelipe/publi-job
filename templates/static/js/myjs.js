// function myFunction() {
//     alert("Hello from a static file!");
//   }

$(".close").click(function() {
    $(this)
      .parent(".alert")
      .fadeOut();
  });
  