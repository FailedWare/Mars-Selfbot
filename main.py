import random
import discord
from discord.ext import commands

client = commands.Bot(command_prefix="$>", self_bot=True, help_command=None)
token = "Insert your token here"

@client.event
async def on_ready():
    print("Welcome to Mars")
    print("Mars Selfbot version 1.2 | Open Beta")
    print("Prefix is '$>'")
    print("Changed the Prefix from '.' to '$>' (Powercord users use '.' and I dont want to interfer with Powercord)")
    print("Added roll commands '$>roll' and '$>roll_more'")
    print("Added a Credits command. '$>credits'")
    print("Added a clear command '$>clear' (Only works on yourself unless you have Admin permissions.)")
    print("Removed the '$>help' command. (I expect you to actually check my code lol)")

@client.command()
async def clear(ctx, amount=6):
    print("Clearing messages...")
    await ctx.channel.purge(limit=amount)
    print("Messages cleared!")

@client.command()
async def roll(ctx):
    n = random.randrange(1, 100)
    await ctx.send("Rolled")
    await ctx.send(n)
    await ctx.send("out of 100.")

@client.command()
async def roll_more(ctx):
    n = random.randrange(1, 1000)
    await ctx.send("Rolled")
    await ctx.send(n)
    await ctx.send("out of 1000.")

@client.command()
async def credits(ctx):
    await ctx.send("***Mars-Selfbot Credits***")
    await ctx.send("**FailedWare** - Creator, Head Developer, and Lead Programmer. links: https://github.com/FailedWare/")
    await ctx.send("***God fucking damn I dont want to code this by myself DM me if you want to help.***")

@client.command()
async def minionsmeme(ctx):
    await ctx.send("Loading a minion meme...")
    await ctx.send(".")
    await ctx.send("..")
    await ctx.send("...")
    await ctx.send("Loaded! enjoy you fucking facebook mom")
    await ctx.send("https://www.youtube.com/watch?v=U6xUDjy6bY8")


@client.command()
async def git(ctx):
    await ctx.send("***Only ever download Mars-SB from github.***")
    await ctx.send("https://github.com/fuckeroftheass/Mars-Selfbot")

@client.command()
async def nikocado_avocado(ctx):
    #discord.message.delete()
    await ctx.send("***Nikocado Avocado's recent video*** Channel: Nikocado Avocado")
    await ctx.send("https://www.youtube.com/watch?v=eTQPOeG3SMs")

@client.command()
async def meme(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/926563652025339924/936809016061992990/despicable_drip.mp4")
    
@client.command()
async def roblox(ctx):
    await ctx.send("***ROBLOX***")
    await ctx.send("https://cdn.discordapp.com/attachments/957160927290081362/975883710169776188/bf6a2f38ead84b9a73c38c78937e45810b11faf2r1-1048-944v2_hq.jpg")


client.run(token, bot=False)
