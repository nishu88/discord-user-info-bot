import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os

bot = commands.Bot(command_prefix='#')

print (discord.__version__)

@bot.event
async def on_ready():
    print ("Im ready Boy")

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: ping!! xSSS")
    print ("user has pinged")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s Info".format(user.name), description="Member", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Maker", value="Developed by- <@366125961206300673> & 24/7 hosted by <@277695189131460609>")
    await bot.say(embed=embed)
@bot.command(pass_context = True)
async def memberstats(ctx):
    online = 0
    idle = 0
    offline = 0
    dnd = 0
    bots = 0
    server = ctx.message.server
    for member in server.members:
        if str(member.status) == "online":
            online += 1
        elif str(member.status) == "idle":
            idle += 1
        elif str(member.status) == "offline":
            offline += 1
        elif str(member.status) == "dnd":
            dnd += 1
    embed = discord.Embed(name="Members Stats", description="Members Stats list is here", color=0x0000ff)
    embed.set_author(name="Members Stats")
    embed.add_field(name="Online Members", value="Members= "+str(online))
    embed.add_field(name="Idle", value="Members= "+str(idle))
    embed.add_field(name="Dnd", value="Members= "+str(dnd))
    embed.add_field(name="Offline", value="Members= "+str(offline))
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here is your server info", color=0x00ff00)
    embed.set_author(name="Server Info")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    embed.add_field(name="Maker", value="Developed by- <@366125961206300673> & 24/7 hosted by <@277695189131460609>")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Cya, {}. Ya loser!".format(user.name))
 

@bot.command(pass_context=True)
async def hi(ctx):
    await bot.say("hello")

bot.run(os.getenv('TOKEN'))

