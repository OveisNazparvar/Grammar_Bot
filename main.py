import os
import subprocess
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from faster_whisper import WhisperModel
from flask import Flask
from threading import Thread

API_KEY = os.environ.get("OPENROUTER_API_KEY")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

whisper_model = WhisperModel("small.en", compute_type="int8")
app = ApplicationBuilder().token(BOT_TOKEN).build()

def ask_openrouter(prompt: str) -> str:
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openrouter/cypher-alpha:free",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7
        }
    )
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        raise RuntimeError(f"OpenRouter Error: {response.text}")

async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    voice = update.message.voice
    if not voice:
        return

    message_id = update.message.message_id
    ogg_path = f"voice_{message_id}.ogg"
    wav_path = f"voice_{message_id}.wav"

    try:
        file = await context.bot.get_file(voice.file_id)
        await file.download_to_drive(ogg_path)
        subprocess.run(['ffmpeg', '-i', ogg_path, wav_path], check=True)

        segments, _ = whisper_model.transcribe(wav_path)
        text = " ".join(segment.text for segment in segments).strip()

        if not text:
            await update.message.reply_text("❌ Could not extract any text from the audio.")
            return

        await update.message.reply_text(f"📝 Text Extracted:\n{text}")

        feedback_prompt = f"""
Please check the following English text for grammar mistakes.
List all the issues clearly with short explanations and suggestions.
Then provide the corrected version of the full text.
Also suggest collocations for better clarity and style. Put these collocations in brackets in the corrected text.
Separate grammar and suggestions with a clear line.

Text:
{text}
"""
        feedback = ask_openrouter(feedback_prompt)
        await update.message.reply_text(
            f"🧠 Grammar Feedback:\n{feedback}",
            reply_to_message_id=message_id
        )
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")
    finally:
        for path in [ogg_path, wav_path]:
            if os.path.exists(path):
                os.remove(path)

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    message_id = update.message.message_id

    if user_text.lower().startswith("question"):
        return

    try:
        reply = ask_openrouter(user_text)
        await update.message.reply_text(
            reply,
            reply_to_message_id=message_id
        )
    except Exception as e:
        await update.message.reply_text(f"❌ Error from OpenRouter:\n{e}")

app.add_handler(MessageHandler(filters.VOICE, handle_voice))
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_text))

# ========== Flask Keep-Alive ==========
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "✅ Bot is alive!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    flask_app.run(host="0.0.0.0", port=port)

# ========== Start Bot ==========
if __name__ == "__main__":
    print("🤖 Bot is running with OpenRouter (Voice + Text)...")
    Thread(target=run_flask).start()
    app.run_polling()
