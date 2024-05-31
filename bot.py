import asyncio
from pyrogram import Client, filters
import requests

# Google Gemini API key and endpoint
API_KEY = "AIzaSyANJ3-DgQtabkZn2gWck1UGWItdcsMiyvw"
API_ENDPOINT = "https://generativeai.googleapis.com/v1/models/gemini:generateText"

# Function to get response from the API
async def get_response(question):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    data = {
        "prompt": question,
        "max_output_tokens": 1024,
        "temperature": 0.7
    }

    response = requests.post(API_ENDPOINT, headers=headers, json=data)
    print(response.text)  # Print the response text
    data = response.json()

    # Check if the response has the correct key (e.g., 'text')
    if 'text' in data:
        return data['text']
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
    await message.reply("Hello! I'm a Gemini AI bot. Ask me anything, and I'll do my best to respond.")

# Handler for user messages
@app.on_message(filters.text & ~filters.command([]))
async def reply_handler(client, message):
    user_message = message.text
    response = await get_response(user_message)
    await message.reply(response)

# Run the bot
app.run()
