
from discord.ext import commands
import socket as s
from dotenv import load_dotenv
import os


server = 'irc.chat.twitch.tv'
port = 6667
nickname = '3jbot'

channel = '#3jrock'

load_dotenv()

twitchToken = os.getenv('twitchToken')
botToken = os.getenv('botToken')




sock = s.socket()
sock.connect((server,port))

sock.send(f"PASS {twitchToken}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))

#here i was messing with the syntax
# while True:#for continuous chat update
#     resp = sock.recv(2048).decode('utf-8')
#     print(resp)

client = commands.Bot(command_prefix=">")
@client.event
async def on_ready():#on startup of bot,tells me it is running
    print('Bot is good g')


@client.command()
async def hi(ctx):
    await ctx.send('hia')



toggle = True
@client.command()
async def chatOn(ctx):# >chatOn
    while toggle:
        resp = sock.recv(2048).decode('utf8')
        #edits texts to make it nicer
        if '#' in resp:
            start = resp.find('#')
            start +=1
            await ctx.send(f' :purple_square: {resp[start:-1]}')


client.run(botToken)