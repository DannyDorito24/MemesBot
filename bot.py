import discord
from discord.ext import commands
import json

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

bot = commands.Bot(command_prefix=',')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command(name="info")
async def info(ctx):
    await ctx.send("This bot was programmed by CactiStaccingCrane ~~using a ton of code from stackoverflow and dannydorito~~")

@bot.command(name="earth")
async def earth(ctx):
    await ctx.send("The earth is a geode, with a spheroid approximation.")

@bot.command(name="brassmonkey")
async def brassmonkey(ctx):
    await ctx.send("<:brassmonkey:869426385062617158>")

@bot.command(name="meme")
async def meme(ctx):
    await ctx.send("<@840036645750702100> Go implement this feature you lazy piece of shit")

@bot.command(name="list")
async def list(ctx):
    await ctx.send("<@840036645750702100> Go implement this feature you lazy piece of shit")

@bot.command(name="save")
async def save(ctx, name: str, url: str):
    table = {"name":name, "url":url}
    jsonString = json.dumps(aList)
    jsonFile = open("urls.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()
    await ctx.send(name + " has been written to the list")

@bot.command(name="github")
async def list(ctx):
    await ctx.send("https://github.com/DannyDorito24/MemesBot")

bot.run(TOKEN) # reeeeeeeee
