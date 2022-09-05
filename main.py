import discord
from discord.ext import commands, tasks
import os

intents = discord.Intents.all()
client = commands.Bot(command_prefix = '_', intents = intents)

# ---------------------------------------------------------------------------------------

# Errors
@client.event
async def on_command_error(ctx, error): 
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all required arguments.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'YOU DONT HAVE PERMISSION TO DO THAT')
    if isinstance(error, commands.BotMissingPermissions):
        await ctx.send(f'i dont have perms')
    else:
        pass

# Startup
@client.event
async def on_ready():
    print('Bot is online.\n')
    yagChannel = client.get_channel(931685534051479652)
    await yagChannel.send("Welcome to your worst nightmare")
    await client.change_presence(activity=discord.Game("gta7"))

  # useless stuff--------------------------------------------------------------------------
'''
@client.command()
async def a(ctx):
  guild = ctx.guild
  for i in range(31):
    role = await guild.create_role(name='a') 
    await ctx.message.author.add_roles(role)
  role = await guild.create_role(name='i') 
  await ctx.message.author.add_roles(role)
  role = await guild.create_role(name='eat') 
  await ctx.message.author.add_roles(role)
  role = await guild.create_role(name='children') 
  await ctx.message.author.add_roles(role)
  for i in range(31):
    role = await guild.create_role(name='a') 
    await ctx.message.author.add_roles(role)

  
# @client.command()
# async def leave(ctx, guild_id):
#   await client.get_guild(int(guild_id)).leave()

@client.command(pass_context = True)
async def massDeleteRoleA(ctx):
  guild = ctx.guild
  roles = guild.roles
  for i in range(len(roles)):
    if roles[i].name == 'a':
      await roles[i].delete()
      await ctx.send(f'{roles[i]} deleted')
    elif roles[i].name == 'i':
      await roles[i].delete()
      await ctx.send(f'{roles[i]} deleted')
    elif roles[i].name == 'eat':
      await roles[i].delete()
      await ctx.send(f'{roles[i]} deleted')
    elif roles[i].name == 'children':
      await roles[i].delete()
      await ctx.send(f'{roles[i]} deleted')
'''
@client.command()
async def credits(ctx):
  await ctx.send("an ikea table#4716: Owner and base code \nYEET#5381: Current maintainer and dev")

# end of usesless stuff------------------------------------------------------------------------    

  
# Cogs ----------------------------------------------------------------------------------

@client.command()
async def reload(ctx, extension):
    await ctx.send("working...")
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Reloaded {extension}')
    
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
# --------------------------------------------------------------------------------------

client.run(os.environ["token"])
client.close()
