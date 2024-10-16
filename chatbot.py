import streamlit as st
import os
import google.generativeai as genai
import dotenv

dotenv.load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Set up the model
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

# Streamlit app
def main():
    st.set_page_config(page_title="PDF Chatbot", page_icon="📚", layout="wide")
    st.markdown("""
        <style>
        /* Change the main background color to black */
        .main {
            background-color: #000000; /* Black background */
            color: white; /* Text color set to white for visibility */
        }
        /* Change the sidebar background color to black */
        .sidebar .sidebar-content {
            background-color: #333333; /* Dark gray sidebar background */
            color: white; /* Text color set to white */
        }
        /* Style for the title */
        h1 {
            font-family: 'Arial', sans-serif;
            color: white; /* Title color set to white */
            text-align: center; /* Center align the title */
            background-color: #0073e6; /* Attractive background for the title */
            padding: 20px; /* Add padding */
            border-radius: 10px; /* Rounded corners */
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Add shadow for depth */
        }
        /* Customize sidebar file uploader */
        .stFileUploader {
            background-color: #222222; /* Dark background for file uploader */
            color: white; /* White text color */
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("PDF Chatbot 📚")
    st.markdown("### Upload a PDF document and start chatting!")

    # Upload PDF
    with st.sidebar:
        uploaded_file = st.file_uploader("Upload your PDF here", type="pdf")

        if uploaded_file is not None:
            # Save the uploaded file to a temporary location
            tmp_filepath = uploaded_file.name
            with open(tmp_filepath, "wb") as f:
                f.write(uploaded_file.getvalue())

            # Upload the file and notify the user
            file_id = genai.upload_file(path=tmp_filepath)
            st.success("Successfully uploaded!")

            # Initialize chat history if the file is uploaded
            if 'chat_history' not in st.session_state:
                st.session_state.chat_history = []

    # Text input for asking questions
    user_input = st.text_input("Please ask a question about the uploaded document:")

    if user_input:
        # Generate response from the model
        response = model.generate_content([file_id, user_input])
        
        # Save to chat history
        st.session_state.chat_history.append({"question": user_input, "response": response.text})

        # Display the answer
        st.write("*Response:*", response.text)

        # Save communication to a text file
        save_to_file(st.session_state.chat_history)

    # Display chat history
    if st.session_state.get('chat_history'):
        with st.expander("Chat History", expanded=False):
            for chat in st.session_state.chat_history:
                st.write(f"*Q:* {chat['question']}")
                st.write(f"*A:* {chat['response']}")
                st.write("---")

    # Clear chat history button
    if st.button("Clear Chat History"):
        st.session_state.chat_history = []
        st.success("Chat history cleared!")

def save_to_file(chat_history):
    """Save chat history to a text file with utf-8 encoding."""
    with open("chat_history.txt", "w", encoding="utf-8") as file:
        for chat in chat_history:
            file.write(f"Q: {chat['question']}\n")
            file.write(f"A: {chat['response']}\n")
            file.write("---\n")


if __name__ == "__main__":
    main()
