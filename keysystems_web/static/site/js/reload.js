// обновление страницы при закрытии модального окна
document.querySelectorAll('.modal-close').forEach(function(element) {
    element.addEventListener('click', function() {
        location.reload();
    });
});

// отслеживание закрытия модального окна
document.querySelectorAll('.modal-close').forEach((closeBtn) => {
    closeBtn.addEventListener('click', () => {
        console.log('Модальное окно закрыто')
    })
})

