# Gemini4U

**Gemini4U** is a simple, local-first Python assistant powered by Google's Gemini 1.5 API (REST). It lets you interact with Gemini in a conversational CLI interface and is built for easy experimentation, learning, and extension.

---

## 🚀 Features

- 🔌 Uses Gemini 1.5 Flash (REST API, not SDK)
- 🔐 API key stored in `.env` file (never exposed)
- 💬 Simple terminal-based chat interface
- ✅ Markdown-based setup instructions
- 🧠 Modular design (ready for memory, voice, GUI add-ons)

---

## 📦 Requirements

- Python 3.10+
- Dependencies listed in `requirements.txt`

---

## 🛠 Setup & Usage

```bash
# Clone the repo
git clone https://github.com/jcash61/gemini4u.git
cd gemini4u

# Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\activate  # or use the appropriate command for your shell

# Install dependencies
pip install -r requirements.txt

# Add your API key to a .env file
GEMINI_API_KEY=your-api-key-here

# Run the assistant
python main.py
```

---

## 📁 Project Structure

```
├── assistant.py         # Gemini REST wrapper
├── main.py              # CLI chat interface
├── .env                 # Your API key (not committed)
├── .gitignore
├── requirements.txt
├── getting_started.md   # Markdown setup walkthrough
└── README.md            # You are here
```

---

## 📌 TODO / Next Steps

- [ ] Add memory system (`memory.json` or SQLite)
- [ ] Voice input/output (SpeechRecognition + pyttsx3)
- [ ] Tkinter or web-based GUI
- [ ] Better error handling & retry logic

---

## 🧠 Credits

Created by **Jeff Cash** under the BorgzWorks initiative. ✊

Feel free to fork, contribute, and customize your own AI assistant!

---

## ⚠️ Disclaimer
This tool is for educational and personal use only. Protect your API key and use responsibly.

