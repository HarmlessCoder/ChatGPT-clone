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
![Screenshot (2163)](https://github.com/HarmlessCoder/ChatGPT-clone/assets/95159170/1b580704-2f49-4ff4-8b3d-3059c07c606c)

![Screenshot (2151)](https://github.com/HarmlessCoder/ChatGPT-clone/assets/95159170/81dd124e-62e0-4e43-ba3f-ed14987f14c8)

![Screenshot (2152)](https://github.com/HarmlessCoder/ChatGPT-clone/assets/95159170/98a78777-3366-4582-b934-0430c9de187b)

![Screenshot (2154)](https://github.com/HarmlessCoder/ChatGPT-clone/assets/95159170/e10841b6-eb45-49fc-90fb-78252c29d8be)

![Screenshot (2156)](https://github.com/HarmlessCoder/ChatGPT-clone/assets/95159170/3e3a37fd-c337-4e3c-9070-ca5cca397b92)

![Screenshot (2158)](https://github.com/HarmlessCoder/ChatGPT-clone/assets/95159170/e9efbf63-91ca-49c0-a50b-366351a32be3)

![Screenshot (2161)](https://github.com/HarmlessCoder/ChatGPT-clone/assets/95159170/e0711179-00ab-40c7-bb8b-052d0724f15a)





