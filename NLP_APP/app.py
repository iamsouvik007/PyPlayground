from tkinter import *
from tkinter import messagebox
from my_api import GeminiNLP
from mydb import Database

class NLPApp:
    def __init__(self):
        self.dbo = Database()
        self.nlp = GeminiNLP("AIzaSyAbwus-q1_OJ54Kj1HotbL1l0cJAM1RFPI")  # Use your API Key

        self.root = Tk()
        self.root.title("✨ NLP Toolkit")
        self.root.geometry("420x620")
        self.root.configure(bg="#1E1E2F")
        self.root.resizable(False, False)
        self.root.iconbitmap("resources/python.ico")

        self.font_heading = ("Segoe UI", 20, "bold")
        self.font_label = ("Segoe UI", 12)
        self.font_btn = ("Segoe UI", 10, "bold")

        self.login_gui()
        self.root.mainloop()

    def clear(self):
        for widget in self.root.pack_slaves():
            widget.destroy()

    def styled_label(self, text, size=14, pady=(10, 5), color="white"):
        Label(self.root, text=text, bg="#1E1E2F", fg=color,
              font=("Segoe UI", size), wraplength=350).pack(pady=pady)

    def styled_button(self, text, command, bg="#6A5ACD"):
        Button(self.root, text=text, bg=bg, fg="white", activebackground="#5A4BCF",
               activeforeground="white", font=self.font_btn, relief=FLAT,
               bd=0, width=25, height=2, command=command).pack(pady=10)

    def styled_entry(self):
        entry = Entry(self.root, width=35, font=("Segoe UI", 11), bg="#2D2D3A", fg="white", insertbackground="white",
                      relief=FLAT)
        entry.pack(pady=7, ipady=7)
        return entry

    def perform_registration(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.dbo.add_data(name, email, password)
        if response == 1:
            messagebox.showinfo("✅ Registration", "Thank you for registering!")
        else:
            messagebox.showerror("⚠️ Error", "Email already exists")

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.dbo.search(email, password)
        if response == 1:
            messagebox.showinfo("✅ Login", "Welcome back!")
            self.home_gui()
        else:
            messagebox.showerror("❌ Login Failed", "Incorrect Email or Password")

    def perform_sentiment_analysis(self):
        text = self.sentiment_input.get()
        result = self.nlp.analyze_sentiment(text)
        emoji = {"Positive": "😊", "Negative": "😞", "Neutral": "😐"}
        self.sentiment_result.config(text=f"{result} {emoji.get(result, '')}")

    def perform_ner_analysis(self):
        text = self.ner_input.get()
        result = self.nlp.analyze_ner(text)
        self.ner_result.config(text=result)

    def perform_emotion_analysis(self):
        text = self.emotion_input.get()
        result = self.nlp.analyze_emotion(text)
        self.emotion_result.config(text=result)

    def login_gui(self):
        self.clear()
        self.styled_label("🔐 Welcome to NLP App", size=22, pady=(40, 10))

        self.styled_label("📧 Email", size=12)
        self.email_input = self.styled_entry()

        self.styled_label("🔒 Password", size=12)
        self.password_input = self.styled_entry()
        self.password_input.config(show="*")

        self.styled_button("Login", self.perform_login)
        self.styled_label("Not a member?", size=10, color="#AAAAAA")
        self.styled_button("Register", self.register_gui, bg="#444456")

    def register_gui(self):
        self.clear()
        self.styled_label("📝 Register", size=22, pady=(40, 20))

        self.styled_label("👤 Name")
        self.name_input = self.styled_entry()

        self.styled_label("📧 Email")
        self.email_input = self.styled_entry()

        self.styled_label("🔒 Password")
        self.password_input = self.styled_entry()
        self.password_input.config(show="*")

        self.styled_button("Register", self.perform_registration)
        self.styled_label("Already a member?", size=10, color="#AAAAAA")
        self.styled_button("Login", self.login_gui, bg="#444456")

    def home_gui(self):
        self.clear()
        self.styled_label("🏠 Home", size=22, pady=(40, 20))
        self.styled_button("📊 Sentiment Analysis", self.sentiment_gui)
        self.styled_button("🔍 Named Entity Recognition", self.ner_gui)
        self.styled_button("😊 Emotion Detection", self.emotion_gui)
        self.styled_button("🚪 Logout", self.login_gui, bg="#AA3333")

    def sentiment_gui(self):
        self.clear()
        self.styled_label("📊 Sentiment Analysis", size=18, pady=(30, 10))
        self.styled_label("Enter your text below:")
        self.sentiment_input = self.styled_entry()

        self.styled_button("Analyze Sentiment", self.perform_sentiment_analysis)

        self.sentiment_result = Label(self.root, text="", bg="#1E1E2F", fg="white",
                                      font=("Segoe UI", 12, "bold"), wraplength=350)
        self.sentiment_result.pack(pady=20)

        self.styled_button("🔙 Go Back", self.home_gui, bg="#444456")

    def ner_gui(self):
        self.clear()
        self.styled_label("🔍 Named Entity Recognition", size=18, pady=(30, 10))
        self.styled_label("Enter your text below:")
        self.ner_input = self.styled_entry()

        self.styled_button("Analyze Entities", self.perform_ner_analysis)

        self.ner_result = Label(self.root, text="", bg="#1E1E2F", fg="white",
                                font=("Segoe UI", 12, "bold"), wraplength=350)
        self.ner_result.pack(pady=20)

        self.styled_button("🔙 Go Back", self.home_gui, bg="#444456")

    def emotion_gui(self):
        self.clear()
        self.styled_label("😊 Emotion Detection", size=18, pady=(30, 10))
        self.styled_label("Enter your text below:")
        self.emotion_input = self.styled_entry()

        self.styled_button("Detect Emotion", self.perform_emotion_analysis)

        self.emotion_result = Label(self.root, text="", bg="#1E1E2F", fg="white",
                                    font=("Segoe UI", 12, "bold"), wraplength=350)
        self.emotion_result.pack(pady=20)

        self.styled_button("🔙 Go Back", self.home_gui, bg="#444456")

# Start the app
nlp = NLPApp()
