import discord
import os
from dotenv import load_dotenv
import asyncio
import random
import datetime

from roomId import textChannel, voiceChannel
import words

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
        # botが書き込むチャンネル
        botRoom = client.get_channel(textChannel["attend-list"])
        # 監視対象のボイスチャンネル
        announceChannelIds = [voiceChannel["virtual-216"]]

        if after.channel is not None and after.channel.id in announceChannelIds:
            join_mes = random.choice(words.F_words) + random.choice(words.L_words)
            await botRoom.send("ようこそ! " + join_mes + " " + member.display_name)
            view = discord.ui.View()
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.danger,
                                            custom_id="free",
                                            label="暇！お話したい！"))
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.primary,
                                            custom_id="question",
                                            label="質問したい！"))
            view.add_item(discord.ui.Button(style=discord.ButtonStyle.secondary,
                                            custom_id="notnotifier",
                                            label="通知しない"))
            await botRoom.send(f"{member.display_name}さんこんにちは！\n何をしていますか？？？？\n（無視しても120秒で消えます）", view=view)


@client.event
async def on_message(message):
    if not message.author.bot:
        return

    if "何をしていますか？？？？" in message.content:
        await asyncio.sleep(120)
        await message.delete()


@client.event
async def on_interaction(interaction):
    utc_hour = datetime.datetime.now().hour
    # 9時間の時差(UTCでは00:00~06:00)
    mention_word = "@everyone" if 15 < utc_hour < 21 else ""
    if interaction.data['custom_id'] == 'free':
        await interaction.channel.send(f'{mention_word} \n{interaction.user.display_name}は暇しています！\nお話してあげましょう！')
    elif interaction.data['custom_id'] == 'question':
        await interaction.channel.send(f'{mention_word} \n{interaction.user.display_name}は質問があるようです！！！')
    interaction.data['custom_id'] = ""
    await interaction.delete_original_message()

load_dotenv()
client.run(os.getenv('BOT_TOKEN'))
