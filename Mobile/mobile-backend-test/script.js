document
  .getElementById("loginForm")
  .addEventListener("submit", async function (e) {
    e.preventDefault();

    const userId = document.getElementById("userId").value;
    const password = document.getElementById("password").value;
    const messageDiv = document.getElementById("message");

    try {
      const response = await fetch("http://localhost:3000/auth/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ userId, password }),
      });

      const data = await response.json();

      if (response.ok) {
        messageDiv.textContent = `Login successful! Redirecting...`;
        messageDiv.style.color = "green";
        localStorage.setItem("token", data.token);
        window.location.href = "turmas.html";
      } else {
        messageDiv.textContent = `Login failed: ${data.message}`;
        messageDiv.style.color = "red";
      }
    } catch (error) {
      messageDiv.textContent = `Login failed: ${error.message}`;
      messageDiv.style.color = "red";
    }
  });
