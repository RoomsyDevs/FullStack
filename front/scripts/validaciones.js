// validacion para q tome formsubmit

document.addEventListener("DOMContentLoaded", () => {
  const telefonoInput = document.getElementById("telefono");
  const errorDiv = document.getElementById("telefono-error");

  if (!telefonoInput || !errorDiv || !telefonoInput.form) return;

  telefonoInput.form.addEventListener("submit", function (e) {
    const valor = telefonoInput.value.trim();

    const repetido = /^(\d)\1{7,14}$/.test(valor);
    const secuencias = [
      "0123456789",
      "1234567890",
      "123456",
      "0123456",
      "234567",
      "345678",
      "456789",
    ];

    const esSecuencia = secuencias.some((seq) => valor.startsWith(seq));

    if (repetido || esSecuencia) {
      e.preventDefault();
      errorDiv.style.display = "block";
      telefonoInput.classList.add("is-invalid");
    } else {
      errorDiv.style.display = "none";
      telefonoInput.classList.remove("is-invalid");
    }
  });

  telefonoInput.addEventListener("input", () => {
    errorDiv.style.display = "none";
    telefonoInput.classList.remove("is-invalid");
  });
});
