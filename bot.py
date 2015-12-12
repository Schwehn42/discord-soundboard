import discord
import logging

logging.basicConfig(level=logging.INFO) #basic logging

client = discord.Client()

#we dónt want you (github) to see the credentials
#so its in a seperate file with the mail in the first and pw in the second line
creds = open(__file__ + '/../' + 'credentials.txt','r').read() #get creds from file
creds = creds.split("\n") #remove \n from pw
client.login(creds[0], creds[1])

@client.event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run()