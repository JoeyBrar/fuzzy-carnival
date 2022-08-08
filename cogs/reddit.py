import discord
from discord.ext import commands, tasks
import asyncpraw
import random

class reddit(commands.Cog): 
    def __init__(self, client):
        self.client = client

    @commands.command(help = 'usage: _shitpost (subreddit, default is r/shitposting)')
    async def post(self, ctx, subred="shitposting"):
        try:
            reddit = asyncpraw.Reddit(
                            client_id = "JnZhcba3Z5mAuF8_-g2SQw",
                            client_secret = "VeZYN41TRJYiPp7VWO5pERUNYV_oag",
                            username = "hellhelperbot",
                            password = "32233223p",
                            user_agent = "discordbot123"
                                )   

            subreddit = await reddit.subreddit(subred)
            post = subreddit.hot(limit = 20)
            allPosts = []   
            async for i in post:
                allPosts.append(i)

            randomPost = random.choice(allPosts)
            pfp_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWp61xAO7c0Yrxss8rPdmbg5EaPwDAR0vJlA&usqp=CAU"
            reddit_logo = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVEylIZNkjaSRU9xzFO8k5gxsPrgTHwvS0hQ&usqp=CAU"
            meme = discord.Embed(
                title = f'{randomPost.title}',
                color = discord.Colour.random()
            )

            meme.set_footer(text='taken from reddit')
            meme.set_image(url=f'{randomPost.url}')
            meme.set_thumbnail(url=f'{reddit_logo}')
            meme.set_author(name='a random redditor', icon_url=f'{pfp_url}')
            meme.add_field(name = 'Link (for comments):', value = f'https://reddit.com' + randomPost.permalink, inline = True)
            meme.add_field(name = 'Subreddit:', value = f'r/{subred}')

            await ctx.send(embed=meme)

        except Exception as e:
            await ctx.send(f'ERROR: ({e}).\nEither you used an invalid subreddit, or one that a normal user wouldn\'t have access to. HOWEVER, If you used a normal subreddit and the problem was on my end, I didn\'t feel like finishing this project and so I wont fix it.')
            print(e)

        



def setup(client): 
    client.add_cog(reddit(client))
