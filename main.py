# This example requires the 'message_content' intent.

import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.environ.get("discordToken")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# client = MyClient(intents=intents)
# client.run(token)

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(token)
