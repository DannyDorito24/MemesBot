import discord
from discord.ext import commands
import json

def write_json(new_data, filename='meme.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data[meme].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

bot = commands.Bot(command_prefix=',')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('---------------------------------------------------')

@bot.command(name="info")
async def info(ctx):
    await ctx.send("This bot was programmed by CactiStaccingCrane with contributions from DannyDorito.")

@bot.command(name="earth")
async def earth(ctx):
    await ctx.send("The earth is a geode, with a spheroid approximation.")

@bot.command(name="brassmonkey")
async def brassmonkey(ctx):
    await ctx.send("<:brassmonkey:869426385062617158>")

@bot.command(name="meme")
async def meme(ctx):
    await ctx.send("<@!840036645750702100> Go implement this feature you lazy piece of shit")

@bot.command(name="list")
async def list(ctx):
    await ctx.send(file=discord.File(r'/content/meme.json')) # being lazy

@bot.command(name="delete")
async def list(ctx, name):
    await ctx.send("<@!840036645750702100> Go implement this feature you lazy piece of shit")

@bot.command(name="save")
async def save(ctx, name, url):
    data = {"name": name, "url": url}
    write_json(data)
    await ctx.send(name + " has been written to the list, its link is " + url)

@bot.command(name="github")
async def list(ctx):
    await ctx.send("https://github.com/DannyDorito24/MemesBot")
    
bot.run(TOKEN) # reeeeeeeee
