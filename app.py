import streamlit as st

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

# ---------------------------------------------------
# PRODUCT DATA
# ---------------------------------------------------
products = [
    {
        "name": "Wireless Headphones",
        "price": 79.99,
        "category": "Electronics",
        "description": "Noise-cancelling Bluetooth headphones with 30-hour battery life."
    },
    {
        "name": "Smart Watch",
        "price": 129.99,
        "category": "Electronics",
        "description": "Fitness tracking, heart-rate monitoring, and notifications."
    },
    {
        "name": "Laptop Backpack",
        "price": 49.99,
        "category": "Accessories",
        "description": "Water-resistant backpack with laptop compartment."
    },
    {
        "name": "Coffee Maker",
        "price": 89.99,
        "category": "Home",
        "description": "Programmable coffee maker with thermal carafe."
    },
    {
        "name": "Gaming Mouse",
        "price": 39.99,
        "category": "Electronics",
        "description": "RGB gaming mouse with adjustable DPI."
    },
    {
        "name": "Yoga Mat",
        "price": 24.99,
        "category": "Fitness",
        "description": "Non-slip yoga mat for workouts and meditation."
    }
]

# ---------------------------------------------------
# SESSION STATE
# ---------------------------------------------------
if "cart_items" not in st.session_state:
    st.session_state.cart_items = 0

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}

.hero {
    padding: 30px;
    border-radius: 15px;
    background: linear-gradient(135deg,#0f172a,#2563eb);
    color:white;
    text-align:center;
    margin-bottom:30px;
}

.product-card {
    background:white;
    padding:20px;
    border-radius:12px;
    box-shadow:0 2px 10px rgba(0,0,0,0.1);
    margin-bottom:20px;
    min-height:280px;
}

.price {
    color:#2563eb;
    font-size:24px;
    font-weight:bold;
}

.floating-btn {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background: #2563eb;
    color: white;
    padding: 14px 20px;
    border-radius: 50px;
    text-decoration: none;
    font-weight: bold;
    z-index: 9999;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
st.sidebar.title("🛍️ Categories")

categories = ["All"] + sorted(
    list(set([p["category"] for p in products]))
)

selected_category = st.sidebar.selectbox(
    "Choose Category",
    categories
)

st.sidebar.markdown("---")
st.sidebar.subheader("🛒 Cart Summary")
st.sidebar.write(f"Items: {st.session_state.cart_items}")
st.sidebar.write("Total: Demo Store")

# ---------------------------------------------------
# HOMEPAGE
# ---------------------------------------------------
st.markdown("""
<div class="hero">
<h1>MiniStore</h1>
<h3>Your Modern Online Shopping Experience</h3>
<p>Find the best products at unbeatable prices.</p>
</div>
""", unsafe_allow_html=True)

st.header("⭐ Featured Products")

filtered_products = products

if selected_category != "All":
    filtered_products = [
        p for p in products
        if p["category"] == selected_category
    ]

# ---------------------------------------------------
# PRODUCT GRID
# ---------------------------------------------------
cols = st.columns(3)

for index, product in enumerate(filtered_products):
    with cols[index % 3]:
        st.markdown(
            f"""
            <div class="product-card">
                <h3>{product['name']}</h3>
                <p><b>Category:</b> {product['category']}</p>
                <p>{product['description']}</p>
                <p class="price">${product['price']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            f"Add to Cart - {product['name']}",
            key=product["name"]
        ):
            st.session_state.cart_items += 1
            st.success(f"{product['name']} added!")

# ---------------------------------------------------
# FLOATING SUPPORT BUTTON
# ---------------------------------------------------
st.markdown(
    """
    <a class="floating-btn"
       href="/Support_Chatbot"
       target="_self">
       💬 Support
    </a>
    """,
    unsafe_allow_html=True
)