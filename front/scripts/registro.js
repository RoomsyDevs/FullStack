document
  .getElementById("registerForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    const name = document.getElementById("userName").value.trim();
    const email = document.getElementById("userEmail").value.trim();
    const password = document.getElementById("password").value.trim();
    const confirmPassword = document
      .getElementById("confirmPassword")
      .value.trim();
    const messageElement = document.getElementById("message");

    // Validación básica
    if (
      name === "" ||
      email === "" ||
      password === "" ||
      confirmPassword === ""
    ) {
      messageElement.textContent = "Por favor completá todos los campos.";
      messageElement.style.color = "red";
      return;
    }

    // Validación de formato de correo
    const emailValido = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    if (!emailValido) {
      messageElement.textContent = "El formato del correo es inválido.";
      messageElement.style.color = "red";
      return;
    }

    // Validación de contraseñas iguales
    if (password !== confirmPassword) {
      messageElement.textContent = "Las contraseñas no coinciden.";
      messageElement.style.color = "red";
      return;
    }

    // Validación de longitud mínima de contraseña
    if (password.length < 6) {
      messageElement.textContent =
        "La contraseña debe tener al menos 6 caracteres.";
      messageElement.style.color = "red";
      return;
    }

    // Si pasa todas las validaciones
    messageElement.textContent = "¡Registro exitoso! 🎉";
    messageElement.style.color = "green";

    // Simulación de guardado de usuario (por ahora solo en consola)
    console.log("Usuario registrado:", { name, email, password });

    window.location.href = "../index.html";
  });
