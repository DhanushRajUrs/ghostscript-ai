import requests
import streamlit as st

st.set_page_config(page_title="GhostScript AI", page_icon="👻")

st.title("👻 GhostScript AI")
st.subheader("The ghost in your machine has awakened.")
st.write(
    "Describe a terminal command or a coding problem. "
    "Your local AI ghost will respond with spooky commentary "
    "and a useful explanation."
)

query = st.text_area(
    "Whisper to the ghost...",
    placeholder="Example: What does git push do?",
    height=120
)

mood = st.selectbox(
    "Choose your haunting",
    ["Playfully spooky", "Mysterious and eerie", "Friendly coding ghost"]
)

if st.button("Summon the Ghost 👻", type="primary"):
    if not query.strip():
        st.warning("The ghost needs a message first!")
    else:
        prompt = f"""
        You are GhostScript, a spooky but helpful coding companion.
        Mood: {mood}
        User message: {query}

        Respond with:
        1. A short spooky opening line.
        2. A clear, accurate, beginner-friendly explanation.
        3. One useful example or next step if appropriate.
        Keep the response concise and fun.

        IMPORTANT: Never claim to execute commands.
        Never ask the user to reveal passwords, tokens, or secrets.
        Do not encourage dangerous terminal commands.
        """

        try:
            with st.spinner("A spirit is crossing the digital realm..."):
                response = requests.post(
                    "http://localhost:11434/api/generate",
                    json={
                        "model": "gemma3:1b",
                        "prompt": prompt,
                        "stream": False
                    },
                    timeout=120
                )
                response.raise_for_status()
                answer = response.json()["response"]

            st.success("The ghost has answered!")
            st.markdown(answer)

        except requests.RequestException:
            st.error(
                "The ghost cannot reach Ollama. Make sure Ollama "
                "is running and Gemma 3:1B is installed."
            )

st.caption("Powered by Python + Streamlit + Ollama + Gemma 3:1B")
