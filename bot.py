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

@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Bot Commands", description="Shows all the commands of the bot", color=0x00ff1e)
    embed.add_field(name=".ping", value="shows the latency of the bot", inline=False)
    embed.add_field(name=".coinflip", value="flips a coin", inline=True)
    embed.add_field(name=".animequote", value="shows a random anime quote and the character", inline=True)
    embed.add_field(name=".fakeidentity", value="gives a random fake identity", inline=True)
    embed.add_field(name=".nsfw (category)", value="shows a nsfw image based on the category you give", inline=True)
    embed.add_field(name=".waifu", value="shows a random waifu image", inline=True)
    embed.set_footer(text="Made by @brandonn")
    await ctx.send(embed=embed)





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