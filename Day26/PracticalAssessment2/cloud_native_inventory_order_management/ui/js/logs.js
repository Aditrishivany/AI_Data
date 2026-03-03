async function loadLogs() {
  const logs = await fetchJson("/api/logs/?limit=100");
  const tbody = document.getElementById("logsTableBody");
  tbody.innerHTML = "";

  logs.forEach((log) => {
    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${log.id}</td>
      <td>${log.action}</td>
      <td>${log.entity}</td>
      <td>${log.details}</td>
      <td>${new Date(log.timestamp).toLocaleString()}</td>
    `;
    tbody.appendChild(row);
  });
}

async function createLog(event) {
  event.preventDefault();
  const payload = {
    action: document.getElementById("logAction").value,
    entity: document.getElementById("logEntity").value,
    details: document.getElementById("logDetails").value,
  };

  try {
    await fetchJson("/api/logs/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    event.target.reset();
    showMessage("logsMessage", "Log saved successfully");
    loadLogs();
  } catch (error) {
    showMessage("logsMessage", error.message, "danger");
  }
}

document.getElementById("logForm").addEventListener("submit", createLog);
document.getElementById("refreshLogsBtn").addEventListener("click", loadLogs);

loadLogs().catch((error) => showMessage("logsMessage", error.message, "danger"));
