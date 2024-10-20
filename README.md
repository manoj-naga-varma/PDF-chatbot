# PDF Chatbot by **Ch. Manoj Naga Varma**

This project is a **PDF Chatbot** that allows users to upload PDF documents and interact with the contents using a chatbot interface. The chatbot is powered by Google Generative AI, specifically the **Gemini 1.5 Pro** model, which generates responses based on user queries about the uploaded document. The web interface is built using **Streamlit**, which provides an intuitive and interactive platform for users to engage with the chatbot. This project concerns a chatbot interacting with the content in desired PDF files. It is like asking answers to questions from the content. Due to our limited resources and budget, we are using a free Google API, which can be accessed only once by a single user at the same time.


## Features

- **Upload and Interact with PDFs**: Users can upload PDF documents through the sidebar and start querying the contents of the document.
- **Real-time Responses**: Powered by the Gemini 1.5 Pro model, the chatbot generates accurate and contextual answers to questions asked about the uploaded PDF.
- **Chat History**: View all previous interactions in the chat history, ensuring users can track their questions and the corresponding responses.
- **File Upload & Processing**: PDF files are securely uploaded and processed to extract relevant information for querying.
- **Session State Management**: Keeps track of chat history during the session and allows users to clear it when needed.
- **Stylish Interface**: A custom theme with a dark background, center-aligned titles, and a clean layout enhances the user experience.

## Prerequisites

- **Python 3.x** installed on your machine.
- A **Google Cloud API key** for the Google Generative AI model.
- **Streamlit** for building the web interface.

## Creating the API Key

You can create the API key for accessing Google Generative AI using the following steps:

- Visit this link: https://aistudio.google.com/app/apikey.
- Click on Create API Key, and it will generate an API key for you.
- Store the API key for use in the project as described below.

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repository/pdf-chatbot.git
   cd PDF-Chatbot
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory to protect the API key:

   ```bash
   .env
   ```

   In the `.env` file, include the following line:

   ```
   GOOGLE_API_TOKEN = "YOUR_GOOGLE_API_KEY"
   ```

   Replace `"YOUR_GOOGLE_API_KEY"` with your actual Google Cloud API key.

4. To set the API key for your environment, use the following command (Dont add the quotes for API Key):

   ```bash
   setx GOOGLE_API_KEY YOUR_GOOGLE_API_KEY
   ```

5. Run the Streamlit app:

   ```bash
   streamlit run {Filename}.py
   ```

6. Access the app through your browser at `http://localhost:8501`.

## Usage

1. **Upload a PDF**: Use the sidebar to upload a PDF document. Once uploaded, the file will be processed, and you can begin asking questions.
   
2. **Ask a Question**: Input your query into the text box. The chatbot will respond with information extracted from the PDF.
   
3. **Chat History**: View all previous questions and responses under the "Chat History" section. Clear the history if needed by clicking the "Clear Chat History" button.

4. **Save Conversations**: The chat history is automatically saved to a text file named `chat_history.txt` for reference.

Here’s how you can format the section for the **README** file to handle Axios errors:

---

### Handling Axios Errors During PDF Uploads

If you encounter an **Axios error** while uploading a PDF document, it might be due to CORS (Cross-Origin Resource Sharing) or XSRF protection issues in Streamlit. To fix this, follow the steps below to configure Streamlit's server settings.

1. **Create a `config.toml` File**:
   - Navigate to your Streamlit configuration folder (usually located at `~/.streamlit/` or the root directory of your project).
   - If the `config.toml` file doesn't already exist, create it in this directory.

2. **Update the `config.toml` File**:
   Add the following lines to the `config.toml` file:
   ```toml
   [server]
   enableXsrfProtection = false
   enableCORS = false
   ```

3. **Restart the Application**:
   After saving the changes, restart your Streamlit app to apply the new settings.

By disabling XSRF protection and CORS, this configuration should resolve the Axios errors related to PDF uploads.


## Example

- Upload a document like `sample.pdf`.
- Ask questions such as, “What is the main topic of the document?” or “Summarize section 2.”
- The chatbot will provide answers based on the document’s contents.

## File Structure

```
.
├── Chatbot.py             # Main Streamlit app file
├── .env                   # Environment file for storing the API key
├── requirements.txt       # Python dependencies
└── chat_history.txt       # Chat history file generated during session
```

## Technologies Used

- **Google Generative AI (Gemini 1.5 Pro)**: Generates responses based on user queries.
- **Streamlit**: Web framework for creating the user interface.
- **Python**: Core programming language used for backend logic and integration.
