$('#cipher-dropdown-menu a').click(function(event) {
    var text = $(event.target).text().trim();
    console.log(text)

    if (text == "Ceaser Cipher"){
        render_cipher_body("ceaser_cipher");
    }
});

function render_cipher_body(name) {
    $('#cipher_body').empty();
    if(name == "ceaser_cipher") {
        $('#cipher_body').append($('#ceaser_cipher_body').clone());
    }
}


$("#cipher_body" ).on("submit", "form",function( event ) {
    event.preventDefault();
    var $form = $( this )
    var url = $form.attr( "action" );
    var post_data = $form.serializeArray();
    // Send the data using post
    
    var posting = $.post( url, post_data );
 
    // Put the results in a div
    posting.done(function( data ) {
      console.log(data)
    });
});
