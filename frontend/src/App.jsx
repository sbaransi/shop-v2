import { useEffect, useState } from "react";

function App() {
  const [products, setProducts] = useState([]);
  const [name, setName] = useState("");
  const [price, setPrice] = useState("");

  const loadProducts = () => {
    fetch("http://localhost:5002/products")
      .then((res) => res.json())
      .then((data) => setProducts(data));
  };

  useEffect(() => {
    loadProducts();
  }, []);

  const addProduct = async () => {
    await fetch("http://localhost:5002/products", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name,
        price: Number(price),
      }),
    });

    setName("");
    setPrice("");

    loadProducts();
  };

  return (
    <div style={{ padding: "40px" }}>
      <h1>Shop V2 Products</h1>

      <div>
        <input
          placeholder="Product Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />

        <input
          placeholder="Price"
          value={price}
          onChange={(e) => setPrice(e.target.value)}
        />

        <button onClick={addProduct}>
          Add Product
        </button>
      </div>

      <hr />

      {products.map((product) => (
        <div key={product.id}>
          <h3>{product.name}</h3>
          <p>${product.price}</p>
        </div>
      ))}
    </div>
  );
}

export default App;