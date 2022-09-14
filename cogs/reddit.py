import discord
from discord.ext import commands, tasks
import asyncpraw
import random

allPosts = []
subredd = "shitposting"

def get_meme(memenum, subred):
    global allPosts

    Post = allPosts[memenum]
    pfp_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWp61xAO7c0Yrxss8rPdmbg5EaPwDAR0vJlA&usqp=CAU"
    reddit_logo = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVEylIZNkjaSRU9xzFO8k5gxsPrgTHwvS0hQ&usqp=CAU"
    meme = discord.Embed(
        title = f'{Post.title}',
        url = "https://reddit.com" + Post.permalink,
        color = discord.Colour.random()
    )

    meme.set_footer(text='taken from reddit (duh)')
    meme.set_image(url=f'{Post.url}')
    meme.set_thumbnail(url=f'{reddit_logo}')
    meme.set_author(name='a random redditor', icon_url=f'{pfp_url}')
    meme.add_field(name = 'Subreddit:', value = f'r/{subred}')
    return meme

class meme_scroll(discord.ui.View):
     global subred
     global meme_num
     meme_num = 0
     async def on_timeout(self):
         for child in self.children:
             child.disabled = True
         await self.message.edit(view = self)

     @discord.ui.button(label = "⭠", style = discord.ButtonStyle.gray)
     async def button_press1(self, button, interaction):
         global meme_num
         global subredd
         meme_num -= 1
         await interaction.response.edit_message(embed = get_meme(abs(meme_num % 40), subredd))

     @discord.ui.button(label = "⭢", style = discord.ButtonStyle.gray)
     async def button_press2(self, button, interaction):
         global meme_num
         global subredd
         meme_num += 1
         await interaction.response.edit_message(embed = get_meme(abs(meme_num % 40), subredd))

     @discord.ui.button(label = "Kill embed", style=discord.ButtonStyle.danger)
     async def button_press9(self, button, interaction):
         for child in self.children:
             child.disabled = True
         await interaction.response.edit_message(view = self)

class reddit(commands.Cog): 
    def __init__(self, client):
        self.client = client

    @commands.command(help = 'usage: _shitpost (subreddit, default is r/shitposting)')
    async def post(self, ctx, subred="shitposting"):
        global allPosts
        global subredd
        try:
            
            reddit = asyncpraw.Reddit(
                            client_id = "JnZhcba3Z5mAuF8_-g2SQw",
                            client_secret = "VeZYN41TRJYiPp7VWO5pERUNYV_oag",
                            username = "hellhelperbot",
                            password = "32233223p",
                            user_agent = "discordbot123"
                                )  

            subreddit = await reddit.subreddit(subred)
            subredd = subred
            post = subreddit.hot(limit = 40)
            allPosts = []
            async for i in post:
                allPosts.append(i)
            await reddit.close()

            randomPost = random.choice(allPosts)
            pfp_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWp61xAO7c0Yrxss8rPdmbg5EaPwDAR0vJlA&usqp=CAU"
            reddit_logo = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVEylIZNkjaSRU9xzFO8k5gxsPrgTHwvS0hQ&usqp=CAU"
            meme = discord.Embed(
                title = f'{randomPost.title}',
                url = "https://reddit.com" + randomPost.permalink,
                color = discord.Colour.random()
            )

            meme.set_footer(text='taken from reddit (duh)')
            meme.set_image(url=f'{randomPost.url}')
            meme.set_thumbnail(url=f'{reddit_logo}')
            meme.set_author(name='a random redditor', icon_url=f'{pfp_url}')
            meme.add_field(name = 'Subreddit:', value = f'r/{subred}')

            await ctx.send(embed=meme, view = meme_scroll(timeout = 45))

        except Exception as e:
            await ctx.send(f'ERROR: ({e}).\nEither you used an invalid subreddit, or one that a normal user wouldn\'t have access to. HOWEVER, If you used a normal subreddit and the problem was on my end, I didn\'t feel like finishing this project and so I wont fix it.')
            print(e)

def setup(client): 
    client.add_cog(reddit(client))
