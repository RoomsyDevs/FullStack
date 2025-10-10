document
  .getElementById("loginForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    const email = document.getElementById("userEmail").value.trim();
    const password = document.getElementById("password").value.trim();
    const messageElement = document.getElementById("message");

    // Validación básica
    if (email === "" || password === "") {
      messageElement.textContent = "Ingresa un correo y contraseña válidos";
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

    // Validación de credenciales
    if (email === "usuario@gmail.com" && password === "admin123+") {
      messageElement.textContent = "¡Login exitoso!";
      messageElement.style.color = "green";
      window.location.href = "../index.html";
    } else {
      messageElement.textContent = "Correo o contraseña incorrectos.";
      messageElement.style.color = "red";
    }
  });
