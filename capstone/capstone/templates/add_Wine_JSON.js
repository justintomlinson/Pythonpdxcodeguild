/**
 * Created by jetto on 4/25/2017.
 */
'use strict'

/**
 * Created by Dylan Brams on 4/25/2017.
 */
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$("#sendWineryData").click(function(){
    var mydata = new Object();
    mydata.winery_name = $("[name=winery_name]").val();
    mydata.winery_addr = $("[name=winery_addr]").val();
    mydata.winery_phn = $("[name=winery_phn]").val();
    var csrftoken = $("[name=csrfmiddlewaretoken]").val();
    $.ajax({
        type: "POST",
        url: "/api/winery/",
        contentType: "application/json;",
        data: JSON.stringify(data),
        dataType: "json",
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }},
    }).error(function(r){ console.log(r) })
        .success(function(r){ console.log("success", r) })
});

