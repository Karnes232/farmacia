function show() {
  var x = document.getElementById("hours");
  if (x.style.display === "none") {
    x.style.display = "block";
} else {
    x.style.display = "none";
  }
};

document.querySelectorAll('#edit').forEach(function(button) {
  button.onclick = function() {
    var post_id = button.dataset.info;
    console.log(post_id)
    fetch(`/blog`, {
      method: 'POST',
      body: JSON.stringify({
        post_id: post_id,
  })  
}) 
    return false  
  }
});
