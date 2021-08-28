import discord
from discord.ext import commands
import json

with open("secrets.json", "r") as f:
    secrets = json.load(f)


# the bot!
bot = commands.Bot(
    command_prefix="_"
)


@bot.event
async def on_ready():
    bot.load_extension("main_cog")


@bot.command()
async def hello_name(context, name):
    await context.send(f"Hello, {name}!")


@bot.command()
async def test(context, name, clss):
    await context.send(f"Hello, {name} from {clss}!")


@bot.command()
async def multiarg(context, *, name):
    await context.send(f"Hello, {name}!")


@hello_name.error
async def anything(context, error):
    await context.send("Please enter a name!")


@bot.event
async def on_command_error(context, error):
    await context.send(error)


# run bot using bot token!
bot.run(secrets["TOKEN"])
