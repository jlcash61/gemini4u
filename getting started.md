# Gemini4U — Python Gemini Assistant (REST API)

Welcome to your local Gemini assistant project! This guide walks you through manually activating your environment, running the app, and understanding the shell setup.

---

## 🧱 Project Structure

```
📁 gemini4u/
🖋️ .env               → Stores your API key (never commit this!)
🖋️ main.py            → Entry point for the assistant
🖋️ assistant.py       → Handles Gemini API logic via REST
📁 venv/              → Your virtual environment (created locally)
🖋️ getting_started.md → This file
```

---

## 🧪 1. Manual Setup (One-Time)

### ✅ Create Virtual Environment

```bash
python -m venv venv
```

### ✅ Activate the Environment

- **Command Prompt (cmd)**:
  ```bash
  .\venv\Scripts\activate
  ```

- **PowerShell (ps)**:
  ```bash
  .\venv\Scripts\Activate.ps1
  ```

> If PowerShell gives you a script execution error, run:
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 🧪 2. Install Dependencies

Once activated:

```bash
pip install -r requirements.txt
```

*(Or install manually if you prefer: `pip install requests python-dotenv`)*

---

## 🔐 3. Set Up `.env` File

Create a file called `.env` in the project root and paste your Gemini API key:

```env
GEMINI_API_KEY=your-api-key-here
```

> 💡 Keep this secret! Never commit `.env` to version control.

---

## 🚀 4. Run the Assistant

With venv still active:

```bash
python main.py
```

You'll see:

```
🤖 Gemini Assistant (REST API) is ready. Type your message, or 'exit' to quit.
```

Then just start chatting!

---

## 🧠 Good to Know

- **You must activate venv every time** you open a new terminal.
- The `(venv)` at the start of the prompt tells you it's active.
- VS Code won’t activate it by default unless you set it up — so practice doing it manually for now.

---

## 🛠️ What’s Next?

- Add memory to the assistant (`memory.json`)
- Add voice I/O (with `pyttsx3` and `SpeechRecognition`)
- Build a GUI (Tkinter or Web front-end)

