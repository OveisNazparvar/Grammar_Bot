# 🎙️ Telegram Grammar Feedback Bot (Voice + Text)

This is a free and open-source **Telegram bot** that automatically:
- Converts **voice messages** to English text using **Whisper AI**
- Sends the extracted text to **OpenRouter (Cypher Model)** for **grammar correction**
- Replies with suggestions, grammar fixes, and improved collocations
- Fully runs on **Railway** for free — no credit card required  
- Works **inside groups** or in private chat



## 🧠 Features

✅ Voice message to text (English)  
✅ Grammar and style feedback using OpenRouter  
✅ Replies with corrected version and collocation suggestions  
✅ Clean codebase (no Flask, no polling threads)  
✅ Can be hosted for free with ffmpeg support  
✅ No manual pinging needed 

## 💥 How to setup

### 1. Telegram Bot Setup

### 🛠️ Create Your Bot on Telegram

1. Open Telegram and search for [@BotFather](https://t.me/BotFather).
2. Use the command `/newbot` and follow the steps to choose a name and username.
3. After creation, you will receive a **bot token** that looks like:
   - 123456789:ABCDefGhIjKlmNoPQRstuVWXyZ

Save this token. It will be used later as the `TELEGRAM_BOT_TOKEN`.



### ➕ Add Bot to Your Group

1. Open your target Telegram group.
2. Tap on the group name → Manage Group → Administrators → Add Administrator.
3. Search for your bot’s username and add it with **permission to read and write messages**.
4. Send a message like `/start` to activate the bot in the group.


### 2. Fork This GitHub Repository

1. Click the **Fork** button on the top right of this GitHub page.
2. This will create a copy of the project in your GitHub account.
3. You can now make changes and connect it to Railway.



### 3. Get a Free AI API Key

### 🤖 Use OpenRouter (Free AI Provider)

1. Go to [https://openrouter.ai](https://openrouter.ai) and sign up.
2. Visit the [models](https://openrouter.ai/docs#models) page and choose a **free** model like `openai/gpt-3.5-turbo` or `mistralai/mixtral`.
3. Click "API Keys" in your profile and generate a new API key.
4. Save this key as `OPENROUTER_API_KEY` for later.

> Note: Some models may require adding usage credit, but many offer free usage.



### 4. Deploy to Railway

### 🚂 Set Up Your Project

1. Go to [https://railway.app](https://railway.app) and sign up (no credit card needed).
2. Click **New Project → Deploy from GitHub Repo**.
3. Select the repository you forked earlier.
4. Railway will automatically detect and build the project.



### 5. Environment Variables

Before deploying, go to the **Variables** section of your project and add these:

| Variable Name        | Description                            |
|----------------------|----------------------------------------|
| `TELEGRAM_BOT_TOKEN` | Your Telegram bot token                |
| `OPENROUTER_API_KEY` | API key from OpenRouter                |


✅ Once deployed, your bot starts running automatically and handles messages in real-time!

### 6. Final Notes

- 📦 All dependencies are listed in `requirements.txt`.
- 🗂 You can customize the code in `main.py` to:
  - Change OpenRouter AI model
  - Change Whisper model
  - Change AI prompt for better feedback


## 🤖 Usage

- Add the bot to a **Telegram group**
- Send a **voice message**
- The bot will:
  - Transcribe the audio using Whisper
  - Provide grammar feedback
  - Suggest better collocations
  - Reply under the original voice message
- You can also ask anything from AI by sending plain **text messages**.



## 🛠 Tech Stack

| Tool / Library       | Purpose                            | Link          
|----------------------|------------------------------------|---------------------------------
| `python-telegram-bot`| Handling Telegram Bot interactions | [Telegram Bot](https://github.com/python-telegram-bot/python-telegram-bot)  
| `faster-whisper`     | Fast and accurate voice-to-text    | [Whisper AI by OpenAI](https://github.com/openai/whisper)
| `OpenRouter API`     | AI-powered grammar correction      | [OpenRouter](https://openrouter.ai)
| `Railway`            | Free cloud deployment & hosting    | [Railway](https://railway.app)
| `ffmpeg`             | Audio conversion (.ogg → .wav)     | [ffmpeg](https://ffmpeg.org/)


## 📬 Contact

Have a suggestion, found a bug, or want to contribute?

- 📧 Email: oveis.nazparvar@gmail.com    
- 💬 Open an issue or PR anytime

Let’s make grammar correction easier for everyone — one message at a time!

---

**License**: [ GNU GENERAL PUBLIC LICENSE](LICENSE)
