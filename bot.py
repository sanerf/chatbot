import asyncio
from pyrogram import Client, filters
import openai

# OpenAI API key
OPENAI_API_KEY = "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"

# Initialize the OpenAI API client
openai.api_key = OPENAI_API_KEY

# Function to get response from the OpenAI API
async def get_response(question):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

# Telegram bot token
API_ID = "28317577"
API_HASH = "05ce3999245099cf810c22553f928b0a"
BOT_TOKEN = "7244351715:AAGnfhyo-XDVoYPOFXdWkjk_syARNAmiGvU"

# Create a new Pyrogram client
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Handler for the /start command
@app.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply("Hello! I'm an OpenAI-powered bot. Ask me anything, and I'll do my best to respond.")

# Handler for user messages
@app.on_message(filters.text & ~filters.command([]))
async def reply_handler(client, message):
    user_message = message.text
    response = await get_response(user_message)
    await message.reply(response)

# Run the bot
app.run()
