import discord
import os
from dotenv import load_dotenv

# Define the intents of the bot
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

# Instead of manually opening and reading the file, use load_dotenv 
# assuming the tokens.env file has the format DISCORD_TOKEN=<your_token>
load_dotenv("C:/Users/leoco/Documents/CerbieBot/tokens.env")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
AUTHORIZED_USER_IDS = os.getenv('AUTHORIZED_USER_IDS').split(',')

# Initialize the bot with the specified intents
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    """Event listener for when the bot switches from offline to online."""
    guild_count = len(bot.guilds)
    print(f"CerbieBot is in {guild_count} guilds.")

@bot.event
async def on_message(message):
    """Event listener for when a new message is sent to a channel."""
    if message.author == bot.user:
        return
    if str(message.author.id) not in AUTHORIZED_USER_IDS:
        return

    # Greetings
    greetings = ["hello", "hi", "hey"]
    if message.content.lower() in greetings:
        await message.channel.send("WOOF! Hi there!")

    # Bot's Status
    elif message.content.lower() == "how are you?":
        await message.channel.send("I'm just a cute doggo bot, but I'm functioning optimally!")

    # Bot's Purpose
    elif message.content.lower() == "what can you do?":
        await message.channel.send("I'm still learning, but I can greet you and answer some basic questions!")

# Run the bot
bot.run(DISCORD_TOKEN)