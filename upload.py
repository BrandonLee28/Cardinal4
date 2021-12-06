import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='.')
class upload(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



def setup(bot):
    bot.add_cog(upload(bot))
