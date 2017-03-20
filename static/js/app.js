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
            success: function (data) {
                jQuery("#basket").text("Basket " + data.count_goods);
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
       success: function(data) {
           alert('Massage send!\n' + data['data']);
           window.open('http://localhost:8090/catalog/', '_self');
       },
       error: function (error) {
           alert('Error!')
       }
   });
   e.preventDefault();
});