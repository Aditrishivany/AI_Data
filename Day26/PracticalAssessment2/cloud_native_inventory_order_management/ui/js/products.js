let productsCache = [];
const IMAGE_STORAGE_KEY = "product_image_overrides";

function getImageOverrides() {
  try {
    return JSON.parse(localStorage.getItem(IMAGE_STORAGE_KEY) || "{}");
  } catch (_) {
    return {};
  }
}

function saveImageOverride(productId, imageUrl) {
  const map = getImageOverrides();
  if (imageUrl) {
    map[productId] = imageUrl;
  } else {
    delete map[productId];
  }
  localStorage.setItem(IMAGE_STORAGE_KEY, JSON.stringify(map));
}

function getProductImage(product) {
  const map = getImageOverrides();
  if (map[product.id]) return map[product.id];
  return `https://source.unsplash.com/600x400/?${encodeURIComponent(product.name + ",product")}`;
}

function renderStats(items) {
  const totalValue = items.reduce((sum, item) => sum + item.price, 0);
  const avg = items.length ? totalValue / items.length : 0;
  document.getElementById("productStats").innerHTML = `
    <div class="stat-pill">Total Products: <strong>${items.length}</strong></div>
    <div class="stat-pill">Average Price: <strong>Rs. ${avg.toFixed(2)}</strong></div>
  `;
}

function renderProducts() {
  const grid = document.getElementById("productsGrid");
  const searchText = document.getElementById("productSearch").value.trim().toLowerCase();
  const sortValue = document.getElementById("productSort").value;

  let items = [...productsCache];
  if (searchText) {
    items = items.filter((item) => {
      return (
        item.name.toLowerCase().includes(searchText) ||
        (item.description || "").toLowerCase().includes(searchText)
      );
    });
  }

  if (sortValue === "priceLow") items.sort((a, b) => a.price - b.price);
  if (sortValue === "priceHigh") items.sort((a, b) => b.price - a.price);
  if (sortValue === "nameAZ") items.sort((a, b) => a.name.localeCompare(b.name));
  if (sortValue === "latest") items.sort((a, b) => b.id - a.id);

  renderStats(items);
  grid.innerHTML = "";

  if (items.length === 0) {
    grid.innerHTML = `<div class="text-secondary">No products found.</div>`;
    return;
  }

  items.forEach((product, index) => {
    const card = document.createElement("div");
    card.className = "product-card fade-up";
    card.style.animationDelay = `${Math.min(index * 0.04, 0.3)}s`;

    card.innerHTML = `
      <img class="product-thumb" src="${getProductImage(product)}" alt="${product.name}">
      <div class="p-3">
        <div class="d-flex justify-content-between align-items-start mb-2">
          <h6 class="mb-0">${product.name}</h6>
          <span class="price-tag">Rs. ${product.price.toFixed(2)}</span>
        </div>
        <p class="product-meta mb-3">${product.description || "No description added."}</p>
        <div class="d-flex gap-2">
          <button class="btn btn-sm btn-outline-dark flex-fill js-edit" data-id="${product.id}">Edit</button>
          <button class="btn btn-sm btn-outline-danger flex-fill js-delete" data-id="${product.id}">Delete</button>
        </div>
      </div>
    `;
    grid.appendChild(card);
  });
}

async function loadProducts() {
  productsCache = await fetchJson("/api/products/");
  renderProducts();
}

async function createProduct(event) {
  event.preventDefault();
  const imageUrl = document.getElementById("productImageUrl").value.trim();
  const payload = {
    name: document.getElementById("productName").value,
    description: document.getElementById("productDescription").value,
    price: parseFloat(document.getElementById("productPrice").value),
  };

  try {
    const created = await fetchJson("/api/products/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    if (imageUrl) saveImageOverride(created.id, imageUrl);
    event.target.reset();
    showMessage("productsMessage", "Product created successfully");
    await loadProducts();
  } catch (error) {
    showMessage("productsMessage", error.message, "danger");
  }
}

async function editProduct(id) {
  const product = productsCache.find((item) => item.id === id);
  if (!product) return;

  const name = prompt("Enter new product name", product.name);
  if (!name) return;
  const description = prompt("Enter new description", product.description || "");
  if (description === null) return;
  const priceText = prompt("Enter new price", product.price);
  if (!priceText) return;
  const imageUrl = prompt("Enter image URL (leave blank for auto image)", getImageOverrides()[id] || "");
  if (imageUrl === null) return;

  try {
    await fetchJson(`/api/products/${id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        name,
        description,
        price: parseFloat(priceText),
      }),
    });

    saveImageOverride(id, imageUrl.trim());
    showMessage("productsMessage", "Product updated successfully");
    await loadProducts();
  } catch (error) {
    showMessage("productsMessage", error.message, "danger");
  }
}

async function deleteProduct(id) {
  if (!confirm("Delete this product?")) return;
  try {
    await fetchJson(`/api/products/${id}`, { method: "DELETE" });
    saveImageOverride(id, "");
    showMessage("productsMessage", "Product deleted successfully");
    await loadProducts();
  } catch (error) {
    showMessage("productsMessage", error.message, "danger");
  }
}

document.getElementById("productForm").addEventListener("submit", createProduct);
document.getElementById("productSearch").addEventListener("input", renderProducts);
document.getElementById("productSort").addEventListener("change", renderProducts);

document.getElementById("productsGrid").addEventListener("click", async (event) => {
  const editButton = event.target.closest(".js-edit");
  if (editButton) {
    await editProduct(parseInt(editButton.dataset.id, 10));
    return;
  }

  const deleteButton = event.target.closest(".js-delete");
  if (deleteButton) {
    await deleteProduct(parseInt(deleteButton.dataset.id, 10));
  }
});

loadProducts().catch((error) => {
  showMessage("productsMessage", error.message, "danger");
});
