
```markdown
# 💬 SupportBot – AI Chatbot with Tkinter GUI

SupportBot is a simple yet powerful AI chatbot built using **Python**, **Tkinter**, **Natural Language Processing (NLP)** with NLTK, and a **Deep Learning model** trained with TensorFlow/Keras. It features a modern GUI using `ttkthemes`, allowing users to interact naturally with the bot.

---

## 🧠 Features

- 🧾 Trained on custom intents from `intents.json`
- 🧠 NLP processing with **NLTK** and **lemmatization**
- 🤖 Deep learning model built with **Keras**
- 🎨 GUI using **Tkinter**, **ttkthemes**, and **ttk widgets**
- 💬 Real-time chat interface
- 🌙 Dark theme enabled with `equilux`

---

## 🛠️ Tech Stack

| Layer        | Tool / Library              |
|--------------|-----------------------------|
| GUI          | Tkinter + ttk + ttkthemes   |
| NLP          | NLTK (tokenizer, lemmatizer)|
| ML Model     | TensorFlow / Keras          |
| Data Storage | JSON, Pickle                |

---

## 📸 Screenshots

> *(Add screenshots of the chatbot UI here)*  
> You can use tools like `Snipping Tool` or `Lightshot` to take a screenshot and upload to your GitHub repo.

---

## 📂 Project Structure

```
.
├── chatbot_model.h5        # Trained Keras model
├── classes.pkl             # Pickled class labels
├── words.pkl               # Pickled vocabulary
├── intents.json            # Training data (intents and responses)
├── main.py                 # Main app (GUI + logic)
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/supportbot.git
cd supportbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` isn't available, install manually:

```bash
pip install nltk keras tensorflow ttkthemes numpy
```

And download required NLTK resources:

```python
import nltk
nltk.download('punkt')
nltk.download('wordnet')
```

---

### 3. Run the Chatbot

```bash
python main.py
```

The GUI will launch. Type your messages in the input field and interact with the chatbot.

---

## 📚 How It Works

1. **User Input** → Tokenized and Lemmatized
2. **Bag of Words** created from vocabulary
3. **Prediction** using pre-trained neural network (`chatbot_model.h5`)
4. **Intent Match** → Response fetched from `intents.json`
5. **Response Displayed** in the chat window

---

## 🧠 Training the Model (Optional)

If you'd like to retrain the chatbot:

- Update `intents.json` with your own data.
- Run your training script (not included here but should build and save `chatbot_model.h5`, `words.pkl`, and `classes.pkl`).

---

## 🙌 Acknowledgements

- [NLTK](https://www.nltk.org/)
- [Keras](https://keras.io/)
- [Tkinter Themes](https://github.com/RedFantom/ttkthemes)
- [Python](https://www.python.org/)

---

## 📄 License

This project is licensed under the MIT License.  
Feel free to use, modify, and share!

---

## 💡 Future Improvements

- Add voice input using `speech_recognition`
- Store chat history
- Connect to external APIs for dynamic responses
- Add chatbot personality customization

---

## ✨ Author

**Your Name**  
📫 [your.email@example.com](mailto:your.email@example.com)  
🌐 [LinkedIn / GitHub Profile Link]
