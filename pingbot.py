import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

with open("token.txt") as f:
    token = f.readlines()[0]

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        await message.channel.send('Hello! You pinged me?')
    await bot.process_commands(message)

# Replace 'YOUR_BOT_TOKEN' with the token you copied earlier
bot.run('token')
