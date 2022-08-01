import discord
from discord.ext import commands

class Bans(commands.Cog): 
    def __init__(self, client):
        self.client = client

    @commands.command(help = '- Kicks users. Usage: _kick @User')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason = None):
        await member.kick(reason = reason)
        await ctx.send(f'Kicked {member.mention}')

    @commands.command(help = '- Bans users. Usage: _ban @User')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason = None):
        await member.ban(reason = reason)
        await ctx.send(f'Banned {member.mention}')

    @commands.command(help = 
    "- Unbans users. Usage: _unban User#1234 (if they changed their name or id after ban, you have to unban manually"
    )
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'{user.mention} was unbanned.')
                return

def setup(client): 
    client.add_cog(Bans(client))