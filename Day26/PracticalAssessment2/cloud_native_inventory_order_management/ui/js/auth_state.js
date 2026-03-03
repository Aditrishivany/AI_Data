function getAuthUser() {
  try {
    return JSON.parse(localStorage.getItem("auth_user") || "null");
  } catch (_) {
    return null;
  }
}

function logoutUser() {
  localStorage.removeItem("auth_user");
  window.location.href = "/login-page";
}

function renderAuthNav() {
  const slot = document.getElementById("authNav");
  if (!slot) return;

  const user = getAuthUser();
  const path = window.location.pathname;
  if (user) {
    slot.innerHTML = `
      <span class="nav-link auth-user">${user.email}</span>
      <button class="btn btn-sm btn-light nav-logout-btn ms-2" id="logoutBtn" type="button">Logout</button>
    `;
    const button = document.getElementById("logoutBtn");
    if (button) {
      button.addEventListener("click", logoutUser);
    }
    return;
  }

  const loginActive = path === "/login-page" ? "active" : "";
  const registerActive = path === "/register-page" ? "active" : "";
  slot.innerHTML = `
    <a class="nav-link ${loginActive}" href="/login-page">Sign In</a>
    <a class="nav-link ${registerActive}" href="/register-page">Register</a>
  `;
}

function enforcePageAccess() {
  const user = getAuthUser();
  const path = window.location.pathname;
  const publicPages = ["/", "/login-page", "/register-page"];
  const isPublic = publicPages.includes(path);

  if (!isPublic && !user) {
    const next = encodeURIComponent(path);
    window.location.href = `/login-page?next=${next}`;
    return;
  }

  if ((path === "/login-page" || path === "/register-page") && user) {
    window.location.href = "/";
  }
}

document.addEventListener("DOMContentLoaded", () => {
  enforcePageAccess();
  renderAuthNav();
});
