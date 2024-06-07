// like.js
$(document).ready(function() {
    $(".post-container button").click(function(event) {
        event.preventDefault(); // Prevent default form submission

        var postId = $(this).data('post-id');
        var contentType = $(this).data('content-type');
        var likeButton = $(this);
        var likeCountSpan = $("#like-count-" + postId);
        var isLiked = $(this).data('liked');  // Get like status from data attribute

        if (likeButton.hasClass('disabled')) {
            return;
        }

        likeButton.addClass('disabled');  // Disable button temporarily

        $.ajax({
            url: '/like-post/' + postId,
            type: 'POST',
            data: {
                content_type: contentType,
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
            },
            success: function(response) {
                likeButton.text(response.like_status ? "Unlike" : "Like");
                likeButton.data('liked', response.like_status);  // Update like status data attribute
                likeCountSpan.text(response.total_likes);
                likeButton.removeClass('disabled');  // Re-enable button
            },
            error: function(error) {
                console.error("Error liking post:", error);
                likeButton.removeClass('disabled');  // Re-enable button on error
            }
        });
    });
});

