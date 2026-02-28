let selectedOrderItems = [];
let productsCache = [];

function renderSelectedItems() {
  const list = document.getElementById("selectedItems");
  list.innerHTML = "";

  selectedOrderItems.forEach((item, index) => {
    const li = document.createElement("li");
    li.className = "list-group-item d-flex justify-content-between align-items-center";
    li.innerHTML = `
      <span>${item.product_name} x ${item.quantity}</span>
      <button class="btn btn-sm btn-outline-danger" onclick="removeOrderItem(${index})">Remove</button>
    `;
    list.appendChild(li);
  });
}

function removeOrderItem(index) {
  selectedOrderItems.splice(index, 1);
  renderSelectedItems();
}

async function loadUsersForOrders() {
  const users = await fetchJson("/api/users/");
  const select = document.getElementById("orderUserId");
  select.innerHTML = "";
  users.forEach((user) => {
    const option = document.createElement("option");
    option.value = user.id;
    option.textContent = `${user.name} (${user.email})`;
    select.appendChild(option);
  });
}

async function loadProductsForOrders() {
  productsCache = await fetchJson("/api/products/");
  const select = document.getElementById("orderProductId");
  select.innerHTML = "";
  productsCache.forEach((product) => {
    const option = document.createElement("option");
    option.value = product.id;
    option.textContent = `${product.name} (Rs. ${product.price.toFixed(2)})`;
    select.appendChild(option);
  });
}

function addOrderItem() {
  const productId = parseInt(document.getElementById("orderProductId").value, 10);
  const quantity = parseInt(document.getElementById("orderQuantity").value, 10);

  if (!productId || quantity < 1) {
    showMessage("ordersMessage", "Select product and valid quantity", "danger");
    return;
  }

  const product = productsCache.find((p) => p.id === productId);
  if (!product) return;

  selectedOrderItems.push({
    product_id: productId,
    quantity: quantity,
    product_name: product.name,
  });
  renderSelectedItems();
}

async function createOrder(event) {
  event.preventDefault();
  if (selectedOrderItems.length === 0) {
    showMessage("ordersMessage", "Add at least one item", "danger");
    return;
  }

  const payload = {
    user_id: parseInt(document.getElementById("orderUserId").value, 10),
    items: selectedOrderItems.map(({ product_id, quantity }) => ({ product_id, quantity })),
  };

  try {
    await fetchJson("/api/orders/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    selectedOrderItems = [];
    renderSelectedItems();
    showMessage("ordersMessage", "Order created successfully");
    loadOrders();
  } catch (error) {
    showMessage("ordersMessage", error.message, "danger");
  }
}

async function loadOrders() {
  const orders = await fetchJson("/api/orders/");
  const tbody = document.getElementById("ordersTableBody");
  tbody.innerHTML = "";

  orders.forEach((order) => {
    const itemsText = order.items
      .map((item) => `${item.product?.name || item.product_id} x ${item.quantity}`)
      .join(", ");
    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${order.id}</td>
      <td>${order.user_id}</td>
      <td>${order.status}</td>
      <td>Rs. ${order.total_amount.toFixed(2)}</td>
      <td>${itemsText || "-"}</td>
      <td>
        <button class="btn btn-sm btn-outline-danger" onclick="deleteOrder(${order.id})">Delete</button>
      </td>
    `;
    tbody.appendChild(row);
  });
}

async function deleteOrder(id) {
  if (!confirm("Delete this order?")) return;
  try {
    await fetchJson(`/api/orders/${id}`, { method: "DELETE" });
    showMessage("ordersMessage", "Order deleted successfully");
    loadOrders();
  } catch (error) {
    showMessage("ordersMessage", error.message, "danger");
  }
}

document.getElementById("addItemBtn").addEventListener("click", addOrderItem);
document.getElementById("orderForm").addEventListener("submit", createOrder);

Promise.all([loadUsersForOrders(), loadProductsForOrders(), loadOrders()]).catch((error) => {
  showMessage("ordersMessage", error.message, "danger");
});
