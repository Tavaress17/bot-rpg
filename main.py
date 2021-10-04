import discord
from discord.ext import commands
import random

bot = commands.Bot(".")

@bot.event
async def on_ready():
    print(f"Dale rapaziada! Meu user é: {bot.user}")


@bot.command(name="dale")
async def send_dale(ctx):
    name = ctx.message.author.mention

    resp = "Dale, " + name

    await ctx.send(resp)


@bot.command(name="d20")
async def roll_d20(ctx):
    
    resp = "Tu tirou " + str(random.randint(1,20))

    await ctx.send(resp)

bot.run("ODk0MzY1MDY0MDUwNjM4ODk4.YVo8Xw.j7Vohxu810sCQphskRmQ_qaYAig")