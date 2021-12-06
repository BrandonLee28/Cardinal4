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
    @commands.has_permissions(administrator=True)
    async def mute(ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True,
                                              read_messages=False)
        embed = discord.Embed(title="muted", description=f"{member.mention} was muted ",
                              colour=discord.Colour.light_gray())
        embed.add_field(name="reason:", value=reason, inline=False)
        await ctx.send(embed=embed)
        await member.add_roles(mutedRole, reason=reason)
        await member.send(f" you have been muted from: {guild.name} reason: {reason}")


def setup(bot):
    bot.add_cog(admin(bot))