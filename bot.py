import discord
from discord.ext import commands
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
async def meme(ctx, name):
    for line in file:
        if name in line:
            del line
        else:
            await ctx.send("I am confused af now, check your spelling")

@bot.command(name="list")
async def list(ctx):
    await ctx.send(file=discord.File(r'/content/meme.csv')) # being lazy

@bot.command(name="delete")
async def list(ctx, name):
    for line in file:
        if name in line:
            await ctx.send(line[2])
        else:
            await ctx.send("I am confused af now, check your spelling")

@bot.command(name="save")
async def save(ctx, name, url):
    data = name + " , " + url
    with open("meme.csv", "a+") as file:
        file.write("\n" + data)
        for line in file:
            if name in line and url in line:
                await ctx.send(name + " and " + url + " has been written to the list")
            else:
                await ctx.send("<@!840036645750702100> Go debug this feature you lazy piece of shit")

@bot.command(name="github")
async def list(ctx):
    await ctx.send("https://github.com/DannyDorito24/MemesBot")
    
bot.run(TOKEN) # reeeeeeeee
