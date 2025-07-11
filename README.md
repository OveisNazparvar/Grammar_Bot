# 🎙️ Telegram Grammar Feedback Bot (Voice + Text)

This is a free and open-source **Telegram bot** that automatically:
- Converts **voice messages** to English text using **Whisper AI**
- Sends the extracted text to **OpenRouter (Cypher Model)** for **grammar correction**
- Replies with suggestions, grammar fixes, and improved collocations
- Fully runs on **Railway** for free — no credit card required  
- Works **inside groups** or in private chat

---

## 🧠 Features

✅ Voice message to text (English)  
✅ Grammar and style feedback using OpenRouter  
✅ Replies with corrected version and collocation suggestions  
✅ Clean codebase (no Flask, no polling threads)  
✅ Can be hosted for free with ffmpeg support  
✅ No manual pinging needed

---

## 🚄 Deployment (Free on Railway)

> 📌 You don't need a credit card. Follow these steps:

- Go to https://railway.app
- Sign up and log in (no credit card required)
- Click on New Project → Deploy from GitHub Repo
- Select your forked repo
- Set the environment variables:
  - TELEGRAM_BOT_TOKEN
  - OPENROUTER_API_KEY
- Railway will automatically detect and build your bot

✅ Once deployed, your bot starts running automatically and handles messages in real-time!



### 📦 Fork This Repository

Click the "Fork" button on the top right, or clone this repo:
```bash
git clone https://github.com/YOUR_USERNAME/telegram-grammar-bot.git
‍‍‍```


---

## 🤖 Usage

- Add the bot to a **Telegram group**
- Send a **voice message**
- The bot will:
  - Transcribe the audio using Whisper
  - Provide grammar feedback
  - Suggest better collocations
  - Reply under the original voice message

You can also ask anything from AI by sending plain **text messages**.

---

## 🛠 Tech Stack

| Tool / Library       | Purpose                                   |
|----------------------|-------------------------------------------|
| `python-telegram-bot`| Handling Telegram Bot interactions        |
| `faster-whisper`     | Fast and accurate voice-to-text           |
| `OpenRouter API`     | AI-powered grammar correction             |
| `Railway`            | Free cloud deployment & hosting           |
| `ffmpeg`             | Audio conversion (.ogg → .wav)            |

---

## 🙌 Credits

- [Whisper AI by OpenAI](https://github.com/openai/whisper)  
- [OpenRouter](https://openrouter.ai) – Free AI models  
- [Railway](https://railway.app) – Free and easy deployment  
- Inspired by language learners and educators worldwide 🌍

---

## 📬 Contact

Have a suggestion, found a bug, or want to contribute?

- 📧 Email: oveis.nazparvar@example.com    
- 💬 Open an issue or PR anytime

Let’s make grammar correction easier for everyone — one message at a time!

---

**License**: [MIT](LICENSE)
