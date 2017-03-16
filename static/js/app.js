$(document).ready(function () {
    console.log("jQuery work!");
});

$(function () {

    $(".book-pk").on("click", function (e) {
        e.preventDefault();
        var book_pk = ($(e.currentTarget).data("id"));
        $.ajax({
            type: "GET",
            url: "add_to_basket/" + book_pk,
            success: function (data) {
                console.log(data);
                jQuery("#basket").text("Basket " + data.count_goods);
            },
            error: function () {
                console.log("Error!")
            }
        })
    });
});
