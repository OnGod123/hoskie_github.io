// Assuming you've included the emoji picker library (e.g., picker.js)
const emojiPicker = new Picker({
  trigger: document.querySelector('.emoji-picker-container'),
  position: {
    at: 'bottom center',
    boundary: document.body
  },
  onSelect: (emoji) => {
    const commentTextArea = document.querySelector('#comment-form textarea');
    commentTextArea.value += emoji;
  }
});
const commentForm = document.getElementById('comment-form');
const commentImageInput = document.querySelector('#comment-form input[name="comment_image"]');
const commentVideoInput = document.querySelector('#comment-form input[name="comment_video"]');

commentForm.addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent default form submission

  const commentText = this.elements['comment_text'].value.trim();
  const contentType = this.elements['content_type'].value;
  const objectId = this.elements['object_id'].value;

  // Handle image upload (optional)
  if (commentImageInput.files.length > 0) {
    const imageFile = commentImageInput.files[0];
    const reader = new FileReader();
    reader.readAsDataURL(imageFile);
    reader.onload = function(e) {
      // Send AJAX request with comment text and image data URL (implement logic)
      // ...
    };
  }

  // Handle video upload (optional)
  if (commentVideoInput.files.length > 0) {
    const videoFile = commentVideoInput.files[0];
    const videoSize = videoFile.size;
    if (videoSize > 10 * 1024 * 1024) { // Limit video size to 10MB (adjust as needed)
      alert('Video size is too large! Please upload a video under 10MB.');
      return;
    }
    const reader = new FileReader();
    reader.readAsDataURL(videoFile);
    reader.onload = function(e) {
      // Send AJAX request with comment text and video data URL (implement logic)
      // ...
    };
  }

  // If no image or video, send comment text only
  if (!commentImageInput.files.length && !commentVideoInput.files.length && commentText) {
    // Send AJAX request with comment text (implement logic)
    // ...
  } else {
    // Handle potential errors (e.g., file type restrictions)
    alert('Please select a valid image or video file.');
  }

  // Clear form fields after successful submission (optional)
  commentForm.reset();
});

