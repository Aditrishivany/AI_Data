async function loadProductsForInventory() {
  const products = await fetchJson("/api/products/");
  const select = document.getElementById("inventoryProductId");
  select.innerHTML = "";

  products.forEach((product) => {
    const option = document.createElement("option");
    option.value = product.id;
    option.textContent = `${product.name} (Rs. ${product.price.toFixed(2)})`;
    select.appendChild(option);
  });
}

async function loadInventory() {
  const items = await fetchJson("/api/inventory/");
  const tbody = document.getElementById("inventoryTableBody");
  tbody.innerHTML = "";

  items.forEach((item) => {
    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${item.id}</td>
      <td>${item.product ? item.product.name : item.product_id}</td>
      <td>${item.quantity}</td>
      <td>
        <button class="btn btn-sm btn-outline-dark" onclick="updateInventory(${item.id}, ${item.quantity})">Update</button>
      </td>
      <td>
        <button class="btn btn-sm btn-outline-danger" onclick="deleteInventory(${item.id})">Delete</button>
      </td>
    `;
    tbody.appendChild(row);
  });
}

async function createInventory(event) {
  event.preventDefault();
  const payload = {
    product_id: parseInt(document.getElementById("inventoryProductId").value, 10),
    quantity: parseInt(document.getElementById("inventoryQuantity").value, 10),
  };

  try {
    await fetchJson("/api/inventory/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    event.target.reset();
    showMessage("inventoryMessage", "Inventory item created successfully");
    loadInventory();
  } catch (error) {
    showMessage("inventoryMessage", error.message, "danger");
  }
}

async function updateInventory(id, currentQty) {
  const quantity = prompt("Enter new quantity", currentQty);
  if (quantity === null) return;

  try {
    await fetchJson(`/api/inventory/${id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ quantity: parseInt(quantity, 10) }),
    });
    showMessage("inventoryMessage", "Inventory updated successfully");
    loadInventory();
  } catch (error) {
    showMessage("inventoryMessage", error.message, "danger");
  }
}

async function deleteInventory(id) {
  if (!confirm("Delete this inventory item?")) return;

  try {
    await fetchJson(`/api/inventory/${id}`, { method: "DELETE" });
    showMessage("inventoryMessage", "Inventory deleted successfully");
    loadInventory();
  } catch (error) {
    showMessage("inventoryMessage", error.message, "danger");
  }
}

document.getElementById("inventoryForm").addEventListener("submit", createInventory);

Promise.all([loadProductsForInventory(), loadInventory()]).catch((error) => {
  showMessage("inventoryMessage", error.message, "danger");
});
