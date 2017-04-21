/**
 * Created by jetto on 4/20/2017.
 */
<script src="{% static 'DJANGO_APP_NAME/ajax_csrf_setup.js' %}"></script>
    <script src="{% static 'DJANGO_APP_NAME/main.js' %}"></script>

var sourceForm = $('#my-form');

/**
 * Returns a promise containing the JSON object for submitting the form.
 */
function submitForm() {
    var actionURL = sourceForm.attr('action');
    var submitMethod = sourceForm.attr('method');
    // This takes the data from the form and packages it up for sending.
    var formData = sourceForm.serialize();
    return Promise.resolve($.ajax({
        dataType: 'json',
        url: actionURL,
        method: submitMethod,
        data: formData
    }));
}