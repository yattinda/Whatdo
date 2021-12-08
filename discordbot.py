import discord
import os
from dotenv import load_dotenv

client = discord.Client()
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_ready()
    if client.user != message.author:
        m = "おはようございます" + message.author.name + "さん！"
        await message.channel.send(m)

load_dotenv()
client.run(os.getenv('BOT_TOKEN'))
