import discord
import logging
import sys
import asyncio

logging.basicConfig(level=logging.INFO) #basic logging

client = discord.Client()

#we dont want you (github) to see the credentials
#so its in a seperate file with the mail in the first and pw in the second line
creds = open(__file__ + '/../' + 'credentials.txt','r').read() #get creds from file
creds = creds.split("\n") #remove \n from pw

def main_task(): #login and connect
    yield from client.login(creds[0], creds[1])
    yield from client.connect()

@client.async_event
async def on_message(message):
    parts = message.content.split()
    cmd = parts[0]
    if len(parts) >= 2:
        param1 = parts[1]
    if len(parts) >= 3:    
        param2 = parts[2]
    if message.content.startswith('!schwehn-exit'):
        print('Exiting')
        sys.exit()
    if message.content.startswith('!listchannels'):
        channels = message.server.channels
        output = ""
        for c in channels:
            output = output + c.name + ": " + c.type + "\n"
        client.send_message(message.channel, output)
    if message.content.startswith('!sjt'):
        await joinVoiceChannel(message.server, param1)

async def joinVoiceChannel(server, channelName):
    joinChannel = getChannelByName(server, channelName)

    discord.opus.load_opus('opus.dll')

    await client.join_voice_channel(joinChannel)

def getChannelByName(server, name):
    channels = server.channels
    for c in channels:
        if c.name == name:
            return c
    return -1

@client.async_event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

loop = asyncio.get_event_loop()
loop.run_until_complete(main_task())
loop.close()
