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
client.login(creds[0], creds[1])
@client.event
def on_message(message):
    if message.content.startswith('!schwehn-exit'):
        print('Exiting')
        sys.exit()
    if message.content.startswith('!listchannels'):
        channels = message.server.channels
        output = ""
        for c in channels:
            output = output + c.name + ": " + c.type + "\n"
        client.send_message(message.channel, output)
    if message.content.startswith('!schwehn-join-test'):
        loop = asyncio.get_event_loop()
        # Blocking call which returns when the hello_world() coroutine is done
        loop.run_until_complete(joinVoiceChannel(message.server))
        loop.close()


async def joinVoiceChannel(server):
    joinChannel = getChannelByName(server, "Kacken")
    print (joinChannel.name)
    client.join_voice_channel(joinChannel)

def getChannelByName(server, name):
    channels = server.channels
    for c in channels:
        if c.name == name:
            return c
    return -1

@client.event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run()
