import asyncio
from pyrogram import Client, filters
import requests

API_URL = "https://chatgpt.apinepdev.workers.dev/?question="

async def get_response(question):
    url = API_URL + question.replace(" ", "%20")
    response = requests.get(url)
    data = response.json()
    if 'answer' in data:
        return data['answer']
    else:
        return "Error aanu myre."

API_ID = "28317577"
API_HASH = "05ce3999245099cf810c22553f928b0a"
BOT_TOKEN = "7244351715:AAGnfhyo-XDVoYPOFXdWkjk_syARNAmiGvU"

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply("Hello! jeevan undu malare.")

@app.on_message(filters.text & ~filters.command([]))
async def reply_handler(client, message):
    user_message = message.text
    response = await get_response(user_message)
    await message.reply(response)
    
app.run()
