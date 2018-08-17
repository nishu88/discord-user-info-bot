import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os


bot = commands.Bot(command_prefix='#')

print (discord.__version__)

@bot.event
async def on_ready():
    print ("Ready when you are xd")

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: ping!! xSSS")
    print ("user has pinged")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Member", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Makers", value="Developed by- <@366125961206300673> & 24/7 hosted by <@277695189131460609>")
    await bot.say(embed=embed)
    
@bot.command(pass_context=True)
async def botinfo(ctx, user: discord.Member):
    await bot.say("Coded by <@366125961206300673>")
    await bot.say("24/7 hosted by <@277695189131460609>")
    
@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here is your server info", color=0x00ff00)
    embed.set_author(name="Server Info")
    embed.add_field(name="Name", value=":video_game: Trivia Victors :video_game:", inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    embed.add_field(name="Makers", value="Developed by- <@366125961206300673> & 24/7 hosted by <@277695189131460609>")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Cya, {}. Ya loser!".format(user.name))
    
@bot.command(pass_context=True)
async def ban(ctx, user: discord.Member):
    await bot.say(":boot: Get lost , {}. Rip loser!".format(user.name))    

@bot.command(pass_context=True)
async def hi(ctx, user: discord.Member):
    await bot.say("hello".format(user.name))
    
@bot.command(pass_context=True)
async def about(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s Info".format(user.name), description="Member", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Makers", value="Developed by- <@366125961206300673> & 24/7 hosted by <@277695189131460609>")
    await bot.say(embed=embed)

bot.run(os.getenv('TOKEN'))

