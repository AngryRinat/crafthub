
window.onload = function () {
    $('.goods-item__btn').on('click', function () {
        let target = event.target;
        let basketID = target.name;
        $.ajax({
            url: '/baskets/basket-edit/' + basketID,
            success: function (data) {
                $('.goods-item__btn').html(data.result);
            }
        })
    })
}