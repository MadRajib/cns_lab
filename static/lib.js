const Ciphers = {
    CEASER_CIPHER   :0,
//  TODO: Add enums for ciphers
//eg NEW_CIPHER :1
}

function parse(params) {
  if (params == "Ceaser Cipher")
    return Ciphers.CEASER_CIPHER  
// TODO: Add parser for ciphers
//eg 
/* if (params == "New Cipher")
    return Ciphers.NEW_CIPHER  
*/
}

$('#cipher-dropdown-menu a').click(function(event) {
    var text = $(event.target).text().trim();

    var $cipherCard = $('#cipher_card').empty();
    switch (parse(text)) {
        case Ciphers.CEASER_CIPHER:            
            $cipherCard.append(
                    $('#ceaser_cipher_body').clone()
            );
            break;
// TODO: Add case for new chipers
/*eg 
        case Ciphers.NEW_CIPHER:
            $cipherCard.append(
                    $('#new_cipher_body').clone()
            );
*/        
        default:
            break;
    }
});


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
      $("#result .form-group").show()
      $("#resultText").val(data)
    });
});
