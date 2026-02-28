async function handleRegister(event) {
  event.preventDefault();
  const payload = {
    name: document.getElementById("registerName").value.trim(),
    email: document.getElementById("registerEmail").value.trim(),
    password: document.getElementById("registerPassword").value,
  };

  try {
    const data = await fetchJson("/api/auth/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    localStorage.setItem("auth_user", JSON.stringify(data));
    showMessage("authMessage", "Registration successful. Redirecting to sign in...");
    setTimeout(() => {
      window.location.href = "/login-page";
    }, 900);
  } catch (error) {
    showMessage("authMessage", error.message, "danger");
  }
}

async function handleLogin(event) {
  event.preventDefault();
  const payload = {
    email: document.getElementById("loginEmail").value.trim(),
    password: document.getElementById("loginPassword").value,
  };

  try {
    const data = await fetchJson("/api/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    localStorage.setItem("auth_user", JSON.stringify(data));
    showMessage("authMessage", "Login successful. Redirecting to dashboard...");
    const next = new URLSearchParams(window.location.search).get("next");
    const redirectPath = next && next.startsWith("/") ? next : "/";
    setTimeout(() => {
      window.location.href = redirectPath;
    }, 900);
  } catch (error) {
    showMessage("authMessage", error.message, "danger");
  }
}

const registerForm = document.getElementById("registerForm");
if (registerForm) {
  registerForm.addEventListener("submit", handleRegister);
}

const loginForm = document.getElementById("loginForm");
if (loginForm) {
  loginForm.addEventListener("submit", handleLogin);
}
