import random
import json
import pickle
import numpy as np
import nltk
import tkinter as tk
from tkinter import Scrollbar, Text

from nltk.stem import WordNetLemmatizer
from keras.models import load_model

lemmatizer = WordNetLemmatizer()
intents = json.loads(open("intents.json").read())

words = pickle.load(open("words.pkl", "rb"))
classes = pickle.load(open("classes.pkl", "rb"))

model = load_model("chatbot_model.h5")

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):    
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]

    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    list_of_intents = intents_json["intents"]
    tag = intents_list[0]["intent"]
    for i in list_of_intents:
        if i["tag"] == tag:
            result = random.choice(i["responses"])
            break
    return result

def send():
    message = entry_box.get("1.0", "end-1c").strip()
    entry_box.delete("0.0", tk.END)

    if message:
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, "You: " + message + '\n\n')
        chat_window.config(foreground="#442265", font=("Verdana", 12))

        ints = predict_class(message)
        res = get_response(ints, intents)

        chat_window.insert(tk.END, "Bot: " + res + '\n\n')
        chat_window.config(state=tk.DISABLED)
        chat_window.yview(tk.END)

# Create GUI
root = tk.Tk()
root.title("Chatbot")
root.geometry("400x500")
root.resizable(width=False, height=False)

# Chat window
chat_window = Text(root, bd=1, bg="white", height="8", width="50", font="Arial", wrap="word")
chat_window.config(state=tk.DISABLED)

# Scrollbar
scrollbar = Scrollbar(root, command=chat_window.yview, cursor="heart")
chat_window['yscrollcommand'] = scrollbar.set

# Entry box
entry_box = Text(root, bd=0, bg="white", width="29", height="5", font="Arial")

# Send button
send_button = tk.Button(root, text="Send", width="12", height=5, bd=0, bg="#32de97", activebackground="#3c9d9b", fg="#ffffff", font=("Arial", 12), command=send)

# Place components on screen
scrollbar.place(x=376, y=6, height=386)
chat_window.place(x=6, y=6, height=386, width=370)
entry_box.place(x=6, y=401, height=90, width=265)
send_button.place(x=275, y=401, height=90)

root.mainloop()
