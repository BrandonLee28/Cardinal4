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
        if amount > 100:
            amount = 100
        if amount == None:
            await ctx.channel.purge(limit=100)
        else:
            await ctx.channel.purge(limit=amount)




def setup(bot):
    bot.add_cog(admin(bot))