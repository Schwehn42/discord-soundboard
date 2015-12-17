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
        #call that dirty slut of a function
        joinVoiceChannel(message.server, "Kacken")


def joinVoiceChannel(server, channelName):
    '''
    note: this is fucking retarded
    might still output errors
    works tho
    '''
    joinChannel = getChannelByName(server, channelName)
    print (joinChannel.name)
    #voiceClient = client.join_voice_channel(joinChannel)
    loop = asyncio.get_event_loop() #the function that needs to be called is a corountine (gay)
    # TL;DR Magic
    loop.run_until_complete(client.join_voice_channel(joinChannel))
    loop.close()

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
