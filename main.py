from flask import Flask,render_template,jsonify,request
from flask_pymongo import PyMongo
import os
import openai

openai.api_key = "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"




app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://Gautam:hello%40123@cluster0.xnyto9h.mongodb.net/chatGPT"
mongo = PyMongo(app)




@app.route("/")
def home():
    chats = mongo.db.chats.find({})
    myChats = [chat for chat in chats]
    print(myChats)
    return render_template("index.html",myChats=myChats)

@app.route("/api",methods=("GET","POST"))
def qa():
    if request.method == "POST":
        print(request.json)
        question = request.json.get("question")
        chat = mongo.db.chats.find_one({"question":question})
        print(chat)
        if chat:
            data = {"question":question,"answer":f"{chat['answer']}"}
            return jsonify(data)
        else:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                # prompt=question,
                messages=[
                    {
                    "role": "user",
                    "content": question
                    }
                ],
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            print(response)
            data = {"question":question,"answer":response["choices"][0]["message"]["content"]}
            mongo.db.chats.insert_one({"question":question,"answer":response["choices"][0]["message"]["content"]})
            return jsonify(data)
    data = {"result":"Hello I am Gautam"}
    return jsonify(data)

app.run(debug=True)