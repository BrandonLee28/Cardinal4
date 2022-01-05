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
        embed=discord.Embed(title="Random Anime Quote", color=0xff00c8)
        embed.add_field(name="Character:", value=r.json()['character'], inline=True)
        embed.add_field(name="Quote:", value=r.json()['quote'], inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def fakeidentity(self, ctx):
        r = requests.get('https://fakerapi.it/api/v1/persons?_quantity=1')
        embed=discord.Embed(title="Fake Identity", color=0x000000)
        embed.add_field(name="Name:", value=r.json()['data'][0]['firstname']+" "+r.json()['data'][0]['lastname'], inline=False)
        embed.add_field(name="Email:", value=r.json()['data'][0]['email'], inline=False)
        embed.add_field(name="Phone:", value=r.json()['data'][0]['phone'], inline=True)
        embed.add_field(name="Birthday:", value=r.json()['data'][0]['birthday'], inline=True)
        embed.add_field(name="Gender:", value=r.json()['data'][0]['gender'], inline=True)
        embed.add_field(name="Address:", value=r.json()['data'][0]['address']['street'], inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    async def nsfw(self,ctx,category):
        if ctx.channel.is_nsfw():
            print("1")
            r = requests.get('https://api.waifu.im/nsfw/'+category)
            print("2")
            embed=discord.Embed(title="why did i waste my time on this...", color=0xdb76d2)
            embed.set_image(url=r.json()['images'][0]['url'])
            await ctx.send(embed=embed)
            print("3")

    @commands.command()
    async def waifu(self,ctx):
        if ctx.channel.name == "anime":
            r = requests.get('https://api.waifu.im/sfw/waifu')
            embed=discord.Embed(title="why did i waste my time on this...", color=0xdb76d2)
            embed.set_image(url=r.json()['images'][0]['url'])
            await ctx.send(embed=embed)









def setup(bot):
    bot.add_cog(games(bot))