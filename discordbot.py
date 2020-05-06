from discord.ext import commands
from PIL import Image
from selenium import webdriver
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    driver = webdriver.PhantomJS()
    driver.get("https://challonge.com/s23h7vfc/module")
    driver.save_screenshot("screenshot.png")
    await ctx.send('ponga')
    await ctx.send_file("screenshot.png")


bot.run(token)
