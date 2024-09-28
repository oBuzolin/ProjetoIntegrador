//  function togglePasswordVisibility() {
//      var senhaField = document.getElementById("senha_reset");
//      if (senhaField.type === "password") {
//          senhaField.type = "text";
//      } else {
//          senhaField.type = "password";
//      }
     
// }

document.addEventListener('DOMContentLoaded', function () {
    var showPasswordCheckbox = document.getElementById('showPassword');
    var passwordField = document.getElementById('senha');

    if (showPasswordCheckbox && passwordField) {
        showPasswordCheckbox.addEventListener('change', function () {
            if (this.checked) {
                passwordField.type = 'text';
            } else {
                passwordField.type = 'password';
            }
        });
    }
});

// (function () {
//     'use strict';

//     // Busca o formulário e impede o envio se não for válido
//     var form = document.getElementById('loginForm');
//     form.addEventListener('submit', function (event) {
//         if (!form.checkValidity()) {
//             event.preventDefault();
//             event.stopPropagation();
//         }
//         form.classList.add('was-validated');
//     }, false);
// })();
