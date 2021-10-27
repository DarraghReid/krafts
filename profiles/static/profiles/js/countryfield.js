/* Handle colour of countryfield in profile form */

// Get value of country field when page loads
let countrySelected = $('#id_default_country').val();
// If first option is selected
if(!countrySelected) {
    // Colour is grey
    $('#id_default_country').css('color', '#aab7c4');
}
// Capture change event
$('#id_default_country').change(function() {
    // Get value of box upon change
    countrySelected = $(this).val();
    // If first option is selected
    if(!countrySelected) {
        // Colour is grey
        $(this).css('color', '#aab7c4');
    } else {
        // Otherwise, colour is black
        $(this).css('color', '#000');
    }
});