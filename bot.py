import asyncio
from pyrogram import Client, filters
import requests

# API endpoint
API_URL = "https://chatgpt.apinepdev.workers.dev/?question="

# Function to get response from the API
async def get_response(question):
    url = API_URL + question.replace(" ", "%20")
    response = requests.get(url)
    data = response.json()
    print(data)
    # Check if the response has a 'result' key
    if 'result' in data:
        return data['result']
    else:
        return "Sorry, I couldn't understand the API response."

# Telegram bot token
API_ID = "28317577"
API_HASH = "05ce3999245099cf810c22553f928b0a"
BOT_TOKEN = "7244351715:AAGnfhyo-XDVoYPOFXdWkjk_syARNAmiGvU"

# Create a new Pyrogram client
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Handler for the /start command
@app.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply("Hello! I'm a ChatGPT bot. Ask me anything, and I'll do my best to respond.")

# Handler for user messages
@app.on_message(filters.text & ~filters.command([]))
async def reply_handler(client, message):
    user_message = message.text
    response = await get_response(user_message)
    await message.reply(response)

# Run the bot
app.run()
