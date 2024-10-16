# PDF-chatbot by **Ch. Manoj Naga Varma**

This project concerns a chatbot that interacts with the content in desired PDF files. It is like asking answers to questions that are from the content.

This project uses the Gemini 1.5 Pro LLM Model and is built using Google API Studio API.

Due to our limited resources and budget, we are using a free Google API, which can be accessed only once by a single user at the same time.

1.) Run this command to install the needful dependencies which are mentioned in the requirements.txt file

 ````
pip install -r requirements.txt
````

  
2.) The code is given

3.) Create a .env file, which is used to protect your API key from explicit display, and safeguards your API key not to be used by anyone.

4.) Store your API key inside a variable, to load that confidential API key into another variable, to access it inside the code

5.) The setx command is used in Windows to set environment variables permanently for the current user session or globally across all sessions. When working with APIs (like Google's APIs), it's common to store sensitive information, such as API keys, in environment variables to keep them secure and accessible without hardcoding them into your application code.

Enter this command in the command prompt of your PC

````
setx GOOGLE_API_KEY your_api_key

````

6.) After this, run your streamlit file in your compiler's terminal
