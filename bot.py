from discord.ext import commands
import os
from dotenv import load_dotenv
import json

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

@bot.event
async def on_message(ctx):
    if ctx.channel.name == "counting":
        try:
            number = float(ctx.content)
            with open('storage.json','r+') as f:
                data = json.load(f)
                if number == data['current']+1:
                    if data['lastcounter'] == ctx.author.id:
                        await ctx.reply('you cant say it twice in a row you moron..')
                        data['current'] = 0
                        f.seek(0)
                        json.dump(data,f,indent=4)
                        f.truncate()
                        await ctx.add_reaction('❌')
                        await ctx.reply('you suck a counting you are back to 0 now bahahaha.')
                    else:
                        data['current'] = data['current'] + 1
                        data['lastcounter'] = ctx.author.id
                        f.seek(0)
                        json.dump(data,f,indent=4)
                        f.truncate()
                        await ctx.add_reaction('✅')

                else:
                    data['current'] = 0
                    f.seek(0)
                    json.dump(data,f,indent=4)
                    f.truncate()
                    await ctx.add_reaction('❌')
                    await ctx.reply('you suck a counting you are back to 0 now bahahaha.')
        except ValueError:
            return

bot.load_extension('admin')
bot.load_extension('upload')
bot.load_extension('games')
bot.run(TOKEN)