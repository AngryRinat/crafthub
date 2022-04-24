
$(document).on('submit','#goods-item__btn', function(e){
    e.preventDefault();

    $.ajax({
        type:'POST',
        url: "{% url 'baskets/basket_remove' %},
        success: function(response){
        alert("Success")
        }
    })
})