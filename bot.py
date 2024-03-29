import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import json

load_dotenv()

TOKEN= os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix='.',case_insensitive=True)

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
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="your messages..."))
    print("Bot is ready!")

@bot.event
async def on_message(ctx):
        if ctx.channel.name == "counting":
            if ctx.guild.id == 929185019879125032:
                try:
                    number = float(ctx.content)
                    with open('929185019879125032.json','r+') as f:
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
                                await bot.process_commands(ctx)
                            else:
                                data['current'] = data['current'] + 1
                                data['lastcounter'] = ctx.author.id
                                f.seek(0)
                                json.dump(data,f,indent=4)
                                f.truncate()
                                await ctx.add_reaction('✅')
                        else:
                            data['current'] = 0
                            data['lastcounter'] = ""
                            f.seek(0)
                            json.dump(data,f,indent=4)
                            f.truncate()
                            await ctx.add_reaction('❌')
                            await ctx.reply('you suck a counting you are back to 0 now bahahaha.')
                    await bot.process_commands(ctx)
                except:
                    await bot.process_commands(ctx)
            if ctx.guild.id == 856970532510367784:
                try:
                    number = float(ctx.content)
                    with open('856970532510367784.json','r+') as f:
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
                                await bot.process_commands(ctx)
                            else:
                                data['current'] = data['current'] + 1
                                data['lastcounter'] = ctx.author.id
                                f.seek(0)
                                json.dump(data,f,indent=4)
                                f.truncate()
                                await ctx.add_reaction('✅')
                        else:
                            data['current'] = 0
                            data['lastcounter'] = ""
                            f.seek(0)
                            json.dump(data,f,indent=4)
                            f.truncate()
                            await ctx.add_reaction('❌')
                            await ctx.reply('you suck a counting you are back to 0 now bahahaha.')
                    await bot.process_commands(ctx)
                except:
                    await bot.process_commands(ctx)

        else:
            await bot.process_commands(ctx)


@bot.event
async def on_message_delete(message):
    if message.channel.name == "counting":
        embed=discord.Embed(title="Message Deleted", description=message.content, color=0xd400ff)
        embed.set_author(name=message.author, icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

bot.load_extension('admin')
bot.load_extension('upload')
bot.load_extension('games')
bot.run(TOKEN)