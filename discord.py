import discord
import token

client = discord.Client()

@client.event
async def on_ready():
    print("on_ready")
    print(discord.__version__)

client.run(bot_token)
