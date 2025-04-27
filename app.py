import streamlit as st
import requests
import time

# Sidebar
with st.sidebar:
    st.title("⚙️ Settings")
    st.write("Adjust your app settings here (coming soon!)")
    st.markdown("---")
    st.write("IEEE AI Hackathon 🔥")
    st.write("By: Your Team Name")

# Main title
st.title("🤖 AI Text Generator App")
st.subheader("Powered by GPT-2 🚀")
st.markdown("---")

# Layout
col1, col2 = st.columns(2)

with col1:
    prompt = st.text_area("📝 Enter a prompt for the AI to complete:")

if st.button("🔮 Generate Text"):
    if prompt:
        with st.spinner('Generating text...'):
            start_time = time.time()

            # Send the prompt to FastAPI server
            response = requests.post("http://127.0.0.1:8000/generate_text", json={"prompt": prompt})

            end_time = time.time()

            if response.status_code == 200:
                data = response.json()
                st.success(data['generated_text'])
                st.info(f"⚡ Response time: {round(end_time - start_time, 2)} seconds")
            else:
                st.error("❌ Oops, something went wrong with the server.")
    else:
        st.warning("⚠️ Please enter a prompt first!")

st.markdown("---")
st.caption("Made with ❤️ using Streamlit, FastAPI, and Hugging Face Transformers")
