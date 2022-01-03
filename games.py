import random
from random import choice
import discord
import asyncio
from discord.ext import commands
import requests

bot = commands.Bot(command_prefix='.')
class games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    determine_flip = [1, 0]

    @commands.command()
    async def coinflip(self,ctx,determine_flip = determine_flip):
        if random.choice(determine_flip) == 1:
            embed = discord.Embed(title="Coinflip",
                                  description=f"{ctx.author.mention} Flipped coin, we got **Heads**!")
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(title="Coinflip",
                                  description=f"{ctx.author.mention} Flipped coin, we got **Tails**!")
            await ctx.send(embed=embed)

    @commands.command()
    async def animequote(self, ctx):
        r = requests.get('https://animechan.vercel.app/api/random')
        embed=discord.Embed(title=Random Anime Quote, color=0xff00c8)
        embed.add_field(name="Character:", value=r.json()['character'], inline=True)
        embed.add_field(name="Quote:", value=r.json()['quote'], inline=False)
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(games(bot))