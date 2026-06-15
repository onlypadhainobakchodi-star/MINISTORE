import streamlit as st

st.set_page_config(
    page_title="MiniStore Support",
    page_icon="💬"
)

# Product catalog
PRODUCTS = {
    "wireless headphones": {
        "price": "$79.99",
        "description": "Noise-cancelling Bluetooth headphones with 30-hour battery life."
    },
    "smart watch": {
        "price": "$129.99",
        "description": "Fitness tracking, heart-rate monitoring, and notifications."
    },
    "laptop backpack": {
        "price": "$49.99",
        "description": "Water-resistant backpack with laptop compartment."
    },
    "coffee maker": {
        "price": "$89.99",
        "description": "Programmable coffee maker with thermal carafe."
    },
    "gaming mouse": {
        "price": "$39.99",
        "description": "RGB gaming mouse with adjustable DPI."
    },
    "yoga mat": {
        "price": "$24.99",
        "description": "Non-slip yoga mat for workouts and meditation."
    }
}


def get_response(user_input):
    text = user_input.lower()

    # Product lookup
    for product, info in PRODUCTS.items():
        if product in text:
            return (
                f"📦 **{product.title()}**\n\n"
                f"💰 Price: {info['price']}\n\n"
                f"📝 {info['description']}"
            )

    # Delivery
    if any(word in text for word in ["delivery", "shipping", "ship"]):
        return (
            "🚚 Standard delivery takes 3–7 business days.\n\n"
            "⚡ Express delivery takes 1–3 business days."
        )

    # Refunds
    if "refund" in text:
        return (
            "💰 Refunds are processed within 5–7 business days "
            "after we receive and inspect the returned item."
        )

    # Returns
    if "return" in text:
        return (
            "↩️ Products may be returned within 30 days "
            "if they are unused and in original packaging."
        )

    # Payment methods
    if any(word in text for word in ["payment", "pay", "card", "upi"]):
        return (
            "💳 Accepted payment methods:\n\n"
            "- Credit Card\n"
            "- Debit Card\n"
            "- UPI\n"
            "- Net Banking\n"
            "- PayPal"
        )

    # Order status
    if any(word in text for word in ["order", "track", "status"]):
        return (
            "📦 Your order is currently being processed.\n\n"
            "Tracking information will appear after shipment."
        )

    # Greetings
    if any(word in text for word in ["hello", "hi", "hey"]):
        return (
            "👋 Welcome to MiniStore Support!\n\n"
            "How can I help you today?"
        )

    return (
        "I can help with:\n\n"
        "• Products\n"
        "• Delivery & Shipping\n"
        "• Refunds\n"
        "• Returns\n"
        "• Payment Methods\n"
        "• Order Status"
    )


# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("💬 MiniStore Support")

st.write("Ask me about products, delivery, refunds, returns, payments, or orders.")

# Show previous chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
prompt = st.chat_input("Ask a question...")

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    response = get_response(prompt)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    with st.chat_message("assistant"):
        st.markdown(response)