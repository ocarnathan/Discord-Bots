import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Get the bot token from the environment
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# Define the intents your bot will use
intents = discord.Intents.default()
intents.message_content = True  # Allow the bot to read message content

# Define the bot and set the command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Event: Called when the bot is ready to start
@bot.event
async def on_ready():
    print(f'{bot.user} is now running!')

# Command: Respond to the !hello command
@bot.command()
async def hello(ctx):
    # Get the author's name from the context
    user_name = ctx.author.name
    # Send a personalized response
    await ctx.send(f'Hello, {user_name}! How can I assist you today?')

# Run the bot
bot.run(TOKEN)