# This example requires the 'message_content' intent.

import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from datetime import date

load_dotenv()
token = os.environ.get("discordToken")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

def get_word_of_the_day():
    """Reads and parses a word from the wordlist file based on the current date."""
    # Get the current date as a number (ordinal)
    day_number = date.today().toordinal()

    with open('wordlist.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        if not lines:
            raise ValueError("The word list is empty.")

        # Use modulo to get a deterministic index based on the day
        word_index = day_number % len(lines)
        daily_line = lines[word_index].strip()

        parts = daily_line.split(';', 2)

        if len(parts) < 3:
            raise ValueError("A line in the word list has an incorrect format.")

        return parts[0].strip(), parts[1].strip(), parts[2].strip()


@bot.command()
async def word(ctx):
    try:
        word, word_type, description = get_word_of_the_day()

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


bot.run(token)
