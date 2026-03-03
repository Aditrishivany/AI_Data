const API_BASE = "";

function showMessage(targetId, message, type = "success") {
  const alertBox = document.getElementById(targetId);
  if (!alertBox) return;
  alertBox.className = `alert alert-${type}`;
  alertBox.textContent = message;
  alertBox.classList.remove("d-none");
  setTimeout(() => alertBox.classList.add("d-none"), 2500);
}

async function fetchJson(url, options = {}) {
  const response = await fetch(`${API_BASE}${url}`, options);
  if (!response.ok) {
    let detail = "Request failed";
    try {
      const errorData = await response.json();
      detail = errorData.detail || detail;
    } catch (_) {}
    throw new Error(detail);
  }

  if (response.status === 204) return null;
  return response.json();
}

function initPageInteractions() {
  const cards = document.querySelectorAll(".page-card");
  cards.forEach((card, index) => {
    if (!card.classList.contains("fade-up")) {
      card.classList.add("fade-up");
      card.style.animationDelay = `${Math.min(index * 0.05, 0.25)}s`;
    }
  });
}

document.addEventListener("DOMContentLoaded", initPageInteractions);
