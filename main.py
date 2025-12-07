# This example requires the 'message_content' intent.

import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.environ.get("discordToken")

# class MyClient(discord.Client):
#     async def on_ready(self):
#         print(f'Logged on as {self.user}!')
#
#     async def on_message(self, message):
#         print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# client = MyClient(intents=intents)
# client.run(token)

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

# This example requires the 'message_content' intent.

import os
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.environ.get("discordToken")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

def get_random_word():
    """Reads and parses a random word from the wordlist file."""
    with open('wordlist.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        if not lines:
            raise ValueError("The word list is empty.")

        random_line = random.choice(lines).strip()
        parts = random_line.split(';', 2)

        if len(parts) < 3:
            raise ValueError("A line in the word list has an incorrect format.")

        return parts[0].strip(), parts[1].strip(), parts[2].strip()

@bot.command()
async def word(ctx):
    try:
        word, word_type, description = get_random_word()

        embed = discord.Embed(
            title=f"**{word.capitalize()}**",
            description=f"*{word_type}*",
            color=discord.Color.blue()
        )
        embed.add_field(name="Meaning", value=description, inline=False)
        await ctx.send(embed=embed)

    except FileNotFoundError:
        await ctx.send("`wordlist.txt` not found. Please create it in the format `word,type,description`.")
    except ValueError as e:
        await ctx.send(str(e))
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(token)
