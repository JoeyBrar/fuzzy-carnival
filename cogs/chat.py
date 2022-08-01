from discord.ext import commands


class Chat(commands.Cog): 
    def __init__(self, client):
        self.client = client

    @commands.command(help = '- Clears a certain amount of chat messages. Usage: _clear {amount of messages}')
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, amount : int):
        await ctx.channel.purge(limit = amount + 1)
        await ctx.send(f'{amount} messages were removed.')

    @commands.command()
    async def clear2(self, ctx, amount : int):
        if ctx.author.id == 608395567994765315:
          await ctx.channel.purge(limit = amount + 1)
        else:
          pass


    @commands.command(help = '- Talk with a bot. Won\'t always respond')
    async def talk(self, ctx):
        channelID = input('channelID > ')
        message = input('message > ')
        givenChannel = self.client.get_channel(int(channelID))
        await givenChannel.send(f'{message}')

def setup(client): 
    client.add_cog(Chat(client))