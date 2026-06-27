import discord
import os
import google.generativeai as genai
from keep_alive import keep_alive

# Configurar Gemini
genai.configure(api_key=os.environ['GEMINI_API_KEY'])
model = genai.GenerativeModel('gemini-pro')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Conectado como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Si alguien escribe algo, Gemini responde
    response = model.generate_content(message.content)
    await message.channel.send(response.text)

keep_alive()
client.run(os.environ['DISCORD_TOKEN'])