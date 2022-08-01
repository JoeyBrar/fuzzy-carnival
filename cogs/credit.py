import discord
import pickle
from discord.ext import commands

# badWords = ['frick china']
# people = []

# #Assets: code/credits/balance/time since last command/time since last daily 

# source = 'assets/userinfo.txt'

# # def intoDict(member):
# #   source = 'assets/userinfo.txt'
# #   userInfo = open(source, 'r+')
# #   data = userInfo.read()
# #   userInfo.close()
  
# #   if str(member) in data:
# #     userInfo = open(source, 'r+')

# #     for line in userInfo:

# #       if '\n' in line:
# #         line = line.rstrip('\n')

# #       if str(member) in line:
# #         user, credits, balance, timeSinceCommand, timeSinceDaily = line.split('/')
# #         userDict = {'user' : {'name':str(member), 'credits':credits, 'balance':balance, 'timeSinceCommand':timeSinceCommand, 'timeSinceDaily':timeSinceDaily}}

# #   return userDict
  
# class Player():
#     def __init__(self, id, credits, balance, timeSinceCommand, timeSinceDaily):
#         self.id = id
#         self.credits = credits
#         self.balance = balance
#         self.timeSinceCommand = timeSinceCommand
#         self.timeSinceDaily = timeSinceDaily
                    
class Credit(commands.Cog): 
    def __init__(self, client):
        self.client = client
  
#     @commands.command(help = '- Checks profile of you or someone else')
#     async def stats(self, ctx):
#       with open(source, "rb") as file:
#         while True:
#           try:
#             people.append(pickle.load(file))
#           except EOFError:
#             break
#       await ctx.send(people)
#       people.clear()


#     @commands.command(help = '- Register')
#     async def register(self, ctx):

#       with open(source, "rb") as file:
#         while True:
#           try:
#             people.append(pickle.load(file))
#           except EOFError:
#             break

#       for i in people:
#         if i[id] == ctx.message.author.id:
#           await ctx.send('already registered dumbass')
#         else:
#           newPlayer = Player(ctx.message.author.id, 0, 5000, 0, 86400)
#           userData = {'id':newPlayer.id, 'credits':newPlayer.credits, 'balance':newPlayer.balance, 'timeSinceCommand':newPlayer.timeSinceCommand, 'timeSinceDaily':newPlayer.timeSinceDaily}
#           with open(source, 'wb') as dataPickle:
#             pickle.dump(userData, dataPickle)
#           await ctx.send('Registered successfully. Balance: 5000')
          
#       people.clear()

        


#     # @commands.Cog.listener()
#     # async def on_message(self, message): 
#     #     for count in badWords:
#     #         if count in message.content.lower():
#     #             print(f'\n{message.author} said {message.content}\n')
#     #             await message.channel.send(f'-13 social creduit')
#     #             return
 
      
def setup(client): 
    client.add_cog(Credit(client))