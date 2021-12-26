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
        #botが書き込むチャンネル
        botRoom = client.get_channel(777506677624799245)
        #監視対象のボイスチャンネル
        announceChannelIds = [777506678068477952]

        if after.channel is not None and after.channel.id in announceChannelIds:
            view = discord.ui.View()
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.danger, custom_id="free", label="暇！"))
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.primary, custom_id="question", label="質問したい！"))
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary, custom_id="notnotifier", label="通知しない"))
            await botRoom.send("これはボタンです。", view=view)

@client.event
async def on_interaction(interaction):
    await interaction.channel.send("Interactionが発生しました。")
    await interaction.channel.send("id:{}\ntype:{}".format(interaction.id, interaction.type))

load_dotenv()
client.run(os.getenv('BOT_TOKEN'))
