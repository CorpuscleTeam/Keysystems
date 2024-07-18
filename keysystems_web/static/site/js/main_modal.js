document.addEventListener('DOMContentLoaded', function () {
  var elems = document.querySelectorAll('.modal');
  var instances = M.Modal.init(elems);

  // Обработчик нажатия на кнопку подтверждения в модальном окне
  document.getElementById('buttonConfirm').addEventListener('click', function () {
    document.getElementById('reg_form').submit();
  });
});