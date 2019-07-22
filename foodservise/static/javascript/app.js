$('.question_req').ready(function () {

    $.ajax({
         type: "GET",
        url : "http://127.0.0.1:8000/foodservise/",
         dataType: "json",
         success : function (data) {
            $('#qus').text(data);
         }
    });
});