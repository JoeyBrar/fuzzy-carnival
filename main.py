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
    await yagChannel.send('<@608395567994765315> read the game name')
    await client.change_presence(type=discord.ActivityType.playing,
            large_image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fi.kym-cdn.com%2Fphotos%2Fimages%2Fnewsfeed%2F001%2F535%2F091%2Fd97.jpg&imgrefurl=https%3A%2F%2Fknowyourmeme.com%2Fmemes%2Fno-i-dont-think-i-will&tbnid=H3nFSiOx6SoRqM&vet=12ahUKEwj9pLbZksf5AhWammoFHSo5BGMQMygAegQIARAj..i&docid=66kj0AgwQSyAZM&w=680&h=382&q=no%20no%20i%20don%27t%20think%20i%20will%20image%20link&ved=2ahUKEwj9pLbZksf5AhWammoFHSo5BGMQMygAegQIARAj",
            large_text = "no, no i don\'t think i will",
            large_image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fi.kym-cdn.com%2Fphotos%2Fimages%2Fnewsfeed%2F001%2F535%2F091%2Fd97.jpg&imgrefurl=https%3A%2F%2Fknowyourmeme.com%2Fmemes%2Fno-i-dont-think-i-will&tbnid=H3nFSiOx6SoRqM&vet=12ahUKEwj9pLbZksf5AhWammoFHSo5BGMQMygAegQIARAj..i&docid=66kj0AgwQSyAZM&w=680&h=382&q=no%20no%20i%20don%27t%20think%20i%20will%20image%20link&ved=2ahUKEwj9pLbZksf5AhWammoFHSo5BGMQMygAegQIARAj",
            large_text = "no, no i don\'t think i will",
            small_image = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fi.kym-cdn.com%2Fphotos%2Fimages%2Fnewsfeed%2F001%2F535%2F091%2Fd97.jpg&imgrefurl=https%3A%2F%2Fknowyourmeme.com%2Fmemes%2Fno-i-dont-think-i-will&tbnid=H3nFSiOx6SoRqM&vet=12ahUKEwj9pLbZksf5AhWammoFHSo5BGMQMygAegQIARAj..i&docid=66kj0AgwQSyAZM&w=680&h=382&q=no%20no%20i%20don%27t%20think%20i%20will%20image%20link&ved=2ahUKEwj9pLbZksf5AhWammoFHSo5BGMQMygAegQIARAj",
            small_text = "no, no i don\'t think i will",
            name = "no, no i don\'t think i will",
            details = "no, no i don\'t think i will",
            state = "no, no i don\'t think i will")))

  # useless stuff--------------------------------------------------------------------------
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
