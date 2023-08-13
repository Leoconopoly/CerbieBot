import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from database import add_reminder, get_reminders, add_task, get_tasks

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
bot = commands.Bot(command_prefix="!", intents=intents)

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

# Check if the bot was mentioned
    if bot.user.mentioned_in(message):
    # Respond to the mention
        await message.channel.send("You mentioned me!")

    # Strip the mention from the message content
    content_without_mention = message.content.replace(f"<@!{bot.user.id}>", "").replace(f"<@{bot.user.id}>", "").strip()

    print(f"Content without mention: {content_without_mention}")  # Debug print

    # Process the query based on your existing conditions
    # Greetings
    greetings = ["hello", "hi", "hey"]
    if content_without_mention.lower() in greetings:
        print("Greeting detected")  # Debug print
        await message.channel.send("WOOF! Hi there!")

    # Bot's Status
    elif content_without_mention.lower() == "how are you?":
        print("Status query detected")  # Debug print
        await message.channel.send("I'm just a cute doggo bot, but I'm functioning optimally!")

    # Bot's Purpose
    elif content_without_mention.lower() == "what can you do?":
        print("Purpose query detected")  # Debug print
        await message.channel.send("I'm still learning, but I can greet you and answer some basic questions!")



    # Allow the bot to process commands
    await bot.process_commands(message)

# Run the bot
bot.run(DISCORD_TOKEN)