window.onload = function () {
//    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    $('.card-list').on('click', 'input[type="number"]', function () {
        var t_href = event.target;

        $.ajax({
            url: "/baskets/edit/" + t_href.name + "/" + t_href.value + "/",
            success: function (data) {
                $('.card-list').html(data.result);
            },

        });
        event.preventDefault();
    });

//    $('#buttonremove').on('click', function() {
//        $.ajax({
//        type: 'POST',
//        data: {csrfmiddlewaretoken: csrftoken},
//        url: "/baskets/remove",
//        success: function (data) {
//                $('.goods').html(data.result)}
//        })
//        event.preventDefault();
//    })
}

