$(document).ready(function () {
    console.log("jQuery work!");
});

$(function () {

    $(".book-pk").on("click", function (e) {
        e.preventDefault();
        let book_pk = ($(e.currentTarget).data("id"));
        $.ajax({
            type: "GET",
            url: "add_to_basket/" + book_pk,
            async: false,
            success: function (data) {
                jQuery("#basket").text("Basket " + data.count_goods)
            },
            error: function () {
                console.log("Error!")
            }
        })
    });
});

$(function () {

    $(".del-book-id").on("click", function (e) {
        e.preventDefault();

        let book_pk = $(e.currentTarget).data("id");
        $.ajax({
            type: "GET",
            url: "delete_from_basket/" + book_pk,
            async: false,
            success: function (data) {
                jQuery('.book-id-' + book_pk).animate({
                        opacity: 0.50,
                        left: "+=10",
                        height: "toggle"
                      }, 500, function() {
                        jQuery("#basket").text("Basket " + data.count_goods);
                        jQuery('.book-id-' + book_pk).remove();
                        let basketContent = jQuery('.not-empty');
                        if (basketContent.length < 1) {
                            window.open('http://localhost:8090/catalog/basket', "_self")
                        }
                      });
                },
            error: function (er) {
                console.log(er)
            }
        })
    });
});


jQuery('#send-massage-to-admin').submit(function(e) {

    let frm  = jQuery('#send-massage-to-admin');

    jQuery.ajax({
       type: frm.attr('method'),
       url: frm.attr('action'),
       data: frm.serialize(),
       async: false,
       success: function(data) {
           if (data['data'] === 'false') {
               alert('Make sure all fields are entered and valid.')
           } else {
           alert('Massage send!\n' + data['data']);
           window.open('http://localhost:8090/catalog/', '_self');
           }
       },
       error: function (error) {
           alert('Error!')
       }
   });
   e.preventDefault();
});