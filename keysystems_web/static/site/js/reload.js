document.querySelectorAll('.modal-close').forEach(function(element) {
    element.addEventListener('click', function() {
        location.reload();
    });
});
