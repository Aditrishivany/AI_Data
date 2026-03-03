async function loadUsers() {
  const users = await fetchJson("/api/users/");
  const tbody = document.getElementById("usersTableBody");
  tbody.innerHTML = "";

  users.forEach((user) => {
    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${user.id}</td>
      <td>${user.name}</td>
      <td>${user.email}</td>
      <td>${user.is_active ? "Active" : "Inactive"}</td>
      <td>
        <button class="btn btn-sm btn-outline-dark me-1" onclick="editUser(${user.id}, '${user.name}', '${user.email}', ${user.is_active})">Edit</button>
        <button class="btn btn-sm btn-outline-danger" onclick="deleteUser(${user.id})">Delete</button>
      </td>
    `;
    tbody.appendChild(row);
  });
}

async function createUser(event) {
  event.preventDefault();
  const payload = {
    name: document.getElementById("userName").value,
    email: document.getElementById("userEmail").value,
    is_active: document.getElementById("userActive").checked,
  };

  try {
    await fetchJson("/api/users/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    event.target.reset();
    showMessage("usersMessage", "User created successfully");
    loadUsers();
  } catch (error) {
    showMessage("usersMessage", error.message, "danger");
  }
}

async function editUser(id, currentName, currentEmail, currentStatus) {
  const name = prompt("Enter new name", currentName);
  if (!name) return;
  const email = prompt("Enter new email", currentEmail);
  if (!email) return;
  const isActive = confirm(`Set active status?\nOK = Active, Cancel = Inactive (Current: ${currentStatus ? "Active" : "Inactive"})`);

  try {
    await fetchJson(`/api/users/${id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, email, is_active: isActive }),
    });
    showMessage("usersMessage", "User updated successfully");
    loadUsers();
  } catch (error) {
    showMessage("usersMessage", error.message, "danger");
  }
}

async function deleteUser(id) {
  if (!confirm("Delete this user?")) return;
  try {
    await fetchJson(`/api/users/${id}`, { method: "DELETE" });
    showMessage("usersMessage", "User deleted successfully");
    loadUsers();
  } catch (error) {
    showMessage("usersMessage", error.message, "danger");
  }
}

document.getElementById("userForm").addEventListener("submit", createUser);
loadUsers();
