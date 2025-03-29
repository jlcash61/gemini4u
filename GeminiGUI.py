import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk
from assistant import GeminiAssistant
import pyttsx3
import speech_recognition as sr
import threading

class GeminiGUI:
    def __init__(self, root):
        self.assistant = GeminiAssistant()
        self.tts = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        self.voices = self.tts.getProperty("voices")
        self.current_voice = tk.StringVar()
        self.current_voice.set(self.voices[0].name)
        self.tts.setProperty("voice", self.voices[0].id)

        root.title("Gemini4U Assistant")
        root.geometry("600x540")

        self.chat_log = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', font=("Consolas", 11))
        self.chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.input_frame = tk.Frame(root)
        self.input_frame.pack(fill=tk.X, padx=10, pady=5)

        self.user_input = tk.Entry(self.input_frame, font=("Consolas", 11))
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        self.user_input.bind("<Return>", self.send_message)

        self.send_button = tk.Button(self.input_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT)

        self.listen_button = tk.Button(self.input_frame, text="🎤", command=self.listen_voice)
        self.listen_button.pack(side=tk.RIGHT, padx=(0, 5))

        self.voice_frame = tk.Frame(root)
        self.voice_frame.pack(fill=tk.X, padx=10, pady=(0, 10))

        tk.Label(self.voice_frame, text="Voice:").pack(side=tk.LEFT)
        self.voice_dropdown = ttk.Combobox(self.voice_frame, textvariable=self.current_voice, state="readonly")
        self.voice_dropdown['values'] = [voice.name for voice in self.voices]
        self.voice_dropdown.pack(side=tk.LEFT, padx=5)
        self.voice_dropdown.bind("<<ComboboxSelected>>", self.change_voice)

        self.append_text("Gemini4U Ready. Type or speak a message below.")

    def change_voice(self, event=None):
        selected_name = self.current_voice.get()
        for voice in self.voices:
            if voice.name == selected_name:
                self.tts.setProperty("voice", voice.id)
                break

    def speak(self, text):
        self.tts.say(text)
        self.tts.runAndWait()

    def append_text(self, text, sender="Gemini"):
        self.chat_log.config(state='normal')
        if sender:
            self.chat_log.insert(tk.END, f"{sender}: {text}\n")
        else:
            self.chat_log.insert(tk.END, f"{text}\n")
        self.chat_log.config(state='disabled')
        self.chat_log.see(tk.END)

    def send_message(self, event=None):
        prompt = self.user_input.get().strip()
        if not prompt:
            return

        self.append_text(prompt, sender="You")
        self.user_input.delete(0, tk.END)

        try:
            response = self.assistant.ask(prompt)
            self.append_text(response)
            self.speak(response)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def listen_voice(self):
        threading.Thread(target=self.capture_voice).start()

    def capture_voice(self):
        self.append_text("[Listening...]", sender=None)
        try:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source, timeout=5)
                prompt = self.recognizer.recognize_google(audio)
                self.user_input.delete(0, tk.END)
                self.user_input.insert(0, prompt)
                self.send_message()
        except sr.WaitTimeoutError:
            self.append_text("[No speech detected. Try again.]", sender=None)
        except sr.UnknownValueError:
            self.append_text("[Could not understand audio.]", sender=None)
        except sr.RequestError as e:
            self.append_text(f"[Speech recognition error: {e}]", sender=None)

if __name__ == "__main__":
    root = tk.Tk()
    app = GeminiGUI(root)
    root.mainloop()
