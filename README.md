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
![image](https://raw.githubusercontent.com/HarmlessCoder/ChatGPT-clone/main/assets/Screenshot%20(2163).png?token=GHSAT0AAAAAACEJ43AXPOVY7S72WLCYH7ZEZFLJ4ZQ)

![image](https://raw.githubusercontent.com/HarmlessCoder/ChatGPT-clone/main/assets/Screenshot%20(2151).png?token=GHSAT0AAAAAACEJ43AXYUYNGLCVXHWGWRP6ZFLJ5JA)

![image](https://raw.githubusercontent.com/HarmlessCoder/ChatGPT-clone/main/assets/Screenshot%20(2152).png?token=GHSAT0AAAAAACEJ43AXK4JMK3BBRHP2RT4CZFLJ5VA)

![image](https://raw.githubusercontent.com/HarmlessCoder/ChatGPT-clone/main/assets/Screenshot%20(2154).png?token=GHSAT0AAAAAACEJ43AXEO76EB6XFNA2SX7EZFLJ6EQ)

![image](https://raw.githubusercontent.com/HarmlessCoder/ChatGPT-clone/main/assets/Screenshot%20(2156).png?token=GHSAT0AAAAAACEJ43AXMVMNIHVFOFHOQOVOZFLJ6QA)

![image](https://raw.githubusercontent.com/HarmlessCoder/ChatGPT-clone/main/assets/Screenshot%20(2158).png?token=GHSAT0AAAAAACEJ43AXHH25HYP3LF7M4MIEZFLJ63A)

![image](https://raw.githubusercontent.com/HarmlessCoder/ChatGPT-clone/main/assets/Screenshot%20(2161).png?token=GHSAT0AAAAAACEJ43AXOKF4M2UJC7EADRCQZFLJ7HA)





