async function loadHomeStats() {
  try {
    const [users, products, orders, inventory] = await Promise.all([
      fetchJson("/api/users/"),
      fetchJson("/api/products/"),
      fetchJson("/api/orders/"),
      fetchJson("/api/inventory/"),
    ]);

    document.getElementById("usersCount").textContent = users.length;
    document.getElementById("productsCount").textContent = products.length;
    document.getElementById("ordersCount").textContent = orders.length;
    document.getElementById("inventoryCount").textContent = inventory.length;
  } catch (error) {
    document.getElementById("usersCount").textContent = "N/A";
    document.getElementById("productsCount").textContent = "N/A";
    document.getElementById("ordersCount").textContent = "N/A";
    document.getElementById("inventoryCount").textContent = "N/A";
  }
}

function renderList(title, values) {
  const titleEl = document.getElementById("dbMetaTitle");
  const bodyEl = document.getElementById("dbMetaBody");
  titleEl.textContent = title;

  if (!values || values.length === 0) {
    bodyEl.innerHTML = `<p class="mb-0 text-secondary">No items found.</p>`;
    return;
  }

  if (typeof values[0] === "string") {
    bodyEl.innerHTML = `
      <ul class="list-group">
        ${values.map((item) => `<li class="list-group-item">${item}</li>`).join("")}
      </ul>
    `;
    return;
  }

  if ("rows" in values[0]) {
    bodyEl.innerHTML = `
      <div class="table-responsive">
        <table class="table table-striped align-middle">
          <thead>
            <tr>
              <th>Table</th>
              <th>Rows</th>
              <th>Columns</th>
              <th>Values</th>
            </tr>
          </thead>
          <tbody>
            ${values
              .map(
                (table) => `
                  <tr>
                    <td><strong>${table.name}</strong></td>
                    <td>${table.rows}</td>
                    <td><small>${(table.columns || []).join(", ")}</small></td>
                    <td>
                      <small class="text-secondary">
                        ${(table.values || []).length === 0
                          ? "No rows"
                          : (table.values || [])
                              .map((row) => JSON.stringify(row))
                              .join("<br>")}
                      </small>
                    </td>
                  </tr>
                `
              )
              .join("")}
          </tbody>
        </table>
      </div>
    `;
    return;
  }

  if ("documents" in values[0]) {
    bodyEl.innerHTML = `
      <div class="table-responsive">
        <table class="table table-striped align-middle">
          <thead>
            <tr>
              <th>Collection</th>
              <th>Documents</th>
              <th>Fields (sample)</th>
              <th>Values</th>
            </tr>
          </thead>
          <tbody>
            ${values
              .map(
                (collection) => `
                  <tr>
                    <td><strong>${collection.name}</strong></td>
                    <td>${collection.documents}</td>
                    <td><small>${(collection.fields || []).join(", ") || "-"}</small></td>
                    <td>
                      <small class="text-secondary">
                        ${(collection.values || []).length === 0
                          ? "No documents"
                          : (collection.values || [])
                              .map((doc) => JSON.stringify(doc))
                              .join("<br>")}
                      </small>
                    </td>
                  </tr>
                `
              )
              .join("")}
          </tbody>
        </table>
      </div>
    `;
  }
}

async function showMySQLTables() {
  try {
    const data = await fetchJson("/api/meta/mysql-tables");
    renderList("MySQL Tables", data.tables);
    bootstrap.Modal.getOrCreateInstance(document.getElementById("dbMetaModal")).show();
  } catch (error) {
    alert(`Unable to load MySQL tables: ${error.message}`);
  }
}

async function showMongoCollections() {
  try {
    const data = await fetchJson("/api/meta/mongodb");
    renderList("MongoDB Collections", data.collections);
    bootstrap.Modal.getOrCreateInstance(document.getElementById("dbMetaModal")).show();
  } catch (error) {
    alert(`Unable to load MongoDB collections: ${error.message}`);
  }
}

const mysqlButton = document.getElementById("mysqlBadgeBtn");
if (mysqlButton) {
  mysqlButton.addEventListener("click", showMySQLTables);
}

const mongoButton = document.getElementById("mongoBadgeBtn");
if (mongoButton) {
  mongoButton.addEventListener("click", showMongoCollections);
}

loadHomeStats();
