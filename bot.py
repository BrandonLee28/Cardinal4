from discord.ext import commands

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
async def on_message(message):
    print(message.content)
    await bot.process_commands(message)

bot.load_extension('admin')
bot.load_extension('games')
bot.run("ODA4MTgyMzExNTc2NTM1MDcx.YCC0bg._judyDV20-hTo7auRv0xMovJHyU")