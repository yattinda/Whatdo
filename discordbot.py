import discord
import os
from dotenv import load_dotenv
from discord_buttons_plugin import *

from roomId import textChannel, voiceChannel

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_voice_state_update(member, before, after):
    if before.channel != after.channel:
        #書き込むテキストチャンネル
        botRoom = client.get_channel(777506677624799245)
        #監視対象のボイスチャンネル
        announceChannelIds = [777506678068477952]

        if after.channel is not None and after.channel.id in announceChannelIds:

load_dotenv()
client.run(os.getenv('BOT_TOKEN'))
