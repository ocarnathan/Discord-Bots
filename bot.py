import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import openai

# Load the environment variables from the .env file
load_dotenv()

# Set the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

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

# Command: Respond to math and physics questions
@bot.command()
async def ask(ctx, *, question):
    try:
        # Use ChatCompletion for GPT-3.5 or GPT-4
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",   # or "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful assistant that answers math and physics questions."},
                {"role": "user", "content": question}
            ],
            max_tokens=150,
            temperature=0.7,
        )

        # Extract the bot's reply from the response
        answer = response.choices[0].message.content.strip()

        # Send the answer back to Discord
        await ctx.send(answer)
    except Exception as e:
        await ctx.send(f"Sorry, I couldn't process your question: {e}")

# Run the bot
bot.run(TOKEN)