# This example requires the 'message_content' intent.

import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from pathlib import Path
from typing import List, Optional, Tuple

load_dotenv()
token = os.environ.get("discordToken")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

_WORDLIST_PATH = Path(__file__).with_name('wordlist.txt')
_word_lines: Optional[List[str]] = None
_word_index = 0


def _load_word_lines() -> List[str]:
    global _word_lines, _word_index

    if _word_lines is not None:
        return _word_lines

    with _WORDLIST_PATH.open('r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    if not lines:
        raise ValueError("The word list is empty.")

    _word_lines = lines
    _word_index = 0
    return _word_lines

def get_word_of_the_day() -> Tuple[str, str, str]:
    """Reads and parses a word from the wordlist file.

    Loads all words once, then returns the next line each call.
    When it reaches the end, it starts again from the top.
    """
    global _word_index

    lines = _load_word_lines()
    if _word_index >= len(lines):
        _word_index = 0

    daily_line = lines[_word_index]
    _word_index += 1

    parts = daily_line.split(';', 2)
    if len(parts) < 3:
        raise ValueError("A line in the word list has an incorrect format. Expected: word;type;description")

    return parts[0].strip(), parts[1].strip(), parts[2].strip()


@bot.command()
async def word(ctx):
    try:
        word, word_type, description = get_word_of_the_day()
        print(f"Selected word: {word}, Type: {word_type}, Description: {description}")
        embed = discord.Embed(
            title=f"**{word.capitalize()}**",
            description=f"*{word_type}*",
            color=discord.Color.blue()
        )
        embed.add_field(name="Meaning", value=description, inline=False)
        await ctx.send(embed=embed)

    except FileNotFoundError:
        await ctx.send("`wordlist.txt` not found. Please create it in the format `word;type;description`." )
    except ValueError as e:
        await ctx.send(str(e))
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")


bot.run(token)
