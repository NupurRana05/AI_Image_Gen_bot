# ai image genration

import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Your Colab API URL
COLAB_API = "https://coat-rebuilt-unpaved.ngrok-free.dev"

st.set_page_config(
    page_title="AI Image Generator",
    page_icon="✨",
    layout="centered"
)

st.title("✨ AI Image Generator")
st.caption("Describe the image you want to create")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        if message["role"] == "user":
            st.write(message["content"])

        else:
            st.image(
                message["image"],
                caption="Generated Image",
                use_container_width=True
            )

# Chat input
prompt = st.chat_input("Describe the image you want...")

if prompt:

    # Show user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.write(prompt)

    # Generate image
    with st.chat_message("assistant"):

        with st.spinner("Creating your image..."):

            try:

                response = requests.post(
                    f"{COLAB_API}/generate",

                    json={
                        "prompt": prompt,
                        "negative_prompt": (
                            "blurry, low quality, distorted face, "
                            "extra fingers, bad anatomy, watermark, text"
                        ),
                        "num_inference_steps": 30,
                        "guidance_scale": 7.5
                    },

                    headers={
                        "ngrok-skip-browser-warning": "true"
                    },

                    timeout=300
                )

                response.raise_for_status()

                image = Image.open(
                    BytesIO(response.content)
                ).copy()

                st.image(
                    image,
                    caption="Generated Image",
                    use_container_width=True
                )

                st.download_button(
                    "⬇️ Download Image",
                    data=response.content,
                    file_name="generated_image.png",
                    mime="image/png"
                )

                st.session_state.messages.append({
                    "role": "assistant",
                    "image": image
                })

            except Exception as e:

                st.error(
                    f"Image generation failed: {e}"
                )
