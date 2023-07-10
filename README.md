# ChatGPT-Clone

This project is a ChatGPT Clone, a web-based chatbot application built using OpenAI, Flask, HTML, TailwindCSS, and MongoDB. It provides a user interface for interacting with the chatbot and utilizes OpenAI's language model to generate responses.MongoDB stores all questions asked and their answers from API request and when next time the same question is asked our model will return answer from the database not from API request, this will reduce the number of API requests.

## Features

- Real-time chat interface with a chatbot powered by OpenAI.
- User-friendly design and layout using HTML and TailwindCSS.
- Backend server implemented in Flask.
- MongoDB integration for storing and retrieving chat history and to reduce the number of API requests.

## Tech Stack Used

* Flask
* HTML
* TailwindCSS
* OpenAI
* MongoDB

## Prerequisites

Make sure you have the following installed on your system:

- Python 3
- MongoDB (Make sure it's running on your machine or accessible via a connection string)

## Getting Started

1. Clone the repository : git clone https://github.com/HarmlessCoder/ChatGPT-Clone.git

2. Navigate to the project directory : cd ChatGPT-Clone

3. Install the required dependencies : pip install -r req.txt

4. Configure the MongoDB connection:

- Open `app.py` file and locate the MongoDB connection settings.
- Modify the connection string with your MongoDB database details.

5. Run the application : python app.py

6. Open your web browser and visit `http://localhost:5000` to access the ChatGPT Clone.

## Usage

- Enter your message in the chat input box and press Enter or click the Send button to send it to the chatbot.
- The chatbot will generate a response based on the input message.
- The chat history is stored in the MongoDB database and can be accessed later.

## Examples
![Screenshot (2163)](https://github.com/HarmlessCoder/ChatGPT-clone/assets/95159170/815b8dff-2e0d-46a7-9887-d7ed9defb442)

![Screenshot (2151)](https://github.com/HarmlessCoder/ChatGPT-clone/assets/95159170/2892330e-2cc6-4171-880a-3634a96c747a)

![Screenshot (2152)](https://github.com/HarmlessCoder/ChatGPT-clone/assets/95159170/4228bde0-ac12-44bb-baa5-45c8c69526d0)

![Screenshot (2154)](https://github.com/HarmlessCoder/ChatGPT-clone/assets/95159170/88ba9308-2d90-4fa9-b336-24efede6e9dc)

![Screenshot (2156)](https://github.com/HarmlessCoder/ChatGPT-clone/assets/95159170/87b2c316-3430-4cb4-a20e-9fb93e8ce330)

![Screenshot (2158)](https://github.com/HarmlessCoder/ChatGPT-clone/assets/95159170/c77b7710-9813-45d8-8f29-26633eb1d43b)

![Screenshot (2161)](https://github.com/HarmlessCoder/ChatGPT-clone/assets/95159170/dc184222-e403-4ffb-b77a-67d7242d2f5f)





