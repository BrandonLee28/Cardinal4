import discord
import asyncio
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix='.')
class admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def ban(self,ctx,user : discord.Member,*,reason):
        await user.ban(reason = reason)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear(self,ctx,amount : int):
        amount = amount + 1
        if amount > 100:
            amount = 100
        if amount == None:
            await ctx.channel.purge(limit=100)
        else:
            await ctx.channel.purge(limit=amount)

    @commands.command()
    async def commands(self, ctx):
        embed=discord.Embed(title="Bot Commands", description="Shows all the commands of the bot", color=0x00ff1e)
        embed.add_field(name=".ping", value="shows the latency of the bot", inline=False)
        embed.add_field(name=".coinflip", value="flips a coin", inline=True)
        embed.add_field(name=".animequote", value="shows a random anime quote and the character", inline=True)
        embed.add_field(name=".fakeidentity", value="gives a random fake identity", inline=True)
        embed.add_field(name=".nsfw (category)", value="shows a nsfw image based on the category you give", inline=True)
        embed.add_field(name=".waifu", value="shows a random waifu image", inline=True)
        embed.add_field(name=".meme", value="shows a random reddit meme", inline=True)
        embed.set_footer(text="Made by @brandonn")
        await ctx.send(embed=embed)




def setup(bot):
    bot.add_cog(admin(bot))