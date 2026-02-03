from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from config import TELEGRAM_TOKEN
from hf_client import ask_llm, ask_short, ask_code, ask_json, summarize


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello! I am your AI-powered bot. Send me a message and I will respond using the LLM!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Send any message and I will reply using the LLM!')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if text.startswith("/short"):
        reply = ask_short(text[6:])
    elif text.startswith("/code"):
        reply = ask_code(text[5:])
    elif text.startswith("/json"):
        reply = ask_json(text[5:])
    elif text.startswith("/summarize"):
        reply = summarize(text[10:])
    else:
        reply = ask_llm(text)

    await update.message.reply_text(reply)

def main() -> None:
    # Use the token loaded from environment via config.py
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == '__main__':
    # print(ask_llm("Explain Python decorators in simple words"))
    main()
   

