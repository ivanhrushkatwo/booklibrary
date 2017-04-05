$(document).ready(function () {
    console.log("jQuery work!");
});

$(function () {
    $(".book-pk").on("click", function (e) {
        e.preventDefault();
        let book_pk = $(e.currentTarget).data("id");
        $.ajax({
            type: "GET",
            url: "add_to_basket/" + book_pk,
            success: function (data) {

                jQuery("#basket").text("Basket " + data['count_goods']);
                let basketAmount = parseInt(jQuery(".amount-of-books").html());
                let priceOfOneBook = parseInt(jQuery(".hide-price-book-id-" + book_pk).html());
                let numberBook = parseInt(jQuery("#number-book-" + book_pk).html()) + 1;

                jQuery("#number-book-" + book_pk).text(numberBook);
                jQuery("#price-few_book-" + book_pk).text(numberBook);
                jQuery("#amount-book-" + book_pk).text(priceOfOneBook * numberBook);
                jQuery(".amount-of-books").html(basketAmount +  priceOfOneBook);

            },
            error: function (error) {
                console.log(error)
            }
        })
    });
});

$(function () {
    $(".delete-one-book-from-basket").on("click", function (e) {
        e.preventDefault();
        let book_pk = $(e.currentTarget).data("id");
        $.ajax({
            type: "GET",
            url: "delete_one_book_from_basket/" + book_pk,
            success: function (data) {
                console.log("Start!");
                jQuery("#basket").text("Basket " + data['count_goods']);

                let basketAmount = parseInt(jQuery(".amount-of-books").html());
                let priceOfOneBook = parseInt(jQuery(".hide-price-book-id-" + book_pk).html());
                let numberBook = parseInt(jQuery("#number-book-" + book_pk).html()) - 1;

                let s = parseInt(jQuery("#amount-book-" + book_pk).html()) - priceOfOneBook;

                console.log(numberBook);
                console.log(priceOfOneBook / numberBook);
                jQuery("#number-book-" + book_pk).text(numberBook);
                jQuery("#price-few_book-" + book_pk).text(numberBook);
                jQuery("#amount-book-" + book_pk).text(s);
                jQuery(".amount-of-books").html(basketAmount -  priceOfOneBook);
                console.log("ENd!")

                if (data["empty"] === "true") {
                    jQuery('.book-id-' + book_pk).remove();
                    let basketContent = jQuery('.not-empty');
                        if (basketContent.length < 1) {
                            window.open('http://10.110.0.10:8000/catalog/basket', "_self")
                        } else {
                            return false
                        }
                }
            },
            error: function () {
                console.log("Error!")
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
           window.open('http://10.110.0.10:8000/catalog/', '_self');
           }
       },
       error: function (error) {
           alert(error)
       }
   });
   e.preventDefault();
});