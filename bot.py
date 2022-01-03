from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN= os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix='.')

@bot.command(pass_context = True)
@commands.cooldown(1,15)
async def ping(ctx):
   await ctx.send(f'My ping is {bot.latency}!')




@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all requirements :rolling_eyes:.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have all the requirements :angry:")

@bot.event
async def on_ready():
    activity = discord.Game(name="uh....", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("Bot is ready!")

bot.load_extension('admin')
bot.load_extension('upload')
bot.load_extension('games')
bot.run(TOKEN)