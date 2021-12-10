import discord
import os
from dotenv import load_dotenv

from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle

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
            buttons = [
            create_button(
                style=ButtonStyle.green,
                label="A Green Button"
                custom_id="push_message_button"
            ),
          ]

        action_row = create_actionrow(*push_message_button)
        await ctx.send("My Message", components=[action_row])

load_dotenv()
client.run(os.getenv('BOT_TOKEN'))
