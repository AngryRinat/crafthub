

    var csrf = $("input[name=csrfmiddlewaretoken]").val();

    $(".goods-item__txt").click(function(){
        $.ajax({
            type: 'POST',
            url: 'basket_remove/',
            data: { csrfmiddlewaretoken: csrf },
            contentType: "application/json",
            dataType: "json",
            success: function (data) {
                console.log("Data added!", data)}
            });
      });






// $.ajax({
//     type: 'POST',
//     url: 'baskets/basket_remove/',
//     data: {'id':1},
//     contentType: "application/json",
//     dataType: "json",
//     success: function(data) {
//      console.log("Data added!", data);
//     }
//   });
// });
//
// // var myObj = {
// //         "name": $('#name').val(),
// //         "drink": $('#drink').val()
// // };
// //
// // var order = JSON.stringify(myObj);


// $(document).on('submit', '#goods-item__btn', function (e) {
//     e.preventDefault();
//
//     $.ajax({
//         type: 'POST',
//         url: "{% url 'baskets/basket_remove' %}
//         success: function (response) {
//             alert("Success")
//         }
//     })
// })