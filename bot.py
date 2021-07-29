import discord
from discord.ext import commands
import json

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

bot = commands.Bot(command_prefix=',', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def info(ctx):
    await ctx.send("This bot was programmed by DannyDorito ~~using a ton of code from stackoverflow~~ \n \n The commands that can be used are: \n ``!save <name> <url>`` to save a file \n ``!meme <name>`` to recall an image \n ``!list`` to list all memes in the database")

@bot.command()
async def earth(ctx):
    await ctx.send("The earth is round.")

@bot.command()
async def brassmonkey(ctx):
    await ctx.send("<:brassmonkey:869426385062617158>")

@bot.command()
async def meme(ctx):
    await ctx.send("<@381608421906186240> Go implement this feature you lazy piece of shit")

@bot.command()
async def list(ctx):
    await ctx.send("<@381608421906186240> Go implement this feature you lazy piece of shit")

@bot.command()
async def save(ctx, name: str, url: str):
    table = {"name":name, "url":url}
    jsonString = json.dumps(aList)
    jsonFile = open("urls.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()
    await ctx.send("``"name"``" + " has been written to the list")

bot.run('token') # reeeeeeeee
