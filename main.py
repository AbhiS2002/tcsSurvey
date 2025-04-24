import streamlit as st

# Sample keyword-based knowledge base
knowledge_base = {
    "health insurance": "Health insurance covers medical expenses such as doctor visits, hospital stays, surgeries, and prescriptions.",
    "life insurance": "Life insurance provides financial support to your family or nominee after the policyholder's death.",
    "auto insurance": "Auto insurance covers damage to your vehicle and third-party liability in case of accidents.",
    "home insurance": "Home insurance protects your house and belongings against damages or losses due to disasters or theft.",
    "claim process": "To file a claim, you need to submit the necessary documents either online or at a branch. Processing takes 7–10 days.",
    "premium payment": "Premiums can be paid monthly, quarterly, or annually. Online and offline options are available.",
    "coverage options": "Coverage varies by policy. Common options include hospitalization, accidental cover, and critical illness benefits.",
    "policy renewal": "Insurance policies can usually be renewed online before the expiry date. Late renewal might incur penalties."
}

# Function to get chatbot response
def get_response(user_input):
    user_input_lower = user_input.lower()
    for keyword, response in knowledge_base.items():
        if keyword in user_input_lower:
            return response
    return "I'm sorry, I couldn't find information on that. Would you like to talk to a human agent?"

# Streamlit UI
st.set_page_config(page_title="Insurance Info Chatbot", layout="centered")
st.title("🤖 AI-Powered Insurance Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Ask me about our insurance policies:", "")

if user_input:
    bot_response = get_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", bot_response))

# Display chat history
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**🧑 You:** {message}")
    else:
        st.markdown(f"**🤖 Bot:** {message}")

# Optional reset button
if st.button("🔁 Reset Chat"):
    st.session_state.chat_history = []
