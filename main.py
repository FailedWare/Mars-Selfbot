import discord
from discord.ext import commands

client = commands.Bot(command_prefix=".", self_bot=True, help_command=None)
token = "Insert your token here"

@client.event
async def on_ready():
    print("Welcome to Mars")
    print("Mars Selfbot version 1.1 | Open Beta")
    print("Prefix is '.'")
    print("Added Spam and Git commands.")

@client.command()
async def git(ctx):
    await ctx.send("***Only ever download Mars-SB from github.***")
    await ctx.send("https://github.com/FailedWare//")

@client.command()
async def help(ctx):
    await ctx.send("***MarsSB Help***")
    await ctx.send("***Commands***")
    await ctx.send("**.help** - shows this message.")
    await ctx.send("**.git** - shows the github link. (this will be seen from ***everyone***)")
    await ctx.send("**.spam**- spam the channel you are currently in.")
    await ctx.send("***Joke/Misc Commands***")
    await ctx.send("**.nikocado_avocado** - shows nikocado's recent video. (From his main channel)")

@client.command()
async def nikocado_avocado(ctx):
    #discord.message.delete()
    await ctx.send("***Nikocado Avocado's recent video*** Channel: Nikocado Avocado")
    await ctx.send("https://www.youtube.com/watch?v=eTQPOeG3SMs")

@client.command()
async def spam(ctx):
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")
    await ctx.send("Spam")


client.run(token, bot=False)