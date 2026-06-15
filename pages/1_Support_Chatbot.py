import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="MiniStore Support",
    page_icon="💬"
)

# --------------------------------------------
# OPENAI CLIENT
# --------------------------------------------
client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

# --------------------------------------------
# STORE CATALOG
# --------------------------------------------
catalog = """
Products:

1. Wireless Headphones
Price: $79.99
Noise-cancelling Bluetooth headphones.

2. Smart Watch
Price: $129.99
Fitness tracking and notifications.

3. Laptop Backpack
Price: $49.99
Water-resistant backpack.

4. Coffee Maker
Price: $89.99
Programmable coffee maker.

5. Gaming Mouse
Price: $39.99
RGB gaming mouse.

6. Yoga Mat
Price: $24.99
Non-slip fitness mat.
"""

# --------------------------------------------
# SYSTEM PROMPT
# --------------------------------------------
SYSTEM_PROMPT = f"""
You are MiniStore's professional customer support assistant.

You only answer questions related to:
- products
- orders
- delivery
- shipping
- refunds
- returns
- payments
- store policies

Store Catalog:
{catalog}

Rules:
1. Only discuss MiniStore support topics.
2. If a user asks unrelated questions,
   politely redirect them to store support.
3. Be professional and concise.
4. Help customers understand products,
   orders, refunds, delivery, and payment options.
"""

# --------------------------------------------
# CHAT HISTORY
# --------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("💬 MiniStore Support Chatbot")

st.write(
    "Ask questions about products, delivery, refunds, payments, and orders."
)

# --------------------------------------------
# DISPLAY CHAT HISTORY
# --------------------------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --------------------------------------------
# USER INPUT
# --------------------------------------------
prompt = st.chat_input("Ask MiniStore Support...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    messages.extend(st.session_state.messages)

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages,
        temperature=0.3
    )

    answer = response.choices[0].message.content

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)