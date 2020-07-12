$(document).ready(function() {
    // CSRF TOKEN SETTINGS

    // USING JQUERY
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var commentsSectionElement = $("#comments-section");
    var commentsCountElement = $(commentsSectionElement).find("#comments-count");
    var commentsListElement = $(commentsSectionElement).find("ul");
    var commentsCreateFormElement = $(commentsSectionElement).find("form");
    var commentsCreateFormInputContentElement = $(commentsCreateFormElement).find("input[name='content']");

    var postSlug = $(commentsSectionElement).data("post-slug");
    var commentsAPIUrl = "/api/posts/" + postSlug + "/comments";

    $.ajax({
        url: commentsAPIUrl,
        type: "GET",
        success: function (data) {
            var commentsCount = data.length;
            $(commentsCountElement).html(commentsCount);

            data.forEach(function(comment){
                var commentUsername = comment.username;
                var commentContent = comment.content;

                var commentData = commentUsername + ': ' + commentContent;
                var commentListElement = $("<li>").text(commentData);
                $(commentsListElement).append(commentListElement);
            });
        },
        error: function (data){

        }
    });
    
    commentsCreateFormElement.submit(function(){
        var content = $(commentsCreateFormInputContentElement).val();
        var data = {
            content: content,
        };

        $.ajax({
            url: commentsAPIUrl,
            type: "POST",
            data: data,
            success: function (data){
                var commentUsername = data.username;
                var commentContent = data.content;

                // APPEND COMMENTS LIST
                var commentData = commentUsername + ': ' + commentContent;
                var commentListElement = $("<li>").text(commentData);
                $(commentsListElement).append(commentListElement);

                // UPDATAE COMMENTS COUNT
                var commentsCount = $(commentsCountElement).html();
                var newCommentCount = Number(commentsCount) + 1
                $(commentsCountElement).html(String(newCommentCount));

                // form 내에 들어가는 value => val()
                $(commentsCreateFormInputContentElement).val("");
            },
            error: function (error){
            }
        });


        return false;
    })
});