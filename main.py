import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from database import add_reminder, get_reminders, add_task, get_tasks
from utils import convert_to_timestamp

# Define the intents of the bot
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

# Load environment variables
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
    # Allow the bot to process commands first
    await bot.process_commands(message)

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
        greetings = ["hello", "hi", "hey"]
        if content_without_mention.lower() in greetings:
            await message.channel.send("WOOF! Hi there!")
        elif content_without_mention.lower() == "how are you?":
            await message.channel.send("I'm just a cute doggo bot, but I'm functioning optimally!")
        elif content_without_mention.lower() == "what can you do?":
            await message.channel.send("I'm still learning, but I can greet you and answer some basic questions!")

@bot.command()
async def remindme(ctx, time: str, *, reminder_content: str):
    # Convert time to a timestamp
    timestamp = convert_to_timestamp(time)
    # Add to Firestore
    add_reminder(str(ctx.author.id), reminder_content, timestamp)
    await ctx.send(f"Reminder set for {time}!")

@bot.command()
async def viewreminders(ctx):
    reminders = get_reminders(str(ctx.author.id))
    for reminder in reminders:
        reminder_data = reminder.to_dict()
        await ctx.send(f"Reminder: {reminder_data['reminder_content']} at {reminder_data['timestamp']}")

@bot.command()
async def addtask(ctx, *, task_content: str):
    add_task(str(ctx.author.id), task_content)
    await ctx.send(f"Task '{task_content}' added!")

@bot.command()
async def viewtasks(ctx):
    tasks = get_tasks(str(ctx.author.id))
    for task in tasks:
        task_data = task.to_dict()
        status = "Completed" if task_data['is_completed'] else "Pending"
        await ctx.send(f"Task: {task_data['task_content']} - Status: {status}")

@bot.event
async def on_command_error(ctx, error):
    print(f"Command error: {error}")

# Run the bot
bot.run(DISCORD_TOKEN)