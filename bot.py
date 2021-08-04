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
    print('------')

@bot.command(name="info")
async def info(ctx):
    await ctx.send("This bot was programmed by CactiStaccingCrane ~~using a ton of code from stackoverflow and dannydorito~~")

@bot.command(name="earth")
async def earth(ctx):
    await ctx.send("The earth is a geode, with a spheroid approximation.")

@bot.command(name="brassmonkey")
async def brassmonkey(ctx):
    await ctx.send(":brassmonkey:")

@bot.command(name="meme")
async def meme(ctx):
    await ctx.send("@CactiStaccingCrane#5920 Go implement this feature you lazy piece of shit")

@bot.command(name="list")
async def list(ctx):
    await ctx.send(file=discord.File(r'/content/meme.json')) # being lazy

@bot.command(name="delete")
async def list(ctx, name):
    await ctx.send("@CactiStaccingCrane#5920 Go implement this feature you lazy piece of shit")

@bot.command(name="save")
async def save(ctx, name, url):
    data = {"name": name, "url": url}
    write_json(data)
    await ctx.send(name + " has been written to the list, its link is " + url)

@bot.command(name="github")
async def list(ctx):
    await ctx.send("https:#github.com/DannyDorito24/MemesBot")
    
bot.run(TOKEN) # reeeeeeeee


# time to increase the line number :admiraaaaaaaaaaaa:


#               ..,,:::;;iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii;::1ffLLLLLLLLLLL
#              ..,,::;iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii;::::iiiiiiii;ii11ttttttttt
#           .,,,:;;;;iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii:. ,:;iiiiiiiiiiiii;;;;;;;;;;
#         .,..,:;iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii:. ,t1iiiiiiiiiiiiiiiiiiiiiiiii
#            :iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii;,  ;C00L1iiiiiiiiiiiiiiiiiiiiiii
#           :iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii;,  :tG0000Gfiiiiiiiiiiiiiiiiiiiiii
# ::::::,,..;iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii:. ,tG00000000Liiiiiiiiiiiiiiiiiiiii
# ;;;;iiii::iiiiiiiiiiiiiiiiiiiii;iiiiiiiiii;.  ;C00000000000C1iiiiiiiiiiiiiiiiiii
# 11i;::;i;;iiiiiiiiiiiiiiii;;;iiii;iiiiii;,  :f0Ct11fC0000000G1;iiiiiiii;;;;i:;ii
# 11111i;:;iiiiiiiiiiiiiiiiiiiiiiii:;iii;,  ,tG00i,. .,iL000000L,:iii;;;;itLCf:ii;
# 1111111i:;iiiiiiiiiiiiiiiiiiii;;iii;:,..,:t0000t,    .:L0000C;,,;;;ifCG88@@L:;;:
# 11111111i;iiiiiiiiiiiiiiiiiiiiiii;;;:::;ii;f000Gt:.. .:f000L;,::;tG8@@@@88Gt:;;i
# 11111111i;iiiiiiiiiiiiiiiiiiiiiii,.:,::;;ii;f0000Cft1tLG0Gf::,,iC8@@8@80CC0C;iii
# 11111111;;iiiiiiiiiiiiiiiiiiii;,.  :;;:;:;ii;1C00000000GLi::,iC8@88@80CG8@@81;;i
# 1111iii;;iiiiiiiiiiiiiiiiiii;,  ..:iiii;:;iii;itCGGGCLti;:::f8@888@8CC8@@@@@8L1i
# 1111;;;;;;;;iiiiiiiiiiiiii;.  .iLCt;;ii;;iiiiii;;i;:::,:::;L8@888@0L0@@@@@@@@8Gf
# 1111111i;;:;iiiiiiiiiiii;,  .1C0000Gt;;iiiiiiiiiii;:;;;;;;G@8888@GC8@@@@@@@8GG08
# 111111i;;;;:iiiiiiiiiii:.  :LGLLLCG00C1;;iiiiiiiiiiiiii;iG@888@@CC@@@@@@@0CG8@@@
# i1111111111;;iiiiiiiii:  .1GL;,..,iL000Li;iiiiiiiiiiii;i0@888@@0C@@@@@@8CC8@@@@@
# .,;i11111111;;iiiiiii:  ;L001,    .:f000Gi:iiiiiiiii;;;C@8888@@@@@@@@8GC8@@@@@@@
#    .,:;iiiii;:;iiiii:  iGG00L:.    .;G000L,;iiii;::::::C8@@8@@@@@@@@0C0@@@@@@@@@
#         ..... .:iiii: .tGGG00L1;,..,iGGGGf.:;iii;,..,. .:f88@@@@@@@CC8@@@@@@@@@@
#                 :iii;.:;tGGGG00GCLffCGGGL:,:iiii;..f0i    L@@@@@@@@8@@@@@88@@@@@
#                  ,:ii;ii;1LGGGGG00GGGGGf;::;ii;;, ;8t.    f@@@@@@@@@@@@@@@8@@@@@
#                    ,;iiiii;1LGGGGGGGGLi,:;:;i1tfi .:      C@@@@@@@@@8GLC8@@@@@@@
#                     .:iiiii;i1fLCCCCt:,:;;:1C08@0i:::::;;i0@@@@@@@0LiiG@@@@@@@@@
#                       ,;iiiiii;iii;:,:;;;;t8@@8@@@88888@@@@@8088G1::f8@@@@@@@@@@
#                        .:iiiiiiii;;;;iii;f8@@@@@@@@@@@@@@@@@@8Gi,,t08G0@@@@@@@@@
#                          ,;iiiiiiiiiiii;i8@80GG@@@@@@@@@@@@@@8t:1G80G88888@@@@@@
#                           .:iiiiiiiiiii;180CC0@@@@@@@@@@@@@@@CL08008@@888@@@@@@@
#                             :iiiiiiiiii;;CG88@@@@@8GG0@@@@@@@@@@@@@888@@@@@@@@@@
#                             ,iiiiiiii;:::0@@8@@8GGG0@@@@@@888@@@@@@@@@@@@@@@@@@@
