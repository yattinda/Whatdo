import discord
import os
from dotenv import load_dotenv

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
        botRoom = client.get_channel(777506677624799245)
        announceChannelIds = [777506678068477952]

        if after.channel is not None and after.channel.id in announceChannelIds:
            await botRoom.send(after.channel.name + "に" + member.name + "が参加！")

load_dotenv()
client.run(os.getenv('BOT_TOKEN'))
