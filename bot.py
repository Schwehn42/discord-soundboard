import discord
from discord.voice_client import *
import logging
import asyncio

#discordAPI
logging.basicConfig(level=logging.INFO)
client = discord.Client()
creds = open(__file__ + '/../' + 'credentials.txt','r').read() #get creds from file
creds = creds.split("\n") #remove \n from pw
client.login(creds[0], creds[1])

#loadOpus
discord.opus.load_opus('opus.dll')

@client.async_event
async def on_message(message):
    if message.content.startswith('!join'):
        await join_voice_cmd(message, message.content.split()[1])
    if message.content.startswith('!playsound'):
        await playsound()

async def join_voice_cmd(message, channel_name):
        server = message.server
        voice_channels = filter(lambda c: c.type is discord.enums.ChannelType.voice, server.channels)
        if channel_name is not None:
            voice_channel = discord.utils.find(lambda c: c.name == channel_name, voice_channels)
        else:
            voice_channel = next(voice_channels)
        if not voice_channel:
            await client.send_message(message.channel, 'Dieser Channel existiert nicht!')
            return

        voice = await client.join_voice_channel(voice_channel)

async def playsound():
        player = client.voice.create_ffmpeg_player('test.mp3')
        player.start()

@client.async_event
def on_ready():

    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(creds[0], creds[1])
